from flask import Blueprint, jsonify, request, abort
from ..auth import requires_auth
from flask_cors import cross_origin
from ..models import db, User

bp = Blueprint('users', __name__, url_prefix="")


@bp.route('/users')
@cross_origin(headers=["Content-Type", "Authorization"])
def get_users():
    users = User.query.all()
    all_users = []
    for user in users:
        all_users.append(user.to_dict())
    return jsonify(all_users)


@bp.route('/users/<int:id>')
@cross_origin(headers=["Content-Type", "Authorization"])
def get_user(id):
    user = User.query.get(id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@bp.route('/users', methods=['POST'])
@cross_origin(headers=["Content-Type", "Authorization"])
def create_user():
    data = request.json
    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        existing_user.nickname = data['username']
        existing_user.email = data['email']
        return jsonify({"userId": existing_user.id, "username": existing_user.nickname, "email": existing_user.email})
    else:
        new_user = User(email=data['email'], username=data['username'])
        db.session.add(new_user)
        db.session.commit()
        new = {"newUserId": new_user.id, "newEmail": new_user.email,
               "newUsername": new_user.username}
        return new


@bp.route('/users/<int:id>', methods=['DELETE'])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(user.to_dict())

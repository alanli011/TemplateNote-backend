from flask import Blueprint, jsonify, request, abort
from ..auth import requires_auth
from sqlalchemy import and_
from flask_cors import cross_origin
from ..models import db, User, Template


bp = Blueprint('templates', __name__, url_prefix='')


# route to get all templates
@bp.route('/templates')
@cross_origin(headers=["Content-Type", "Authorization"])
# @requires_auth
def get_all_templates():
    templates = Template.query.all()
    all_templates = [template.to_dict() for template in templates]
    return jsonify(all_templates)


# route to get one specific template from database
@bp.route('/templates/<int:template_id>')
@cross_origin(headers=["Content-Type", "Authorization"])
# @requires_auth
def get_one_template(template_id):
    template = Template.query.get(template_id)
    if template is None:
        abort(404)
    return jsonify(template.to_dict())


# route to get all templates for specific user
@bp.route('/users/<int:user_id>/templates')
@cross_origin(headers=["Content-Type", "Authorization"])
# @requires_auth
def get_all_templates_for_user(user_id):
    templates = Template.query.filter(Template.user_id == user_id).all()
    all_templates = [template.to_dict() for template in templates]
    return jsonify(all_templates)


# route to get one template from user
@bp.route('/users/<int:user_id>/templates/<int:template_id>')
@cross_origin(headers=["Content-Type", "Authorization"])
# @requires_auth
def get_one_template_for_user(user_id, template_id):
    template = Template.query.filter(and_(Template.user_id == user_id, Template.id == template_id)).one()
    if template is None:
        abort(404)
    return jsonify(template.to_dict())


# route to create template
@bp.route('/templates', methods=['POST'])
@cross_origin(headers=["Content-Type", "Authorization"])
# @requires_auth
def create_template_for_user():
    data = request.json
    new_template = Template(
        name=data['name'],
        content=data['content'],
        user_id=data['user_id']
    )
    db.session.add(new_template)
    db.session.commit()
    return jsonify(data)


# route to delete template
@bp.route('/templates/<int:id>', methods=['DELETE'])
@cross_origin(headers=["Content-Type", "Authorization"])
# @requires_auth
def delete_template(id):
    template = Template.query.get(id)
    db.session.delete(template)
    db.session.commit()
    return jsonify(template.to_dict())

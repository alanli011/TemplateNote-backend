from flask import Blueprint, jsonify, request, abort
from sqlalchemy import and_
from ..auth import requires_auth
from flask_cors import cross_origin
from ..models import db, User, NoteBook, Note, Tag, note_tags

bp = Blueprint('tags', __name__, url_prefix='')


# create route for adding tags with association to notes
@bp.route('/notes/<int:note_id>/tags', methods=['POST'])
@cross_origin(headers=["Content-Type", "Authorization"])
# @requires_auth
def create_note_tag(note_id):
    data = request.json
    note = Note.query.get(note_id)
    new_tag = Tag(
        name=data['name']
    )
    if note is not None:
        new_tag.notes.append(note)
    db.session.add(new_tag)
    db.session.commit()
    return jsonify(new_tag.to_dict())


@bp.route('/notes/<int:note_id>/tags')
@cross_origin(headers=["Content-Type", "Authorization"])
def get_notes_tags(note_id):
    query = Tag.query.join(Note, Tag.notes)
    tags = query.order_by(Tag.name).all()
    all_tags = [tag.to_dict() for tag in tags]
    return jsonify(all_tags)


# create route for adding tags without note
@bp.route('/tags', methods=['POST'])
@cross_origin(headers=["Content-Type", "Authorization"])
# @requires_auth
def create_tag():
    data = request.json
    new_tag = Tag(
        name=data['name']
    )
    db.session.add(new_tag)
    db.session.commit()
    return jsonify(new_tag.to_dict())


# this route will get all the tags from the database. need to come back to try and figure out how to limit it by user created??
@bp.route('/tags')
@cross_origin(headers=["Content-Type", "Authorization"])
# @requires_auth
def get_tags():
    tags = Tag.query.all()
    all_tags = [tag.to_dict() for tag in tags]
    return jsonify(all_tags)


# returns one specific tag based on id
@bp.route('/tags/<int:id>')
@cross_origin(headers=["Content-Type", "Authorization"])
# @requires_auth
def get_one_tag(id):
    tag = Tag.query.get(id)
    if tag is None:
        abort(404)
    return jsonify(tag.to_dict())


# route to delete specific tag based on id
@bp.route('/tags/<int:id>', methods=['DELETE'])
@cross_origin(headers=["Content-Type", "Authorization"])
# @requires_auth
def delete_tag(id):
    tag = Tag.query.get(id)
    db.session.delete(tag)
    db.session.commit()
    return jsonify(tag.to_dict())

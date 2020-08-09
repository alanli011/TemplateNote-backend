from flask import Blueprint, jsonify, request, abort
from sqlalchemy import and_
from ..auth import requires_auth
from flask_cors import cross_origin
from ..models import db, User, NoteBook, Note, Tag, note_tags

bp = Blueprint('notes', __name__, url_prefix='')


# route to get all the notes associated with user_id and notebook_id
@bp.route('/users/<int:user_id>/notebooks/<int:notebooks_id>/notes')
@cross_origin(headers=["Content-Type", "Authorization"])
# @requires_auth
def get_notes(user_id, notebooks_id):
    # filters out the notes where notebook id is equal to what's coming in and the user id
    notes = Note.query.filter(and_(Note.notebook_id == notebooks_id, NoteBook.user_id == user_id)).all()
    all_notes = [note.to_dict() for note in notes]
    return jsonify(all_notes)


# route to get one note associated with user_id and notebook_id
@bp.route('/users/<int:user_id>/notebooks/<int:notebooks_id>/notes/<int:notes_id>')
@cross_origin(headers=["Content-Type", "Authorization"])
# @requires_auth
def get_note_id(user_id, notebooks_id, notes_id):
    # filters out the notes where notebook id is equal to what's coming in and the user id
    note = Note.query.filter(and_(NoteBook.user_id == user_id, Note.id == notes_id, Note.notebook_id == notebooks_id)).first()
    if note is None:
        abort(404)
    return jsonify(note.to_dict())


# route to create notes
@bp.route('/notebooks/<int:notebook_id>/notes', methods=['POST'])
@cross_origin(headers=["Content-Type", "Authorization"])
# @requires_auth
def create_note(notebook_id):
    # set data to be what comes in from the client side for POST
    data = request.json
    new_note = Note(
        title=data['title'],
        content=data['content'],
        notebook_id=notebook_id
    )
    db.session.add(new_note)
    db.session.commit()
    return jsonify(new_note.to_dict())


# Updates specific notebook
@bp.route('/users/<int:user_id>/notebooks/<int:notebook_id>/notes/<int:note_id>', methods=['PUT'])
@cross_origin(headers=["Content-Type", "Authorization"])
# @requires_auth
def update_notebook(user_id, notebook_id, note_id):
    # grabs data from the request
    data = request.json
    note = Note.query.get(note_id)
    # updating the current database with the setattr
    setattr(note, 'title', data['title'])
    setattr(note, 'content', data['content'])
    setattr(note, 'notebook_id', notebook_id)
    db.session.commit()
    return jsonify(note.to_dict())


# route to delete specific note
@bp.route('/notebooks/<int:notebooks_id>/notes/<int:notes_id>', methods=['DELETE'])
@cross_origin(headers=["Content-Type", "Authorization"])
# @requires_auth
def delete_note(notes_id, notebooks_id):
    note = Note.query.get(notes_id)
    db.session.delete(note)
    db.session.commit()
    return jsonify(note.to_dict())


# Search notes
@bp.route('/notebooks/<int:notebooks_id>/notes/search')
@cross_origin(headers=["Content-Type", "Authorization"])
# @requires_auth
def find_notes(notebooks_id):
    search_notes = Note.query.filter(Note.content.op('regexp')(r'\b{}\b'.format(request.query_string))).all()
    all_search = [search_notes.to_dict() for note in search_notes]
    return jsonify(all_search)

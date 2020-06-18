from flask import Blueprint, jsonify, request, abort
from sqlalchemy import and_
from ..auth import requires_auth
from flask_cors import cross_origin
from ..models import db, User, NoteBook, Note

bp = Blueprint('notes', __name__, url_prefix='/users/<int:user_id>')


@bp.route('/notebooks/<int:notebooks_id>/notes')
@cross_origin(headers=["Content-Type", "Authorization"])
def get_notes(user_id, notebooks_id):
    notes = Note.query.filter(and_(Note.notebook_id == notebooks_id, NoteBook.user_id == user_id)).all()
    all_notes = [note.to_dict() for note in notes]
    return jsonify(all_notes)


@bp.route('/notebooks/<int:notebooks_id>/notes/<int:notes_id>')
@cross_origin(headers=["Content-Type", "Authorization"])
def get_note_id(user_id, notebooks_id, notes_id):
    note = NoteBook.query.filter(and_(NoteBook.user_id == user_id, Note.id == notes_id, Note.notebook_id == notebooks_id))
    if note is None:
        abort(404)
    return jsonify(note.to_dict())


@bp.route('/notes', methods=['POST'])
@cross_origin(headers=["Content-Type", "Authorization"])
def create_note(notebooks_id):
    data = request.json
    new_note = Note(
        title=data['title'],
        content=data['content'],
        notebook_id=data['notebook_id']
    )
    db.session.add(new_note)
    db.session.commit()
    return jsonify(data)


@bp.route('/notebooks/<int:notebooks_id>/notes/<int:notes_id>')
@cross_origin(headers=["Content-Type", "Authorization"])
def delete_note(notes_id):
    note = Note.query.get(notes_id)
    db.session.delete(note)
    db.session.commit()
    return jsonify(note.to_dict())

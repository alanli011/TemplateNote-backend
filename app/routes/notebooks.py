from flask import Blueprint, jsonify, request, abort
from ..auth import requires_auth
from flask_cors import cross_originz
from ..models import db, User, NoteBook

bp = Blueprint('notebooks', __name__, url_prefix='')


# gets all notebooks
@bp.route('/notebooks')
@cross_origin(headers=["Content-Type", "Authorization"])
def get_notebooks():
    notebooks = NoteBook.query.all()
    all_notebooks = []
    for notebook in notebooks:
        all_notebooks.append(notebook.to_dict())
    return jsonify(all_notebooks)


# get specific notebook based on id
@bp.route('/notebooks/<int:id>')
@cross_origin(headers=["Content-Type", "Authorization"])
def get_notebook(id):
    notebook = NoteBook.query.get(id)
    if notebook is None:
        abort(404)
    return jsonify(notebook.to_dict())


# creates a new notebook
@bp.route('/notebooks', methods=['POST'])
@cross_origin(headers=["Content-Type", "Authorization"])
def create_notebook():
    data = request.json
    new_notebook = NoteBook(
        name=data['name'],
        user_id=data['user_id']
    )
    db.session.add(new_notebook)
    db.session.commit()
    return jsonify(data)


# delete specific notebook based on id
@bp.route('/notebooks/<int:id>', methods=['DELETE'])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def delete_notebook(id):
    notebook = Notebook.query.get(id)
    db.session.delete(notebook)
    db.session.commit()
    return jsonify(notebook.to_dict())

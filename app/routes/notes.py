from flask import Blueprint, jsonify, request, abort
from ..auth import requires_auth
from flask_cors import cross_origin
from ..models import db, User, NoteBook, Note

bp = Blueprint('notes', __name__, url_prefix='')

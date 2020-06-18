from flask import Blueprint, jsonify, request, abort
from sqlalchemy import and_
from ..auth import requires_auth
from flask_cors import cross_origin
from ..models import db, User, NoteBook, Note, Tag

bp = Blueprint('tags', __name__, url_prefix='')

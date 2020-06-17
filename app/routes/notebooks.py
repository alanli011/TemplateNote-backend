from flask import Blueprint, jsonify, request
from sqlalchemy import and_
from ..auth import requires_auth
from flask_cors import cross_origin
from ..models import db, User, NoteBook

bp = Blueprint('notebooks', __name__, url_prefix='')

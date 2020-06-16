from flask import Blueprint, jsonify
from sqlalchemy import and_

bp = Blueprint('main', __name__, url_prefix='')


@bp.route('/')
def main():
    return jsonify('Hello World')

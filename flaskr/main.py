import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def main():
    # return "INDEX"
    return render_template('main/index.html')

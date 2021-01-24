from flask import Blueprint, render_template, send_from_directory

bp = Blueprint('battleship', __name__)


@bp.route('/', methods=['GET'])
def main():
    return render_template('index.html')

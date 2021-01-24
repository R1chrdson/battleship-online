from os import environ
from flask import Flask
from flask_socketio import SocketIO
import app.server

socketio = SocketIO()


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    try:
        app.config['SECRET_KEY'] = environ['BATTLESHIP_GAME_SECRET']
    except KeyError:
        print('Please, set `BATTLESHIP_GAME_SECRET` to your environ')
        exit(1)

    app.register_blueprint(server.bp)
    socketio.init_app(app)
    return app

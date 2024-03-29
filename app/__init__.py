from flask import Flask, jsonify
from dotenv import load_dotenv
from os import getenv


def create_app():
    app = Flask(__name__)

    load_dotenv()

    app.config['SECRET_KEY'] = getenv('SECRET_KEY')

    #SocketIO
    from .socketi0 import socketio
    socketio.init_app(app)

    #OAuth Googel
    from .google_auth import oauth
    oauth.init_app(app)

    #blueprints register
    from app.route.views import views
    app.register_blueprint(views, url_prefix='/')

    from app.route.auth import auth
    app.register_blueprint(auth, url_prefix='/')

    

    return app
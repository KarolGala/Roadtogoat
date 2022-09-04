from flask import Flask
from os import path



def create_app():
    app = Flask(__name__, static_folder='static')
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    return app


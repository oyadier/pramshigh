# App creating engine

from flask import Flask
from flask_sqlalchemy import SQLALchemy


def create_app():
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ningo_ahwiam'
    # setting up the database
  
# registering the blueprint of all views here.
    from .views import views

    app.register_blueprint(views, url_prefix='/pramshigh')

    return app
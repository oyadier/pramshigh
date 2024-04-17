# App creating engine

from flask import Flask
#package to install
from .database import init_db
from flask_sqlalchemy import SQLAlchemy
#IMporting os path to enable file to be write and read
from os import path


DATABASE_NAME = 'noteapp.db'
def create_app():
    
    app = Flask(__name__)
    
    
    app.config['SECRET_KEY'] = 'ningo_ahwiam'
    
    # registering the blueprint of all views here.
    from .views import views
    app.register_blueprint(views, url_prefix='/pramshigh')
    

 #   init_db()

 
        
    #importing the models to load all classes before the db is created
    
    return app
        
# App creating engine

from flask import Flask
#package to install
from flask_sqlalchemy import SQLAlchemy
#IMporting os path to enable file to be write and read
from os import path

#creating database
db = SQLAlchemy()
DATABASE_NAME = "note_database.db"

def create_app():
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ningo_ahwiam'
    
    # setting up the database
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE_NAME}'
    db.init_app(app)
    
# registering the blueprint of all views here.
    from .views import views
    
    #importing the models to load all classes before the db is created
    from .models import Note, User
    create_app(app)
    

    app.register_blueprint(views, url_prefix='/pramshigh')
    return app

    def create_db(app_name):
        if path.exists('web_dynamic/' + {DATABASE_NAME}):
            pass
        else:
            db.create_all(app=app_name)
            print('Database created!')
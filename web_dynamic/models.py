#the . import from this directory. You can also use the dir name
from web_dynamic import db
#package to install
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Models, UserMixin):
    user_Id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(150))
    firs_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique= True)
    created_date = db.Column(db.Date(timezone=True), default=func.now())
    notes = db.relationship('Note')
    
    
class Note(db.Models):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=True)
    note = db.Column(db.String(1000))
    date = db.Column((db.DateTime(timezone=True)), default=func.now())
    user = db.Column(db.Integer, db.Foriegnkey('user.id'))
    
    

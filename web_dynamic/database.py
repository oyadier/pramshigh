# Importing the neccessary libraries for the setting up of the dp
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from os import path, getcwd


DATABASE_NAME = 'noteapp.db'
db_engine = create_engine('sqlite:///web_dynamic/'+DATABASE_NAME, echo=True)
Session = sessionmaker(bind=db_engine)
session = Session()
Base = declarative_base()

def init_db():
   
    import web_dynamic.models.user as modes
    
    Base.metadata.create_all(bind=db_engine)
    
    print("Database created!")  
#the . import from this directory. You can also use the dir name
#package to install
from datetime import datetime, timezone
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import func
from web_dynamic.database import Base
import uuid

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    password = Column(String(150))
    first_name = Column(String(150))
    last_name = Column(String(150))
    created_at = Column(DateTime, default=datetime.now())

    
    def __init__(self, first_name=None, last_name=None, password=0):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.created_at = str(datetime.now(timezone.utc))
    
    
        
    def to_dict(self):
        return {
            "id":self.id,
            "first_name":   self.first_name,
            "second": self.last_name,
            "pass": self.password,
            "created_at":self.created_at
        }
       
    

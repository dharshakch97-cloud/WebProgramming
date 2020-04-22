from datetime import datetime
from sqlalchemy.types import TIMESTAMP
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"

    username = Column(String(100), primary_key=True)
    email = Column(String(100))
    password = Column(String(100))
    created_at = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return "<User: {} Email: {}>".format(self.username, self.email)

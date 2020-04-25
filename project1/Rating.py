import sys
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class  Star(db.Model):

    _tablename_ = "User Review"
    UserName = db.Column(db.String, nullable=False, primary_key=True)
    Book_ID = db.Column(db.Integer, primary_key=True)
    Rating = db.Column(db.String, nullable=False)
    Feedback = db.Column(db.String(140),nullable=False)
    
    def _init_(self,UserName, Book_ID, Rating, Feedback) :
        self.UserName = UserName
        self.Book_ID = Book_ID
        self.Rating = Rating
        self.Feedback = Feedback
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = "books"

    isbn = db.Column(db.String(100), primary_key=True, nullable = False)
    title = db.Column(db.String(100), nullable = False)
    author = db.Column(db.String(128))
    year = db.Column(db.Integer,nullable=False)

    def __init__(self,isbn,title,author,year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year    

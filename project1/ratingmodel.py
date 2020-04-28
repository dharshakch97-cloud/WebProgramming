from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Review(db.Model):
    __tablename__ = "review"

    title = db.Column(db.String, primary_key=True)
    username = db.Column(db.String, unique=True)
    rating = db.Column(db.String, nullable=False)
    review = db.Column(db.String, index=False, unique=False, nullable=False)

    def __init__(self, Username, title, rating, review):
        
        self.title = title
        self.username = Username
        self.rating = rating
        self.review = review

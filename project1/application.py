import os
import requests
from flask import Flask, session, render_template, request, url_for, redirect, json
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import models
from models import Base, Users
from bookmodel import Book

app = Flask(__name__, template_folder='./templates', static_folder='./static')
# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
Base.query = db.query_property()

@app.route("/")
def landpage():
    if (request.method == 'GET'):
        if session.get("user_name") is not None:
            return render_template("userhome.html", user=session["user_name"])
        return render_template("landingpage.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/admin")
def admin_page():
    users = db.query(Users)
    return render_template("admin-users.html", users=users)

@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route("/submit", methods=['POST'])
def show_result():
    if request.method=='POST':
        user_name=request.form['username']
        user_email=request.form['email']
        user_password=request.form['psw']
        new_user = Users(username=user_name, email=user_email, password=user_password)
        try:
            db.add(new_user)
            db.commit()
            session["user_name"] = user_name
            return render_template("userhome.html", user=user_name)
        except:
            text = "Account already exists! Please login with your account"
            return render_template("login.html", text=text)
    else:
        return render_template("register.html")

@app.route("/auth", methods=['POST'])
def auth():
    email = request.form['email']
    password = request.form['password']

    user = db.query(Users).filter_by(email=email)
    if (user[0].email == email and user[0].password == password):
        session["user_name"] = user[0].username
        return render_template("userhome.html", user=user[0].username)
    return render_template("login.html", text="email or password is incorrect")

@app.route("/bookpage")
def bookpage():
    return render_template("bookpage.html")

@app.route("/<string:isbn>", methods = ["GET"])
def get_book(isbn):
    response = bookreads_api(isbn)
    return render_template("bookpage.html", 
                name=response["name"], author=response["author"], ISBN = response["isbn"], 
                year=response["year"], rating=response["average_rating"], count=response["reviews_count"], 
                image=response["img"])

def bookreads_api(isbn):
    query = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "GeJUHhlmNf7PYbzeKEnsuw", "isbns": isbn})
    response = query.json()
    response = response['books'][0]
    query = db.query(Book).filter(Book.isbn.like(f'{isbn}'))
    title=list()
    author = list()
    year = list()
    for row in query:
        response["name"] = row.title
        response["author"] = row.author
        response["year"] = row.year
        response["img"] = "http://covers.openlibrary.org/b/isbn/" + isbn + ".jpg"
        return response

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("landpage"))

if __name__ == "__main__":
    app.run(debug=True)

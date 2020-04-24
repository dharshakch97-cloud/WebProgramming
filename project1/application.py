import os

from flask import Flask, session, render_template, request, url_for, redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import models
from models import Base, Users
import bookmodel
from bookmodel import *

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
            return render_template("result.html", user_email=user_email, user_name=user_name)
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

#         return render_template("home.html",text = "No matches found")        
@app.route("/search", methods=["GET","POST"])
def search():
    
    if request.method == "POST":
        word = request.form['searchbox']
        choice = request.form['choice']
        if choice == "isbn":
            print(word)
            
            query = db.query(Book).filter(Book.isbn.like(f'%{word}%'))
        elif choice == "title":
            
            query = db.query(Book).filter(Book.title.like(f'%{word}%'))
        else:
            
            query = db.query(Book).filter(Book.author.like(f'%{word}%'))
        
        isbn = []
        title=[]
        author = []
        year = []
        for row in query:
            isbn.append(row.isbn)
            title.append(row.title)
            author.append(row.author)
            year.append(row.year)
            
        if len(isbn)==0:
            return render_template("userhome.html",text = "No Matches Found")    
        return render_template("books.html", isbn=isbn,title=title,author=author,year=year,length=len(isbn))
        
    elif request.method == "GET":
        return render_template("landingpage.html")



    

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("landpage"))

if __name__ == "__main__":
    app.run(debug=True)

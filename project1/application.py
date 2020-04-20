import os

from flask import Flask, session, render_template, request, url_for, redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import models
from models import Base, Users

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
        db.add(new_user)
        db.commit()
        db.close()
    return render_template("result.html", user_email=user_email, user_name=user_name)
    
@app.route("/auth", methods=['POST'])
def auth():
    email = request.form['email']
    password = request.form['password']

    user = db.query(Users).filter_by(email=email)
    if (user[0].email == email and user[0].password == password):
        session["user_email"] = user[0].email
        session["user_password"] = user[0].password
        return render_template("userhome.html", user=user[0].username)
    err_message = email + "is not a registered user!"
    return render_template("register.html", err_message)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("landpage"))

if __name__ == "__main__":
    app.run(debug=True)

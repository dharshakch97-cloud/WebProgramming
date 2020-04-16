import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

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


@app.route("/")
def landpage():
    return render_template("landingpage.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route("/submit", methods=['POST'])
def show_result():
    if request.method=='POST':
        user_name=request.form['username']
        user_email=request.form['email']
    return render_template("result.html", user_email=user_email, user_name=user_name)
    
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, session, render_template, redirect, url_for, request
from flask_session import Session
from cs50 import SQL
db = SQL("sqlite:///specialEats.db")

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def homepage():
    if not session.get("username") and not session.get("password"):
        return redirect("/home")
    return render_template("home.html")

@app.route("/home")
def prototype():
    return render_template("homePrototype.html")

# @app.route("/signup", methods=["GET", "POST"])
# def signup():
#     if request.method == "POST":
#         session["username"] = request.form.get("username")
#         session["password"] = request.form.get("password")
#         return redirect("/")
#     return render_template("signup.html")

# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         session["username"] = request.form.get("username")
#         session["password"] = request.form.get("password")
#         return redirect("/")
#     return render_template("login.html")

# @app.route("/logout")
# def logout():
#     session.get("username") = None
#     session.get("password") = None
#     return redirect("/login")
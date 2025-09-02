from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from cs50 import SQL
db = SQL("sqlite:///app.db")

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def home():
    return render_template("home.html", page_id = "home")

@app.route("/api/shows")
def shows():
    title = request.args.get("title")
    shows = db.execute("SELECT * FROM shows WHERE title LIKE '?%'", title)
    return render_template("shows.html", shows = shows)


if __name__ == "__main__":
    app.run(debug =True, use_reloader = True, reloader_type = "watchdog")

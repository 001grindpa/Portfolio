from flask import Flask, session, render_template, redirect, url_for, request
from flask_session import Session
from randomModules import password_sys, password_gen
from cs50 import SQL
db = SQL("sqlite:///specialEats.db")

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

languages = ["English", "Hausa", "Igbo", "Yoruba"]

@app.route("/")
def homepage():
    if not session.get("password"):
        return redirect("/landing")
    return render_template("home.html", page_id = "home")

@app.route("/landing")
def prototype():
    return render_template("landing.html", langs=languages, page_id = "landing")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        session["username"] = request.form.get("username")
        password = request.form.get("password")
        session["first_name"] = request.form.get("first_name")
        session["last_name"] = request.form.get("last_name")
        session["dob"] = request.form.get("dob")
        result = password_sys(password)
        if result == "valid_password":
            session["password"] = password
            db.execute("INSERT INTO userData(username, password, first_name, last_name, d_o_b) VALUES(?, ?, ?, ?, ?)", session.get("username"), session.get("password"), session.get("first_name"), session.get("last_name"), session.get("dob"))
            return redirect("/")
        else:
            return render_template("signup.html", result = result, page_id = "signup")
    return render_template("signup.html", page_id = "signup")
@app.route("/signup/returned")
def returned():
    query = request.args.get("q")
    result = password_sys(query)
    return render_template("result.html", result = result)
@app.route("/signup/generated")
def generate():
    query_2 = request.args.get("gen")
    generated = password_gen(query_2)
    return render_template("generated.html", generated=generated)
    

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
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, reloader_type='watchdog')

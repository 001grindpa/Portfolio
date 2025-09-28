from flask import Flask, session, render_template, redirect, url_for, request, jsonify
from flask_session import Session
from randomModules import password_sys, password_gen
from cs50 import SQL
db = SQL("sqlite:///specialEats.db")

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

languages = ["English", "Hausa", "Igbo", "Yoruba"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
genders = ["Male", "Female"]

@app.route("/")
def homepage():
    if not session.get("password"):
        return redirect("/landing")
    userData = db.execute("SELECT * FROM userData WHERE username = ? AND password = ?", session.get("username"), session.get("password"))
    for data in userData:
        first_name = data.get("first_name")
        last_name = data.get("last_name")
    return render_template("home.html", page_id = "home", langs = languages, first_name = first_name, last_name = last_name)

@app.route("/landing")
def prototype():
    return render_template("landing.html", langs=languages, page_id = "landing")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        session["username"] = username
        username_low = username.lower()
        password = request.form.get("password")
        session["first_name"] = request.form.get("first_name")
        session["last_name"] = request.form.get("last_name")
        session["dob"] = request.form.get("dob")
        result = password_sys(password)
        if result == "valid_password":
            session["password"] = password
            user_data = db.execute("SELECT * FROM userData")
            for data in user_data:
                if data.get("username") == session.get("username") and data.get("password") == session.get("password"):
                    return redirect("/signupError")
            db.execute("INSERT INTO userData(username, password, first_name, last_name, d_o_b, e_mail, gender) VALUES(?, ?, ?, ?, ?, ?, ?)", username_low, session.get("password"), session.get("first_name"), session.get("last_name"), session.get("dob"), "example@email.com", "null")
            return redirect("/")
        else:
            return render_template("pWordError.html")
    return render_template("signup.html", page_id = "signup", months = months)
@app.route("/usernamecheck")
def namecheck():
    username = request.args.get("namecheck").lower()
    userData = db.execute("SELECT * FROM userData")
    for data in userData:
        if data.get("username") == username:
            name_error = "username already exists"
            return render_template("usernameCheck.html", name_error = name_error )
    if len(username) <= 4:
        error = "username must be more than 4 characters long"
        return render_template("usernameCheck.html", error = error)
    nameError = "valid username \U00002705"
    return render_template("usernameCheck.html", nameError = nameError)
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
@app.route("/signupError")
def signupError():
    return render_template("signupError.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form.get("username").lower()
        session["password"] = request.form.get("password")
        userData = db.execute("SELECT * FROM userData")
        for data in userData:
            if data.get("username") == session.get("username") and data.get("password") == session.get("password"):
                return redirect("/")
        return redirect("/loginError")
    return render_template("login.html", page_id = "login")
@app.route("/loginError")
def loginError():
    return render_template("loginError.html")

@app.route("/logout")
def logout():
    session["username"] = None
    session["password"] = None
    session["first_name"] = None
    session["last_name"] = None
    session["dob"] = None
    return redirect("/signup")

@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        username_new = request.form.get("username")
        first_name_new = request.form.get("first_name")
        last_name_new = request.form.get("last_name")
        gender_new = request.form.get("gender")
        e_mail_new = request.form.get("e_mail")
        userData_1 = db.execute("SELECT id FROM userData WHERE username = ?", session.get("username"))
        for data_1 in userData_1:
            user_id = data_1["id"]
        if username_new:
            db.execute("UPDATE userData SET username = ? WHERE id = ?", username_new, user_id)
        if first_name_new:
            db.execute("UPDATE userData SET first_name = ? WHERE id = ?", first_name_new, user_id)
        if last_name_new:
            db.execute("UPDATE userData SET last_name = ? WHERE id = ?", last_name_new, user_id)
        if gender_new:
            db.execute("UPDATE userData SET gender = ? WHERE id = ?", gender_new, user_id)
        if e_mail_new:
            db.execute("UPDATE userData SET e_mail = ? WHERE id = ?", e_mail_new, user_id)
    userData_2 = db.execute("SELECT id FROM userData WHERE username = ?", session.get("username"))
    for data_1 in userData_2:
        user_id2 = data_1["id"]
    n = []
    cContent = db.execute("SELECT user_id FROM cart WHERE user_id = ?", user_id2)
    for x in cContent:
        y = x.get("user_id")
        n.append(y)
    userData = db.execute("SELECT * FROM userData WHERE username = ?", session.get("username"))
    for data in userData:
        first_name = data["first_name"]
        last_name = data["last_name"]
        username = data["username"]
        e_mail = data["e_mail"]
        gender = data["gender"]
    return render_template("profile.html", n = len(n), first_name = first_name, last_name = last_name, username = username, e_mail = e_mail, genders = genders, gender = gender, page_id = "profile")

@app.route("/sCuisines")
def sCuisines():
    s_id = [2,3,4,32,47,48,51,75,85,92,88,70,57,31,94,95]
    userData = db.execute("SELECT * FROM userData WHERE username = ? AND password = ?", session.get("username"), session.get("password"))
    for data in userData:
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        meals = db.execute("SELECT * FROM meals WHERE id IN (?)", s_id)
    return render_template("sCuisine.html", meals = meals, page_id = "sCuisine", langs = languages, first_name = first_name, last_name = last_name)

@app.route("/nCuisines")
def nCuisines():
    n_id = [5,6,7,11,30,37,38,39,40,42,41,43,44,45,71,20,81]
    userData = db.execute("SELECT * FROM userData WHERE username = ? AND password = ?", session.get("username"), session.get("password"))
    for data in userData:
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        meals = db.execute("SELECT * FROM meals WHERE id IN (?)", n_id)
    return render_template("nCuisine.html", meals = meals, page_id = "nCuisine", langs = languages, first_name = first_name, last_name = last_name)

@app.route("/wCuisines")
def wCuisines():
    w_id = [8,9,10,12,52,53,62,63,64,65,66,67]
    userData = db.execute("SELECT * FROM userData WHERE username = ? AND password = ?", session.get("username"), session.get("password"))
    for data in userData:
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        meals = db.execute("SELECT * FROM meals WHERE id IN (?)", w_id)
    return render_template("wCuisine.html", meals = meals, page_id = "wCuisine", langs = languages, first_name = first_name, last_name = last_name)

@app.route("/eCuisines")
def eCuisines():
    e_id = [1,13,14,15,16,18,23,50,54,55,56,58,59,69,91,93]
    userData = db.execute("SELECT * FROM userData WHERE username = ? AND password = ?", session.get("username"), session.get("password"))
    for data in userData:
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        meals = db.execute("SELECT * FROM meals WHERE id IN (?)", e_id)
    return render_template("eCuisine.html", meals = meals, page_id = "eCuisine", langs = languages, first_name = first_name, last_name = last_name)

@app.route("/cart", methods=["GET", "POST"])
def cart():
    identity = db.execute("SELECT id FROM userData WHERE username = ?", session.get("username"))
    for user in identity:
        user_id = user.get("id")
    if request.method == "POST":
        item_id = request.form.get("item_id")
        db.execute("INSERT INTO cart(user_id, item_id) VALUES(?, ?)", user_id, item_id)
        resp = {"msg": "Successfully added to cart"}
        return jsonify(resp)
    x = []
    cart_data = db.execute("SELECT item_id FROM cart WHERE user_id = ?", user_id)
    for item in cart_data:
        item_id2 = item["item_id"]
        x.append(item_id2)
    cart_meals = db.execute("SELECT * FROM meals WHERE id IN (?)", x)
    return render_template("cart.html", cart_meals = cart_meals, page_id = "cart")

@app.route("/remove", methods=["GET", "POST"])
def remove():
    if request.method == "POST":
        meal_id = request.form.get("meal_id")
        db.execute("DELETE FROM cart WHERE item_id = ?", meal_id)
        # db.execute("DELETE FROM cart WHERE item_id = ?", meal_id)
        # db.execute("DELETE FROM cart WHERE item_id = ?", meal_id)
        promise = {"msg": "removing this dish from your cart"}
        return jsonify(promise)


if __name__ == '__main__':
    app.run(debug=True, port=8000, use_reloader=True, reloader_type='watchdog')

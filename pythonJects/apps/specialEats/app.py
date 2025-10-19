from flask import Flask, session, render_template, redirect, url_for, request, jsonify
from flask_session import Session
from randomModules import password_sys, password_gen
from cs50 import SQL
import json
import ast
from random import randint
db = SQL("sqlite:///specialEats.db")

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

languages = ["English", "Hausa", "Igbo", "Yoruba"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
genders = ["Male", "Female"]
@app.context_processor
def cart_countS():
    if not session.get("username"):
        n = 0
        return dict(n = n)
    userData = db.execute("SELECT id FROM userData WHERE username = ?", session.get("username"))
    for data in userData:
        user_id = data["id"]
        cartContent = db.execute("SELECT COUNT(*) AS cartCounter FROM cart WHERE user_id = ?", user_id)
    for content in cartContent:
        n = content.get("cartCounter")
        return dict(n = n)

@app.route("/")
def homepage():
    if not session.get("password"):
        return redirect("/landing")
    userData = db.execute("SELECT * FROM userData WHERE username = ? AND password = ?", session.get("username"), session.get("password"))
    for data in userData:
        first_name = data.get("first_name")
        last_name = data.get("last_name")
    return render_template("home.html", page_id = "home", langs = languages, first_name = first_name, last_name = last_name)

@app.route("/cartCount")
def cart_count():
    userData = db.execute("SELECT * FROM userData WHERE username = ?", session.get("username"))
    for data in userData:
        user_id = data["id"]
    cContent = db.execute("SELECT COUNT(*) AS cCounter FROM cart WHERE user_id = ?", user_id)
    for content in cContent:
        n2 = content.get("cCounter")
        count = {"count": n2}
    return jsonify(count)

@app.route("/landing")
def prototype():
    return render_template("landing.html", langs=languages, page_id = "landing")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        d_o_b = request.form.get("dob")
        result = password_sys(password)
        if result == "valid_password":
            user_data = db.execute("SELECT * FROM userData")
            for data in user_data:
                if data.get("username") == session.get("username") and data.get("password") == session.get("password"):
                    return redirect("/signupError")
            session["password"] = password
            session["username"] = username.lower()
            session["first_name"] = first_name
            session["last_name"] = last_name
            session["d_o_b"] = d_o_b
            db.execute("INSERT INTO userData(username, password, first_name, last_name, d_o_b, e_mail, gender, card, address) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", session.get("username"), session.get("password"), session.get("first_name"), session.get("last_name"), session.get("d_o_b"), "example@email.com", "null", " ", " ")
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
        username = request.form.get("username").lower()
        password = request.form.get("password")
        userData = db.execute("SELECT * FROM userData")
        for data in userData:
            if data.get("username") == username.lower() and data.get("password") == password:
                session["username"] = username
                session["password"] = password
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
        card = request.form.get("card")
        address = request.form.get("address")

        userData_1 = db.execute("SELECT id FROM userData WHERE username = ?", session.get("username"))
        for data_1 in userData_1:
            user_id = data_1["id"]
        #account change
        if card:
            db.execute("UPDATE userData SET card = ? WHERE id = ?", card, user_id)
            msg = {"msg": "Payment details updated"}
            return jsonify(msg)
        if address:
            db.execute("UPDATE userData SET address = ? WHERE id = ?", address, user_id)
            msg2 = {"msg": "Shipping address updated"}
            return jsonify(msg2)
        
        #bio change
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
        response = {"msg": "Updating profile..."}
        return jsonify(response)
    
    userData = db.execute("SELECT * FROM userData WHERE username = ?", session.get("username"))
    for data in userData:
        first_name = data["first_name"]
        last_name = data["last_name"]
        username = data["username"]
        e_mail = data["e_mail"]
        gender = data["gender"]
        card = data["card"]
        address = data["address"]
    return render_template("profile.html", card = card, address = address, first_name = first_name, last_name = last_name, username = username, e_mail = e_mail, genders = genders, gender = gender, page_id = "profile")

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

@app.route("/veggie")
def veggie():
    v_id = [8,10,19,24,25,26,27,35,50,51,52,57,60,63,78,85,87,86,90,91,92,93,96]
    userData = db.execute("SELECT * FROM userData WHERE username = ? AND password = ?", session.get("username"), session.get("password"))
    for data in userData:
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        meals = db.execute("SELECT * FROM meals WHERE id IN (?)", v_id)
    return render_template("veggie.html", meals = meals, page_id = "veggie", langs = languages, first_name = first_name, last_name = last_name)

@app.route("/snacks")
def snacks():
    sn_id = [20,21,22,28,28,30,40,41,51,57,60,66,78,79,83,84,85,87,88,89,90,93,97,98,99]
    userData = db.execute("SELECT * FROM userData WHERE username = ? AND password = ?", session.get("username"), session.get("password"))
    for data in userData:
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        meals = db.execute("SELECT * FROM meals WHERE id IN (?)", sn_id)
    return render_template("snacks.html", meals = meals, page_id = "snacks", langs = languages, first_name = first_name, last_name = last_name)

@app.route("/dandp")
def dandp():
    dnp_id = [11,7,31,32,33,34,35,36,99]
    userData = db.execute("SELECT * FROM userData WHERE username = ? AND password = ?", session.get("username"), session.get("password"))
    for data in userData:
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        meals = db.execute("SELECT * FROM meals WHERE id IN (?)", dnp_id)
    return render_template("dandp.html", meals = meals, page_id = "dandp", langs = languages, first_name = first_name, last_name = last_name)

@app.route("/cereal")
def cereal():
    dnp_id = [14,17,51,74,73,75,62,65]
    userData = db.execute("SELECT * FROM userData WHERE username = ? AND password = ?", session.get("username"), session.get("password"))
    for data in userData:
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        meals = db.execute("SELECT * FROM meals WHERE id IN (?)", dnp_id)
    return render_template("cereal.html", meals = meals, page_id = "cereal", langs = languages, first_name = first_name, last_name = last_name)

@app.route("/cart", methods=["GET", "POST"])
def cart():
    identity = db.execute("SELECT id FROM userData WHERE username = ?", session.get("username"))
    for user in identity:
        user_id = user.get("id")
    if request.method == "POST":
        item_id = request.form.get("item_id")
        cart_data = db.execute("SELECT * FROM cart WHERE user_id = ?", user_id)
        for item in cart_data:
            if item.get("item_id") == item_id:
                return jsonify({"msg": "This item is already in your cart"})
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
        in_cart = request.form.get("in_cart")
        if in_cart is not None:
            new_in_cart = ast.literal_eval(in_cart)
        else:
            new_in_cart = False
        if meal_id:
            db.execute("DELETE FROM cart WHERE item_id = ?", meal_id)
            promise = {"msg": "removing this dish from your cart..."}
            return jsonify(promise)
        if in_cart:
            db.execute("DELETE FROM cart WHERE item_id IN (?)", new_in_cart)
            msg = {"msg": "Ordered items are removed from cart"}
            return jsonify(msg)

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    if request.method == "POST":
        # items request is a dictionary, containes item_id as key and item_count as value
        # tPrice request contains total price
        x = []
        y = {}
        items_count = request.form.get("itemCount")
        if int(items_count) >= 3:
            n = randint(1, 20)
        else:
            n=""
        items = json.loads(request.form.get("items"))
        tPrice = request.form.get("totalPrice")
        for i in items:
            x.append(i)
        inCheckout = db.execute("SELECT url FROM meals WHERE id IN (?)", x)
        for meal, count in zip(inCheckout, items):
            y[meal.get("url")] = items[count]
        details = db.execute("SELECT * FROM userData WHERE username = ?", session.get("username"))
        for data in details:
            address = data["address"]
            card = data["card"]
        return render_template("checkout.html", items = items, x = x, address = address, card = card, paidShip = n, page_id = "checkout", co = y, tPrice = tPrice)

@app.route("/orders", methods=["GET", "POST"])
def orders():
    if request.method == "POST":
        buggy_item_info_json = request.form.get("item_info")
        #to fix the json object we need to replace every single quoted property key with double quote
        fixed_item_info_json = buggy_item_info_json.replace("'", '"')
        item_info = json.loads(fixed_item_info_json)
        orderTotal = request.form.get("orderTotal", " ")
        user_data = db.execute("SELECT id FROM userData WHERE username = ?", session.get("username"))
        for data in user_data:
            user_id = data.get("id")

        db.execute("INSERT INTO orderIDs(username) VALUES(?)", session.get("username"))
        data = db.execute("SELECT COUNT(*) AS order_id FROM orderIDs")

        #filling up the orders table with neccesary details
        for id in item_info:
            #assigning an order id
            for x in data:
                order_id = x.get("order_id")
                db.execute("INSERT INTO orders(order_id) VALUES(?)", order_id)

            db.execute("UPDATE orders SET user_id = ? WHERE order_id = ? AND user_id IS NULL", user_id, order_id)

            db.execute("UPDATE orders SET quantity = ? WHERE order_id = ? AND quantity IS NULL", item_info[id], order_id)
            db.execute("UPDATE orders SET order_total_price = ? WHERE order_id = ? AND order_total_price IS NULL", orderTotal, order_id)
            name_price = db.execute("SELECT name, price FROM meals WHERE id = ?", id)
            for info in name_price:
                name = info.get("name")
                price = info.get("price")
            db.execute("UPDATE orders SET meal = ? WHERE order_id = ? AND meal IS NULL", name, order_id)
            db.execute("UPDATE orders SET price = ? WHERE order_id = ? AND price IS NULL", price, order_id)
        return jsonify({"msg": "user order updated"})
    meals = []
    counts = []
    order_ids = []
    user = db.execute("SELECT id FROM userData WHERE username = ?", session.get("username"))
    for id in user:
        user_identity = id.get("id")

    order_details = db.execute("SELECT * FROM orders WHERE user_id = ?", user_identity)
    for details in order_details:
        order_identity = details.get("order_id")
        order_ids.append(order_identity)
        quantity = details.get("quantity")
        counts.append(quantity)
        meal_name = details.get("meal")
        meals.append(meal_name)
    name_price_img = db.execute("SELECT * FROM meals WHERE name IN (?)", meals)

    return render_template("orders.html", page_id = "orders", zip = zip, counts = counts, order_ids = order_ids, name_price_img = name_price_img)


@app.route("/redirected")
def redirected_page():
    return render_template("redirect.html")

@app.errorhandler(404)
def error(e):
    return redirect("/redirected")

if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=True, reloader_type='watchdog')

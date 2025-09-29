from cs50 import SQL

db = SQL("sqlite:///specialEats.db")

user_cart = db.execute("SELECT COUNT(*) AS cartContent FROM cart WHERE user_id = ?", 1)
for content in user_cart:
    x = content.get("cartContent")

print(x)

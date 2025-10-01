from cs50 import SQL

db = SQL("sqlite:///specialEats.db")

userData = db.execute("SELECT * FROM userData WHERE username = ?", "0xgrindpa")
for data in userData:
    user_id = data["id"]
cContent = db.execute("SELECT COUNT(*) AS cCounter FROM cart WHERE user_id = ?", user_id)

bio = {"name": "SAMUEL", "job": "Teacher"}

print(bio.get("name").lower())

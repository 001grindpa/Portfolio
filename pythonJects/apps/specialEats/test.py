from cs50 import SQL

db = SQL("sqlite:///specialEats.db")

userData = db.execute("SELECT * FROM userData WHERE username = ?", "0xgrindpa")


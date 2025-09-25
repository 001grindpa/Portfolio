from cs50 import SQL

db = SQL("sqlite:///specialEats.db")

table = db.execute("SELECT * FROM test")
for data in table:
    print(data.get("name"))

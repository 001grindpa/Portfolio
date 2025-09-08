from cs50 import SQL

db = SQL("sqlite:///app.db")

title = input("enter show title: ")

shows = db.execute("SELECT * FROM shows WHERE title LIKE ?", title + '%')

for show in shows:
    print(f"The title is {show.get('title')} released in {show.get('year')}")

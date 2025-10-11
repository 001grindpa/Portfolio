import csv

with open("meals.csv", "r") as file:
    reader = csv.reader(file)
    for meal in reader:
        print(meal)

from random import randint


def spin():
    outcome = {1 : 100000, 2: -1500, 3: "better luck next time", 4: 60000, 5: -10000, 6: 20000, 7: "better luck next time", 8: 2000, 9: "better luck next time"}

    n = randint(1, 9)

    r = outcome[n]

    return r

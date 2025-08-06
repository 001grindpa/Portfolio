from random import randint

def password_sys(password):
    if len(password) <= 8:
        return "Password must be more than 8 characters long"

    intChecker = False
    for c in password:
        if c.isdigit():
            intChecker = True
    if intChecker == False:
        return "Password must contain at least one integer"

    upperChecker = False
    for c in password:
        if c.isupper():
            upperChecker = True
    if upperChecker == False:
         return "Password must contain at least one uppercase character"

    return "valid_password"

def password_gen(number):
    generated_n = []
    for i in range(int(number)):
        x = randint(1, 9)
        generated_n.append(x)

    n_dictionary = {1:"D1@", 2:"E2#", 3:"F3$", 4:"4A", 5:"5B", 6:"6C", 7:"G7!", 8:"H8*", 9:"I9(-"}

    generated_pass = []
    for n in generated_n:
        y = n_dictionary[n]
        generated_pass.append(y)

    final = "".join(generated_pass)
    return final

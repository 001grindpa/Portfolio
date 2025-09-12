def drink_lim(uname, age):
    ready = int(age) >= 18

    if ready == True:
        return f"{uname} is within drinking age"
    else:
        return f"brah, {uname} is too young now."


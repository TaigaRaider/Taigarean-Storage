def add():
    result = a + b
    return result


def subtract():
    result = a - b
    return result


def divide():
    result = a / b
    return result


def multiply():
    result = a * b
    return result


error = f"Invalid Input!"
operator = input(f"Enter your desired operator")

a = float(input("Enter first number"))
b = float(input("Enter second number"))


def cac():
    if operator == "add":
        add()
    elif operator == "subtract":
        subtract()
    elif operator == "divide":
        divide()
    elif operator == "multiply":
        multiply()
    else:
        print(error)


cac()

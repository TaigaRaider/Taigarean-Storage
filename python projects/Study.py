import sys

error = f"Invalid Input!"

run = True

def add():
    a = float(input("Enter first number "))
    b = float(input("Enter second number "))

    result = a + b

    return result


def subtract():
    a = float(input("Enter first number "))
    b = float(input("Enter second number "))

    result = a - b

    return result


def divide():
    a = float(input("Enter first number "))
    b = float(input("Enter second number "))

    result = a / b

    return result


def multiply():
    a = float(input("Enter first number "))
    b = float(input("Enter second number "))

    result = a * b

    return result

def verify_operation():
    while run:
        if operator == "1":
            print(add())
            break

        elif operator == "2":
            print(subtract())
            break

        elif operator == "3":
            print(divide())
            break

        elif operator == "4":
            print(multiply())
            break

        elif operator == "0":
            print(f"bye")
            sys.exit()

        else:
            print(error)

def new_operation():


operator= input(f"Enter your desired operation: \n"
                 f"1. Add\n"
                 f"2. Subtract\n"
                 f"3. Divide\n"
                 f"4. Multiply\n"
                 f"0. Exit\n") #sentinel value termination

verify_operation()
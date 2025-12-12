import sys

error = f"Invalid Input!"  # simple Error Message

choices = ["1", "2", "3", "4", "-1", "multiply", "add", "divide", "subtract", "exit"]  #List of Valid Operations


def addition():  # addition
    while True:
        a = input("Enter first number ")
        b = input("Enter second number ")

        if a.isdigit() and b.isdigit():  # verification
            result = float(a) + float(b)  # Values are typecasted after verification
            return result

        else:
            print(f"ValueError: You entered a string\n"
                  f"Enter a valid number\n")


def subtraction():  # subtraction
    while True:
        a = input("Enter first number ")
        b = input("Enter second number ")

        if a.isdigit() and b.isdigit():
            result = float(a) - float(b)  # Values are typecasted after verification
            return result

        else:
            print(f"ValueError: You entered a string\n"
                  f"Enter a valid number\n")


def division():  # division
    while True:
        a = input("Enter first number ")
        b = input("Enter second number ")

        if a.isdigit() and b.isdigit():
            result = float(a) / float(b)  # Values are typecasted after verification
            return result

        else:
            print(f"ValueError: You entered a string\n"
                  f"Enter a valid number\n")


def multiplication():  # multiply
    while True:
        a = input("Enter first number ")
        b = input("Enter second number ")

        if a.isdigit() and b.isdigit():
            result = float(a) * float(b)  # Values are typecasted after verification
            return result

        else:
            print(f"ValueError: You entered a string\n"
                  f"Enter a valid number\n")


def initialize_operator():  # get Operation
    while True:
        operator = input(f"Enter your desired operation: \n"
                         f"1. Add\n"
                         f"2. Subtract\n"
                         f"3. Divide\n"
                         f"4. Multiply\n"
                         f"\n"
                         f"-1. Exit\n")  # sentinel value termination

        if operator in choices:  # verify operator is legal
            return operator

        else:
            print(f"Enter Valid Operation Choice\n")


def verify_operation():
    operator = initialize_operator()

    if operator in ("1", "add"):
        print(addition())

    elif operator in ("2", "subtract"):
        print(subtraction())

    elif operator in ("3", "divide"):
        print(division())

    elif operator in ("4", "multiply"):
        print(multiplication())

    elif operator in ("-1", "exit"):
        print(f"Bye")
        sys.exit()

    else:
        print(error)


def start_new_operation():  # Restart or Exit calculator
    while True:
        new_operation = input(f"Continue? (yes/no) ").strip().lower()
        if new_operation in ("yes", "no"):

            if new_operation == "no":  # Exit calculator
                print(f"Thanks for Using my Calculator")
                sys.exit()

            elif new_operation == "yes":  # Restart calculator
                calculator()

        else:
            print(error)


def calculator():
    verify_operation()
    start_new_operation()


calculator()

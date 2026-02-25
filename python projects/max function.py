import random

from colorama import Fore

arr = []
index = 0


def get_work_members():
    while index < members:
        try:
            member = int(input(f"Enter a number"))
            arr.append(member)
        except ValueError:
            get_work_members()


def work_main():
    members = int(input(f"How many numbers are in the group? "))

    for member in arr:
        maximum = arr[0]
        if member > maximum:
            maximum = member
    return maximum


def work_fun():
    decision = input(f"{Fore.BLUE}Do you want to have fun or do you want to just work? ")
    if decision == "work":
        workmax = work_main()
        return workmax
    elif decision == "fun":
        fun_main()
    else:
        pass

def get_numberofmembers():
    try:
        numberofmembers = int(input("How many numbers should your array contain? "))
        return numberofmembers
    except ValueError:
        print(f"Enter ONLY INTEGERS")
        get_numberofmembers()


def define_lower_boundary():
    try:
        lower_boundary = int(input("What should be the lower boundary of the array? "))
        return lower_boundary
    except ValueError:
        print(f"Enter ONLY INTEGERS")
        define_lower_boundary()


def define_upper_boundary():
    try:
        upper_boundary = int(input("What should be the upper boundary of the array? "))
        upper_boundary = upper_boundary - random.randint(0, 10)
        return upper_boundary
    except ValueError:
        print(f"Enter ONLY INTEGERS")
        define_upper_boundary()




def generate_numbers(numberofmembers, lower_boundary, upper_boundary):
    for member in range(numberofmembers):
        member = random.randint(lower_boundary, upper_boundary)
        arr.append(member)

def find_largest_member():
    while index <= len(arr) - 1:
        if index == len(arr) - 1:
            break
        if arr[index] <= arr[index + 1]:
            arr.pop(index)
        elif arr[index] >= arr[index + 1]:
            arr.pop(index + 1)
    print(arr)


def fun_main():
    lowerBoundary = define_lower_boundary()
    upperBoundary = define_upper_boundary()
    numberOfMembers = get_numberofmembers()

    generate_numbers(numberOfMembers, lowerBoundary, upperBoundary)
    print(arr)
    print(f"The Lower Boundary of this selection is: {lowerBoundary}")
    print(f"The Upper Boundary of this selection is: {upperBoundary}")
    print(f"The Number of Members in this selection is: {numberOfMembers}")
    find_largest_member()


work_fun()

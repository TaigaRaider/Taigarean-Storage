import random

arr = []
index = 0


def get_numberofmembers():
    numberofmembers = int(input("How many numbers should your array contain? "))
    return numberofmembers


def define_lower_boundary():
    lower_boundary = int(input("What should be the lower boundary of the array? "))
    lower_boundary = lower_boundary - random.randint(0, 10)
    return lower_boundary


def define_upper_boundary():
    upper_boundary = int(input("What should be the upper boundary of the array? "))
    return upper_boundary


def validate_values(numberofmembers, lower_boundary, upper_boundary):
    if numberofmembers & upper_boundary & lower_boundary.is_integer():
        return
    else:
        print(f"Enter only INTEGERS!")


def generate_numbers(numberofmembers, lower_boundary, upper_boundary):
    for member in range(numberofmembers):
        member = random.randint(lower_boundary, upper_boundary)
        arr.append(member)


lowerBoundary = define_lower_boundary()
upperBoundary = define_upper_boundary()
numberOfMembers = get_numberofmembers()


def find_largest_member():
    validate_values(numberOfMembers, lowerBoundary, upperBoundary)
    generate_numbers(numberOfMembers, lowerBoundary, upperBoundary)

    print(arr)

    while index <= len(arr) - 1:
        if index == len(arr) - 1:
            break
        if arr[index] <= arr[index + 1]:
            arr.pop(index)
        elif arr[index] >= arr[index + 1]:
            arr.pop(index + 1)
    print(arr)


find_largest_member()

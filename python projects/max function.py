import random

from colorama import Fore

arr = []
index = 0


def int_error():
    print(f"Enter ONLY INTEGERS")


def get_work_members(members, work_index):
    work_array = []
    while work_index < members:
        try:
            member = int(input(f"Enter a number "))
            work_array.append(member)
            work_index += 1
            print(f"{work_array}, {work_index}")
        except ValueError:
            int_error()
            get_work_members(members, work_index)

        if work_index == members:
            print("Done!")
    return work_array


def define_number_of_members():
    try:
        members = int(input(f"How many numbers are in the group? "))

        return members
    except ValueError:
        int_error()
        define_number_of_members()


def work():
    work_array = get_work_members(define_number_of_members(), 0)
    work_maximum = work_array[0]

    for member in work_array:
        if member > work_maximum:
            work_maximum = member
    return work_maximum


def main():
    decision = input(
        f"{Fore.RED}Do you want to have {Fore.YELLOW}fun{Fore.RED} or do you want to just {Fore.CYAN}work? ").strip().lower()
    if decision == "work":
        return print(work())
    elif decision == "fun":
        return fun()
    else:
        print("ERROR Invalid input!")
        return main()


def get_numberofmembers():
    try:
        numberofmembers = int(input("How many numbers should your array contain? "))
        return numberofmembers
    except ValueError:
        int_error()
        get_numberofmembers()


def define_lower_boundary():
    try:
        lower_boundary = int(input("What should be the lower boundary of the array? "))
        return lower_boundary
    except ValueError:
        int_error()
        define_lower_boundary()


def define_upper_boundary(lower_boundary):
    try:
        upper_boundary = int(input("What should be the upper boundary of the array? "))
        upper_boundary = upper_boundary - random.randint(0, 10)
        return upper_boundary
    except ValueError:
        int_error()
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


def fun():
    lowerboundary = define_lower_boundary()
    upperboundary = define_upper_boundary()
    numberofmembers = get_numberofmembers()

    generate_numbers(numberofmembers, lowerboundary, upperboundary)
    print(arr)
    print(f"The Lower Boundary of this selection is: {lowerboundary}")
    print(f"The Upper Boundary of this selection is: {upperboundary}")
    print(f"The Number of Members in this selection is: {numberofmembers}")
    find_largest_member()


if __name__ == '__main__':
    main()

#         if lower_boundary < upper_boundary:
#             upper_boundary = upper_boundary
#         else:

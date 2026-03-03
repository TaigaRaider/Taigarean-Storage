import random
from colorama import Fore   #this was done just for fun

arr = []
random_difference = random.randint(0, 10)

global_index = 0


def int_error():    #Reusability!
    print(f"Enter ONLY INTEGERS")

#redesign required
def get_work_members(members, work_index):
    #I defined a new parameter index here specifically for the work function;
    #To eliminate the need for creating a new variable for it and also ease accessibility

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
        #The try-except statements are used here to prevent crashing due ValueError from inserting a string
        # or any non integer into an integer variable

    print("Done!")
        #This is a teaser to an incoming feature;
        #where I will implement the time module to mae the fun function much more interactive, Stay Tuned.
    return work_array


def define_number_of_members():
    try:
        members = int(input(f"How many numbers are in the group? "))

        return members
    except ValueError:
        int_error()
        define_number_of_members()


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


def define_upper_boundary():
    try:
        upper_boundary = int(input("What should be the upper boundary of the array? "))
        upper_boundary = upper_boundary - random_difference

        return upper_boundary
    except ValueError:
        int_error()
        define_upper_boundary()


def maintain_boundary_range_balance(lower_boundary, upper_boundary):
    if upper_boundary<lower_boundary:
        upper_boundary = upper_boundary + random_difference
    else:
        upper_boundary = upper_boundary
        #Just for the sake of a complete if-else statement, I equated the upper boundary to the same value passed as an argument.
    return upper_boundary


def generate_numbers(numberofmembers, lower_boundary, upper_boundary):
    for member in range(numberofmembers):
        member = random.randint(lower_boundary, upper_boundary)
        arr.append(member)


def find_largest_member():
    index = global_index
    while index <= len(arr) - 1:
        if index == len(arr) - 1:
            break
        #This ensures the while loop is terminated when all members have been evaluated

        if arr[index] <= arr[index + 1]:
            arr.pop(index)
        elif arr[index] >= arr[index + 1]:
            arr.pop(index + 1)
        #The pop method allows us to remove the lesser element in the collection
    print(arr)


def work():
    work_array = get_work_members(define_number_of_members(), 0)
    work_maximum = work_array[0]
    #Here the max is set to the first element in the collection

    for member in work_array:
        if member > work_maximum:
            work_maximum = member
    #The algorithms for the fun and work max functions are different just because I wanted test the different ways I could
    #evaluate the largest element in a collection

    return work_maximum


def fun():
    lowerboundary = define_lower_boundary()
    upperboundary = define_upper_boundary()
    numberofmembers = get_numberofmembers()

    upperboundary = maintain_boundary_range_balance(lowerboundary, upperboundary)
    #I restated the value of upper_boundary just incase the random difference doesn't set off an error with the random.randrange function
    generate_numbers(numberofmembers, lowerboundary, upperboundary)

    print(arr)
    print(f"The Lower Boundary of this selection is: {lowerboundary}")
    print(f"The Upper Boundary of this selection is: {upperboundary}")
    print(f"The Number of Members in this selection is: {numberofmembers}")

    find_largest_member()


def main():     #the main function of the code that sums up all relevant outcomes of this program
    decision = input(
        f"{Fore.RED}Do you want to have {Fore.YELLOW}fun{Fore.RED} or do you want to just {Fore.CYAN}work? ").strip().lower()
    if decision == "work":
        return print(work())
    elif decision == "fun":
        return fun()
    else:
        print("ERROR Invalid input!")
        return main()


if __name__ == '__main__':  #This ensures ease of access when this script is imported into another script
    main()
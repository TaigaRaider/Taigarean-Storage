import random

error = f'Invalid choice!'  # error message


def roll_1_die():  # dice roll function for 1 die.
    first_dice = random.randint(1, 6)
    return first_dice


def roll_2_die():  # dice roll function for 2 dies.
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)

    return first_dice, second_dice


def roll_num():  # confirm the number of times to roll.
    while True:
        num_of_roll = input(f"How many times would you like to roll? (1/2) ")
        if num_of_roll == '1':
            die_play = roll_1_die()
            break

        elif num_of_roll == '2':
            die_play = roll_2_die()
            break

        else:
            print(error)

    return die_play


counter = 0  # count variable; set to 0 as origin.


def count_msg():  # count message function to ensure proper grammar as the counter changes to and from 1.
    counter_message = f"You have spun {counter} times"
    if int(counter) == 1:
        counter_message = f"You have spun {counter} time"
    else:
        counter_message = counter_message
    return counter_message


while True:  # main loop
    roll = input('Would you like to roll (y/n)? ').strip().lower()  # ask for input
    if roll in ('y', 'n'):
        if roll == 'n':
            print(f"Thanks for playing!")
            break

        else:
            print(roll_num())
            counter += 1
            print(count_msg())

    else:
        print(error)

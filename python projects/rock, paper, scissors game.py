import random
import sys

error = f"Invalid choice!"      #simple error message

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
choices = {     #dictionary for key-value pairs
    ROCK: '🪨',
    PAPER: '📃',
    SCISSORS: '✂️'
}


choice_list = tuple(choices.keys())     #tuple used to prevent unnecessary changes
leave = "quit"

def player_input():
    while True:
        player_choice = input(f"Rock, paper or scissors? (r/p/s) ").strip().lower()
        if player_choice in choice_list:  # verify the player's choice
            return player_choice
        elif player_choice == leave:
            print(f"Bye")
            sys.exit()
        else:
            print(error)

def display_choice(player_choice, computer_choice):
    print(f"You picked{choices[player_choice]}\n"
          f"Computer picked{choices[computer_choice]}")


def determine_winner(player_choice, computer_choice):
    while True:
        if  player_choice == computer_choice:
            return f"It's a Tie!"
        elif ((player_choice == ROCK and computer_choice == SCISSORS) or
              (player_choice == PAPER and computer_choice == ROCK) or
              (player_choice == SCISSORS and computer_choice == PAPER)):
            return f"You won!"

        else:
            return f"You lose!"


def game_play():
    while True:
        player_choice = player_input()
        computer_choice = random.choice(choice_list)
        display_choice(player_choice,computer_choice)
        print(determine_winner(player_choice, computer_choice))

        while determine_winner(player_choice, computer_choice) == "You won!":
            replay = input(f"Continue? (y/n) ").strip().lower()
            if replay in ("y", "n"):

                if replay == "n":
                    print(f"Thanks for playing")
                    sys.exit()

                elif replay == "y":
                    game_play()

            else:
                print(error)


game_play()
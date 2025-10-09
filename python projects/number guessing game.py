import random

number_to_guess = random.randint(1, 100)
is_guessed = False
winner = f'Congratulations! You guessed the number'
error = f'Invalid choice!'
while not is_guessed:
    try:
        guess = int(input(f'Guess the number between 1 and 100: '))

        if 1 <= guess <=100:    #confirm guess validity
            if guess == number_to_guess:
                print(winner)
                is_guessed = True
            elif guess < number_to_guess:
                print(f'Too low!')
            elif guess > number_to_guess:
                print(f'Too high!')
        else:
            print(error)
    except ValueError:  #prevert crash if guess isn't an integer
        print(error)
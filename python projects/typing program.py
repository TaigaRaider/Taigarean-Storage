import sys
import time

time_choice = (0.01,0.02,0.03,0.04,0.05)
def typing_animation():
    message = {

    }
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

typing_animation()
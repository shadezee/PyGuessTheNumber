# Create a guess the number program and copy its answer to clipboard
"""ALGORITHM????
set a variable with a random value
ask user to guess and enter value
If value is equal to variable say with
If value is not equal to variable let the loop begin again.
After 10 attempts, end program and copy answer to clipboard.
"""

import random, pyperclip, time


print("Enter your name:")
Pname = input()


def objective():
    print("Hi " + Pname + ", Welcome to Guess the Number.")
    time.sleep(3)
    print("Here are the rules.")
    time.sleep(2)
    print("The program will pick any random number between 0 to 20.")
    time.sleep(4)
    print("Your job is to guess that number correctly in 10 attempts.")
    time.sleep(4)
    print("Let us begin!")
    time.sleep(3)
    print()


objective()
secret = random.randint(0, 20)

for number_guess in range(1, 10):
    print("Guess the number, " + Pname + ".")
    guess = int(input())

    if guess < secret:
        print("Try going higher.")
    elif guess > secret:
        print("Try going lower")
    else:
        if number_guess == 10:
            print("You are out of attempts, try again.")
        else:
            break
        break

if number_guess == 1 and guess == secret:
    print("Yay you guessed it right in a single attempt " + Pname + "!!!")
elif guess == secret and number_guess > 1:
    print(
        "Yay you guessed it right in " + str(number_guess) + " attempts, " + Pname + "!"
    )
else:
    print("Oof you could not guess it, the answer has been copied to your clipboard.")
    pyperclip.copy("The correct number was " + str(secret) + ".")

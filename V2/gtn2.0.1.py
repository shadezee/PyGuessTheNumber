# Allow replay functionality
import random, time

secret = random.randint(0, 20)

print("Enter your name:")
name = input()

def objective():
    print("Hi " + name + ", Welcome to Guess the Number.")
    time.sleep(3)
    print("Here are the rules.")
    time.sleep(2)
    print("The program will pick any random number from 0 to 20.")
    time.sleep(4)
    print("Your job is to guess that number in 10 attempts.")
    time.sleep(4)
    print("Let's begin!")
    time.sleep(3)
    print("Enter the number, " + name + "...")
    guessGame(secret)


def replay():
    print("Would you like to play again (Y\\N)?")
    rep = input().lower()
    if rep == "y":
        newSecret = random.randint(0, 20)
        print("Enter the number: ")
        guessGame(newSecret)


def guessGame(inputSec):
    secret = inputSec
    for attempts in range(1, 11):
        guess = int(input())

        if (attempts == 1) and (guess == secret):
            print("Yay you guessed it right in a single attempt!!!")
            break
        elif attempts == 10:
            print("Oof you ran out of attempts, the number was " + str(secret) + ".")
            break
        else:
            if guess == secret:
                print("Yay you guessed it right in " + str(attempts) + " attempts.")
                break
            else:
                if guess > secret:
                    print("Try again but go lower...")
                if guess < secret:
                    print("Try again but go higher.")
    replay()

objective()
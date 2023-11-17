# code re-write
import random, time

secret = random.randint(0, 20)

print("Enter your name:")
name = input()

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


for attempts in range(1, 11):
    guess = int(input())

    if (attempts == 1) and (guess == secret):
        print("Yay you guessed it right in a single attempt!!!")
    elif attempts == 10:
        print("Oof you ran out of attempts, the number was " + str(secret) + ".")
    else:
        if guess == secret:
            print("Yay you guessed it right in " + str(attempts) + " attempts.")
        else:
            if guess > secret:
                print("Try again but go lower...")
            if guess < secret:
                print("Try again but go higher.")

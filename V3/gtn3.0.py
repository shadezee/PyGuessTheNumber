# Introduce new variation
import logging, os, platform, random, shutil, socket, time, psutil
from cryptography.fernet import Fernet


runningDirectoryPath = os.path.dirname(os.path.abspath(__file__))
logDirectoryPath = runningDirectoryPath + "\log"
logFilePath = logDirectoryPath + "\logFile.log"

if os.path.exists(logDirectoryPath) == False:
    os.makedirs(logDirectoryPath)

try:
    shutil.copy(logFilePath, (logDirectoryPath + "\logOld.log"))
except FileNotFoundError:
    pass

logging.basicConfig(
    filename=logFilePath,
    filemode="w",
    level=logging.NOTSET,
    format=
    "%(asctime)s - %(funcName)s - %(levelname)s - %(processName)s - %(message)s",
)

logging.warning("Running version 3.0")

class invalidChoiceException(Exception):

    def __init__(self, args):
        self.args = args
        print(str(args) + " is not a valid entry. Please try again...")
        time.sleep(1)


class Type1:

    def objective():
        logging.debug("START: game objectives.")
        print("Hi " + GTNClass.name + ", Welcome to Guess the Number.")
        time.sleep(3)
        print("Here's how it goes!")
        time.sleep(2)
        print("The program will pick any random number from 0 to 20.")
        time.sleep(4)
        print("Your job is to guess that number in 10 attempts.")
        time.sleep(4)
        print("Let's begin!")
        time.sleep(3)
        logging.debug("END: game objectives.")
        Type1.guessGame(GTNClass.secretType1)

    def replay():
        replayCounter = 1
        loopCounter1 = 0
        logging.debug("function replay called for " + str(replayCounter))
        print("Would you like to play again (Y\\N)?")
        while loopCounter1 == 0:
            try:
                rep = input().lower()
                if rep == "y":
                    logging.critical("DECISION: REPLAY")
                    newSecret = random.randint(0, 20)
                    Type1.guessGame(newSecret)
                    break
                elif rep == "n":
                    loopCounter1 = 1
                    replayCounter += 1
                    print("The application will close in 3 seconds...")
                    time.sleep(3)
                    logging.warning("APPLICATION CLOSED.")
                    break
                else:
                    raise invalidChoiceException(rep)
            except invalidChoiceException:
                replayCounter += 1

    def guessGame(inputSec):
        secret = inputSec
        loopCounter2 = 1
        while loopCounter2 == 1:
            try:
                for attempts in range(1, 11):
                    logging.debug("running game @" + str(attempts))
                    guess = int(
                        input("Enter the number, " + GTNClass.name + "...\n"))

                    if (attempts == 1) and (guess == secret):
                        print(
                            "Yay you guessed it right in a single attempt!!!")
                        logging.critical("DECISION: SMART")
                        loopCounter2 = 0
                        break
                    elif attempts == 10:
                        print("Oof you ran out of attempts, the number was " +
                              str(secret) + ".")
                        loopCounter2 = 0
                        logging.critical("DECISION: OUT OF ATTEMPTS")
                        break
                    else:
                        if guess == secret:
                            print("Yay you guessed it right in " +
                                  str(attempts) + " attempts.")
                            logging.critical("DECISION: CYCLE COMPLETE.")
                            loopCounter2 = 0
                            break
                        else:
                            if guess == (secret - 1):
                                print("Just a little more...")
                            elif guess == (secret + 1):
                                print("Just a little less...")
                            elif guess > secret:
                                print("Try again but go lower...")
                            elif guess < secret:
                                print("Try again but go higher...")
                        print()
            except ValueError:
                logging.warning(f"invalid number for comparison")
                print("Value entered is not a valid input, try again...")
                time.sleep(2)
        logging.debug("call replay")
        Type1.replay()

    def cycleOne():
        print(
            f"Hi {GTNClass.name}, would you like to know the game objectives (Y\\N)?"
        )
        while True:
            try:
                tut = input().lower()
                if tut == "y":
                    logging.debug(f"objective function called")
                    Type1.objective()
                    break
                elif tut == "n":
                    logging.debug(f"objective function skipped")
                    Type1.guessGame(GTNClass.secretType1)
                    break
                else:
                    raise invalidChoiceException(tut)
            except invalidChoiceException:
                pass


class Type2:

    def objective():
        logging.debug("START: Type2 game objectives.")
        print("Hi " + GTNClass.name + ", Welcome to Guess the Number.")
        time.sleep(3)
        print("Here's how it goes!")
        time.sleep(2)
        print("The program will pick any random number from 11 to 41.")
        time.sleep(4)
        print("Your job is to guess that number in 5 attempts.")
        time.sleep(2)
        print("2 hints will be provided to you.")
        time.sleep(2)
        print("Let's begin!")
        time.sleep(3)
        logging.debug("END: Type2 game objectives.")
        Type2.guessGame(GTNClass.secretType2)

    def numCat(inputNum):
        logging.debug("generating hint1")
        hint1 = ""
        isPrime = True
        if (inputNum % 2) == 0:
            hint1 = "Number is Even"
        elif (inputNum % 2) != 0:
            for divisor in range(2, int(inputNum / 2)):
                if (inputNum % divisor) == 0:
                    isPrime = False
            if isPrime == False:
                hint1 = "Number is Odd"
            else:
                hint1 = "Number is Prime."
        return hint1

    def sumDigSum(inputNum):
        logging.debug("generating hint2")
        hint2 = ""
        sumNum = 0
        for digits in str(inputNum):
            sumNum = sumNum + int(digits)

        hint2 = f"The sum of digits in number is {sumNum}"
        return hint2

    def replay():
        replayCounter = 1
        loopCounter1 = 0
        logging.debug("function replay called for " + str(replayCounter))
        print("Would you like to play again (Y\\N)?")
        while loopCounter1 == 0:
            try:
                rep = input().lower()
                if rep == "y":
                    logging.critical("DECISION: REPLAY")
                    newSecret = random.randint(11, 41)
                    Type2.guessGame(newSecret)
                    break
                elif rep == "n":
                    loopCounter1 = 1
                    replayCounter += 1
                    print("The application will close in 3 seconds...")
                    time.sleep(3)
                    logging.warning("APPLICATION CLOSED.")
                    break
                else:
                    raise invalidChoiceException(rep)
            except invalidChoiceException:
                replayCounter += 1

    def guessGame(inputSec):
        logging.debug("running main for type2")
        secret = inputSec
        getHint1 = Type2.numCat(secret)
        print(getHint1)
        getHint2 = Type2.sumDigSum(secret)
        print(getHint2)
        loopCounter2 = 1
        while loopCounter2 == 1:
            try:
                for attempts in range(1, 6):
                    logging.debug("running Type2 game @" + str(attempts))
                    guess = int(
                        input("Enter the number, " + GTNClass.name + "...\n"))
                    if (attempts == 1) and (guess == secret):
                        print(
                            "Yay smarty, you guessed it right in a single attempt!!!"
                        )
                        logging.critical("DECISION: SMART")
                        loopCounter2 = 0
                        break
                    elif (attempts == 5) and (guess == secret):
                        print(f"Yup, finally you guessed it right.")
                        loopCounter2 = 0
                        logging.critical("DECISION: FINAL ATTEMPT RIGHT")
                        break
                    elif (attempts == 5) and (guess != secret):
                        print("Oof you ran out of attempts, the number was " +
                              str(secret) + ".")
                        loopCounter2 = 0
                        logging.critical("DECISION: OUT OF ATTEMPTS")
                        break
                    else:
                        if guess == secret:
                            print("Yay you guessed it right in " +
                                  str(attempts) + " attempts.")
                            logging.critical("DECISION: CYCLE COMPLETE.")
                            loopCounter2 = 0
                            break
                        else:
                            if guess == (secret - 1):
                                print("Just a little more...")
                            elif guess == (secret + 1):
                                print("Just a little less...")
                            elif guess > secret:
                                print("Try again but go lower...")
                            elif guess < secret:
                                print("Try again but go higher...")
                        print()
            except ValueError:
                logging.warning(f"invalid number for comparison")
                print("Value entered is not a valid input, try again...")
                time.sleep(2)
        logging.debug("call type2 replay")
        Type2.replay()

    def cycleOne():
        print(
            f"Hi {GTNClass.name}, would you like to know the game objectives (Y\\N)?"
        )
        while True:
            try:
                tut = input().lower()
                if tut == "y":
                    logging.debug(f"objective function called")
                    Type2.objective()
                    break
                elif tut == "n":
                    logging.debug(f"objective function skipped")
                    Type2.guessGame(GTNClass.secretType2)
                    break
                else:
                    raise invalidChoiceException(tut)
            except invalidChoiceException:
                pass


class GTNClass:

    def initSecretT1():
        secretType1 = random.randint(0, 20)
        logging.debug("secretType1 initialized.")
        return secretType1

    def initSecretT2():
        secretType2 = random.randint(11, 41)
        if secretType2 < 11:
            print(1223345576657658585)
        logging.debug("secretType2 initialized.")
        return secretType2

    def getName():
        print("Enter your name:")
        name = input()
        logging.debug("player name initialized.")
        return name

    name = getName()
    secretType1 = initSecretT1()
    secretType2 = initSecretT2()

    def systemInfo():
        logging.info("platform: " + platform.system())
        logging.info("platform-release: " + platform.release())
        logging.info("platform-version: " + platform.version())
        logging.info("architecture: " + platform.machine())
        logging.info("hostname: " + socket.gethostname())
        logging.info("processor: " + platform.processor())
        logging.info("RAM: " +
                     str(round(psutil.virtual_memory().total /
                               (1024.0**3), 4)))
        logging.info("The program is running in " + str(runningDirectoryPath))

    def chooseType():
        print(f"Pick the type of game you want to play:\n \
            1. Type1- standard guess the number with 10 attempts.\n\n \
            2. Type2- guess the number in 5 attempts with two hints provided.\n\n \
            3. Enter 3 to exit.")
        while True:
            try:
                typeChosen = int(input("Type: "))
                if typeChosen == 1:
                    logging.warning("starting cycle for type1")
                    Type1.cycleOne()
                    break
                elif typeChosen == 2:
                    logging.warning("starting cycle for type2")
                    Type2.cycleOne()
                    break
                elif typeChosen == 3:
                    logging.warning("APPLICATION CLOSED.")
                    break
                else:
                    raise invalidChoiceException(typeChosen)
            except invalidChoiceException:
                pass
            except ValueError:
                print(f"Value entered is not a valid input, try again...")
                pass
            except TypeError:
                print(f"Value entered is not a valid input, try again...")
                pass

    def start():

        GTNClass.systemInfo()
        GTNClass.chooseType()
        GTNClass.enc()

    def enc():
        logging.critical("enc loaded")
        secretK = "LiiOAVcW5SfB_2I6QCsnxfNgv50hypUUtesyOkokjNk="
        f = Fernet(secretK)
        finTime = time.perf_counter()
        logging.warning("Finished execution in " +
                        str(round(finTime - startTime, 2)) + " seconds.")
        logging.warning("terminating logs")

        with open(logFilePath, "rb") as inpLog:
            data = inpLog.read()
            inpLog.close()

        encData = f.encrypt(data)

        with open(logFilePath, "wb") as outLog:
            outLog.write(encData)
            outLog.close()


startTime = time.perf_counter()
GTNClass.start()

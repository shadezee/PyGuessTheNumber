# Initiating logging
import random, time, os, shutil, logging, platform, socket, psutil

runningDirectoryPath = os.path.dirname(os.path.abspath(__file__))
logDirectoryPath = runningDirectoryPath + "\log"
logFilePath = logDirectoryPath + "\logFile.log"

if os.path.exists(logDirectoryPath) == False:
    os.makedirs(logDirectoryPath)

try:
    shutil.copy(logFilePath, (logDirectoryPath + "\logOld.log"))
except FileNotFoundError:
    print()

logging.basicConfig(
    filename=logFilePath,
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(funcName)s - %(levelname)s - %(processName)s - %(message)s",
)

logging.warning("Running version 2.2")


def systemInfo():
    logging.info("platform: " + platform.system())
    logging.info("platform-release: " + platform.release())
    logging.info("platform-version: " + platform.version())
    logging.info("architecture: " + platform.machine())
    logging.info("hostname: " + socket.gethostname())
    logging.info("processor: " + platform.processor())
    logging.info("RAM: " + str(round(psutil.virtual_memory().total / (1024.0**3), 3)))
    logging.info("The program is running in " + str(runningDirectoryPath))


systemInfo()

secret = random.randint(0, 20)
logging.debug("secret initialized.")

print("Enter your name:")
name = input()
logging.debug("player name initialized.")


def objective():
    logging.debug("START: game objectives.")
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
    logging.debug("END: game objectives.")
    guessGame(secret)


def replay():
    logging.debug("function replay called")
    print("Would you like to play again (Y\\N)?")
    rep = input().lower()
    if rep == "y":
        logging.critical("DECISION: REPLAY")
        newSecret = random.randint(0, 20)
        print("Enter the number: ")
        guessGame(newSecret)
    else:
        logging.warning("APPLICATION CLOSED.")


def guessGame(inputSec):
    secret = inputSec
    for attempts in range(1, 11):
        guess = int(input())
        logging.debug("running game @" + str(attempts))

        if (attempts == 1) and (guess == secret):
            print("Yay you guessed it right in a single attempt!!!")
            logging.critical("DECISION: SMART")
            break
        elif attempts == 10:
            print("Oof you ran out of attempts, the number was " + str(secret) + ".")
            logging.critical("DECISION: OUT OF ATTEMPTS")
            break
        else:
            if guess == secret:
                print("Yay you guessed it right in " + str(attempts) + " attempts.")
                logging.critical("DECISION: CYCLE COMPLETE.")
                break
            else:
                if guess > secret:
                    print("Try again but go lower...")
                if guess < secret:
                    print("Try again but go higher.")

    logging.debug("call replay")
    replay()


logging.debug("START: 1st cycle.")
objective()

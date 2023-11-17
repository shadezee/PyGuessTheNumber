import random, time, os, shutil, logging, platform, socket, psutil
from cryptography.fernet import Fernet

runningDirectoryPath = os.path.dirname(os.path.abspath(__file__))
# logDirectoryPath = runningDirectoryPath + "\log"
# logFilePath = logDirectoryPath + "\logFile.log"
logFilePath = input("Enter file path: ")

newF = input("Create new file (Y/N)? ").lower()

# with open("key.key", "rb") as keyF:
#     secretK = keyF.read()
#     keyF.close()
secretK = "LiiOAVcW5SfB_2I6QCsnxfNgv50hypUUtesyOkokjNk="
f = Fernet(secretK)
with open(logFilePath, "rb") as decInp:
    newData = decInp.read()
    decInp.close()
newD1 = f.decrypt(newData)

if newF == "n":
    with open(logFilePath, "wb") as outInp:
        outInp.write(newD1)
        outInp.close()
    print('File Overwritten')
else:
    newFile = runningDirectoryPath + "\decryptedLog.log"
    with open(newFile, "wb") as outInp:
        outInp.write(newD1)
        outInp.close()
    print(f"New file created at {runningDirectoryPath}."f"You may exit the program.")
    time.sleep(5)

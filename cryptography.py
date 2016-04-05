"""
cryptography.py
Author: Eli Woloshin
Credit: none
Assignment:
Write and submit a program that encrypts and decrypts user data.
See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
z = input("Enter e to encrypt, d to decrypt, or q to quit: ")
message = input("Message: ")
key = input("Key: ")

if z == "e":
    associations.find(a) + key.find(a)
    if z == "d":
        print()

if z != "q" and z != "e" and z != "d":
    print("Did not understand command, try again.")
if z == "q":
    print("Goodbye!")

#associations.find("e")
#associations[index]
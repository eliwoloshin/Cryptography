"""
cryptography.py
Author: Eli Woloshin
Credit: none
Assignment:
Write and submit a program that encrypts and decrypts user data.
See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"


#while key.count <= message.count:
    #print()
z=""
while z !="q":
    z = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    message = input("Message: ")
    key = input("Key: ")
    a=[]
    for c in message:
        a.append(c)
    b=[]
    for c in key:
        b.append(c)
    print(a)
    print(b)
    g=len(message)*key
    key=g
    if z == "e":
        c=[]
        tuples = zip(a, b)
        for x in tuples:
            n=associations.find(x[0])
            m=associations.find(x[1])
            e=m+n
            c.append(associations[e])
        print(c)
    elif z == "d":
        print()
    elif z != "q" and z != "e" and z != "d":
        print("Did not understand command, try again.")
if z == "q":
    print("Goodbye!")


#associations.find("e")
#associations[index]



#!/usr/bin/env python3


import math
import random
import string

list1 = " " + string.ascii_letters + string.punctuation + string.digits
list1 = list(list1)

list2 = list1.copy()
random.shuffle(list2)

def encr(option1):

    if option1 == "yes":
        original = input("Enter the string : ")
        print(f"Original String is {original}")
        encrypted = ""

        for letter in original:
            index1 = original.index(letter)
            encrypted += list2[index1]

    else:
        print("Thanks for using this tool")

    print(f"Encrpted String is {encrypted}")
    return encrypted,original

def decr(option2,encrypted,original):
    if option2 == "yes":
        decrypted = ""

        for char in encrypted:
            index2 = encrypted.index(char)
            decrypted += original[index2]

        print(f"Decrypted String String is {decrypted}")
        print(f"Decrypted String : {decrypted}")
    else:
        print("Thanks for choosing the tool")

print("Welcome to Encrypt/Decrypt Tool")
option1 = input("Do you want to encrypt any string - yes/no : ")

if option1 == "yes":
    output = encr(option1)
    print(output)
    option2 = input(f"Do you want to decrypt {output[0]} - yes/no : ")
    decr(option2,output[0],output[1])
else:
    print("Thanks for choosing the tool")


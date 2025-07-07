#!/usr/bin/env python3 

import random

options = ["rock", "paper", "scissors"]
replay = "yes"

while replay == "yes":
    player1 = input("Enter your choice : ")
    computer = random.choice(options)
    print(f"Computer's Choice : {computer}")
    if player1 == computer:
        print("Its a tie")
    elif player1 == "rock" and computer == "scissors":
        print("You win")
    elif player1 == "scissors" and computer == "paper":
        print("You win")
    elif player1 == "paper" and computer == "rock":
        print("You win")
    else:
        print("You loose")

    replay = input("Do you want to play (yes/no) : ")

print("Thanks for playing Rock/Paper/Scissors.")


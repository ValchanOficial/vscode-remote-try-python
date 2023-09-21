#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# import random module
import random

# create a list of play options
t = ["Rock", "Paper", "Scissors"]
player_score = 0
computer_score = 0
rounds = 0

# assign a random play to the computer
computer = t[random.randint(0,2)]

# set player to False
player = False

while player == False:
# set player to True
    player = input("Rock, Paper, Scissors?")
    rounds += 1
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            computer_score += 1
        else:
            print("You win!", player, "smashes", computer)
            player_score += 1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            computer_score += 1
        else:
            print("You win!", player, "covers", computer)
            player_score += 1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            computer_score += 1
        else:
            print("You win!", player, "cut", computer)
            player_score += 1
    else:
        print("That's not a valid play. Check your spelling!")

    computer = t[random.randint(0,2)]

    # check if player wants to continue
    player = input("Do you want to play again? (yes/no)")
    if player == "yes":
        player = False
    elif player == "no":
        print("Final Scores:")
        print("Player score: ", player_score)
        print("Computer score: ", computer_score)
        print("Number of rounds: ", rounds)        
        player = True
    else:
        print("That's not a valid answer. Check your spelling!")
        player = False


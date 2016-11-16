# In a big loop for each game

# User enters rock paper scissors

# PC randomises an answer and prints it asap

# Determins a win or loss

# Starts game again

import random
import time

# returns true if choice1 is the winner
def CheckWin(choice1, choice2):
    choice1looser = (choice1-1) % 3
    return choice1looser == choice2

random.seed(time.time())

idToWord = { 0 : "rock", 1 : "paper", 2 : "scissors"}
wordToId = { "rock" : 0, "paper" : 1, "scissors" : 2}

command = ''
while command != "stop":
    command = input("Please enter rock, paper or scissors: ")
    if command == "done":
        break
    choice = wordToId[command]

    computerchoice = int(random.randint(0, 2))
    computercommand = idToWord[computerchoice]

    print("PC chose {}".format(computercommand))

    if CheckWin(choice, computerchoice):
        print("You win!")
    elif choice == computerchoice:
        print("Tied!")
    else:
        print("You lose!")


# In a big loop for each game

# User enters rock paper scissors

# PC randomises an answer and prints it asap

# Determins a win or loss

# Starts game again

import random
import time

random.seed(time.time())

command = ''
while command != "stop":
    command = input("Please enter rock, paper or scissors: ")
    if command == "done":
        break
    choice = -1
    if command == "rock":
        choice = 0
    elif command == "paper":
        choice = 1
    elif command == "scissors":
        choice = 2
    elif command == "stop":
        break

    computercommand = ""
    computerchoice = int(random.randint(0, 2))
    if computerchoice == 0:
    computercommand = "rock"
    elif computerchoice == 1:
        computercommand = "paper"
    elif computerchoice == 2:
        computercommand = "scissors"

    print("PC chose {}".format(computercommand))

    if (((choice-1) % 3) == computerchoice):
        print("You win!")
    elif choice == computerchoice:
        print("Tied!")
    else:
        print("You lose!")

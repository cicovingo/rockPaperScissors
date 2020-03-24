#assign a random play to the computer
from random import randint

#create a list of play options
t = ["r", "p", "s"]

#set player to False
player = False

print("Welcome Rock, Paper and Scissors Game!!!\n")

while player != True:
  #assign a random play to the computer
  computer = t[randint(-1,2)]
  #set player to True
  player = input("Please enter r for Rock, p for Paper, s for Scissors, e for Exit\n")
  if player == computer:
    print("Tie!")
  elif player == "r":
    if computer == "p":
      print("You lose!", computer, "covers", player)
    else:
      print("You win!", player, "smashes", computer)
  elif player == "p":
    if computer == "s":
      print("You lose!", computer, "cut", player)
    else:
      print("You win!", player, "covers", computer)
  elif player == "s":
    if computer == "r":
      print("You lose...", computer, "smashes", player)
    else:
      print("You win!", player, "cut", computer)
  elif player == "e":
    player = True
  else:
    print("That's not a valid command. Check your spelling!")
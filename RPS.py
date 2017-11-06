"""this program will play rock paper scissors with you """
from random import randint
from time import sleep

options = ["R", "P", "S"]

lose = "You Lose"
win = "You Win!"

def decide_winner (user_choice, computer_choice):
  print "You have chosen, " + user_choice
  print "Computer selecting....."
  sleep(1)
  print "The computer has chosen, " + computer_choice
  user_choice_index = options.index(user_choice)
  computer_choice_index = options.index(computer_choice)
  if user_choice == computer_choice:
    print "Its a Tie"
  elif user_choice == options[0] and computer_choice == options[2]:
    print win
  elif user_choice == options[1] and computer_choice == options[0]:
    print win
  elif user_choice == options[2] and computer_choice == options[1]:
    print win
  else:
    print lose
    
def play_RPS ():
  print "Welcome to Rock, Paper, Scissors"
  print "Please make a selection, R for rock, P for paper, or S for scissors"
  user_choice = raw_input(">  ")
  user_choice = user_choice.upper()
  sleep(1)
  computer_choice = options[randint(0,len(options)-1)]
  decide_winner(user_choice, computer_choice)
  
play_RPS()
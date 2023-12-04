import random

#initialize computer moves
moves = ["rock" , "paper" , "scissors"]

#pick computer moves
pick = random.randint(0,2)

#user move
user = int(input("Pick your move: \n1 = rock\n2 = paper\n 3 = scissors"))

if (user == moves[pick]):
  print ("Tie!")
#elif ()

#print computer move
print (moves[pick])
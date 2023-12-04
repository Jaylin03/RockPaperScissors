import random

#initialize and pick computer moves
moves = ["Rock" , "Paper" , "Scissors"]
compMove = moves[random.randint(0,2)]

#user move
userPick = int(input("1 = Rock\n2 = Paper\n3 = Scissors\nPick your move (Enter a number): "))
userMove = moves[userPick-1]

#print moves
print ("\nCurrent Round:\n" + str(userMove) + " vs " + compMove)


'''
How to win:
- rock > scissors --> 0 > 2
- paper > rock --> 1 > 0
- scissors > paper --> 2 > 1
'''
if (userMove == compMove):
  print ("Tie!")
elif ((userMove == "Rock" and compMove == "Scissors") or (userMove == "Paper" and compMove == "Rock") or (userMove == "Scissors" and compMove == "Paper")):
  print("You win!")
else:
  print("You lose! Try again next time.")

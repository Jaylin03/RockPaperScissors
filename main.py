import random

def play(rounds):
  # keep track of scores
  userScore = 0
  compScore = 0

  moves = ["Rock" , "Paper" , "Scissors"]
  
  for __ in range (rounds):
    #pick computer move
    compMove = moves[random.randint(0,2)]
    
    #user move
    userPick = int(input("\n1: Rock\n2: Paper\n3: Scissors\nPick your move (Enter a number): "))
    userMove = moves[userPick-1]

    print ("\nCurrent Round:\n" + str(userMove) + " vs " + compMove)
    '''
    How to win:
    - rock > scissors --> 0 > 2
    - paper > rock --> 1 > 0
    - scissors > paper --> 2 > 1
    '''
    if (userMove == compMove):
      print("Round Results:\nTie!")
    elif ((userMove == "Rock" and compMove == "Scissors") or (userMove == "Paper" and compMove == "Rock") or (userMove == "Scissors" and compMove == "Paper")):
      print("Round Results:\nYou win!")
      userScore += 1
    else:
      print("Round Results:\nYou lose!")
      compScore += 1

  print("Final Results:\nYou = " + str(userScore) + "\nComputer = " + str(compScore))


# allow user to play more than 1 game and keep track of total scores for user and computer


rounds = int(input("How many rounds would you like to play? Enter a whole number: "))
play(rounds)

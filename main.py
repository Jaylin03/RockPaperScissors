import random

def play(rounds):
  # keep track of scores
  userScore = 0
  compScore = 0

  moves = ["Rock" , "Paper" , "Scissors"]
  
  for x in range (rounds):
    #pick computer move
    compMove = moves[random.randint(0,2)]
    
    #user move
    try:
      userPick = int(input("\n1: Rock\n2: Paper\n3: Scissors\nPick your move (Enter a number): "))
    except:
      print("Invalid response. Try again.")
      userPick = int(input("\n1: Rock\n2: Paper\n3: Scissors\nPick your move (Enter a number): "))

    if (userPick < 1 or userPick > 3):
      print("Invalid response. Try again.")
      userPick = int(input("\n1: Rock\n2: Paper\n3: Scissors\nPick your move (Enter a number): "))
      
    userMove = moves[userPick-1]

    print ("\nRound " + str(x+1) + ": " + str(userMove) + " vs " + compMove)
    '''
    How to win:
    - rock > scissors --> 0 > 2
    - paper > rock --> 1 > 0
    - scissors > paper --> 2 > 1
    '''
    if (userMove == compMove):
      print("Tie!")
    elif ((userMove == "Rock" and compMove == "Scissors") or (userMove == "Paper" and compMove == "Rock") or (userMove == "Scissors" and compMove == "Paper")):
      print("You win!")
      userScore += 1
    else:
      print("You lose!")
      compScore += 1

  print("\nFinal Results:\nYou = " + str(userScore) + "\nComputer = " + str(compScore))
  if (userScore > compScore):
    print("Nice work!")
  else:
    print("Bummer. Try again next time!")


# allow user to play more than 1 game
again = "yes"

while (again == "yes"):
  try:
    rounds = int(input("How many rounds would you like to play? Enter a whole number: "))
  except:
    print("Invalid response. Try again.")
    rounds = int(input("How many rounds would you like to play? Enter a whole number: "))
    
  play(rounds)

  againResponse = input("\nWould you like to play again? Enter \"yes\" or \"no\": ")
  again = againResponse.strip().lower()
print("Thank you for playing!")
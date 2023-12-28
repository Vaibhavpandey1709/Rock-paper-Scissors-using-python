import random as r
ucount=0
ccount=0
l=["rock","paper","scissor"]
while True:
  uc=int(input('''
  Game Start...
  1.YES
  2 NO | EXIT
  '''))
  if uc==1:
    for a in range(1,6):
      userinput=int(input('''
      Enter your choice
  1 ROCK
  2 SCISSOR
  3 PAPER
  '''))
      if userinput==1:
        uchoice="rock"
      elif userinput==2:
        uchoice="paper"
      elif userinput==3:
        uchoice="scissor"
      cchoice=r.choice(l)
      if cchoice==uchoice:
        print("compuetr value",cchoice)
        print("user value", uchoice)
        print("game draw")
        ucount=ucount+1
        ccount=ccount+1
      elif(uchoice=="rock" and cchoice=="scissor")or(uchoice=="paper" and cchoice=="rock")or(uchoice=="scissor" and cchoice=="paper"):
        print("computer value", cchoice)
        print("user value", uchoice)
        ucount=ucount+1
      else:
        print("computer value", cchoice)
        print("user value", uchoice)
        ccount=ccount+1
    if ucount==ccount:
      print("final game draw...")
      print("user score", ucount)
      print("computer score", ccount)
    elif ucount>ccount:
      print("you win the game...")
      print("user score", ucount)
      print("user score", ucount)
    else:
      print("computer win the game")
      print("computer score", ccount)
      print("user score", ucount)
  else:
    break



#A game of Pig
#Roll the dice when it is your turn. If you get anything but
#1, you can roll again or keep your score and end your turn
#if you roll a 1, your score for that turn is deleted and
#your turn is skipped. First to 100 score wins
#type x at anytime to quit
#Tip to speed up the game: instead of clicking the "ok"
#button in the pop-up, press enter on your keyboard


import random
pScore=0
cScore=0
pTotal=0
cTotal=0
d=input("Type 'easy', 'medium', 'hard', or 'expert' for difficulty")
while (d != "expert" and d != "hard" and d != "medium" and d != "easy"):
    if (d == "x"):
        print(0/0)
    d=input("Invalid Input, please type 'easy' or 'hard' for difficulty")
if (d == "easy"):
    while (pTotal<100 and cTotal<100):
        cChoice=0
        pChoice=input("type 'r' to roll the dice")
        if (pChoice == "x"):
            print (0/0)
        while (pChoice != "r"):
            pChoice=input("Invalid Input: type 'r' to roll the dice")
        while (pChoice == "r"):
            dice = random.randint(1, 6)
            if (dice == 1):
                pChoice=input("Rolled a "+str(dice)+", no score for this round! Your total score: "+str(pTotal)+". Press enter to continue")
                if (pChoice == "x"):
                    print (0/0)
                pChoice="ok"
                pScore=0
            else:
                pScore=pScore+dice
                pChoice=input("Rolled a "+str(dice)+", "+str(pScore)+" score for this round. Your total score: "+str(pTotal)+". Type 'r' to roll again or type 'h' to keep your score")
                while (pChoice != "r" and pChoice != "h"):
                    if (pChoice == "x"):
                        print (0/0)
                    pChoice=input("Invalid input. Please type 'r' or 'h'")
                if (pChoice == "h"):
                    pTotal=pScore + pTotal
                    pScore=0
        while (cChoice == 0):
            dice = random.randint(1, 6)
            pChoice=input("Computer rolls a "+str(dice)+". Press enter to continue")
            if (pChoice == "x"):
                print (0/0)
            if (dice != 1):
                cScore=cScore + dice
                cChoice=random.randint(0, 1)
                if (cChoice == 0):
                    pChoice=input("Computer decides to roll again, Press enter to continue")
                    if (pChoice == "x"):
                        print (0/0)
                else:
                    cTotal=cTotal+cScore
                    cScore=0
                    pChoice=input("Computer decides to hold. \nYour total score: "+str(pTotal)+". Computer's total score: "+str(cTotal)+".\nPress enter to continue")
                    if (pChoice == "x"):
                        print (0/0)
            else:
                cChoice=1
                cScore=0
                pChoice=input("Computer's turn is over. \nYour total score: "+str(pTotal)+". Computer's total score: "+str(cTotal)+".\nPress enter to continue")
                if (pChoice == "x"):
                    print (0/0)
if (d == "medium"):
    while (pTotal<100 and cTotal<100):
        cChoice=0
        pChoice=input("type 'r' to roll the dice")
        if (pChoice == "x"):
            print (0/0)
        while (pChoice != "r"):
            pChoice=input("Invalid Input: type 'r' to roll the dice")
        while (pChoice == "r"):
            dice = random.randint(1, 6)
            if (dice == 1):
                pChoice=input("Rolled a "+str(dice)+", no score for this round! Your total score: "+str(pTotal)+". Press enter to continue")
                if (pChoice == "x"):
                    print (0/0)
                pChoice="ok"
                pScore=0
            else:
                pScore=pScore+dice
                pChoice=input("Rolled a "+str(dice)+", "+str(pScore)+" score for this round. Your total score: "+str(pTotal)+". Type 'r' to roll again or type 'h' to keep your score")
                while (pChoice != "r" and pChoice != "h"):
                    if (pChoice == "x"):
                        print (0/0)
                    pChoice=input("Invalid input. Please type 'r' or 'h'")
                if (pChoice == "h"):
                    pTotal=pScore + pTotal
                    pScore=0
        while (cChoice < 5):
            dice = random.randint(1, 6)
            pChoice=input("Computer rolls a "+str(dice)+". Press enter to continue")
            if (pChoice == "x"):
                print (0/0)
            if (dice != 1):
                cScore=cScore + dice
                if (cScore < 5): 
                    cChoice=0
                elif (cScore < 10):
                    cChoice=random.randint(0, 6)
                elif (cScore < 15):
                    cChoice=random.randint(0, 10)
                else:
                    cChoice=10
                if (cChoice < 5):
                    pChoice=input("Computer decides to roll again, Press enter to continue")
                    if (pChoice == "x"):
                        print (0/0)
                else:
                    cTotal=cTotal+cScore
                    cScore=0
                    pChoice=input("Computer decides to hold. \nYour total score: "+str(pTotal)+". Computer's total score: "+str(cTotal)+".\nPress enter to continue")
                    if (pChoice == "x"):
                        print (0/0)
            else:
                cChoice=10
                cScore=0
                pChoice=input("Computer's turn is over. \nYour total score: "+str(pTotal)+". Computer's total score: "+str(cTotal)+".\nPress enter to continue")
                if (pChoice == "x"):
                    print (0/0)

if (d == "hard"):
    while (pTotal<100 and cTotal<100):
        cChoice=0
        pChoice=input("type 'r' to roll the dice")
        if (pChoice == "x"):
            print (0/0)
        while (pChoice != "r"):
            pChoice=input("Invalid Input: type 'r' to roll the dice")
        while (pChoice == "r"):
            dice = random.randint(1, 6)
            if (dice == 1):
                pChoice=input("Rolled a "+str(dice)+", no score for this round! Your total score: "+str(pTotal)+". Press enter to continue")
                if (pChoice == "x"):
                    print (0/0)
                pChoice="ok"
                pScore=0
            else:
                pScore=pScore+dice
                pChoice=input("Rolled a "+str(dice)+", "+str(pScore)+" score for this round. Your total score: "+str(pTotal)+". Type 'r' to roll again or type 'h' to keep your score")
                while (pChoice != "r" and pChoice != "h"):
                    if (pChoice == "x"):
                        print (0/0)
                    pChoice=input("Invalid input. Please type 'r' or 'h'")
                if (pChoice == "h"):
                    pTotal=pScore + pTotal
                    pScore=0
        while (cChoice < 5):
            dice = random.randint(1, 6)
            pChoice=input("Computer rolls a "+str(dice)+". Press enter to continue")
            if (pChoice == "x"):
                print (0/0)
            if (dice != 1):
                cScore=cScore + dice
                if (cScore < 10): 
                    cChoice=0
                elif (cScore < 15):
                    cChoice=random.randint(0, 5)
                elif (cScore < 20):
                    cChoice=random.randint(0, 10)
                else:
                    cChoice=10
                if (cChoice < 5):
                    pChoice=input("Computer decides to roll again, Press enter to continue")
                    if (pChoice == "x"):
                        print (0/0)
                else:
                    cTotal=cTotal+cScore
                    cScore=0
                    pChoice=input("Computer decides to hold. \nYour total score: "+str(pTotal)+". Computer's total score: "+str(cTotal)+".\nPress enter to continue")
                    if (pChoice == "x"):
                        print (0/0)
            else:
                cChoice=10
                cScore=0
                pChoice=input("Computer's turn is over. \nYour total score: "+str(pTotal)+". Computer's total score: "+str(cTotal)+".\nPress enter to continue")
                if (pChoice == "x"):
                    print (0/0)
if (d == "expert"):
    while (pTotal<100 and cTotal<100):
        cChoice=0
        count=0
        pChoice=input("type 'r' to roll the dice")
        if (pChoice == "x"):
            print (0/0)
        while (pChoice != "r"):
            pChoice=input("Invalid Input: type 'r' to roll the dice")
        while (pChoice == "r"):
            dice = random.randint(1, 6)
            if (dice == 1):
                pChoice=input("Rolled a "+str(dice)+", no score for this round! Your total score: "+str(pTotal)+". Press enter to continue")
                if (pChoice == "x"):
                    print (0/0)
                pChoice="ok"
                pScore=0
            else:
                pScore=pScore+dice
                pChoice=input("Rolled a "+str(dice)+", "+str(pScore)+" score for this round. Your total score: "+str(pTotal)+". Type 'r' to roll again or type 'h' to keep your score")
                while (pChoice != "r" and pChoice != "h"):
                    if (pChoice == "x"):
                        print (0/0)
                    pChoice=input("Invalid input. Please type 'r' or 'h'")
                if (pChoice == "h"):
                    pTotal=pScore + pTotal
                    pScore=0
        while (cChoice < 5):
            dice = random.randint(1, 6)
            pChoice=input("Computer rolls a "+str(dice)+". Press enter to continue")
            if (pChoice == "x"):
                print (0/0)
            if (dice != 1):
                cScore=cScore + dice
                count=int(count+1+(count)/2)
                e=int((100-cTotal)/20)
                if (cTotal+cScore<pTotal):
                    h=-1
                else:
                    h=0
                if (pTotal>80 and pTotal>cTotal+cScore+20):
                    if (cScore+cTotal >= 100):
                        cChoice=10
                    elif (cScore < 15): 
                        cChoice=0
                    elif (cScore < 20):
                        cChoice=random.randint(h+0-e, 6+count)
                    elif (cScore < 25):
                        cChoice=random.randint(h+0-e, 10+count)
                    else:
                        cChoice=10
                else:
                    if (cScore+cTotal >= 100):
                        cChoice=10
                    elif (cScore < 10): 
                        cChoice=0
                    elif (cScore < 15):

                        cChoice=random.randint(h+0-e, 6+count)
                    elif (cScore < 20):
                        cChoice=random.randint(h+0-e, 10+count)
                    else:
                        cChoice=10
                if (cChoice < 5):
                    pChoice=input("Computer decides to roll again, Press enter to continue")
                    if (pChoice == "x"):
                        print (0/0)
                else:
                    cTotal=cTotal+cScore
                    cScore=0
                    pChoice=input("Computer decides to hold. \nYour total score: "+str(pTotal)+". Computer's total score: "+str(cTotal)+".\nPress enter to continue")
                    if (pChoice == "x"):
                        print (0/0)
            else:
                cChoice=10
                cScore=0
                pChoice=input("Computer's turn is over. \nYour total score: "+str(pTotal)+". Computer's total score: "+str(cTotal)+".\nPress enter to continue")
                if (pChoice == "x"):
                    print (0/0)
if (pTotal >= 100):
    print ("You Win! Your score: "+str(pTotal)+" Computer's score: "+str(cTotal))
else:
    print ("You Lost, Computer's score: "+str(cTotal)+" Your score: "+str(pTotal))

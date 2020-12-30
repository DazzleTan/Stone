from stone import stone
from scissors import scissors
from palm import palm
import random

def judgment(a):
    if a == "stone":
        stone()
    elif a == "scissors":
        scissors()
    else:
        palm()

number = 0
while True:
    if number > 0:
        c = input("Do you want to continue the game? Please enter n to exit, enter other to continue the game.")
        if c == "n":
            break
        else:
            number = 0
    else:
        while number == 0:
            a = input("Please enter stone, scissors and paper:")
            if a== "stone" or a== "scissors" or a== "paper":
                number += 1
            else:
                print("Is the input wrong, please re-enter")
        print("--------Battle process--------")
        b = random.randint(1,3)
        if b == 1:
            print("The computer came out: stone")
            stone()
            print("You out:")
            judgment(a)
        elif b == 2:
            print("The computer came out: scissors")
            scissors()
            print("You out:")
            judgment(a)
        else:
            print("The computer came out: paper")
            palm()
            print("You out:")
            judgment(a)
        print("--------Result--------")
        if a == "stone":
            if b == 1:
                print("Tie")
            elif b == 2:
                print("You win")
            else:
                print("The computer win")
        elif a == "scissors":
            if b == 1:
                print("The computer win")
            elif b == 2:
                print("Tie")
            else:
                print("You win")
        else:
            if b == 1:
                print("You win")
            elif b == 2:
                print("The computer win")
            else:
                print("Tie")
        number += 1
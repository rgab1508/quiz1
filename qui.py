import os
def cls():
    os.system("cls")
def qsetup():
    cls()
    print("\t"*7,end="")
    print("PROGRAM QUIZ")
    print("-"*120)
    print("\t"*5,end="")
    print("WELCOME \tTO \tTHE \tQUIZ")
    print("-"*120)
    print("\t"*6,end="")
    print("press any key to start")

    _tempp = input()

    cls()
    print("ENTER YOUR NAME: ")
    playerName = input()
    cls()

    print("*****************welcome {} to the quiz game**********************".format(playerName))
    print("\n    Here are some tips before starting the game")
    print("\t >> Questions are selected on random basis.\n")
    print("\t >> You will be given 4 options and you have to press A, B ,C or D \n\t    for the right option.\n")
    print("\t >> No negative marking for wrong answers!\n")
    print("\n\t!!!!!!!!!!!!! ALL THE BEST !!!!!!!!!!!!!\n")
    print("\n\tPress any key to continue  to start the game!\n")
    cls()


    

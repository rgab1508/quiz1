import random
import os
from qui import qsetup
from qutils import getQuestion
import time
from questions import Question

def cls():
    os.system("cls")



def main():
    os.system("color 02")
    NO_OF_QUESTIONS = 7
    TOTAL_TIME_TAKEN = 0
    SCORE = 0
    randQids = [x for x in range(NO_OF_QUESTIONS) ]
    random.shuffle(randQids)
    timeTaken = []
    qsetup()

    choice = input("s to start")
    for i in range(NO_OF_QUESTIONS):
        q = getQuestion(randQids[i])
        q.printQ(randQids[i],i)
        t1 = time.time()
        choice = input()
        corrAns = False
        if choice == "a" or choice == "A":
            t2 = time.time()
            corrAns = q.checkAnswer(0,t2 -t1)
            timeTaken.append(t2-t1)
        elif choice == "b" or choice == "B":
            t2 = time.time()
            corrAns = q.checkAnswer(1,t2 -t1)
            timeTaken.append(t2-t1)
        elif choice == "c" or choice == "C":
            t2 = time.time()
            corrAns = q.checkAnswer(2,t2 -t1)
            timeTaken.append(t2-t1)
        elif choice == "d" or choice == "D":
            t2 = time.time()
            corrAns = q.checkAnswer(3,t2 -t1)
            timeTaken.append(t2-t1)
        elif choice =="q" or choice =="Q":
            break

        if corrAns:
            print("\n\n\t\t\tcorrect")
            SCORE += 1
        else:
            print(f"\n\n\t\t\tWrong Answer (correct Answer:{q.options[q.answer]})")
        
        time.sleep(0.5)
        
    for t in range(len(timeTaken)):
        TOTAL_TIME_TAKEN += timeTaken[t]
                

    print(f"SCORE:{SCORE}")
    print(f"TOTAL TIME TAKEN: {TOTAL_TIME_TAKEN}")




if __name__ == "__main__":
    main()
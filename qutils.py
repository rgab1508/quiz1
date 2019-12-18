import random

from questions import Qs



def getRandQids(no_of_ques):
    randQids = set()
    while len(randQids) < no_of_ques:
        j = random.randrange(no_of_ques)
        randQids.add(j)

    return list(randQids)


def getQuestion(id):
    return Qs[id]
    
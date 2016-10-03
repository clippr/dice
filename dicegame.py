import random
import time
min = 1
max = 6

game = 1
turn = 1
score1 = 0
score2 = 0



def player_1():
    score_add = 0
    score1a = random.randint(min, max)
    score1b = random.randint(min, max)
    if score1a == 1 or score1b == 1:
        return 0
    score_add1 = score1a + score1b
    return score_add1

def player_2():
    score_add = 0
    score2a = random.randint(min, max)
    score2b = random.randint(min, max)
    if score2a == 1 or score2b == 1:
        return 0
    score_add2 = score2a + score2b
    return score_add2


while game == 1:
    while turn == 1:
        if player_1() == 2:
            score1 = 0
            game = 2
        score1 = score1 + player_1()
        if score1 > 100:
            print "Computer 1 wins"
            print score1, "to,", score2
            game = 0
        turn = 2

    while turn == 2:
        if player_2() == 2:
            score2 = 0
            game = 1
        score2 = score2 + player_2()
        if score2 > 100:
            print "Computer 2 wins"
            print score2, "to", score1
            game = 0
        turn = 1

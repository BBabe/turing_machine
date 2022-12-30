'''
The main function "verif_fun" of this script is called in "turing.py" and gives
the list of all criteria cards.
More precisely, each criteria card is represented by a list of functions, each
representing an alternative of the card.
Note that not all criteria cards have been coded yet.
'''
import pickle
from functools import partial
import numpy as np
##

# triangle, blue
tr = 0
# square, yellow
sq = 1
# round, purple
ro = 2

## Intermediate functions for criteria definitions

# def compare(bool, a, b):
#     if bool == -1:
#         return a < b
#     elif bool == 0:
#         return a == b
#     elif bool == 1:
#         return a > b

def number_3(n,c):
    return ((c[tr] == 3) + (c[sq] == 3) + (c[ro] == 3)) == n

def smallest(c, small, other1, other2):
    return c[small]<c[other1] and c[small]<c[other2]

def number_1(n,c):
    value = 1
    return ((c[tr] == value) + (c[sq] == value) + (c[ro] == value)) == n

def biggest(c, big, other1, other2):
    return c[big] > c[other1] and c[big] > c[other2]

def number_even(n,c):
    return (((c[tr]+1) % 2) + ((c[sq]+1) % 2) + ((c[ro]+1) % 2)) == n

def repet(n,c):
    tmp = (c[tr] == c[sq]) + (c[tr] == c[ro]) + (c[ro] == c[sq])
    if tmp == 3:
        tmp = 2
    return tmp == n

## Function giving the list containing all criteria cards


def verif_fun():
    verifs = [None] * 48

    verifs[4] = [lambda c: c[sq] < 4,\
                lambda c: c[sq] == 4,\
                lambda c: c[sq] > 4]

    '''Trying to define card n°4 more properly, to prevent errors,
    but it doesn't work, as all functions are the same: they all take the
    final value of "i" '''
    # verifs[4] = []
    # for i in [-1, 0, 1]:
    #     verifs[4].append(lambda c: compare(i, c[sq], 4))

    verifs[8] = [partial(number_1, i) for i in range(4)]

    verifs[9] = [partial(number_3, i) for i in range(4)]


    verifs[11] = [lambda c: c[tr] < c[sq],\
                lambda c: c[tr] == c[sq],\
                lambda c: c[tr] > c[sq]]

    verifs[12] = [lambda c: c[tr] < c[ro],\
                lambda c: c[tr] == c[ro],\
                lambda c: c[tr] > c[ro]]

    verifs[13] = [lambda c: c[sq] < c[ro],\
                lambda c: c[sq] == c[ro],\
                lambda c: c[sq] > c[ro]]

    verifs[14] = [lambda c: smallest(c, tr, ro, sq),\
                lambda c: smallest(c, sq, ro, tr),\
                lambda c: smallest(c, ro, tr, sq)]

    verifs[15] = [lambda c: biggest(c, tr, ro, sq),\
                lambda c: biggest(c, sq, ro, tr),\
                lambda c: biggest(c, ro, tr, sq)]

    verifs[17] = [partial(number_even, i) for i in range(4)]

    verifs[20] = [partial(repet, i) for i in [2,1,0]]

    verifs[27] = [lambda c: c[tr] < 4,\
                  lambda c: c[sq] < 4,\
                  lambda c: c[ro] < 4]

    verifs[31] = [lambda c: c[tr] > 1,\
                  lambda c: c[sq] > 1,\
                  lambda c: c[ro] > 1]


    verifs[38] = [lambda c: c[tr] + c[sq] == 6,\
                  lambda c: c[tr] + c[ro] == 6,\
                  lambda c: c[ro] + c[sq] == 6]

    verifs[40] = [lambda c: c[tr] < 3,\
                  lambda c: c[tr] == 3,\
                  lambda c: c[tr] > 3,\
                  lambda c: c[sq] < 3,\
                  lambda c: c[sq] == 3,\
                  lambda c: c[sq] > 3,\
                  lambda c: c[ro] < 3,\
                  lambda c: c[ro] == 3,\
                  lambda c: c[ro] > 3]

    verifs[44] = [lambda c: c[sq] < c[tr],\
                  lambda c: c[sq] == c[tr],\
                  lambda c: c[sq] > c[tr],\
                  lambda c: c[sq] < c[ro],\
                  lambda c: c[sq] == c[ro],\
                  lambda c: c[sq] > c[ro]]

    return verifs

## Test new criteria cards

if 0:
    v = verif_fun()
    c = [2,2,2]

    print((c[tr] == c[sq]) + (c[tr] == c[ro]) + (c[ro] == c[sq]))
    # print(((c[tr]+1) % 2) + ((c[sq]+1) % 2) + ((c[ro]+1) % 2))

    for i in range(3):
        print(v[20][i](c))

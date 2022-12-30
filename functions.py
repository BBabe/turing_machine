'''
Functions used in main "turing.py" script
'''
from itertools import product
from math import prod
##


def reduced_codes(pb):
    '''
    Gives all code combinations, without those never verifying one of the
    criteria cards (to limit computations)
    '''
    # All possible codes (there are 125)
    values = range(1,6)
    codes0 = list(product(values, repeat = 3))

    codes = []
    for code in codes0:
        # Check if there are criteria cards of problem "pb" with none of their
        # alternatives being True with this code
        # ex: card 31 (one of the colors > 1) => code (1,1,1) is not considered
        ind_verif = 0
        while ind_verif < len(pb) and sum(pb[ind_verif][ind_prop](code) for ind_prop in range(len(pb[ind_verif]))):
            ind_verif += 1

        if ind_verif == len(pb):
            codes.append(code)
    return codes


def generate_combi(pb):
    '''
    Gives a list of all combinations of criteria
    '''
    # List of possible values for each criterion card
    verif_prop = []
    for i in range(len(pb)):
        verif_prop.append(list(range(len(pb[i]))))
    # All combinations of these possible values
    list_tmp = list(product(*verif_prop))
    return list_tmp


def verif2code(codes, fun_verif):
    '''
    Checks if there is one and only code solution of the given set of verificators
    '''
    count = 0
    code_sol = [] # init in case no solution
    for code in codes:
        # Test if solution of the given set of verificators
        if fun_verif(code):
            count += 1
            # If more than one solution => impossible (game definition)
            if count > 1:
                break
            else:
                code_sol = code
    return count, code_sol


def redondance(pb, combi_verif, codes):
    '''
    Checks if the unique solution code could have been found with one (or more)
    cards less
    '''
    ind_verif0 = 0
    count0 = 2
    # If count0 == 1 (0 impossible, as one more card gives a solution),
    # then the solution could have been found with less cards
    while ind_verif0 < len(pb) and count0 > 1:
        # Function being the concatenation of all verificators except one
        fun_tmp = lambda c: prod(pb[ind_verif][combi_verif[ind_verif]](c) for ind_verif in range(len(pb)) if ind_verif != ind_verif0)
        count0,_ = verif2code(codes, fun_tmp)
        ind_verif0 += 1
    return ind_verif0

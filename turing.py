'''
- Choose a problem, by giving the number of the criterion cards used in "crits"
- This script gives all the combinations between the different alternatives of
each card, with the correspond solution code
'''
from math import prod
import numpy as np
# local
from verif import verif_fun
from functions import reduced_codes, generate_combi, verif2code, redondance
from operator import itemgetter

## Choose the criteria cards of your problem

# Problem 1 of the rules
crits = [4, 9, 11, 14]

# Problem 2 of the rules
# crits = [4, 9, 13, 17]

# Problem 7 of the rules
# crits = [8, 12, 15, 17]

# A difficult problem
# crits = [20, 27, 31, 38, 44]

##

# Load the list of all criteria cards
verifs = verif_fun()
# "pb" is the list of the criteria cards of the chosen problem
pb = itemgetter(*crits)(verifs)
# Compute all combinations of criteria
combi_verifs = generate_combi(pb)
# All code combinations, without those never verifying one of the criteria cards
codes = reduced_codes(pb)

print('Possible verificator values:')
print([len(pb[i]) for i in range(len(pb))])

##

# Will contain valid criteria combinations, and their solution
sols = []
# "codes_diff" will contain all possible codes corresponding to "pb"
codes_diff = np.zeros((5,5,5))

# Loop on all possible criteria combinations
for combi_verif in combi_verifs:
    # Function being the concatenation of the current tested criteria
    fun_verif = lambda c: prod(pb[ind_verif][combi_verif[ind_verif]](c) for ind_verif in range(len(pb)))
    # Codes verifying this function
    count, code_sol = verif2code(codes, fun_verif)
    # Test if there is one and only solution
    if count == 1:
        # Test if one criterium was redundant
        ind_verif0 = redondance(pb, combi_verif, codes)
        if ind_verif0 == len(pb):
            sols.append([combi_verif, code_sol])
            code_tmp = tuple([-1+code_sol[i] for i in range(3)]) # (1:5) -> (0:4)
            codes_diff[code_tmp] = 1

##

print('Solution codes:')
print(1+np.argwhere(codes_diff == 1))  # (0:4) -> (1:5)

N = len(sols)
print('Number of possibilities =', N)

print('Possible combinations:')
for i in range(N):
    print(sols[i])

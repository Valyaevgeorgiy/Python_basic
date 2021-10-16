import itertools

def union(A, B):
    return {a + b for a in A for b in B}
teams = union('w', '12') | union('l', '0') | union('N', '3456789')

import itertools
from fractions import Fraction

def Omega(p, k):
    return {' '.join(comb) for comb in itertools.combinations(p, k)}

omega = Omega(teams, 5)
print(len(omega))
A = {a for a in omega if a.count('w') == 1}
print(len(A))
# A - события, а Р - это вероятность событий

def P(event, space):
    return Fraction(len(event & space), len(space))

print('P(A)=', P(A, omega))
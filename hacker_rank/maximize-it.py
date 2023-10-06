import itertools
from math import sqrt

mat = [[2, 5, 4], [3, 7, 8, 9], [5, 5, 7, 8, 9, 10]]
# print(int(sqrt(12)))

N = 1000
S_max = 0
L_max = None
for l in itertools.product(*mat):
    s = sum([x ** 2 for x in l]) % N

    if s > S_max:
        S_max = s
        L_max = l

print(S_max, L_max)
# b= '''2 5 4
# 3 7 8 9
# 5 5 7 8 9 10'''
#
#
# print([[int(_) for _ in a.split(' ')] for a in b.split('\n')])
#

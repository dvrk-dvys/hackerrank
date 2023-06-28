# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

# import numpy as np

N = int(input())
S = list(map(str, input().split()))
K = int(input())

# 12 13 14 23 24 34
# print(S)

# i_S = np.where(S == 'a')[0]

i_S = [i + 1 for i, a in enumerate(S) if a == 'a']
# print(i_S)

x = list(range(1, N + 1))
# print(x)

perm = list(itertools.combinations(x, K))
# print(perm)

l = []
for _ in i_S:
    l += list(filter(lambda x: _ in x, perm))
l = sorted(set(l))
# print(l)

calc = len(l) / len(perm)
print(calc)

# list(filter(lambda x:_ in x, perm))
# any(isinstance(x, (str, list, tuple, int)) for x in data)


# https://www.hackerrank.com/challenges/iterables-and-iterators/problem
# https://github.com/rene-d/hackerrank/blob/master/python/py-itertools/iterables-and-iterators.py



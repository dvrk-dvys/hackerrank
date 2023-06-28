# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools
import re

S = input()
# print(S)
# S = list(map(str, input()))
# matches = re.findall(r'(\w)\1*', S)
# print(matches)

_res = [''.join(group) for key, group in itertools.groupby(S)]

# print(res)
res = []
for _ in _res:
    res.append(str((len(_),int(_[0]))))

print(' '.join(res))

# print(' '.join(str((len(list(g)), int(c)))
#                for c, g in itertools.groupby(s)))

# https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true
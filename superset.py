# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))

# print(sorted(A))

N = int(input())
# print(N)
res = True
for _ in range(N):
    s = set(map(int, input().split()))

    # print(sorted(s))
    # x = A - s
    x = list(set(A).difference(s))
    y = list(set(s).difference(A))

    # print(x)
    # print(y)

    if not ((len(y) == 0 and len(x) > 0)):
        res = False
        break
print(res)

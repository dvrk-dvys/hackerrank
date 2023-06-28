# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import itertools

x = str(input())
y = str(input())

# x = 'aabcdeffgabcdef'
# y = 'abcdef'
# a = 'aaadaa'
# b = 'aa'

l_x = len(x)
l_y = len(y)

if y in x:
    for i, _ in enumerate(list(x)):
        if x[i:i + l_y] == y:
            # print(x[i:i+l_y])
            print('(' + str(i) + ', ' + str(i + l_y - 1) + ')')
else:
    print("(-1, -1)")

# print(x.split(y))
# print(a.split(b))


# # a[start:stop:step] start through not past stop, by step
# x[1:]
# l_x = len(x)
# l_y = len(y)

# print(x.split(y))
# print(x[1:])

# output_string = ' '.join(''.join(pair) for pair in itertools.zip_longest(x, x[1:], fillvalue=''))
# output_index = ' '.join(f"{i}{i+1}" for i in range(len(x)-1))

# print(output_string)
# print(output_index)

# for i, each in enumerate(output_string.split(' ')):
#     # print()
#     if each == y:
#         print('(' + str(i) + ', ' + str(i + l_y - 1) + ')')

# # A = list(map(y, x.split()))

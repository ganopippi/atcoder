import math
n = int(input())

i = 1
# whileじゃなくても計算量間に合う
while math.floor(i * 1.08) <= n*1.08:
    if int(i*1.08) == n:
        print(i)
        exit()
    i += 1
print(':(')

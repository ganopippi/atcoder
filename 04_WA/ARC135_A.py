from collections import deque
import math
import sys
input = sys.stdin.readline
res = 1

x = int(input())
num_list = deque([])

num_list.append(x)
if x <= 4:
    print(x)
    exit()

while num_list:
    num = num_list.popleft()
    # if num <= 4:
    #     res = res * num
    if num <= 8:
        res = res * math.floor(num/2) * math.ceil(num/2)
    # 分割する処理
    else:
        num_list.appendleft(math.floor(num/2))
        num_list.appendleft(math.ceil(num/2))

print(res % 998244353)

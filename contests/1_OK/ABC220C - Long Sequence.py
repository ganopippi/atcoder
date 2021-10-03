n = int(input())
a = list(map(int, input().split()))
x = int(input())
res = 0
# aの合計
a_sum = sum(a)
# 何週できるか
cnt_sum = x//a_sum
res = cnt_sum*n

x = x - a_sum*cnt_sum

i = 0


while x >= 0:
    x -= a[i]
    i += 1

res = res + i
"""
if cnt_sum == 0:
    res += 1
"""
print(res)

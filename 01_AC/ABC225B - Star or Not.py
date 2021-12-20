import collections
n = int(input())
l = [list(map(int, input().split())) for i in range(n-1)]

# 一番多い要素を確認する
sample = []
for i in range(2):
    sample.append(l[i][0])
    sample.append(l[i][1])
# print(sample)
c = collections.Counter(sample)
key = c.most_common()[0][0]

flag = True

for i in range(n-1):
    a = l[i][0]
    b = l[i][1]
    if a == key or b == key:
        continue
    else:
        flag = False
if flag:
    print('Yes')
else:
    print('No')

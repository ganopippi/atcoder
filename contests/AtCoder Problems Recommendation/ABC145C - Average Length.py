import itertools
import math

n = int(input())
x = [list(map(int, input().split())) for i in range(n)]

# 全通りの配列を作成
x_all = list(itertools.permutations(x))

all_dis = 0
for i in x_all:
    dis = 0
    for j in range(len(i)-1):
        # 距離を計算する
        dis += math.sqrt(((i[j+1][0] - i[j][0]) ** 2 +
                         (i[j+1][1] - i[j][1]) ** 2))
    all_dis += dis
print(all_dis/len(x_all))

from collections import deque

n, x = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n)]

# pos = deque([])
# pos.append(0)
pos = [0]

# ジャンプのクエリ
for i in range(len(ab)):
    # 現在の位置の分岐ごとに次の結果を確認
    temp = []
    for j in range(len(pos)):
        temp.append(pos[j] + ab[i][0])
        temp.append(pos[j] + ab[i][1])
    pos = list(set(temp))
# print(pos)

for i in range(len(pos)):
    if pos[i] == x:
        print('Yes')
        exit()

print('No')

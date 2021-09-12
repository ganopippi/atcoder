N = int(input())
d = [int(input()) for i in range(N)]

d = list(set(d))  # 重複を削除
d = sorted(d)[::-1]  # サイズの降順にソート


step = 0
current_size = d[0]

for i in range(len(d)):
    if i == 0:
        step += 1
    elif d[i-1] > d[i]:
        step += 1
    else:
        break

print(step)

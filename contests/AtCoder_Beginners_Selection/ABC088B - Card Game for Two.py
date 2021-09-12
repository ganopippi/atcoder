N = int(input())
a = list(map(int, input().split()))
Alice = 0
Bob = 0

a = sorted(a)[::-1]  # 得点の降順にソート
cnt = 1
for i in a:
    if cnt % 2 != 0:
        Alice += i
    else:
        Bob += i
    cnt += 1

print(Alice-Bob)

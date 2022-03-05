n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(m):
    # 判定
    if b[i] in a:
        a.pop(a.index(b[i]))
    else:
        print('No')
        exit()
print('Yes')

a, b, k = map(int, input().split())

ans = []

for i in range(k):
    if a+i <= b:
        ans.append(a+i)
    else:
        break
for i in range(k):
    if a <= b-i:
        ans.append(b-i)
    else:
        break

# ユニーク化
ans = list(set(ans))
# ソート
ans = sorted(ans)

for i in ans:
    print(i)

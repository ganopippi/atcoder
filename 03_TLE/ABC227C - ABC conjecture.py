n = int(input())
ans = 0
# abc = [] #確認用

for c in range(1, n+1):
    for b in range(1, c+1):
        if c*b*1 > n:
            break
        for a in range(1, b+1):
            if a*b*c <= n:
                ans += 1
                # 確認用
                #temp = []
                # temp.append(a)
                # temp.append(b)
                # temp.append(c)
                # abc.append(temp)
            else:
                break


print(ans)
# print(abc)

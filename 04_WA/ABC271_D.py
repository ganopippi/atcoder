n,s = map(int, input().split())
x = [list(map(int, input().split())) for i in range(n)]

l = x[0]

for i in range(1,len(x)):
    res = []
    for j in range(len(l)):
        res.append(l[j]+x[i][0])
        res.append(l[j]+x[i][1])
    l = res
        
# print(res)

if s in res:
    print('Yes')
    idx = res.index(s)+1
    ans = ''
    for i in range(n):
        if idx % 2 == 0:
            # print('T')
            ans = 'T' + ans
            idx = idx // 2
        else:
            # print('H')
            ans = 'H' + ans
            idx = idx - 1
    print(ans)
else:
    print('No')


# HHH,HHT,HTH,

# HH,HT,TH,TT
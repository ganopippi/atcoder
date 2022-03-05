n = int(input())
s = list(input())
res = ['0']

for i in range(1, n+1):
    cur = s[i-1]
    index = res.index(str(i - 1))
    if cur == 'L':
        res.insert(index, str(i))
    else:
        res.insert(index+1, str(i))

print(' '.join(res))

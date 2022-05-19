v, a, b, c = map(int, input().split())

res = v
while res >= 0:
    if res < a:
        print('F')
        exit()
    else:
        res -= a

    if res < b:
        print('M')
        exit()
    else:
        res -= b

    if res < c:
        print('T')
        exit()
    else:
        res -= c

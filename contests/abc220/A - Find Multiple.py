a, b, c = map(int, input().split())

while c <= 1000:
    if a <= c and c <= b:
        print(c)
        exit()
    else:
        c = c*2

print(-1)

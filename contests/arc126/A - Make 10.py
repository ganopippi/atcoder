t = int(input())
case = [list(map(int, input().split())) for i in range(t)]
result = []

# 2*5,2*3+4*1,2*2+3*2,3*2+4*1
for c in case:
    count = 0
    x = c[0]
    y = c[1]
    z = c[2]
    if y >= 2 and z >= 1:
        if y // 2 >= z // 1:
            count = count + z // 1
            y = y - (z // 1)*2
            z = z - (z // 1)
        else:
            count = count + y // 2
            y = y - (y // 2)*2
            z = z - (y // 2)
    if x >= 2 and y >= 2:
        if x // 2 >= y // 2:
            count = count + y // 2
            x = x - (y // 2)*2
            y = y - (y // 2)*2
        else:
            count = count + x // 2
            x = x - (x // 2)*2
            y = y - (x // 2)*2
    while x >= 3 and z >= 1:
        if x // 3 >= z // 1:
            count = count + z // 1
            x = x - (z // 1)*3
            z = z - (z // 1)
        else:
            count = count + x // 3
            x = x - (x // 3)*3
            z = z - (x // 3)
    if x >= 5:
        count = count + (x//5)
    result.append(count)

for i in result:
    print(i)

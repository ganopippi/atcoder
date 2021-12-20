h, w = map(int, input().split())
canlist = []
for i in range(h):
    line = input()
    for j in range(w):
        if line[j] == '.':
            canlist.append([i+1, j+1])
# print(canlist)

route = 1

curr_x = 1
curr_y = 1

flg = True
while flg:
    flg = False
    # 右優先探索

    result = []
    for i in range(len(canlist)):

        if canlist[i][0] == curr_x + 1 and canlist[i][1] == curr_y:
            result.append(canlist[i])
            curr_x += 1
            flg = True
        elif canlist[i][0] == curr_x and canlist[i][1] == curr_y + 1:
            result.append(canlist[i])
            curr_y += 1
            flg = True
    if route < len(result) + 1:
        route = len(result) + 1

flg = True
curr_x = 1
curr_y = 1

while flg:
    flg = False
    # 右優先探索
    result = []
    for i in range(len(canlist)):

        if canlist[i][0] == curr_x and canlist[i][1] == curr_y + 1:
            result.append(canlist[i])
            curr_y += 1
            flg = True
        elif canlist[i][0] == curr_x+1 and canlist[i][1] == curr_y:
            result.append(canlist[i])
            curr_x += 1
            flg = True
    # print(result)
    if route < len(result) + 1:
        route = len(result) + 1

print(route)

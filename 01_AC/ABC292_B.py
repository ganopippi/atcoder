n,q = map(int, input().split())
event = [list(map(int, input().split())) for i in range(q)]

yellow = []
red = []

for i in range(q):
    player = event[i][1]
    # yellow
    if event[i][0] == 1:
        if player in yellow:
            red.append(player)
        else:
            yellow.append(player)
    if event[i][0] == 2:
        red.append(player)
    if event[i][0] == 3:
        if player in red:
            print("Yes")
        else:
            print("No")
    # print("yellow")
    # print(yellow)
    # print("red")
    # print(red)
    # print("-------")
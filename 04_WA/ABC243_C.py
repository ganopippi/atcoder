n = int(input())
pos = [list(map(int, input().split())) for i in range(n)]
s = list(input())

# print(pos)
r_list = []
l_list = []

# for i in range(n):
#     if s[i] == 'R':
#         for j in range(i,n):
#             if s[j] == 'L' and pos[i][1] == pos[j][1] and pos[i][0] < pos[j][0]:
#                 print('Yes')
#                 exit()


for i in range(n):
    if s[i] == 'L':
        for j in range(len(r_list)):
            if r_list[j][1] == pos[i][1]:
                if r_list[j][0] < pos[i][0]:
                    print('Yes')
                    exit()
        l_list.append(pos[i])
    else:
        for j in range(len(l_list)):
            if pos[i][1] == l_list[j][1]:
                if pos[i][0] < l_list[j][0]:
                    print('Yes')
                    exit()
        r_list.append(pos[i])

# for i in range(len(r_list)):
#     for j in range(len(l_list)):
#         # 右に進む人のy座標と左に進む人のy座標が同じで、x座標が右<左のときYes
#         if r_list[i][1] == l_list[j][1]:
#             if r_list[i][0] < l_list[j][0]:
#                 print('Yes')
#                 exit()

print('No')

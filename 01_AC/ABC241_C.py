n = int(input())  # 幅
s = [list(input()) for i in range(n)]


def cnt_ls(lst):
    cnt = 0
    for i in range(len(lst)):
        if lst[i] == '#':
            cnt += 1
    if cnt >= 4:
        print('Yes')
        exit()


# 横の調査
for i in range(n):  # 縦の動き
    for j in range(n-5):  # 横の動き
        str = s[i]
        # ['1', '2', '3', '4', '5', '6']
        cnt_ls(str[j:j+6])

# 縦の調査
for i in range(n-5):  # 縦の動き
    for j in range(n):  # 横の動き
        temp = []
        for k in range(6):
            temp.append(s[i+k][j])
        # ['1', '2', '3', '4', '5', '6']
        cnt_ls(temp)

# ななめの調査
# 右下方向
for i in range(n-5):  # 縦の動き
    for j in range(n-5):  # 横の動き
        temp = []
        for k in range(6):
            temp.append(s[i+k][j+k])
        # ['1', '2', '3', '4', '5', '6']
        cnt_ls(temp)

# 右上方向
for i in range(5, n):  # 縦の動き
    for j in range(n-5):  # 横の動き
        temp = []
        for k in range(6):
            temp.append(s[i-k][j+k])
        # ['1', '2', '3', '4', '5', '6']
        # print(temp)
        cnt_ls(temp)

print('No')

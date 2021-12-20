n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())

black_list = []

# 黒塗りリスト
for i in range((n-a)-(1-a)+1):
    temp = []
    temp.append(1-a+i+a)
    temp.append(1-b+i+b)
    black_list.append(temp)
print(black_list)

# 出力
# 左下は(P,R)
# 上から下
for j in range(s-r+1):
    line = []
    # 左から右
    for i in range(q-p+1):
        left = False
        right = False
        # if i == n - a:
        #    left = True
        # if j == b - 1 and :
        #    right = True
        if left and right:
            line.append('#')
        else:
            line.append('.')
    print(''.join(line))

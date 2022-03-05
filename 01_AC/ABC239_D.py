a, b, c, d = map(int, input().split())


prime_num = []
limit = 200
for i in range(2, limit):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime_num.append(i)

# 高橋くんの戦略
for i in range(a, b+1):
    flg = False
    # 青木くんの戦略
    for j in range(c, d+1):
        for k in range(len(prime_num)):
            if flg == True:
                break
            # print(i,j,i+j,prime_num[k])
            if i + j == prime_num[k]:
                # print('hit')
                # print(i,j,i+j,prime_num[k])
                flg = True  # この数字は青木の勝ち
                break
    # 素数テーブルと1つも一致しなかった場合、高橋くんが勝つことになる
    if flg == False:
        print('Takahashi')
        exit()

print('Aoki')

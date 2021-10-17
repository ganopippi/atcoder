from operator import itemgetter
n, m = map(int, input().split())
a_list = [list(input().split()) for i in range(2*n)]
# 何番目のプレイヤーか管理する
for i in range(2*n):
    a_list[i].append(i+1)
    a_list[i].append(0)
# じゃんけん
for i in range(m):
    for j in range(n):
        a = a_list[j*2][0][i]
        b = a_list[j*2+1][0][i]
        # print(str(a_list[j*2][1])+str(a_list[j*2][0])+'さんの手')
        # print(a)
        # print(str(a_list[j*2+1][1])+str(a_list[j*2+1][0])+'さんの手')
        # print(b)
        # 手の確認
        if a != b:
            # aの勝ち
            if a+b == 'GC' or a+b == 'CP' or a+b == 'PG':
                # print(a_list[j*2][1])
                a_list[j*2][2] += 1
            # bの勝ち
            else:
                # print(a_list[j*2+1][1])
                a_list[j*2+1][2] += 1
    a_list.sort(key=itemgetter(1))
    a_list.sort(key=itemgetter(2), reverse=True)

for i in a_list:
    print(i[1])
    # print(a_list[0][0][i])

# print('確認用')
# print(a_list)

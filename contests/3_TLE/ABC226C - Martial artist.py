n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
# 必要時間 必要な前提技の数 技1 技2 ...
time = 0
must_waza = []
# 必要な技リスト 最初は最終的に必要な技を入れる
must_waza.append(n)

learned_waza = []
while len(must_waza) > 0:
    next_learn_waza = set()
    for i in range(len(must_waza)):
        # 対象の技を覚えるために必要な技があるかどうか
        # print(l[must_waza[i]-1])
        # if l[must_waza[i]-1][1] != '0':

        # 習得処理
        # print(str(must_waza[i])+'番目'+str(l[must_waza[i]-1][0])+'時間')
        time += l[must_waza[i]-1][0]
        learned_waza.append(must_waza[i])
        # 次の習得技候補に加える
        for j in range(l[must_waza[i]-1][1]):
            next_learn_waza.add(l[must_waza[i]-1][j+2])
    must_waza = list(set(next_learn_waza) - set(learned_waza))
    # print('習得済み:'+str(learned_waza))
    # print('次に習得:'+str(must_waza))
    # print("-----")
    # must_waza.sort(reverse=True)

# print(learned_waza)

learned_waza = list(set(learned_waza))
# print(learned_waza)
# print(l)

# 時間の計算

# for i in range(len(learned_waza)):
print(time)

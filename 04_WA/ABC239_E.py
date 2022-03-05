from collections import deque

n, q = map(int, input().split())
x = list(map(int, input().split()))
temp_ab = [list(map(int, input().split())) for i in range(n-1)]
q_list = [list(map(int, input().split())) for i in range(q)]

ab = []
for i in range(n-1):
    ab.append(sorted(temp_ab[i]))

# print(ab)
hist_bbnki = []
# クエリ
for i in range(q):
    choten = q_list[i][0]

    # 過去に同じ履歴があれば取得
    hist_flg = False
    for j in range(len(hist_bbnki)):
        if hist_bbnki[j] == choten:
            bbnki = hist_bbnki[j]
            hist_flg = True
            break

    if hist_flg == False:
        # 部分木の検索処理
        search_list = deque([])
        search_list.append(choten)
        # 部分木の取得作業
        bbnki = []
        bbnki.append(choten)
        while search_list:
            num = search_list.popleft()
            for j in range(n-1):
                if ab[j][0] == num:
                    # 子要素を抽出
                    search_list.appendleft(ab[j][1])
                    bbnki.append(ab[j][1])
        # 部分木の保存処理
        temp = []
        temp.append(choten)
        temp.append(bbnki)
        hist_bbnki.append(temp)

    # 対応する数字を抽出
    numlist = []
    for k in range(len(bbnki)):
        numlist.append(x[bbnki[k]-1])
    numlist.sort(reverse=True)
    print(numlist[q_list[i][1]-1])
# print(n,q,x)
# print(ab)
# print(q_list)
# # print(a,b)

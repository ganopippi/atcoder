n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
numlow = []
# print(l)

for i in range(n):
    curr_numlow = []
    # 数列のみを取り出す
    # print("いまは"+str(i))
    for j in range(l[i][0]):
        # print(l[i])
        curr_numlow.append(l[i][j+1])
    # print(curr_numlow)
    # 既出の数列かどうかを確認
    numlow.append(','.join(map(str, curr_numlow)))
    # for k in range(len(uniq_numlow)):
    #    a

print(len(set(numlow)))

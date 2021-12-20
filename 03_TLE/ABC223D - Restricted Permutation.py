import itertools
n, m = map(int, input().split())
pairs = [list(map(int, input().split())) for i in range(m)]
rev_pairs = []
# print(pairs)

for i in range(m):
    lists = []
    lists.append(pairs[i][1])
    lists.append(pairs[i][0])
    rev_pairs.append(lists)
for i in range(m):
    result = rev_pairs[i] in pairs
    if result:
        print(-1)
        exit()
pairs.sort()
# print(pairs)
# 数列をつくる
num_list = []
for i in range(n):
    num_list.append(i+1)
all_list = list(itertools.permutations(num_list))
result_list = []
# print(all_list)
for i in range(len(all_list)):
    flg = True
    # print(all_list[i])
    for j in range(m):
        if all_list[i].index(pairs[j][0]) > all_list[i].index(pairs[j][1]):
            flg = False
            continue
    if flg:
        result_list.append(all_list[i])
result_list.sort()
print(' '.join(map(str, result_list[0])))
# print(result_list)

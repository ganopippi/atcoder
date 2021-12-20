import itertools

n, m = map(int, input().split())
ab_list = [list(map(int, input().split())) for i in range(m)]
cd_list = [list(map(int, input().split())) for i in range(m)]
# print(ab_list)
# print('------')
# print(cd_list)

if m == 0:
    print('Yes')
    exit()

num_list = []
for i in range(n):
    num_list.append(i+1)

# print(num_list)
all_list = list(itertools.permutations(num_list))

# 全ての組み合わせごと
for i in range(len(all_list)):
    # print("対象")
    # print(all_list[i])
    after_list = []
    for j in range(len(cd_list)):
        temp = []
        # print('temp---')
        temp.append(all_list[i][cd_list[j][0]-1])
        temp.append(all_list[i][cd_list[j][1]-1])
        after_list.append(sorted(temp))
        # print(after_list)
        # cd_list[j]
    ab_set = sorted(ab_list)
    after_set = sorted(after_list)
    # print(after_set)
    if ab_set == after_set:
        print('Yes')
        exit()
    # 組み合わせの1つの数字ごと
    # for j in range(n):
    #     temp = []
    #     if cd_list[k][0]
    #     temp.append(cd_list[k][0])
    #     temp.append(cd_list[k][1])
    #     after_list.append(temp)
    # print('----')
    # print(after_list)
print('No')

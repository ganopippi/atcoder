s = input()
s_cnt = len(s)

mst = 'oxxoxxoxxoxxoxxoxxoxxoxx'
mst_cnt = 24
for i in range(mst_cnt-s_cnt):
    # print(mst[i:s_cnt+i])
    if mst[i:s_cnt+i] == s:
        print('Yes')
        exit()
print('No')

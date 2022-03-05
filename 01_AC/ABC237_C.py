

import re
s = input()
rem = s.strip('a')
slen = len(rem)
# 最初のaの連続より最後のaの連続が短い場合はFalse
# a_start = 0
# a_end = 0
m = re.search('[b-z]', s)
# print(m)
if m:
    a_start = m.start()
    a_end = m.end()
    # start_a_cnt = a_start
    # end_a_cnt = len(s) - a_end
    for i in range(a_start):
        if s[-i-1] != 'a':
            print('No')
            exit()


flg = True
# print(rem,slen)
for i in range(slen):
    # print(rem[i],rem[-i-1])
    if rem[i] != rem[-i-1]:
        flg = False

if flg:
    print('Yes')
else:
    print('No')

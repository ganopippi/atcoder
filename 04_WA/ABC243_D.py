import re
n, x = map(int, input().split())
s = input()

curr = x


# print(s)
s = re.sub('LU|RU', '', s)
# print(s)

culc_lst = []
temp = []
temp.append(s[0])
temp.append(1)
culc_lst.append(temp)

for i in range(1, len(s)):
    # print(culc_lst[-1][0][0],s[i])
    if culc_lst[-1][0] == s[i]:
        culc_lst[-1][1] += 1
    else:
        temp = []
        temp.append(s[i])
        temp.append(1)
        culc_lst.append(temp)

# print(culc_lst)

for i in range(len(culc_lst)):
    curr_s = culc_lst[i][0]
    cnt = culc_lst[i][1]
    if curr_s == 'U':
        curr = curr // (2 ** cnt)
    if curr_s == 'L':
        curr = curr * (2 ** cnt)
    if curr_s == 'R':
        for j in range(cnt):
            curr = curr * 2 + 1

# for i in range(len(s)):
#     if s[i] == 'U':
#         curr = curr // 2
#     if s[i] == 'L':
#         curr = curr * 2
#     if s[i] == 'R':
#         curr = curr * 2 + 1

print(int(curr))

s = input()
s_list = []

for i in range(len(s)):
    # print(s[i:]+s[0:i])
    s_list.append(s[i:]+s[0:i])
s_list.sort()
print(s_list[0])
print(s_list[len(s_list)-1])

n,q = map(int, input().split())


l = [list(map(int, input().split())) for i in range(n)]
s = [list(map(int, input().split())) for i in range(q)]

for i in range(len(s)):
    ans_list = l[s[i][0]-1]
    print(ans_list[s[i][1]])
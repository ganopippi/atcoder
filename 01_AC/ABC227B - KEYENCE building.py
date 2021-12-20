n = int(input())
s = list(map(int, input().split()))
cnt = 0
for i in range(n):
    # print(s[i]) #予想値
    for j in range(1, 1001):
        for k in range(1, 1001):
            if s[i] < 4*j*k+3*(j+k):
                continue
            if s[i] == 4*j*k+3*(j+k):
                #print(str(s[i])+'='+str(4*j*k+3*j+3*k)+'j:'+str(j)+' k:'+str(k))
                cnt += 1
                break
        else:
            continue
        break
print(n-cnt)

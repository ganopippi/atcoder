n, k, a = map(int, input().split())
cnt = 0
while cnt < k:
    cnt += 1
    #print(str(cnt)+'枚目： 人'+str(a))
    if a == n:
        a = 0
    if cnt != k-1:
        a += 1
print(a)
print((k % n)+1)

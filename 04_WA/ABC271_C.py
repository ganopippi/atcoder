n = int(input())
a = list(map(int, input().split()))

a.sort()

s = list(set(a))

dup_cnt = len(a)- len(s)
cnt = 0
pos = 0
drop_cnt = 0 - dup_cnt


for i in range(len(a)):
    # print(str(cnt+1)+'冊目')
    # print(cnt , a[i] )
    if cnt + 1 == a[pos]:
        pos += 1
        cnt += 1
    else: 
        # print(cnt,drop_cnt,n)
        # drop_cntとの比較・加算
        if cnt + drop_cnt  <= n - 2:
            drop_cnt += 1
            cnt += 1
        else:
            break

print(cnt)
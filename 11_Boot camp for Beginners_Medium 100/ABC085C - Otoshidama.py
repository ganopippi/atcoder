N, Y = map(int, input().split())
# N=枚数、Y=金額

for i in range(N+1):
    for j in range(N+1):
        k = N-i-j
        if 0 <= k <= 2000 and 10000*i+5000*j+1000*k == Y:
            print(i, j, k)
            exit()
print(-1, -1, -1)

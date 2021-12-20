n = int(input())
a = list(map(int, input().split()))
i = 0
count = 0

while a[i] % 2 == 0:
    a[i] = a[i] / 2
    if i == n-1:
        i = 0
        count += 1
    else:
        i += 1

print(count)

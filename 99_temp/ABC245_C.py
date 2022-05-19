n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# curr = ()
# curr.add(a[0])
# curr.add(b[0])
curr = []
curr.append(a[0])
curr.append(b[0])
curr = list(set(curr))

for i in range(n-1):
    next_a = a[i+1]
    next_b = b[i+1]

    temp = []
    for j in range(len(curr)):
        if abs(curr[j] - next_a) <= k:
            temp.append(next_a)
        if abs(curr[j] - next_b) <= k:
            temp.append(next_b)
    if len(temp) == 0:
        print('No')
        exit()
    curr = list(set(temp))

    # curr_a = a[i]
    # curr_b = b[i]
    # next_a = a[i+1]
    # next_b = b[i+1]
    # if abs(curr_a - next_a) > k and abs(curr_b - next_b) > k and abs(curr_a - next_b) > k and abs(curr_b - next_a) > k:
    #     print('No')
    #     exit()

print('Yes')

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

same_position = 0
not_same_position = 0

for i in range(n):
    for j in range(n):
        if a[i] == b[j]:
            if i == j:
                same_position += 1
            else:
                not_same_position += 1

print(same_position)
print(not_same_position)

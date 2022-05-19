n = int(input())
x = list(set(list(map(int, input().split()))))

for i in range(2001):
    if i not in x:
        print(i)
        exit()

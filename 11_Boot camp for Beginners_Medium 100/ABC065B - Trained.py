n = int(input())
a = [int(input()) for i in range(n)]

# aに2がなければ-1を出力する

history = []
current = 0
# aがある番目のボタンがあればOK
for i in range(n):
    history.append(a[current])
    current = a[current]-1
# print(history)
two_count = history.count(2)
if two_count == 0:
    print(-1)
    exit()
two_place = history.index(2)
print(two_place+1)

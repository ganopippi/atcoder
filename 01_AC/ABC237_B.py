h, w = map(int, input().split())
a = [list(input().split()) for i in range(h)]
# print(a)

# res = list(zip(*a))
res = [list(x) for x in zip(*a)]
# print(res)

for i in range(w):
    print(' '.join(res[i]))

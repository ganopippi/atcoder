a, b, c, d = map(int, input().split())

# print(a,b,c,d)

x_list = []
# a, bからの距離がルート5となる格子点
x_list.append([a+1, b+2])
x_list.append([a+1, b-2])
x_list.append([a+2, b+1])
x_list.append([a+2, b-1])
x_list.append([a-1, b+2])
x_list.append([a-1, b-2])
x_list.append([a-2, b+1])
x_list.append([a-2, b-1])

y_list = []
y_list.append([c+1, d+2])
y_list.append([c+1, d-2])
y_list.append([c+2, d+1])
y_list.append([c+2, d-1])
y_list.append([c-1, d+2])
y_list.append([c-1, d-2])
y_list.append([c-2, d+1])
y_list.append([c-2, d-1])

# print(x_list)
# print(y_list)

for i in range(len(x_list)):
    for j in range(len(y_list)):
        if x_list[i] == y_list[j]:
            print('Yes')
            exit()

print('No')

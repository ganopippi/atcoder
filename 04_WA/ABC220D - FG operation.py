# 出来ていない問題

def action_f(a_list):
    x = a_list[0]
    y = a_list[1]
    del a_list[0:2]
    a_list.insert(0, (x+y) % 10)
    return a_list


def action_g(a_list):
    x = a_list[0]
    y = a_list[1]
    del a_list[0:2]
    a_list.insert(0, (x*y) % 10)
    return a_list


n = int(input())
a = [int(i) for i in input().split()]


for i in range(0, 10):
    for j in range(len(a)-1):
        a = action_f(a)
        for k in range(len(a)-1):
            a = action_g(a)
            if len(a) == 1:
                exit()
            print(n, a)

print(a)
# print(i)

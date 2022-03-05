from collections import deque
import sys
input = sys.stdin.readline


def main():

    n = int(input())

    cnt = 0
    # lst = [1,1,1,1,1,1,1,1,1]
    lst = deque([1, 1, 1, 1, 1, 1, 1, 1, 1])
    lst = deque([1, 1, 1, 1, 1])
    for i in range(n-1):
        temp = deque([0, 0, 0, 0, 0])
        temp[0] = lst[0] + lst[1]
        temp[1] = lst[0] + lst[1] + lst[2]
        temp[2] = lst[1] + lst[2] + lst[3]
        temp[3] = lst[2] + lst[3] + lst[4]
        temp[4] = lst[3]*2 + lst[4]
        # for j in range(len(temp)):
        # for j in range(1,5):
        #     temp[j] = lst[j-1] + lst[j] + lst[j+1]
        # temp[5] = temp[3]
        # temp[6] = temp[2]
        # temp[7] = temp[1]
        # if j == 0:
        #     temp[j] = lst[j] + lst[j+1]
        # elif j == 8:
        #     temp[j] = lst[j-1] + lst[j]
        # else:
        #     temp[j] = lst[j-1] + lst[j] + lst[j+1]
        # print(temp)
        lst = temp

    for i in range(len(lst)):
        if i != 4:
            cnt += lst[i]*2
        else:
            cnt += lst[i]

    print(cnt % 998244353)


main()

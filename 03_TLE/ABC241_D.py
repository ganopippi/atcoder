import numpy as np

q = int(input())
query = [list(map(int, input().split())) for i in range(q)]
a = []

for i in range(q):
    current_query = query[i]
    # print(current_query)
    if current_query[0] == 1:
        a.append(current_query[1])
        a.sort()
    else:
        x = current_query[1]
        k = current_query[2]
        if len(a) < k:
            print('-1')
        #  A の x 以下の要素のうち、大きい方から k 番目の値を出力する。
        elif current_query[0] == 2:
            # res = [i for i in a if i <= x]
            arr = np.array(a)
            res = np.where(arr <= x)
            if np.count_nonzero(arr <= x) < k:
                print('-1')
            else:
                print(res[-k])
        # A の x 以上の要素のうち、小さい方から k 番目の値を出力する。(k は 5 以下)
        elif current_query[0] == 3:
            # res = [i for i in a if i >= x]
            arr = np.array(a)
            res = np.where(arr >= x)
            # if len(res) < k:
            if np.count_nonzero(arr >= x) < k:
                print('-1')
            else:
                print(res[k-1])

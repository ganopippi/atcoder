n = int(input())  # ボールの個数
k = int(input())  # タイプBのロボットの初期x座標
x = list(map(int, input().split()))  # ボールが置かれるx座標(list)

m = k/2  # 中間地点
r = 0  # 距離

for i in x:
    # タイプBよりにボールがある場合
    if x[i] >= m:
        r += (k - x[i])*2
    else:
        r += x[i]*2
print(r)

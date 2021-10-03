N = int(input())
result = 0
res_str = '0'


start_num_str = ''
start_num = 1
if N > 10:
    # 9,99,999,9999 で 1,12,123,1234と増えていく
    for i in range(1, len(str(N))):
        res_str = res_str + str(i)
    # 1桁少ない数の最大値を簡易的に計算
    for i in range(1, len(str(N))):
        start_num_str = start_num_str + '9'
    start_num = int(start_num_str) + 1

# print(start_num)

s = start_num
"""
#これはダメっぽい
while s <= N:
    cnt = 0
    #1を先頭から何個含むか確認する処理
    for j in range(len(str(s))):
        if str(s)[j] == '1':
            cnt += 1
        else:
            break
    result += cnt
    
    
    if str(s) == '1'+'9'*(len(str(s))-1):
        s = s +int('8' + '0'*(len(str(s))-2) + '1')
    else:
        s+=1
"""
if N > 100:
    if N >= N/int('12'+'0'*(len(str(N))-2)):
        result = result + int('1'*len(str(N))) - int('8'+'0'*(len(str(N))-1))
        result = result + (int('8'+'0'*(len(str(N))-2)) -
                           int('12'+'0'*(len(str(N))-2)))


else:
    # 999 であれば 100~999を計算
    for i in range(start_num, N+1):
        cnt = 0
        for j in range(len(str(i))):
            if str(i)[j] == '1':
                cnt += 1
            else:
                break
        result += cnt


result = result + int(res_str)

print(result)

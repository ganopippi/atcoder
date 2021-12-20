n = int(input())
lines = [list(map(int, input().split())) for i in range(n)]
passed_len = 0
# 導火線の合計の長さ
# for i in range(len(lines)):
#    all_len += lines[i][0]
# print(all_len)
# 導火線ごとにかかる時間
all_times = []
sum_times = 0
for i in range(len(lines)):
    time = lines[i][0] / lines[i][1]
    all_times.append(time)
    sum_times += time
hit_time = sum_times/2
# print('当たる時間:'+str(hit_time))
# ぶつかる導火線の本目
passed_time = 0
hit_line = 0
for i in range(len(lines)):
    if hit_time > passed_time + all_times[i]:
        passed_time += all_times[i]  # 経過時間
        passed_len += lines[i][0]  # 通過距離
        hit_line += 1
    else:
        break
# print('当たる本目:'+str(hit_line))
# 残り時間
remain_time = hit_time - passed_time
# print('残り時間:'+str(remain_time))
# print('すでに進んだ長さ:'+str(passed_len))
# 次の導火線を進む長さ
going_len = lines[hit_line][1] * remain_time
print(passed_len + going_len)

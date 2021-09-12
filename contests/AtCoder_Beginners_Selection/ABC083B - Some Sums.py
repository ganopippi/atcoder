N, A, B = map(int, input().split())
i = 1
num_sum = 0  # 返す合計値
while i <= N:
    str_num_list = list(str(i))
    int_num_list = list(map(int, str_num_list))
    if A <= sum(int_num_list) and sum(int_num_list) <= B:
        num_sum += i
    i += 1

print(num_sum)

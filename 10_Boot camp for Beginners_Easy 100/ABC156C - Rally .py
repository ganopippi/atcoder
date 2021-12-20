n = int(input())
x = list(map(int, input().split()))

l_power = []
p_max = max(x)
p_min = min(x)
p_now = 0

while p_min + p_now <= p_max:
    power = 0
    for i in range(n):
        # print(str(p_min+p_now)+'で開催するときの'+str(i)+'さん_'+str(x[i])+'住み')
        #print('距離:'+str(x[i] - p_min + p_now))
        power = power + ((x[i] - (p_min + p_now)) ** 2)
        # print(p_min)
        # print(power)
    l_power.append(power)
    p_now += 1
print(min(l_power))

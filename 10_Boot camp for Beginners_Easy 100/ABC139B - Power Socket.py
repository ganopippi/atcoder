a, b = map(int, input().split())
now_plag = 1
plag_count = 0
while b > plag_count * a - plag_count + 1:
    #print(plag_count * a - plag_count + 1)
    plag_count += 1

print(plag_count)

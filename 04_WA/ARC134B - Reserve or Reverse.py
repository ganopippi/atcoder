n = int(input())
s = list(input())

ki = []
gu = []

for i in range(n):
    if i % 2 != 0:
        ki.append(s[i])
    else:
        gu.append(s[i])

# ki = sorted(ki)
gu = sorted(gu)
# print(ki, gu)

result = ''

for i in range(n//2):
    result = result + gu[i]
    if n % 2 == 0:
        result = result + ki[i]

print(result)

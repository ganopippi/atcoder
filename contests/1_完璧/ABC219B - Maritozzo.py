a = input()
b = input()
c = input()
t = input()

y = ''

x = list(t)

# print(x)

for i in x:
    if i == '1':
        y = y + a
    elif i == '2':
        y = y + b
    else:
        y = y + c

print(y)

a = int(input())
b = int(input())

if str(b) in str(a*2):
    print(a)
    exit()
else:
    start = 1
    if b > a:
        start = b * 2 * 10 ** (len(str(b)) - len(str(a)))
    for i in range(1, 10**(18 - len(str(a)))):
        for j in range(len(str(i))+1):
            if str(b) in str(int(str(i)[:j] + str(a) + str(i)[j:])*2):
                print(int(str(i)[:j] + str(a) + str(i)[j:]))
                exit()

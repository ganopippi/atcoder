n, a, b = map(int, input().split())
s = list(input())

passed = 0
passed_foreign = 0

for i in range(n):
    if passed < a + b:
        if s[i] == 'a':
            print('Yes')
            passed += 1
        elif s[i] == 'b' and passed_foreign < b:
            print('Yes')
            passed += 1
            passed_foreign += 1
        else:
            print('No')
    else:
        print('No')

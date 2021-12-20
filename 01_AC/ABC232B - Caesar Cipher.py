s = input()
t = input()

diff = ord(s[0]) - ord(t[0])

after = ''

for i in range(len(t)):
    word = ord(t[i]) + diff
    # print('a')
    # print(ord('a'))
    # print('z')
    # print(ord('z'))
    # print('H')
    # print(ord('H'))
    # print(word)
    if word < 97:
        word = word + 26
    if word > 122:
        word = word - 26
    after = after + chr(word)
# print(after)
if s == after:
    print('Yes')
else:
    print('No')

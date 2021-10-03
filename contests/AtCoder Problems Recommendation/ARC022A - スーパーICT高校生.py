s = input()
# すべて小文字にする
s = s.lower()
# 文字列の位置を検索、見つかった場所から後ろを検索する
i = s.find('i')
c = s.find('c', i)
t = s.find('t', c)
if i > -1 and c > -1 and t > -1:
    print('YES')
else:
    print('NO')

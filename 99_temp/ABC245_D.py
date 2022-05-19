from numpy.polynomial import Polynomial
n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

b = []

# a.reverse()
# c.reverse()
# 係数を指定する場合は、高次の項から順番に指定する
p1 = Polynomial(a)
# np.poly1d(a)
p2 = Polynomial(c)
# print(p1)

# print(p2/p1)

p3 = p2//p1
ans = p3.convert().coef

for i in range(len(ans)):
    ans[i] = int(ans[i])
print(' '.join(ans))

# print(p3.c)
# print(p3.r)

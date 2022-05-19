a, b, c, d = map(int, input().split())

ab = int(str(a).zfill(2)+str(b).zfill(2))
cd = int(str(c).zfill(2)+str(d).zfill(2))

if ab <= cd:
    print('Takahashi')
else:
    print('Aoki')

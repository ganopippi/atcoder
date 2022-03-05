n, l, w = map(int, input().split())
a = list(map(int, input().split()))  # a: シートのある場所
# n: すでにあるシート
# l: 橋の長さ
# w: シートの長さ

sheet_count = 0
start = 0
end = 0

for i in range(len(a)):
    range_length = a[i] - end
    if range_length > 0:
        sheet_count += -(-range_length // w)
    start = a[i]
    end = a[i] + w

if end != l:
    sheet_count += -(-(l-end) // w)

print(sheet_count)

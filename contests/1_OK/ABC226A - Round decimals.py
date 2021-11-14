from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
x = float(input())

# print(int(round(x,0)))
print(Decimal(str(x)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))

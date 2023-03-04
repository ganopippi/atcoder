n = int(input())

ans = 0

def get_divisors_len(num):
    divisors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divisors.append(i)  
            if i**2 == num:
                continue
            divisors.append(int(num/i))
    return len(divisors)

b_point = n // 2

if n % 2 == 0:
    is_even = True
    for i in range(1,n // 2):
        l = i
        r = n-i
        
        ans += get_divisors_len(l) * get_divisors_len(r)
else:
    is_even = False
    for i in range(1,n // 2 + 1):
        l = i
        r = n-i
        
        ans += get_divisors_len(l) * get_divisors_len(r)

if is_even:
    print(ans * 2 + get_divisors_len(n // 2) * get_divisors_len(n // 2))
else:
    print(ans * 2)
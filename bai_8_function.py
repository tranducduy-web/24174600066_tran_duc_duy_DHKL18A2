def find_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

print(find_divisors(12))
print(find_divisors(25))
print(find_divisors(7))
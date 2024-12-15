def is_perfect_number(n):
    if n <= 0: return False
    total = sum(i for i in range(1, n) if n % i == 0)
    return total == n

print(is_perfect_number(6))
print(is_perfect_number(28))
print(is_perfect_number(12))
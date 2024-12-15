def is_perfect_square(n):
    if n < 0:
        return False
    for i in range(n + 1):
        if i * i == n:
            return True
    return False

print(is_perfect_square(16))
print(is_perfect_square(25))
print(is_perfect_square(10))
print(is_perfect_square(-4))
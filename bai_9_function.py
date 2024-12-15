def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(ucln(12, 15))
print(ucln(25, 30))
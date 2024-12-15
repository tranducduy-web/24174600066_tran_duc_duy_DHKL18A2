import math

def decimal_to_fraction(x):
    denom = 10**len(str(x).split('.')[1])
    num = int(x * denom)
    gcd = math.gcd(num, denom)
    return num // gcd, denom // gcd

print(decimal_to_fraction(0.75))
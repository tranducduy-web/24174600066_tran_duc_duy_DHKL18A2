def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

print(is_float("123"))
print(is_float("-456.78"))
print(is_float("12.3e4"))
print(is_float("abc"))
print(is_float("12.3.4"))
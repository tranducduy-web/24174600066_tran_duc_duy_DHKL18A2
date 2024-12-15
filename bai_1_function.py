def is_integer(string):
    if string.isdigit():
        return True
    if string.startswith('-') and string[1:].isdigit():
        return True
    return False

print(is_integer("123"))
print(is_integer("-456"))
print(is_integer("12.3"))
print(is_integer("abc"))
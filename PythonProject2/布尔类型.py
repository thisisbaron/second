print(type(True))
print(type(False))

print(True + 1)
print(False + 1)

bool_true = True
bool_false = False
print(bool_true)

# 非0即真
print(bool(1))  # True
print(bool(0))  # False
print(bool(-1)) # True
print(bool(0.00))   #False
print(bool(0.001))  # True

# 字符串的真假值，只要不是空，就是True,否则就是False
print(bool("a")) # True
print(bool(" "))    # True
print(bool(""))# False
print(bool("True"))# True
print(bool("False"))# True
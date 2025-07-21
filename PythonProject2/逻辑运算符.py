a = True
b = False

print(a and b)
print(a or b)
print(not (a and b))

a = 3
b = 4
c = 5

print(a > b and b < c)
print(a > b or b < c)
print(not (a > b))
print(not (a > b and b < c))
# 当and 从左到右.若所有值均为真,则返回最后一个值，只有一个假的值，则返回第一个假的值】
# 当or 从左到右 返回第一个真的值，若全为假，则返回最后一个为假的值



a = 20
b = 30
print(a and b)
print(b and a)
print(a or b)
# 逻辑运算的优先级

print(not 3 > 2 and 3 < 4 or 4 > 5 and 9 < 8)
print(3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2)
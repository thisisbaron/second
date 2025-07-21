name = 'abcdef'
#注意 : 字符串的索引值从0开始计算的
print(name[0]) #a
print(name[-1]) #f
print(name[-2]) #e
print(name[3]) #d
print(name[4])  #e

name = 'abcdef'
print(name[0:3]) # 下标为0-2的字符
print(name[0:5]) # 下标为0-4的字符
print(name[3:5]) # 下标为3、4的字符
print(name[2:]) # 取下标2开始到最后的字符
print(name[1:-1]) # 取从下标1开始 到 最后第二个之间的字符
print(name[5:1:-2])
# 起始:结束:步长 步长是整数类型
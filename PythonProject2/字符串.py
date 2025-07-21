# 1. 将字符串"abcd”转成大写
print("abcd".upper())
# 2. 计算字符串 "cd”在 字符串"abcd"中出现的位置
print("abcd".find("cd"))
print("abcd".index("cd"))
# 3. 字符串"a，b，c，d”，请用逗号分割字符串，分割后的结果是什么类型的?
a_string = "a,b,c,d"
a_list = a_string.split(",")
print(a_list)
print(type(a_list))
# 4."{}喜欢{}".format("张三")执行会出错，请修改代码让其正确执行
print("{}喜欢{}".format("张三","打游戏"))
# 5. string = "python is good"，请将字符串里的Python替换成python, 并输出替换后的结果
string = "python is good"
print(string.lower())
print(string.replace("P","p"))
# 6. "this is python"，请将字符串里的python替换成apple
print("this is python".replace("python","apple"))
# 7. "this is python"，请用程序判断该字符串是否以this开头
print("this is python".startswith("this"))
# 8. "this is python"，将此字符串的每一个单词首字母大写
print("this is python".title())
# 9. "this is a book\n"， 字符串的末尾有一个换行符，请将其删除
print("this is python\n".strip())
print(11111111111)
# 10. "\nthis is a book\n"，字符串的首尾有一个换行符，请将其开头的换行符删除
print("\nthis is a book\n".lstrip())
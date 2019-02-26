# 整型
i = 30
print(i)
# type()函数返回变量的数据类型
print(type(i))

# 浮点类型
a = 12.35
print(a)
print(type(a))

# 布尔值
# 布尔值只有两种结果True和False 对应二进制中的0和1
b = 1
print(b == 1)
print(b == 3)

# 字符串
# 单引号之间的单行字符串
s = 'a'
print(s)
print(type(s))

# 双引号之间的单行字符串
s1 = "as myself"
print(s1)
print(type(s1))

# 三个引号之间的多行字符串
s2 = ''' as me
you are 
my friend
'''
print(s2)
print(type(s2))

# 转义字符
str1 = "oh \\my friend"
print(str1)

str2 = "c:\\user"
print(str2)
# 换行符
str3 = "oh \r\nmy friend"
print(str3)

str4 = "let's go"
print(str4)
str4 = 'let\'s go'
print(str4)

# 字符串的格式化
str1 = "I am %s,I am %d years old."
print(str1%("Jack", 26))

str1 = "I am %s"
print(str1 % "jack")
# format函数格式化字符串
str2 = "I am {0},I am {1} years old.".format("jack", 18)
print(str2)
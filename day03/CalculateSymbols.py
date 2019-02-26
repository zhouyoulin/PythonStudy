# 数字运算符
a = 5 + 2 * 3 - 6 / 2
print(a)
print(type(a))
# 和python2.x Java不同
a = 9 / 4
print(a)
# 取整
a = 9 // 4
print(a)
# 取余
a = 9 % 4
print(a)
# 幂运算
a = 3**3
print(a)

# 比较运算符
a = 8 > 7
print(a)

a = 8 < 7
print(a)

a = 8 == 7
print(a)

# 逻辑运算符
a = 8 > 7
b = 8 < 7
c = a and b
print(c)

c = a or b
print(c)

c = not a
print(c)


# 成员运算符
a = [1, 2,  3, 4]
b = 7
c = 3
print(b in a)
print(c in a)
print(b not in a)


# 身份运算符
a = 1
b = 1
print(a is b)

a = "you and me"
b = "you and me"
print(a is b)

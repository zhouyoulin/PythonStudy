# 函数
def add(a, b):
    print("{0}+{1}={2}".format(a, b, a+b))
add(5, 45)

# 参数传值
# 不可变对象传值
def changeInt(a):
    a = 20
    print("函数内a的值为: ",a)
b = 10
changeInt(b)
print(b)

def changeStr(str):
    str = "hello wrod"
    print(str)
str = "1a"
changeStr(str)
print(str)

# 可变对象传值
def changeList(list):
    list.append([1, 2, 3, 4])
    print(list)
list = [12, 13, 14]
changeList(list)
print(list)


# 参数类型
# 普通参数，关键字参数，默认参数，收集参数
def print_info(name, age, *args, gender="male",  **kwargs):
    print("name = ", name)
    print("age = ", age)
    print("gender = ", gender)
    for i in args:
        print(i)
    print("*"*50)
    for item in kwargs.items():
        print(item)
# 普通参数调用
print_info("xiaoli", 45)

# 关键字参数调用
print_info(age=45, name="jack")

# 修改默认参数
print_info(age=45, name="jack", gender="female")

# 传递元组参数
# print_info(age=45, name="jack",  "I am good", "I love u", gender="female")
# 调用收集参数的时候，前面用普通参数调用
print_info(45, "jack", "I am good", "I love u", gender="female")

# 字典收集参数
print_info(45, "jack", "I am good", "I love u", gender="female", hobby="游泳")


# 函数的返回值
def area(width, high):
    return width*high
arae = area(5, 8)
print(arae)

# 递归函数
# 斐波那契数列
def fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)
print(fibo(6))

# 汉诺塔问题

def hano(n, a, b, c):
    if n == 1:
        print(a, "-->", c)
        return None
    if n == 2:
        print(a, "--->", b)
        print(a, "--->", c)
        print(b, "--->", c)
        return None
    hano(n-1, a, c, b)
    print(a, "--->", c)
    hano(n-1, b, a, c)
hano(4, "a", "b", "c")
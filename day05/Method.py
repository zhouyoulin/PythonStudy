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
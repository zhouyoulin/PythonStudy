# 分支结构
# grade = input("输入你的成绩:")
# grade = int(grade)
grade = 80
if grade > 90:
    print("A+")
elif grade > 80:
    print("A-")
elif grade > 70:
    print("B")
elif grade >= 60:
    print("C")
else:
    print("D")

# 循环
# 打印99乘法表

for i in range(1, 10):
    for j in range(1, i+1):
        print(i*j, end=" ")
    print("")

# 打印一个菱形
#    *
#   * *
#  *   *
#   * *
#    *

for i in range(0, 4):
    for j in range(0, 4-i):
        print(" ", end="")
    print("*",end="")
    for m in range(0,i*2-1):
        print(" ", end="")
    if i != 0:
        print("*", end="")
    print("")
else:
    for i in range(0, 4):
        for j in range(0, i+1):
            print(" ", end="")
        print("*", end="")
        for m in range(0, (4-i-1)*2 - 1):
            print(" ", end="")
        if i != 3:
            print("*",end="")
        print("")

a = 0
while a < 10:
    print(a)
    a += 1
else:
    print("else {0}".format(a))
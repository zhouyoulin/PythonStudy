# 类的定义与实例化
class A:
    pass
a = A()

# 类的构造方法
class Student:
    work = "study"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("__init__")
stu = Student("xiaohong", 16) # 构造方法在类被实例化的时候就被调用
print(stu.name)
print(stu.age)
print(stu.work)



class Teacher:
    __age = 20
    _name = "teacher"
    work = "teach"
    def __init__(self,name):
        self.name = name

# __dict__函数可以查看类的所有属性方法
# 通过该方法可以看出私有变量在python中是通过改名来实现的
print(Teacher.__dict__)
print(Teacher._Teacher__age) # 通过dict打印出来的属性名来访问私有属性

print(Teacher._name)


# 类属性和实例属性的区别
class Test:
    test_attr = 100

    def __init__(self):
        self.sl_attr = 100

    def func(self):
        print("类属性的值", Test.test_attr)
        print("self.类属性的值", self.test_attr)
        print(id(self.test_attr))
        print("self.实例属性的值", self.sl_attr)

a = Test()
print(id(Test.test_attr))
a.func()
print("*"*50)
b = Test()
print(id(Test.test_attr))
b.func()
print("*"*50)
a.test_attr = 200
a.sl_attr = 200
a.func()
b.func()
print("*"*50)
Test.test_attr = 300
print(id(Test.test_attr))
a.func()
b.func()


# 类的方法
class Dog:
    # 实例方法
    def eat(self):
        print("eating")

    # 类方法
    @classmethod
    def sleep(cls):
        print("sleep-ing")

    # 静态方法
    @staticmethod
    def check():
        print("checking.....")

d = Dog()
d.eat()
# Dog.eat() # 报错
Dog.eat(d)
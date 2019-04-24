# 继承构造方法
class Parent:

    def __init__(self):
        print("parent __init__")

    def eat(self):
        print("parent eating")

    def talk(self):
        print("parent talking---------")
class Child(Parent):
    def __init__(self):
        super().__init__() # 子类如果有构造方法时，子类实例化的时候不会主动调用父类的构造方法，需要手动调用
        print("child  __init__")

    def eat(self):
        Parent.eat(self) # 子类通过父类类名来调用父类方法
        super().eat()

child = Child()
child.eat()
child.talk() # 子类没有重写父类的方法


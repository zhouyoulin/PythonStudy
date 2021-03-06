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

print(None)

list = [1, 2, 3, 4, 5, 6, 7]

# list访问
# 打印下标为1的元素
print(list[1])

# list的分片操作（注意list分片操作会生成一个新的list）
# 可以用id()函数来查看，id用于区分变量的内存地址
# 打印下标1到末尾的元素

print(id(list))
list1 = list[1:]
print(id(list1))
print(list1)
# 打印下标1-4的元素
print(list[1:5])
# 割一个元素打印下标1-5的元素
print(list[1:6:2])
# 下标可以为负数 用负数打印时默认开始下标为-1 为list最后一个元素
print(list[-1])
print(list[-6:-1])

print(list[-1:-6:-1])

# 更新list
# 更新list中某个元素用下标重新赋值
print(list)
list[2] = 100
print(list)


# 删除list中的元素
# del用于删除操作

print(list)
del list[2]
print(list)
# del 也可以清空list所有元素
# del list
# print(list)
# print(list[0])


# list遍历
for i in list:
    print(i)

# 列表的操作符运算
l1 = [1, 2, 3]
l2 = [5, 6, 7]
# 相加 组合
print(l2+l1)
# len函数 用于取长度
print(len(l1))
# 乘法 列表乘法扩充多少
print(l1*4)
# 成员判断
print(1 in l1)
print(1 in l2)

# 列表的特殊创建方式 看起来很牛逼
# 下面表达式用于创建一个1-19的偶数列表
l = [x for x in range(1, 20) if x % 2 == 0]
print(l)

# 关于列表的常用函数
# max函数 用于取最大值
# min函数 用于取最小值

print(max(l))
print(min(l))

# append函数，向list中追加一个值，放在最后
print(l)
l.append(20)
print(l)


# count函数 用于统计某个元素在list中出现的次数
l = [1, 2, 4, 5, 2, 3, 4, 1, 2, 3]
print(l.count(1))

# extend函数 在列表的最后一次性追加另一个序列里的值
l1 = ["nihao", "hello", "word"]
l.extend(l1)
print(l)

# index函数 用于查找第一个匹配元素的下标
print(l.index(2))
# 若没有，返回？ 事实证明 没有会报错
# 所以在进行index操作的时候要先判断值是否存在于列表中
# print(type(l.index("kkkk")))

# 插入操作 list.insert(index, obj)
# index 插入的下标位置，插入的时候将该值放到此下标，原列表中的该下标值和后面的值往后移
# obj 要插入的值

print(l)
l.insert(1, "kkk")
print(l)
print("*" * 30)
l.insert(40, "kkk")
# 移除操作
# list.pop(index=-1) 用于移除列表中的元素，默认为最后一个元素
print(l)
l.pop()
print(l)
# 也可以用于移除指定下标的元素
l.pop(2)
print(l)
# 若移除的下标超过长度 会发生什么？
# 下面代码证明会报错
# l.pop(99)
# print(l)

# list.remove(obj) 移除列表中指定的元素
print(l)
l.remove("kkk")
print(l)

# "kkk"已经被移除了 如果再移除一次
# ValueError: list.remove(x): x not in list
# l.remove("kkk")
# print(l)

# list.reverse() 反转列表

l.reverse()
print(l)


# list.sort列表排序
# sort 函数不能对同时存在string和int的列表进行排序
print("*" * 50)
# l.sort()
# print(l)

l1 = [1, 3, 2, 6, 7, 9, 5]
l1.sort()
print(l1)

# 清空列表
# list.clear()

l1.clear()
print(l1)

# 列表复制
# list.copy()
# 此复制操作是浅复制，只复制一层

l1 = [1, 2, ["222", "ssss", "kkk"], 4]
print(id(l1))
print(id(l1[2]))
l2 = l1.copy()
print(id(l2))
print(id(l2[2]))
# 可以看出嵌套列表的元素的地址还是相同的指向


print("*" * 50)

# tuple创建
tup1 = (10, 2, 3, "hell")
print(type(tup1))

# 访问元组
print(tup1[0])
print(tup1[1:])

# 元组是不允许修改的
# 下面的代码将两个元组进行拼接，但是得到的元组已经不是tup1了
print(id(tup1))
tup2 = "hello", "word"
tup1 += tup2
print(id(tup1))
print(tup1)
# 元组的遍历
for i in tup1:
    print(i)

# 字典
# 字典的创建
dict = {"name": "jack", "age": 15, "work": "student"}
print(dict)

# 字典的访问
print(dict["name"])
# 若访问没有的键 会报错
# print(dict["k"])

# 字典的修改
# 字典的修改可以通过key来修改
dict["name"] = "rose"
print(dict["name"])

# 字典的删除也可以用del
del dict["name"]
print(dict)

del dict
print(dict)

# 字典中的值可以多次出现，但是key值是唯一的
# 创建字典的时候如果一个key值被赋予多次值，字典默认为最后一次的值
dict = {"name": "jack", "age": 15, "work": "student", "name": "bob"}
print(dict["name"])

# 字典的函数
# len 求字典的长度
print(len(dict))
# str 将字典转化成字符串
str = str(dict)
print(str)
# 字典内置函数
# get 返回指定键的值，如果值不存在返回default的值
print(dict.get("name"))
print(dict.get("grade", 98))
# 成员判断，判断键是否在字典中
print("name" in dict)

# 遍历
# 通过items遍历键值
for k, v in dict.items():
    print(k, "----", v)
# 通过keys得到所有的key，根据key来得到所对应的值
for key in dict.keys():
    print(key, "---", dict[key])
# 通过values得到字典中所有的值
for v in dict.values():
    print(v)

# 通过setdefault方法获取一个键所对应的值，如果不存在会设置默认default的值 并添加到字典中
print(dict.setdefault("name"))

# update 将另一个字典的元素更新到字典中
dict1 = {"name": "tick", "sex": "male"}
dict.update(dict1)
print(dict)

# 字典也存在copy函数，同list一样是浅复制
# clear函数 和list一样

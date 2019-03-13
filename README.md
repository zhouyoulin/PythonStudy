# PythonStudy
## python概述
-  python编年史
    - 1989 Guido开始写python语言
    - 1990 python第一个版本诞生
    - 2001 python2.x诞生
    - 2013 python3.0诞生
- python应用领域 
    - 常规软件开发 
    - 科学计算
    - 自动化运维
    - 云计算
    - web开发
    - 网络爬虫
    - 数据分析
    - 人工智能
## python基础
### 注解
- python注释 以#号键开头的单行注释
### 变量
- 数据类型（利用type()函数查看变量的数据类型）
    - number 数字
        - int类型 整型
        - float 浮点数
    - 布尔值
        - 布尔值只有两个值True和False，分别对应二进制中的0和1
    - 字符串
        - 字符串的表示
            - 使用一个单引号表示('')，中间的内容
            - 使用一个双引号表示("")，中间的内容
            - 使用三个单引号或者三个双引号(''' ''')(""" """)之间的内容
            - 注意，一个单双引号只是单行字符串，三个引号可以多行字符串
        - 转义字符
            - 转义字符用\（反斜杠）加上后面的字母表示
            - \n 表示换行符 \\\表示一个反斜杠 \\'表示一个单引号
        - 字符串的格式化
            - 可以用%s和%d等来占位表示字符串和整数等其他
            - 可以使用string的format函数来格式化字符串（推荐使用这种方式）
    - None型
        - None表示什么都没有，空
        - None可以用于删除变量的引用
    - 列表
        - 列表的创建
        ```text
        使用中括号括起来，之间值由逗号分隔开来
        ```
        ```python
      list1 = [1,2,3,4,6,7]
      list2 = ["a", "b", "g", "l"]
        ```
        - 访问列表中的值
        ```text
        访问列表用下标来访问，如list1[0]
        ```
        ```python
      list1 = [1,2,3,4,6,7]
      list2 = ["a", "b", "g", "l"]
      print("list1[0]={0}".format(list1[0]))
      print("list2[3]={0}".format(list2[3]))
      print("list1[1:3]={0}".format(list1[1:3]))
        ```
        - 更新列表
       ```text
      更新列表即对列表中的元素进行重新赋值
      list1[2] = "hello"
        ```
        - 删除列表元素
        ```text
      删除列表的元素用del语句
      del list1[2]
      print(list1)
        ```
## 运算符
- 数字运算符
    - 基本数字运算符(+ - * / // % **)
        - 加号（+）加法运算，减号（-）减法运算
        - 乘号（*）乘法运算，除号（/）除法运算
        - 双斜杠（//）取整运算，百分号（%）取余运算
        - 两个星号（**）幂运算
        - 注意python2.x和python3.x中除法运算不同，python2.x取整，python3.x直接数学运算
- 比较运算符
    - 基本比较运算（==表示相等 != 表示不等于 >= <= > <和数学中的相同），返回的结果为布尔值
- 逻辑运算符
    - and 表示与
    - or 表示或
    - not 表示非
    - python无异或运算
- 赋值运算符
    - =号表示赋值
    - a += 7 表示 a = a + 7的缩写
    - 缩写 += -= *= /= //= **= %=
- 位运算符
- 成员运算符
    - in表示是否在变量中
    - not in 表示不在
- 身份运算符
    - is 我所理解的身份运算符表示值相等并且内存地址相同
    - is not
## 分支和循环
### 分支
- 单路分支
    - 语法格式
    ```py
    if 条件语句:
        语句块
    ```
    - 例如
    ```python
  a = 10
  if a < 20:
      print("a小于20")
    ```
- 多路分支
    - 语法格式
    ```py
    if 条件语句1:
        语句块1
    elif 条件语句2:
        语句块2
    ...
    else:
        语句块
    ```
    - 例如
    ```text
    学生成绩如果在90分以上打印a，80分以上打印b，60分以上打印c，其他打印d
    ```
    ```python
  grade = 80
  if grade>=90:
      print("a")
  elif grade>=80:
      print("b")
  elif grade>=60:
      print("c")
  else:
      print("d")
    ```
    - 注意python中没有switch语句
### 循环
- for循环
    - 语法结构
    ```text
    for 变量 in 列表:
        语句块
        ...   
    ```
    - 代码示例
    ```python
  list1 = ["a","b","v",45,14]
  for item in list1:
      print(item)
    ```
    - for else 结构 在for循环结束后执行else语句中的代码
    ```text
    for 变量 in 列表:
        语句块
        ... 
    else:
        语句块
    ```
    - range()函数
        - range函数用于生成一个左闭右开的数字列表
        - 例如打印1-10，注意右区间11
        ```python
      for i in range(1, 11):
          print(i)
        ```
- while循环
    - 语法结构
    ```text
    while 条件语句:
         代码块
    ```
    - 代码示例
    ```python
  a = 0
  while a > 20:
      print(a)
      a+=1
    ```
    - while循环同样也有while else结构
## 函数
- 函数的定义
    ```text
    函数是组织好的，可重复使用的，用来实现单一功能，或者相关功能的代码段。
    函数能提高应用的模块性，和代码的复用率。
    python中函数有内建函数和自定义函数。
    函数的语法：
    def func(value1, value2):
        代码块
    ```
- 参数传递
    ```text
    在python中，string和number，元组都是不可改变的对象，列表和字典是可以改变的对象。
    在函数参数传值的时候，不可变对象在传值过程中只是传递了变量的值，变量本身值不会发生改变。
    可变对象在传值过程中，如果修改了其值，对应的变量的值也发生了改变
    ```
    ```python
  def change_int(num):
      num = 20
      print(num)
  b = 2
  change_int(b)
  print(b)  
    ```
- 参数类型
    - 普通参数
    ```text
    语法定义
      def func(v1, v2,...):
          func
    调用（遵循顺序）
      func(v1, v2,...)
    ```
    - 关键字参数
    ```text
    语法定义
    def func(name1, name2,....):
          func
    关键字调用（不用遵循顺序）
    func(name2=v2,name1=v1,...)
    ```
    - 默认参数
    ```text
    语法
    def func(v1,v2=value):
          func
    调用（默认参数带有默认值可以不传）
    func(v1)
    func(v1,v2=value)
    ```
    - 收集参数
    ```text
    语法
    def func(*args):
          func
    收集参数以*号标识，将所有未命名的变量参数以元组的形式传入
    func(v1,v2,v3...)
    收集参数还有一种以字典方式传入的，以**来标注
    def func(**kwargs):
          func
    调用(以键值对的方式传入)
    func(arg1=v1,arg2=v2,...)
    ```
- return语句
    ```text
    return语句用于向调用者返回一个表达式，不带参数的return默认返回None
    ```
- 变量作用域
    - 遵循LEGB原则，在局部找不到就在局部外的局部去找，如果在找不到就找全局的，全局找不到就找内置的
#### 一、函数

> 如果在一个程序中，有些代码我需要重复的使用，比如隔一段代码打印五遍“you are good”

##### 1.函数的概述【方法】

**1.1 认识函数**

> **函数**：在一个完整的项目中，某些功能会反复的使用，那么会将功能会反复的使用，那么会将功能封装成函数，当我们要使用此功能的时候调用即可。
>
> **优点：**
>
> 1.简化代码结构，增加了代码的复用性(重复使用的程度)
>
> 2.增加代码的可维护性，如果想修改某个BUG，只需要对应的函数即可。

**1.2 定义函数**

> 格式：
>
> def   函数名(参数列表)：
>
> 	语句
>		
> 	return  表达式
>
> 解释：
>
> **def**  ： 函数代码块以def关键字开始
>
> **函数名**：遵循标识符规则
>
> **参数列表**：任何传入函数的参数和变量，必须放在小括号之间，使用逗号分隔，函数从函数的调用者那里获取信息【调用者给函数传递的信息】
>
> **（）**：是参数列表的开始以及结束
>
> **冒号**：函数内容【封装的功能】以冒号开始，并且缩进
>
> **语句**：函数封装的功能
>
> **return**：一般用于结束函数，并且返回信息给函数的调用者
>
> **表达式**：要返回给函数调用者的信息
>
> **注意**：最后的return表达式可以不写，若不写的情况下默认return None
>
> 参数列表 = 参数1，参数2，…,参数n

##### 1.3函数的调用

> 语法： 函数名(参数列表)
>
> 函数名：是要使用的功能的函数的函数名字
>
> 参数列表：函数的调用者给函数传递的信息
>
> 函数调用的本质：实参给形参赋值的过程

```
>>> int(1.3)
1
>>> abs(-10)
10
```



##### 1.4 最简单的函数

> 说明：最简单的函数，无参数，无返回值的函数

```python
#定义函数
def myPrint():
	print("you are a good man")
#调用函数
myPrint()
```

##### 1.5 函数的参数

> 参数列表：如果函数所实现的需求中涉及到未知项参与运算，就可以将未知项设置为参数。
>
> 格式：参数1，参数2，参数3，...
>
> 形式参数：在方法中定义的，用于接收中间参数的值
>
> 实际参数：在函数外面定义，实际参与运算的值，就是为了给形式参数赋值

```python
#函数的定义
#name是形参
def myPrint(name):
	print("%s is a good man !"%name)

#"lili" 是实参
myPrint("lili")
#结果
lili is a good man !
```

```python
#形参 参数一：name  参数二：age
def myPrint(name, age):
	print("%s is %d year old"%(name, age))
#函数调用，传递两个参数	
myPrint("lili", 18)
#结果
lili is 18 year old
```

##### 1.6函数的返回值

> 函数的返回值表示一个函数执行完成之后得到的结果
>
> 使用return返回函数的返回值，用于结束函数，得到最终运算的结果。

> 需求：编写函数实现功能，给函数传递两个整数，获取这两个整数的之和

```python
def add(num1, num2):
	sum = num1 + num2
	#将结果返回函数的调用者
	return sum
	#注意：return的作用是结束整个函数，因此return后面的语句不会被执行
	print("hello")

#调用函数
res = add(10, 20)
print(res)
```

##### 1.7 参数传递

> 参数传递的本质：实参给形参赋值的过程

**1.7.1 位置参数之值传递**

> 值传递指传递不可变类型，一般指string、tuple和number类型

```python
def func1(a):
	print(a)
	a = 10
	print(a)
temp = 20
#将temp作为实参传递给func1函数，将赋值给形参a
#相当于 a = temp
func1(temp)
print(temp)
```

打印地址，如下

```python
def func1(a):
	print(id(a))
	a = 10
	print(id(a))
	
temp = 20
#将temp作为实参传递给func1函数，将赋值给形参a
#相当于 a = temp
print(id(temp))
func1(temp)
print(temp)
```

**1.7.2 位置参数之引用传递**

> 引用传递一般传递的是可变类型，一般指list，dict和set

```python
def func1(c):
	c[0] = 100
	
d =[1, 2, 3, 4]
#将引用传递过去
func2(d)
print(d[0])
```

说明：引用传递的本质上还是值传递，只不过传递的是地址

**位置参数又称必选参数**

**1.7.3 关键字参数**

> 概念：用于函数调用时，通过“键-值”的形式加以指定，可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求

```python
def func(name, age):
	print("I am %s, and I am %d year old"%(name, age))
#一般调用
func("lili", 18)
#使用关键字参数
func(age = 18, name = "lili")
```

注意：有位置参数时，位置参数必须在关键字参数的前面，但是关键字参数之间是不存在先后顺序的。



**1.7.4 默认参数**

> 概念：用于定义函数，为参数提供默认值，调用函数时可传可不传该默认参数的值。
>
> 调用函数时，如果没有传递参数则会使用默认参数
>
> 比如：在使用sort()排序的时候，不更改其参数的时候我们一般情况下默认会升序排列

```python
def func(name, age=18)
	print("I am %s, and I am %d year old"%(name, age))

#一般的函数调用
func('lilei', 19)
#关键字参数调用
func(name = 'leilei')
#使用默认参数调用
func('lili')
```

使用默认参数可以简化函数的调用。

使用默认参数的时候需注意：

1.必选参数在前，默认参数在后，否则python解释器会报错

2.默认参数必须指向不变对象

如何设置默认参数

> 当函数有多个参数时，把变化大的参数放在前面，变化小的放在后面，变化小的可以作为默认参数。

练习：

我们写一个小学生入学注册信息，要求输入姓名，性别，年龄，城市等信息，设计一个函数。

```python
def student(name, sex, age = 6, city = '广州'):
	print("name :", name)
	print("sex :",sex)
	print("age :",age)
	print("city :",city)
#函数调用
student('lili', 'boy')
student('lili', 'boy', 7)
student('lili', 'boy', city='Beijing')
```

注意：有多个默认参数的时候，可以按顺序提供默认参数，当不按顺序提供参数的时候需要使用关键字参数进行调用。

**1.7.5 不定长参数**【可变参数】

> 概念：定义函数时，有时候我们不确定调用的时候会传递多少个参数（或者传递参数的个数为0），此时我们可以使用包裹位置参数或者包裹关键字参数来进行参数传递。
>
> 特点：能处理比当初声明时更多的参数，换句话说，就是传递多少参数，我就处理多少参数，不传递则不处理

**1.包裹位置传递--*args**

```python
#与之前形参不同的是在hoby的变量名之前添加了“*”
#添加了星号(*)的变量名会存放所有未命名的变量参数
#如果在函数调用时没有指定参数，它就是一个空的元组
#一般情况下使用*args
def func(name, *hoby):
	print("I am ",name,"I like",hoby)
	
func('lili','flower','money')
```

注意：我们传进去的所有参数都会被args变量收集，他会根据传进参数的位置合并成一个元组（tupe），args是元组类型，这就是包裹位置传递。

#####2.包裹关键字参数--**kwargs 

```python
#若是两个*，则当做dict处理
# 注意：在使用**kwargs的时候，传递参数必须使用关键字传参
def func(**kwargs):
	print(kwargs)
	print(type(kwargs))
func(x = 1, y = 2)
```

```python
#能处理任意长度的参数
def func(*args, **kwargs):
	#代表一个空语句
	pass
```

kwargs是一个字典（dict），收集所有的关键字参数。



**注意：在python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4中参数可以一起使用，或者是只用其中的某些，但是注意，参数定义与调用的顺序必须是：必选参数【位置参数】、默认参数、可变参数【包裹位置】和关键字参数【包裹关键字】**。



**1.7.6  匿名函数**

> 概念：是指一类无需定义标识符（函数名）的函数或者子程序。
>
> 特点：匿名函数不使用def定义函数，使用lambda来创建匿名函数
>
> 1.lambda只是一个表达式，函数体比def简单
>
> 2.关键字lambda表示匿名函数,冒号前面的x表示函数参数.
>
> 3.匿名函数有个限制,就是只能有一个表达式,不用写return,返回值就是该表达式的结果.

> 语法：
>
> lambda 参数1，参数2，…,参数n: expression[表达式]
>
> **好处**:函数没有名字,不必担心函数名冲突,此外,匿名函数也是一个函数对象,也可以把匿名函数赋值给一个变量,再利用变量来调用该函数.

```python
sum = lambda num1, num2: num1 + num2
print(sum(1, 2))
```



##### 拓展

在python中双冒号的使用：

我们之前学过list1[:]是对list1进行切片，但是若是出现list1[::]

这个有什么作用呢？

```python
#在python中使用list1[::]参数如下[start:end:step]
'''
start:指定开始截取的位置
end：指定截取结束的位置
step：指定步长
'''
list1 = [1,2,3,4,5]
#当step=-1的时候，情况会特殊一点，它可以进行列表的反转
list2 = list1[::-1]
```

**zip()** 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。





#### 练习

> 1.设计一个函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5
>
> ```
> def fun(obj=None):
>     # if type(obj) in [str,list,tuple]:
>     if isinstance(obj,(str, list, tuple)):
>         if len(obj)>5:
>             return True
>         else:
>             return False
>
> print(fun("1234567"))
> print(fun((1,2,3,4,5,6)))
> print(fun([1,2,3,4,5]))
> print(fun())
> print(fun("1234"))
> ```
>
> ```
> def len5(args=None):
>     if args!=None:
>         if len(args)>5:
>             return True
>         else:
>             return False
> print(len5("1234567"))
> print(len5((1,2,3,4,5,6)))
> print(len5([1,2,3,4,5]))
> print(len5())
> print(len5("1234"))
> ```

```
def len5(*args):
    if args != tuple():
        print(args[0])
        if len(args[0])>5:
            return True
        else:
            return False
print(len5("1234567"))
print(len5((1,2,3,4,5,6)))
print(len5([1,2,3,4,5]))
print(len5())
print(len5("1234"))
```



> 2.设计一个函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容【字符串中含有空格，列表与元组中函数有空串】。
>
> 若含有则返回True，否则返回False
>
> ”hello world“ [12,34,"",23]
>
> ```
> def fun2(object=None):
>     if type(object) in [list,tuple]:
>         if '' in object:
>             return True
>         else:
>             return False
>     elif type(object) ==str:
>         if " " in object:
>             return True
>         else:
>             return False
> print(fun2("hello world")) # True
> print(fun2([1,2,'',3,4]))  # True
> print(fun2((1,2,'',3,4)))  # True
> print(fun2((1,2,3,4)))     # False
> print(fun2([1,2,3,4]))     # False
> print(fun2("1234"))        # False
> print(fun2("helloworld"))  # False
> ```

```
def myinspace(args=None):
    if args != None:
        list1 = [x for x in args]
        if '' in list1:
            return True
        else:
            return False


print(myinspace("hello world")) # False
print(myinspace([1,2,'',3,4]))  # True
print(myinspace((1,2,'',3,4)))  # True
print(myinspace((1,2,3,4)))     # False
print(myinspace([1,2,3,4]))     # False
print(myinspace("1234"))        # False
print(myinspace("helloworld"))  # False
```

```
def myinspace(*args):
    if args != tuple():
        # print(args[0])
        # print(type(args[0]))
        list1 = [x for x in args[0]]
        # print(list1)
        if '' in list1:
            return True
        else:
            return False


print(myinspace("hello world")) # False
print(myinspace([1,2,'',3,4]))  # True
print(myinspace((1,2,'',3,4)))  # True
print(myinspace((1,2,3,4)))     # False
print(myinspace([1,2,3,4]))     # False
print(myinspace("1234"))        # False
print(myinspace("helloworld"))  # False
```



> 3.设计一个函数，从控制台输入一个整数，计算整数绝对值的阶乘，n！=1 x 2 x … x n【写成函数】

```
num = int(input("请输入一个整数："))
def jiecheng(n):
    ji =1
    for x in range(1, n+1):
        ji *=x
    return ji

print(jiecheng(num))
```

> 4.从控制台输入两个正数，求这两个正数的最大公约数，与最小公倍数

注意：最大公约数的公式：

m % n = r ，m = n  n = r  ，r == 0  输出m ，若不为0则继续循环

最小公倍数的公式：

最小公倍数 = 两个正数的乘积/最大公约数

```
def fun4(m,n):
    m1 = m
    n1 = n
    r = m
    while r != 0:
        r = m%n
        m = n
        n = r
    return m,m1*n1/m

print(fun4(2,7))
```

```
m = int(input("请输入第一个数m："))
n = int(input("请输入不大于m的一位数："))

def zhishu(a):
    for x in range(1,a):
        if a%x != 0:
            break
    else:
        return True
    return False

def gongyue(m1, n1):
    if zhishu(m1) and zhishu(n1):
        while m1%n1:
            m1 = n1
            n1 = m1%n1
        m1 =n1
        return m1
    else:
        return 1

def gongbei(m2,n2):
    gongbeinum = m2*n2/gongyue(m2, n2)
    return gongbeinum

print(gongyue(m,n))
print(gongbei(m,n))
```



> 5.输入一串整数，对其进行冒泡排序【函数】

```
# [4,3,2,1]
str1 = input("输入一串整数：")
list1 = [x for x in str1]
def maopao(list2):
    for i in range(0,len(list2)-1):
        for j in range(1,len(list2)-i):
            if list2[-j] > list2[-1-j]:
                list2[-j],list2[-1-j] = list2[-1-j],list2[-j]
    print(list2)

maopao(list1)


```






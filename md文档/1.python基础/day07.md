#### 一、装饰器

##### 1.1 概述

> 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
>
> 装饰器实际上就是一个闭包，把一个函数当做函数参数传入，然后返回一个替代版函数，本质上就是一个返回函数的高阶函数

#####1.2 简单的装饰器

> 函数也可以是一个对象，而且函数对象可以被赋值给变量，所以通过变量也可以调用该函数

```python
def now():
	ptint("2018-3-18")
f = now
f()
```

> 函数对象有一个____name____属性,可以拿到函数的名字:

```python
def now():
    print("2018-4-3")

f = now
f()
print(now.__name__)
print(f.__name__)
#结果
'now'
'now'
```

> 现在我们要增强now()的函数功能，比如在函数调用前打印一段分隔符。

```python
def log(func):
	def wrapper():
		print("**********")
		return func()
	return wrapper

def now():
	print("2018-3-18")
	
#装饰器的调用
f = log(now)
f()
```

##### 1.3 复杂一点的装饰器

> 需求：输入年龄，并打印出来

```python
def getAge(age):
	print("Tom age is %d"%age)
getAge(10)

#调用getAge方法得到年龄，但是如果输入的是负数就会得到不符合常理的结果
getAge(-10)

def wrapper(func):
	def inner(num):
		if num < 0:
			num = 0
		return func(num)
	return inner
newGetAge = wrapper(getAge)
newGetAge(-10)
```

> 通过这样的方式，我们的代码变得更加简洁，将边界检查的逻辑隔离到单独的方法中，然后通过装饰器包装的方式应用到我们需要进行检查的地方。

> 另外一种方式通过在计算方法的开始处和返回值之前调用边界检查的方法能够达到同样的目的，但是不可置否的是，使用装饰器能够让我们以最少的代码量达到坐标边界检查的目的。

##### 1.4 装饰器@标识符

> 使用@标识符将装饰器应用到函数
>
> python2.4及以上版本支持使用标识符@将装饰器应用在函数上，只需要的函数的定义之前上@和装饰器的名称

```python
def logger(func):
	def inner(*args,**kwargs):
		print("***********")
		return func(args, kwargs)
	return inner

@logger
def myPrint():
	print("you are very good")

myPrint()
```

> 说明：比如在公司实际开发的过程中，如果有一个别人写好的函数，你想向其中添加某些功能或者修改某些功能，而人家要求你不能随意修改人家的函数，则这时就可采用装饰器，在不修改别人的源码的同时，还可以增加自己的功能。

#### 二、偏函数

> python中的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。
>
> 简单来讲偏函数的作用就是把函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新的函数会更简单。

```python
#functools 模块
import functools
#int()函数将字符串转换为整数，默认按十进制转换
#可以设置进制
print(int("100",base = 2))
#结果为4，100是二进制中4的表示

#类似于偏函数的功能
def int2(str, base=2):
	return int(str, base)
print(int2("10"))

#functools.partical可以帮助创建偏函数，不用自己定义int2函数
#作用：把一个函数的某些参数给固定住(也就是设置默认值)，返回一个新的函数，调用这个新的函数会更简单。
int3 = functools.partial(int, base=2)
print(int3("100"))
#在创建偏函数的时候，实际上固定了关键字参数base
#结果
4
```

例2

```python
import functools
max2 = functools.partical(max, 10)
#实际上会把10作为*args的一部分自动加到左边
max2(5, 6, 7)
相当于
args =(10, 5, 6, 7)
max(args)
```

练习：

> 设计一个加法的偏函数，使用add()的时候需要导入operator模块，偏函数需要实现的功能是，求任意数与100相加的和。
>
> ```
> import operator
> import functools
> add100 = functools.partial(operator.add, 100)
> print(add100(7))
> ```

#### 三 、变量的作用域

#####3.1 概述

>在python程序中,创建,改变,查找变量名的时候,都是在一个保存变量名的空间中进行,我们称之为命名空间,也被称之为作用域.
>
>简单来说,变量的作用域就是指变量可以使用的范围
>
>程序的变量并不是在任意的位置都可以访问,访问权限取决于这个变量是在哪里赋值的.

##### 3.2 作用域的划分

> **L(local) 局部作用域**
>
> 局部变量:包含在def关键字定义的语句块中,即在函数中定义变量,每当函数被调用的时候都会创建一个新的局部作用域.
>
> 注意:如果需要在函数内部对全局变量赋值,需要在函数内部通过global语句声明该变量为全局变量

> **E(enclosing) 嵌套作用域**
>
> 又称函数作用域,在闭包函数外的函数中

>**G(global) 全局作用域**
>
>在模块层次中定义的变量,每个模块都是一个全局作用域
>
>注意:全局作用域的作用范围仅限单个模块文件内

>**B(built-in)内置作用域**
>
>系统内部固定模块定义的变量,比如预定义在builtin模块内部.

```python
#查看所有的内置变量
print(vars())
```

##### 3.3 变量名解析LEGB法则

> 搜索变量名的优先级:局部变量>嵌套作用域>全局作用域>内置作用域

**LEGB法则**:

> 当在函数中使用未确定的变量名时,python会按照优先级依次搜索4个作用域,依此来确定变量名的意义.
>
> 首先搜索局部作用域(L),之后是上一层嵌套结构中的def或者是lambda函数的嵌套作用域(E),之后是全局作用域(G),最后是内置作用域(B).
>
> 按照这个查找原则,在第一处找到的地方停止,如果是都没找到,则会发生NameError错误

```python
def func():
	var = 300
	print("var",var)
var = 100
func()
print("var", var)
#结果
300
100
```

#####3.4 关键字global

```python
#声明全局变量
global var

var = 200
def func():
    # var = 200
    print("var_", var)
    def fun():
        var = 100
        print("var", var)
    fun()
func()
```

注意:python中只有模块(module),类(class)以及函数(def,lambda)才会引入新的作用域,其他的代码块,比如if/else, try/except,for/while 等是不会引入新的作用域的,也就是说这些语句内定义的变量,在外部也可以使用.

```python
if 1:
	num = 10
print(num)
```








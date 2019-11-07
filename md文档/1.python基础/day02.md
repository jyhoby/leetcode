#### 一.python的编码规范

> 1.分号：不要在行尾加分号，也不要使用分号将两条命令放在同一行
>
> 2.行长度：一般情况下每行不要超过80个字符
>
> 3.括号：宁缺毋滥的使用括号
>
> 4.缩进：使用4个空格来缩进代码
>
> 5.空行：顶级定义之间空两行，方法定义之间空一行
>
> 6.语句：每个语句应该独占一行
>
> 7.尽量避免文件名中出现空格和中文



####二、python的基本语法

python的语法比较简单，采用缩进的方式，写出的代码大概是这样的：

```python
# print absolute value of an integer:
a = 100
if a >= 0:
    print(a)
else:
    print(-a)
```

其中#开头的语句是注释，注释是给编程人员看的，解释器会忽略掉注释。其他每一行就是一个语句，当语句以：冒号结尾是，缩进的语句为代码块。

按照约定始终使用4个空格的缩进(不管是空格或是Tab键都可以)，在文本编辑器中，设置把Tab自动转成4个空格即可

​	注意：Python程序是大小写敏感的	

####三、标识符

> 什么是标识符？说白了它就是一个字符串

标识符规则：

​	1.只能由字母、数字、下划线组成

​	2.开头不能是数字

​	3.不能是python的关键字

​	例如：def  False True and break class del 等等

​	4.区分大小写

​	5.取名字要做到见名知义

作用：

给变量、函数 , 类等命名

#### 四、python数据类型和变量

####（一）数据类型

> 为什么会有不同的数据类型
>
> 计算机是用来做数学计算的机器，因此它可以处理各种数值，但是计算机能够处理的远远不止是数值，它还可以处理文本、图形、音频、视频等各种各样的数据，不同的数据要定义不同的数据类型。

python的数据类型分为几种？

#####1.Number(数字)

>           ​		a.整数 ：python可以处理任意大小的整数，当然包括负整数，在程序的表示方法和数学上的写法是一模一样的，例如：1， 100， -10等
>
>           ​		b.浮点数：浮点数又称小数，之所以称之为浮点数，是因为按照科学计数法表示的的时候，一个浮点数的位置是可变的，比如1.23x10^5 与 12.3x10^4是相等的。[在python中浮点数的表示会有一定的误差,这个误差的原因是实数的无限精度跟计算机的有限内存之间的矛盾]
>
>           注意：整数与浮点数在计算机内存的存储方式不同，整数运输是精确的，而浮点数运算则可能会有四舍五入的误差。
>
>           ​		c.复数：复数由实数部分和虚数部分组成，可以用a+bj或者complex(a,b)的形式表示，复数的实部a和虚部b都是浮点型。		

#####2.String(字符串)

>字符串是以单引号或双引号括起来的任意文本，比如“abc”，‘xy’等等，请注意‘’或者“”本身只是一种表示方式，并不是字符串的一部分。

a.若字符串内部包含单引号又包含双引号怎么办？

```python
print('I\'m \"ok\"')
```

表示的字符串内容是：

```python
I'm "ok"
```

注意：转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也需要转义，所以\\\表示的字符就是\等等

```python
>>>print('I\'m ok.')
I'm ok.
>>>print('I\'m learning\n python.')
I'm leanring
Python.
>>> print('\\\n\\')
\
\
```

但是，如果字符串里面很多字符串需要转义，就需要添加很多\,为了简化，python还允许用r''“表示内部的字符串默认不转义。

```python
>>> print('\\\t\\')
\	\
>>>print(r'\\\t\\')
\\\t\\
```

如果字符串内部很多换行，用\n写在一行里不好阅读，为了简化，python允许用三引号'''text'''的格式表示多行内容：

```python
>>> print('''line1
	line2
	line3''')
line1
line2
line3
```

#####3.Boolean(布尔值)

>布尔值只有True、False两种值，在python中可以直接用True、False表示布尔值【注意大小写】，也可以通过布尔运算计算出来：

```python
>>> True
True
>>> 3 > 2
True
```

#####4.None(空值)

>空值是python里一个特殊的值，用None表示，None不能为0，而None是一个特殊的空值。

#####5.list(列表)

Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素

可以存放任何基本数据类型，自定义的也可以

```python
>>> list1 = ["张三", "王二", "李四"]
>>> type(list1)
<class 'list'>
```

#####6.tuple(元组)

另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改

```python
>>> tuple1 = ("张三", "王二", "李四")
>>> type(tuple1)
<class 'tuple'>
```

#####7.dict(字典)

Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

本质：无序的集合，key是不可变的，key不可重复



```python
>>> dict1 = {'lisi': 89, 'lili':90}
>>> type(dict1)
<class 'dict'>
```

#####8.set(集合)

set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。



```python
>>> set1 = {"lisi", "wanger"}
>>> type(set1)
<class 'set'>
```

#####（二）变量

> 变量的概念基本上和初中代数的方程变量是一致的，只是在计算机程序中，变量不仅可以是数字，还可以是任意数据类型。

1.概述：程序可操作的存储区的名称，在运行的期间能够改变的数据，每个变量都是特定的类型

在程序运行期间可以改变的量

作用：将不同类型的数据存储到内存中

2.变量的定义：

> 变量名=初始值   

```python
age = 18
```

在python中定义变量无需声明类型，变量类型由值来决定，因为python是一门动态数据类型的语言

注：给定初始值的原因是因为确定变量的类型

```python
age = 18
print('age =', age)
#查看变量的类型
print(type(age))
#查看变量的地址
print(id(age))
```

3.删除变量：

> del 变量名

注意：删除后的变量无法引用

```python
age = 18
#删除age变量
del age
#打印age的值
print('age =', age)
```

注意：在Python中，等号=是赋值符号，可以把任意数据类型赋值给变量，同一个变量也可以反复赋值，而且可以是不同类型的变量。像这种本身类型不固定的语言被称为**动态语言**。

当然你也可以这么理解，变量的类型取决于被赋的值的类型。

```python
a = 123 #a是整数
print(a)
print(type(a))
a = 'abc' #a变为字符串
print(a)
print(type(a))
```

#####(三)常量：

程序运行期间不能改变的数据

作用：给变量赋值的

```python
#常见的常量
123
'abc'
```

#### 五、Number(数字)

#####1.数字类型之间的转换

```python
> int(x) :将x转换为一个整数
  int(x)将字符串或者float类型【字符串必须是合法的字符串】
合法：字符串'12', '-12','+12'
不合法：'12.34','1+2'

> float(x) :将x转换为一个浮点数
    将将字符串或者int类型【字符串必须是合法的字符串】
    合法：'12','12.34','-12.3','+12.34'
    不合法：'1+2'
```

```python
#浮点数转为int
print(int(1.9))
# int转为浮点数
print(float(1))
#字符串转为int
print(int('123'))
#字符串转为float
print(float('12.3'))
#注意：如果有其他无用字符会报错，比如：
print(int('abc'))
#只有正负号才有意义
print(int('+123'))
print(int('-123'))

```

#####2.数学函数

> abs(x):返回数字的绝对值 #不属于math模块里的函数
>
> (x > y)-(x < y) :比较大小,取值为正x>y  ,取值为负x<y
>
> max(n1, n2, n3,…):返回给定指定参数的最大值
>
> min(n1, n2, n3)：返回给定指定参数最小值
>
> pow(x,y)：求x的y次方的值
>
> round(x, n):返回浮点数x的四舍五入值，如果给定n值，则代表舍入到小数点后的位数

```python
#返回数字的绝对值
num1 = -10
num2 = abs(num1)
print(num2)

#比较两个数的大小
num3 = 100
num4 = 8
print((num3 > num4)-(num3 < num4))

#返回给定参数的最大值
print(max(1, 2, 3, 45, 34, 12))

#返回给定参数的最小值
print(min(1，2，3，5，4))

#求x的y次方  2^5
print(pow(2, 5))

#round(x[,n])返回浮点数x的四舍五入的值，如果给出n值，则代表舍入到小数点后n位
#默认保留整数
print(round(2.1234))
print(round(2.13334, 3))
#python2.x中0.5遇到随机，python3中默认向偶数靠拢
print(round(2.5))   #2 偶数靠拢
print(round(3.5))   #4
```

#####3.math模块的使用

> 导入math模块
>
> math.ceil(x):返回x的向上取整数值
>
> math.floor(x):返回x的向下取整的数值
>
> math.modf(x):返回x的整数部分和小数部分，两部分的数值符号与x相同，整数部分以浮点数表示。
>
> math.sqrt(x):反回数字的x的开平方根，返回类型为实数【浮点型】

```python
import math

#向上取整
print(math.ceil(18.1))
print(math.ceil(18.8))

#向下取整
print(math.floor(18.1))
print(math.floor(18.9))

#返回整数部分与小数部分
print(math.modf(22.123))
#返回小数部分和整数部分，以元组方式返回，小数有误差

#开方
print(math.sqrt(16))
#返回浮点数类型
```

#####4.随机数函数

> 导入random模块
>
> random.choice([1,2,3,4]) ：随机返回一个元素【从指定序列中挑选一个元素】
>
> random.randrange(n):从0~n-1之间选择一个随机数[0,n)
>
> random.random() :随机产生[0,1)之间的数，结果为浮点数
>
> l1 = [1, 2, 4, 5]
>
> random.shuffle(l1) :将序列中的所有元素进行随机排列
>
> random.uniform(m, n) :随机产生一个[m, n]之间的浮点数

```python
import random

nums = range(10)
# range([start,] stop[,step])
# range()函数返回一个可迭代对象
# start:计数从start开始,默认从0开始
# stop:计数到stop结束,但不包括stop
# step: 步长,默认为1
list(nums)
# 使用list可以把可迭代对象转为一个列表,返回的类型为列表
#随机数
print(random.choice([1,3,4,5]))
print(random.choice(range(5)))
print(random.choice("hello"))

#产生一个1~100之间的随机数
r1 = random.choice(range(100))+1
print(r1)

#从指定范围内，按指定的基数递增的集合中选取一个随机数
#random.randrange([start,]stop[, step])
#start:指定范围的开始值，包含在范围内，默认是0
#stop：指定范围结束值，不包含在范围内
#step：指定的递增基数，默认是1
print(random.randrange(1, 100, 2))
# [1,100)

#从0~99选取一个随机数
print(random.randrange(100))

#随机产生[0，1）之间的数(浮点数)
print(random.random())

#随机产生一个实数，在[3，9]范围内 包含3.0 9.0
print(random.uniform(3, 9))

#随机产生一个整数，在[3，9]范围内 包含3 9
print(random.randint(3,9)) 

list = [1, 2, 3, 23, 21]

#将序列的所有元素随机排序
random.shuffle(list)
print(list)
```

#####5.三角函数

> 需要导入math模块



#### 六、算术运算符与表达式

#####算术运算符

```python
 假设变量 a = 10， b = 20
+  ：加 两个对象相加   例如 a + b = 30
-  ：减 标识负数/一个数减去另一个数  a - b = -10
*  ：乘 两个数相乘/返回一个被重复若干次的字符串 a*b=200
/  : 除 b除以a  b/a = 2
%  : 取模 返回除法的余数  b%a = 0
** ：幂，返回x的y次幂  a**b=10^20
// : 取整除返回商的整数部分  9//2=4, 9.0//2.0=4.0
```

#####算术运算表达式

```python
3+2  3-1  8**9  5%3
功能：进行相关符号的数学运算，不会改变变量的值
值：相关的数学运算的结果
```



#### 七、比较运算符

> ==  等于，比较对象是否相等，返回布尔类型的值

```python
>>> a = 10
>>> b = 20
>>> print(a == b)
False
```

> !=  不等于，比较对象是否不相等

```python
>>> a = 10
>>> b = 20
>>> print(a != b)
True
```

>  大于，x > y,返回x是否大于y

```python
>>> a = 10
>>> b = 20
>>> print(a > b)
False
```

> <    小于，x < y,返回x是否小于y

```python
>>> a = 10
>>> b = 20
>>> print(a < b)
True
```



> ‘>=’   大于等于，x >= y,返回x是否大于等于y

```python
>>> a = 10
>>> b = 20
>>> print(a >= b)
False
```



> <=   小于等于，x <= y,返回x是否小于等于y

```python
>>> a = 10
>>> b = 20
>>> print(a <= b)
True
```



#### 八、赋值运算符与赋值运算表达式

> 赋值运算符  =
> 赋值运算表达式
> 格式：变量 = 表达式
>
> 功能：计算了等号右侧的“表达式”的值，并赋值给等号左侧的变量
> 值：赋值结束之后的变量
>
> python中赋值用=来进行

```python
num1 = 10
num2 = num1 + 2
num1, num2 = num2, num1 #交叉赋值
```

**复合运算符**

```python
+=  加法赋值运算符		a += b   a = a + b
-=  减法赋值运算符		a -= b   a = a - b
*=  乘法赋值运算符		a *= b   a = a * b
/=  除法赋值运算符		a /= b   a = a / b
%=  取模赋值运算符		a %= b   a = a % b
**= 幂赋值运算符		 a **= b  a = a ** b
//= 取整除赋值运算符	a //= b  a = a // b
```

#### 九、逻辑运算符

**and运算是与运算，只有所有都为True，and运算的结果才是True**：

```python
>>> True and True
True
>>> True and False
False
>>> 5>3 and 3>1
True


```

**or运算是或运算，只要其中一个为True，or运算结果就是True**

```python
>>>True or True
True
>>>True or False
True
>>>False or False
False
```

**not 运算是非运算，它是一个单目运算符，把True变成False,False变成True**

```python
>>> not True
False
>>> not False
True
>>> not 1>2
True
```

**短路原则**

> 表达式1 and 表达式2 and 表达式3 … 如果表达式1为假，则整个表达式的值为假，后面的表达式则没有计算的必要
>
> 表达式1 or 表达式2 or 表达式3 … 如果表达式1为真，则整个表达式的值为真，后面的表达式的值就没有计算的必要
>
> 

```
print(True and 0)
print(True and None)
print(True and '')
print(True and {})
print(True and [])
print(True and ())
# 0,None,'',{},[],()都是假False
# 非空字符，列表，字典，集合都是True
```



#### 十、位运算符



```python
我们进行位运算的时候，我们需要把数字转换为二进制数来进行计算
&   按位与
|   按位或
^	按位异或
~	按位取反
<<	左移
>>	右移
```

> 1.与运算【&】
>
> 参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0

```python
3 & 2 = 2

0 1 1
0 1 0
------
0 1 0
```

> 2.按位或【|】
>
> 只要对应的两个二进位有一个为1时，结果位就为1

```python
3 | 2 = 3

0 1 1
0 1 0
-----
0 1 1
```

> 3.按位异或【^】
>
> 当两对应的二进位相异时，结果为1

```python
3 ^ 2 = 1
0 1 1
0 1 0
-----
0 0 1
```

> 4.按位取反【~】
>
> 对数据的每个二进制位取反,即把1变为0,把0变为1

```python
~3 = 4
0 1 1
-----
1 0 0
```

> 5.左移运算符【<<】
>
> 运算数的各二进位全部左移若干位，由”<<”右边的数指定移动的位数，低位补0
>
> 注意：向左移动，右边空出来的补0，左移其实就是乘以2的位数次幂

```python
3 << 2 = 12 = 3 * 2^2 

0 1 1
------
0 1 1 0 0
```

> 6.右移运算符【>>】
>
> 把”>>”左边的运算数的各二进位全部右移若干位，”>>”右边的数指定移动的位数
>
> 注意：如果最高位0，右移后，用0补空位，如果最高位1，右移后，用1补空位，右移其实就是除以2的位数次幂。

```python
3 >> 2 = 0 = 3/(2^2) 
0 1 1
-----
0 0 0 1 1

-4 >> 2 = -1
1 0 0 0  0 1 0 0
----------------
1 0 0 0  0 0 0 1 0 0
```



#### 十、成员运算符

in:如果在指定的序列中找到返回值True，否则返回False

```python
>>>a = 10
>>>list1 = [1, 2, 4, 5]
>>>list2 =[20, 10, 15]
>>>print(a in list1)
False
>>>print(a in list2)
True
>>>print('1' in '12345' )
True
```

not in:如果在指定的序列中没有找到值返回True，否则返回False

```python
>>>a = 10
>>>list = [1, 2, 4, 5]
>>>list2 =[20, 10, 15]
>>>print(a not in list)
True
>>>print(a not in list2)
False
```

#### 十一、身份运算符【先不讲】

is：is判断两个标识符是不是引用自一个对象

```python
>>> a = 1000
>>> b = a
>>> print( a is b)
True
#就是比较地址
```

is not:判断两个标识符是不是引用自不同的对象

```python
>>>a =1000
>>>b = 1000
>>>print(a is not b)
False
#pycharm 缓存数据更大 不止[-5,257)
```

> 注意：在[-5, 257)的整数取值范围内，python的内部具有缓存机制，因此在比较这个数值以内的数据可能就会有些问题。

#### 拓展

> 1.字符串和数值类型可以直接输出

```python
>>>print(1)
1
>>>print("hello world")
hello world
```

> 2.变量，无论是什么类型，数值，布尔，列表。字典都可以直接输出

```python
>>> x=12
>>>print(x)
12
>>> list1 = [1, 2, 3]
>>> print(list1)
[1, 2, 3]
```

> 3.格式化输出

```python
>>> s = 'hello'
>>> s
'hello'
>>> x = len(s)
>>> print("the length of %s is %d"%(s,x))
the length of hello is 5
```

> 注意，格式化输出的时候，
>
> 1.%字符：标记转换说明符的开始；
>
> 2.如果只有一个参数可以加括号也可以不加
>
> 3.根据类型不同使用的格式化符号也不同，
>
> %d 整数  %f浮点型  %s 字符串
>
> 4.可以控制输出长度%0.2f 保留小数点后两位
>
>   %02d,长度2，不足前面补0
>
> 5.%-nd  -表示左对齐，总长度n,左对齐不能添加占位符，占位符只能是0

#### 十二、分支语句

> 计算机之所以能够自动化执行任务，是因为它自己可以做条件判断。
>
> 思考1：现有一需求，比如，输入用户年龄，如果小于18，则打印”未成年人禁止进入“

![370AA951-25BC-4374-B07E-4D6BA76BC694](/Users/zhangjiao/Library/Containers/com.tencent.qq/Data/Library/Application Support/QQ/Users/1838887021/QQ/Temp.db/370AA951-25BC-4374-B07E-4D6BA76BC694.png)

```python
if 判断条件：
	执行语句...
```

> if语句的判断条件可以用>(大于)、<(小于)、==（等于)、>=(大于等于)、<=(小于等于)来表示关系。



> 需求2：如果年龄小于18，则打印”未成年人禁止进入“，否则打印”欢迎光临！“

```python
if 判断条件:
	执行语句...
else:
	执行语句...
```

> 分析：判断条件：年龄小于18， 如果成立，则执行”未成年人禁止进入“，若不成立，则执行”欢迎光临！“

```python
age = 17
if age < 18：
	print("未成年人禁止进入")
else:
	print("欢迎光临！")
```

拓展:

```python
#可以使用ord 和chr两个内置函数用于字符与ASCII码之间的转换
>>> ord('a')
97
>>> chr(97)
a
```



作业：

1.输入一个年份，判断是否为闰年。

条件1：不能被100整除且能被4整除

条件2：能被100整除且能被400整除

```
year = int(input("请输入年份："))
if (year%400)==0:
    print("%d 年是闰年"%(year))
elif (year%100)!=0 and (year%4)==0:
    print("%d 年是闰年"%(year))
else:
    print("%d 是平年"%(year))
# not 优先级最高 and优先级其次  or最低
```

2.输入一位三位数，判断是否为水仙花数abc

  abc = = a^3+b^3+c^3

 153是水仙花数

```
num=int(input("请输入一位三位数的整数:"))
if num<1000 and num>99:
    a = num//100
    b = (num//10)%10
    c= num%10
    if num==a**3+b**3+c**3:
        print("%d 是水仙花数"%(num))
    else:
        print("%d 不是水仙花数"%(num))
else:
    print("你输入的数值有误")
    
```

3.输入一个五位数，判断是否为回文数 abcba

12321

```
num=int(input("输入一个五位数的值："))
if num<100000 and num> 9999:
    a = num // 10000
    b = (num%10000)//1000
    c = (num%1000)//100
    d = (num%100)//10
    e = num%10
    num2=e*10000+d*1000+c*100+b*10+a
    if num==num2:
        print("%d 是回文数"%(num))
    else:
        print("%d 不是回文数"%(num))
else:
    print("您的输入有误！")
```

```
num=int(input("请输入5位数的数字："))
if num<100000 and num> 9999:
    a=str(num)
    b=a[::-1]
    if a==b:
        print("%d 是回文数"%(num))
    else:
        print("%d 不是回文数"%(num))
else:
    print("您的输入有误！")
```

4.摇色子，

提示:押大还押小  ： 大  或者 小

开始摇色子，

【1~6】取值【1， 2， 3】 小 

 取值【4， 5， 6】大

若押中，则打印“”恭喜你中了五百万“

若没押中，则打印”谢谢惠顾！“

```
import random
while(True):
    str=input("请输入您押的大小(大或小)：")
    x=random.randrange(1,6)
    if str =="大" or str=="小":
        if x>0 and x<4:
            if str =='小':
                print("你的点数为%d,恭喜你中了五百万"%(x))
                break
            else:
                print("你的点数为%d,谢谢惠顾！"%(x))
                break
        else:
            if str =='小':
                print("你的点数为%d,谢谢惠顾！"%(x))
                break
            else:
                print("你的点数为%d,恭喜你中了五百万"%(x))
                break
    else:
        print("您的输入有误")
```

```
import random

value = random.randint(1,6)
num =input("押大押小？")
print("%d "%value)
if num=="大" and value >3 or num =="小" and value<4:
    print("中奖")
else:
    print("很遗憾没中奖")
```

5.写个个人所得税计算器:

http://www.gszhuli.com/

```
wage = int(input("请输入您的工资："))
safe = int(input("请输入您扣除的五险一金："))
value = wage-safe-5000
if value > 0:
    if value <=1500:                          #3%
        value-=(value*0.03)
    elif value > 1500 and value <= 4500:      #10%
        value-=(value*0.1)
    elif value > 4500 and value <= 9000:      #20%
        value-=(value*0.2)
    elif value > 9000 and value <= 35000:     #25%
        value-=(value*0.25)
    elif value > 35000 and value <= 55000:    #30%
        value-=(value*0.3)
    elif value > 55000 and value <= 80000:    #35%
        value-=(value*0.35)
    else:                                     #45%
        value-=(value*0.45)
    wage = value+5000
    print("您的税后工资是 %d"%(wage))
else:
    print("您输入的工资或五险一金有误")
```

```
money = float(input("请输入工资："))
xian = float(input("请输入五险一金："))
zheng = float(input("请输入起征点："))

mon = money -xian -zheng

if mon<0:
    Print("输入有误")
elif mon<1500:
    sui = mon*0.03
elif mon<4500:
    sui = mon*0.01-105
elif mon <9000:
    sui = mon*0.2-555

elif mon<35000:
    sui = mon*0.25 -1005
elif mon<55000:
    sui = mon*0.3 -2755
elif mon<80000:
    sui = mon*0.35 -5505
else:
    sui = mon*0.45-13505
print("您应纳的税额为%0.2f"%(sui))
```
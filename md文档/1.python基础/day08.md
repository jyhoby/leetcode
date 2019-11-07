#### 一  回调函数

>回调函数就是一个通过函数指针调用的函数,如果你把函数的指针(地址)作为一个参数传递给另一个参数,当这个指针被用来调用其所指向的函数时,这就是我们说的回调函数.
>
>简单来说:回调函数就是把函数当成一个参数传递到函数中.

>需求:现在酒店提供免费叫醒服务,叫醒的方式有多种,你可以自己选择,比如夺命电话连环call, 或者是早起冷水迎头泼,随你自己喜欢,只要你提前预约,则酒店工作人员将在你指定的时间用你喜欢的方式叫醒你.

```python
def  wake_call(time):
	#第一种叫醒服务
	print(time,"使用夺命电话连环call叫醒主人")

def wake_water(time):
	#第二种叫醒服务
	print(time,"使用早起泼冷水的方式叫醒主人")

def call_wake(time, func_name):
	# 这个很重要,这个就是酒店服务业务的系统业务
	#这是实现回调函数的核心
	# time :预约时间
	# func_time:回调函数名
	# return :调用的函数的结果
	return func_name(time)

#调用函数
#wake_call 被调用的函数就是回调函数
call_wake("凌晨7点", wake_call)
```



> **拓展**: 编程分为两大类:系统编程和应用编程,所谓的系统编程简单来说就是编写库,而应用编程就是利用写好的各种库来编写具体的某种功能的程序,也就是应用. 系统程序员会在自己写的库中留下API(应用编程接口),以供应用程序员使用.【程序具有高内聚，低耦合】
>
> 当程序跑起来,一般情况下,应用程序会时常通过API调用库中所预备好的函数,但是有些库函数却要求应用先给它传递一个函数,好在合适的时候调用,以完成目标,这个被传入的后来又被调用的函数成为**回调函数**

####二  返回函数

函数作为返回值

> 在python中除了可以接受函数作为参数外,还可以把函数作为结果值返回.

> 需求:实现一个可变参数的求和.通常是这么定义的:

```python
def calc_sum(*args):
	sum = 0
	for i in args:
		sum += i
	return sum
```

>现在需求有变,现在我不需要立即求和,而是在后面的代码中,根据需要再进行计算,这时候,我们可以不返回求和的结果,而是返回求和的函数.

```python
def lazy_sum(*args):
	def calc_sum():
		sum = 0
		for i in args:
			sum += i
		return sum
	return calc_sum
```

当我们调用lazy_sum()时,返回的并不是求和的结果而是求和的函数

```python
>>> f = lazy_sum(1, 2, 3, 4)
>>> f
<function lazy_sum.<locals>.calc_sum at 0x101b61598>
```

这时候调用f时,才真正计算求和的结果

```python
>>> f()
10
```



>像如上的函数,我们在函数lazy_sum中又定义了函数calc_sum,并且内部函数calc_sum可以使用lazy_sum的参数和局部变量,当lazy_sum返回函数calc_sum时,相关的参数以及变量都保存在返回的函数中,这种称为"闭包"

注意:当我们调用lazy_sum()时,每次调用都会返回一个新的函数,即使传入相同的参数.



#### 三  闭包

> 若在一个函数内部定义了另一个函数,外部的我们暂且称之为外函数,内部的称之为内函数
>
> **闭包:**在一个外函数中定义了一个内函数,内函数里运用了外函数的临时变量,并且外函数的返回值是内函数的引用,这样就构成了一个闭包
>
> 一般情况下,如果一个函数结束,函数内部所有的东西都会被释放掉,还给内存,局部变量也会消失,但是闭包是一种特殊的情况,如果外函数在结束的时候发现有自己的临时变量将来还会在内部函数中用到,就把这个临时变量绑定给了内函数,然后再自己结束.

```python
#外函数, a与b都是临时变量
def outer(a):
	b = 10
	#内函数
	def inner():
		#在内函数中用到了外函数的临时变量
		print(a+b)
	#外函数的返回值是内函数的引用
	return inner
# 调用函数传入参数5
f = outer(5)
f()
#结果
15

```

> 在函数外访问函数内的东西.闭包也具有提高代码可复用性的作用。闭包有效的减少了函数所需定义的参数数目

#### 四  递归函数

> **递归函数**:在函数的内部,可以调用其他的函数,如果一个函数在内部调用自身本身,这个函数就是递归函数.
>
> **递归调用**:一个函数调用自身,成为递归函数

> 需求:计算n! = 1x2x3x4x…x(n-1)xn

> 使用递归解决问题的思路
>
> 方法:
>
> 1.写出临界条件
>
> 2.找这一次和上一次的关系
>
> 3.假设当前函数已经能用,调用自身计算上一次的结果,再求出本次的结果

```python
# 关系: n!= (n-1)!xn
def fact(n):
	#临界条件
	if n==1:
		return 1
	#返回本次的调用结果
	return n*fact(n-1)
```

>递归函数的优点是定义简单,逻辑清晰,理论上所有的递归函数都可以写成循环的方式,但是循环的逻辑不如递归清晰.

注意:使用递归函数需要注意防止栈溢出,在计算机中函数是通过栈(stack)这种数据结构实现的,每当进入一个函数调用,就会增加一层栈帧,每当函数返回,栈就会减一层栈帧,栈的大小是有限制的,所以当调用的次数过多的时候,会导致栈溢出

> 求斐波那契数列：1,1,2,3,5,8,13,21,34,55,89.....
> 需求：报一个数，直接获取这个位置上的数值

```python
#关系 第n个位置上的数值=(n-1)+(n-2)
#临界值 第一个位置和第二个位置的值为1
def func1(n):
	if n==1 or n==2:
		#临界值
		return 1
	else:
		#返回本次调用的结果
		return func1(n-1) + func1(n-2)
```

> **练习**从控制台输入输入一个数,递归求和.



#### 五 os模块

>在自动化测试中,经常需要查找操作文件,比如查找配置文件(从而读取配置文件的信息),查找测试报告等等,经常会对大量文件和路径进行操作,这就依赖os模块



**1. os.getcwd()**

> 功能:查看当前所在路径

```python
import os
print(os.getcwd())
```

**2. os.listdir()**

>列举目录下所有的文件,返回的是列表类型
>
>默认当前工作目录

```python
import os
print(os.listdir("c:\file"))
```

**3. os.path.abspath(path)**

> 功能:返回path的绝对路径

```python
import os
print(os.path.abspath("."))
```

**4. os.path.split(path)**

> 功能: 将路径分解为(文件夹,文件名),返回的是元组类型

注意:若路径字符串最后一个字符是\,则只有文件夹部分有值,若路径字符串中均无\,则只有文件名部分有值,若路径字符串有\且不在最后,则文件夹和文件名都有值,且返回的结果不包括\

```python
import os
print(os.path.split(r"D:\python\file\hello.py"))
#结果
('D:\python\file','hello.py')

print(os.path.split("."))
#结果
('','.')

os.path.split('D:\\pythontest\\ostest\\')
#结果
('D:\\pythontest\\ostest', '')

os.path.split('D:\\pythontest\\ostest')
('D:\\pythontest', 'ostest')
```

**5. os.path.join(path1,path2,...)**

> 将path进行组合,若其中有绝对路径,则之前的path将会被删除.

```python
>>> import os
>>> os.path.join(r"d:\python\test",'hello.py')
'd:\pyhton\test\hello.py'
>>> os.path.join(r"d:\pyhton\test\hello.py",r"d:\pyhton\test\hello2.py")
'd:\pyhton\test\hello2.py'

```

**6. os.path.dirname(path)**

> 返回path中文件夹部分,不包括"\\"

```python
>>> import os
>>> os.path.dirname(r"d:\pyhton\test\hello.py")
'd:\pyhton\test'
>>> os.path.dirname(".")
''
>>> os.path.dirname(r"d:\pyhton\test\")
'd:\pyhton\test'
>>> os.path.dirname(r"d:\pyhton\test")
test
```

**7. os.path.basename(path)**

> 功能:返回path中文件名

```python
>>> import os
>>> os.path.basename(r"d:\pyhton\test\hello.py")
'hello.py'
>>> os.path.basename(".")
'.'
>>> os.path.basename(r"d:\pyhton\test\")
''
>>> os.path.basename(r"d:\pyhton\test")
'test'
```

**8. os.path.getsize(path)**

> 功能: 获取文件的大小,若是文件夹则返回0python2.7
>
> 是目录的话统计不出来

```python
>>> import os
>>> os.path.getsize(r"d:\pyhton\test\hello.py")
38L
>>> os.path.getsize(r"d:\pyhton\test")
0L
```

**9. os.path.exists(path)**

判断文件是否存在

```python
>>> import os
>>> os.listdir(os.getcwd())
['hello.py','test.txt']
>>> os.path.exists(r"d:\python\test\hello.py")
True
>>> os.path.exists(r"d:\python\test\hello1.py")
False
```

**10.os.path.isdir(path)**

判断指定路径是否为目录 是返回True,否则返回False(路径不存在也是False)

**11.os.path.isfile(path)**

判断指定路径是否为文件 是返回True,否则返回False(文件不存在也是False)

#### 五 栈与队列

##### 5.1 栈 stack

>特点:先进后出[可以抽象成竹筒中的豆子,先进去的后出来] 后来者居上

```python

mystack = []
#压栈[向栈中存数据]
mystack.append(1)
print(mystack)
mystack.append(2)
print(mystack)
mystack.append(3)
print(mystack)

#出栈[从栈中取数据]
mystack.pop()
print(mystack)
mystack.pop()
print(mystack)
```

##### 5.2 队列 queue

> 特点: 先进先出[可以抽象成一个平放的水管]

```python
#导入数据结构的集合
import collections
queue = collections.deque([1, 2, 3, 4, 5])
print(queue)

#入队[存数据]
queue.append(8)
print(queue)
queue.append(9)
print(queue)

#取数据
print(queue.popleft())
print(queue)
```

#### 六  目录遍历

##### 6.1 递归遍历目录

``` python
import os

def getall(path, treeshow):
	filelist = os.listdir(path)
	treeshow += "	"
	for filename in filelist:
		#拼接绝对路径
		filepath = os.path.join(path, filename)
		if os.path.isdir(filepath):
			print(treeshow,"目录",filename)
			getall(filepath, treeshow)
		else:
			print(treeshow,"文件",filename)
getall(r"d:\python\test","")
```

##### 6.2 栈模拟递归遍历目录

> 也称为深度遍历

画图分析:

![度遍](./深度遍历.png)

```python
import os

def getAllDirDE(path):
	stack = []
	stack.append(path)
	#处理栈,当栈为空的时候结束循环
	while len(stack) != 0:
		#从栈里取出数据
		dirPath = stack.pop()
		#目录下所有文件
		fileList = os.listdir(dirPath)
		for fileName in fileList:
			fileAbsPath = os.path.join(dirPath,fileName)
			if os.path.isdir(fileAbsPath):
				#是目录就压栈
				print("目录:", fileName)
				stack.append(fileAbsPath)
			else:
				#打印普通文件
				print("普通文件:", fileName)
getAllDirED(r"/Users/zhangjiao/PycharmProjects/teaching")
```

##### 6.3 队列模拟递归遍历目录

> 也被称为广度遍历

画图分析:

![度遍](./广度遍历.png)

```python
import os
import collections
def getAllDirQU(path):
	queue = collections.deque()
	#进队
	queue.append(path)
	while len(queue) != 0:
		#出队数据
		dirPath = queue.popleft()
		#找出所有的文件
		fileList = os.listdir(dirPath)
		for fileName in fileList:
			#绝对路径
			fileAbsPath = os.path.join(dirPath, fileName)
			#判断是否是目录,是目录就进队,不是就打印
			if os.path.isdir(fileAbsPath):
				print("目录:", fileName)
				queue.append(fileAbsPath)
			else:
				print("普通文件:", fileName)
getAllDirQU(r"/Users/zhangjiao/PycharmProjects/teaching")
```

作业：

1.【递归】有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？

2.一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

3.猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少


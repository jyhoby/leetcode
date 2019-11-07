#### python2与python3的区别

##### 性能：

> 1.python3.x起始比python2.x效率低，但是python3.x有很大的优化空间，效率正在追赶
>
> 2.python3.x原码文件默认使用utf-8，使得命名更加广泛。

python3.x

```python
>>> 中国 = 'china'
>>> print(中国)
'china'
>>> str = "我爱北京天安门"
>>> str
'我爱北京天安门'
```

python2.x

```python
>>> str = "我爱北京天安门"
>>> str
'\xe6\x88\x91\xe7\x88\xb1\xe5\x8c\x97\xe4\xba\xac\xe5\xa4\xa9\xe5\xae\x89\xe9\x97\xa8'
```

所以使用python2.x的时候需要在文件的头部添加

```python
#-*-coding:utf-8-*-
str = "我爱北京天安门"
print(str)
```

> 3.print函数
>
> print语句没有了，取而代之的是print()函数

python2.x中这两种打印是等价的

```python
print "fish"
print ("fish")#注意print后面有个空格
```

python3.x中打印

```python
print("fish")
```

> 4.除法运算
>
> python中的除法比较其他语言显得非常的高端，有套复杂的规则，python中的除法
>
> 有//和/
>
> 首先来说/除法：与其他语言类似，在python2.x中它只计算整数部分，小数部分忽略掉
>
> 浮点数除法会得到浮点数的结果

python2.x中的“/”

```python
>>> 1/2
0
>>> 1.0/2.0
0.5
```

python3.x中的“/”

```python
>>> 1/2
0.5
```

> 5.异常
>
> 在python3.x中处理异常也轻微的改变了，在python3中我们使用as作为关键字

```python
#3.x
try:
    ...
except exc as var:
    ....
    
 #2.x
try:
    ...
except exc, var:
    ...

```



#### 高阶函数

##### 1.MapReduce

> MapReduce主要应用于分布式中。
>
> 大数据实际上是在15年下半年开始火起来的。
>
> 分布式思想：将一个连续的字符串转为列表，元素类型为字符串类型，将其都变成数字类型，使用分布式思想【类似于一件事一个人干起来慢，但是如果人多呢？效率则可以相应的提高】，同理，一台电脑处理数据比较慢，但是如果有100台电脑同时处理，则效率则会快很多，最终将每台电脑上处理的数据进行整合。
>
> python的优点：内置了map()和reduce()函数，可以直接使用。

```python
#python内置了map()和reduce()函数
'''
def myMap(func,li):
	resList = []
	for paser in li:
		res = func(paser)
		resList.append(res)
'''       
```

##### map()函数

> 功能：将传入的函数依次作用在序列中的每一个元素，并把结果作为新的Iterator返回
>
> 语法：
>
> map(func, lsd)
>
> 参数1是函数，参数2是序列

```python
#一、map()
#原型 map(func, lsd)
#将单个字符转成对应的字面量整数
def chrToint(chr):
    return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[chr]

list1 = ["2","1","4","5"]
res = map(chrToint, list1)
#[chr2int("2"),chr2int("1"),chr2int("4"),chr2int("5")]
print(res)
print(list(res))

#将整数元素的序列，转为字符串型
#[1，2，3，4] --》[“1”，“2”，“3”，“4”]
l = map(str,[1,2,3,4])
print(list(l))
```

> 练习：使用map函数，求n的序列[1,4,9,..,n^2]

##### reduce()函数

> 功能：一个函数作用在序列上，这个函数必须接受两个参数，reduce把结果继续和序列的下一个元素累计运算
>
> 语法：reduce(func，lsd)
>
> 参数1为函数，参数2为列表
>
> reduce(f，[1，2，3，4])等价于f(f(f(1，2)，3)，4)，类似于递归

```python
import functools
#需求，求一个序列的和
list2 = [1, 2, 3, 4]
def mySum(x,y)
	return x+y
r = functools.reduce(mySum,list2)
print("r=",r)
```

> 练习，将字符串转成对应字面量数字

```python
#将字符串转成对应字面量数字
def strToint(str1)
	def fc(x, y):
        return x*10 + y
    def fs(chr):
   		return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[chr]
    return reduce(fc,map(fs,list(str1)))
a = strToint("12345")
print(a)
print(type(a))

#模拟map()函数
def myMap(func,li):
    resList = []
    for n in li:
        res = func(n)
        resList.append(res)
```

##### filter()函数

> 作用：把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留该元素还是丢弃该元素【通过一定的条件过滤列表中的元素】

```python
'''
语法：
filter(func,lsd)
参数一：函数名
参数二：序列
功能：用于过滤序列
简单理解：把传入的函数依次作用于序列红的每一个元素，根据返回的True还是False，决定是否保留该元素。
'''
#需求：将列表中的偶数筛选出来。
list1 = [1,2,3,4,5,6,7,8]
#筛选条件
def func(num):
    #保留偶数元素
    if num%2 == 0:
        return True
    #剔除奇数元素
    return False
l = filter(func,list1)
print(l)
print(list1)
```

> 注意：使用filter()这个高阶函数，关键在正确实现一个“筛选”函数，filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter完成计算结果，需要使用list()函数获取所有的结果并且返回list.

> 练习
>
> 需求；将爱好为“无”的数据剔除掉
>
> data= [["姓名","年龄","爱好"],["tom", 25, "无"],["hanmeimei", 26, "金钱"]]

##### sorted() 函数

> 作用：实现对列表的排序。
>
> iterable：是可迭代类型;
> cmp：用于比较的函数，比较什么由key决定;
> key：用列表元素的某个属性或函数进行作为关键字，有默认值，迭代集合中的一项;
> reverse：排序规则. reverse = True  降序 或者 reverse = False 升序，有默认值。
> 返回值：是一个经过排序的可迭代类型，与iterable一样。

```python
#排序
#第一类：冒泡 选择
#第二类：快速，插入，计数器
#注意：如果数据量小的情况下，上述两类用法的效率基本相同，但是，如果数据量大的情况下，第一类的效率很低

#1.普通排序
list1 = [4,3,5,6,1]
#默认为升序排序
list2 = sorted(list1)
print(list2)

#2.按绝对值大小排序
list3 = [4，-3，5，2，-9]
#key接受函数来实现自定义排序规则
#abs表示通过绝对值进行排序
list4 = sorted(list3, key=abs)
#利用map可以实现取绝对值之后的排序
list5 = sorted(map(abs,list3))
print(list3)
print(list4)
print(list5)

#3.降序排序
list5 = [2,1,4,5,6,7]
#通过设置reverse=True来表示反转
list6 = sorted(list5,reverse=True)
print(list5)
print(list6)

list7 = ['a','b','c','d']
list8 = sorted(list7)
print(list7)
#同样也可以实现升序排列，结果为abcd，排序依据为ASCII值
print(list8)

#自定义函数：按照字符串的长短来进行排序
def myLen(str1)：
	return len(str1)
list7 = ['sddd','dded','et54y5','6576986oy']
#使用自定义函数，进行排序，key=函数名
list8 = sorted(list7, key = myLen)
print(list7)
print(list8)
```

##### zip()函数

zip() 函数用于将可迭代对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象。

如果各个可迭代对象的元素个数不一致，则返回的对象长度与最短的可迭代对象相同。

利用 * 号操作符，与zip相反，进行解压。

zip() 函数语法：

```python
`zip``(iterable1,iterable2, ...)`
```

参数说明：

- iterable -- 一个或多个可迭代对象（字符串、列表、元祖、字典）

返回值：

- Python2中直接返回一个由元组组成的列表，Python3中返回的是一个对象，如果想要得到列表，可以用 list() 函数进行转换。

```python
>>> a = [1,2,3] #此处可迭代对象为列表
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)
>>> zipped
<zip object at 0x02B01B48> #返回的是一个对象
>>> list(zipped)
[(1, 4), (2, 5), (3, 6)] #使用list()函数转换为列表
>>> list(zip(a,c))
[(1, 4), (2, 5), (3, 6)]
>>> zipped = zip(a,b)
>>> list(zip(*zipped)) #解压也使用list进行转换
[(1, 2, 3), (4, 5, 6)]
```



#### 单元和文档测试

测试分类：

App测试、接口测试

测试用例 [自动化测试]

黑盒测试【要求最低】，白盒测试，灰盒测试

##### 单元测试

> 单元测试就是用来对一个模块、一个函数或者一个类来进行正确性的检测工作。
>
> 1.若是单元测试通过，则证明测试的函数能够正确的工作，
>
> 2.反之则证明要么函数有bug要么输入不合法，总之我们需要修复我们的函数功能。

##### 对函数进行单元测试

> 创建python文件MathFunc.py，内容如下:

```python
def mySum(x,y):
    return x + y

def mySub(x,y)
	return x -y
print(mySum(1,2))
```

> 创建python文件的text01.py，内容如下：

```python
import unittest
from MathFunc import mySum, mySub

#测试类 继承自unittest.TestCase
class Test(unittest.TestCase):
    #下面两个方法存在的意义：假设需要连接数据库，当测试完毕之后，需要断开和数据库的连接
    def setUp(self):
        print("开始测试时自动调用")
    
    def tearDown(self):
        print("结束时自动调用")
    
    #测试相应的函数
    #一般情况下，测试函数命名格式：test_需要被测试的函数名
    def test_mySum(self):
        #断言：对函数命名格式：text_需要被测试的函数名
        self.assertEqual(mySum(1,2),3,"加法有误")
    
    def test_mySub(self):
        self.asserEqual(mySub(2,1),1,"减法有误")
        
#当主程序运行的时候，开始进行单元测试
if __name__ == "__main__":
    unittest.main()
```

> 运行text01.py文件，发现正常，然后修改MathFunc.py文件中的内容，可按照下面的方式修改。

```python
def mySum(x,y):
    return x + y + 1

def mySub(x, y):
    return x - y

print(mySub(1,2))
```

> 再次运行text01.py文件，会出现错误信息。



##### 对类进行单元测试

> 先创建一个类文件person.py,内容如下：

```python
class Person(object):
    #构造方法
    def __init__(self, name, age):
        #给成员变量赋值
        self.name = name
        self.age = age
    
    def getAge(self):
        return self.age  
```

> 创建text02.py文件，进行类的单元测试，内容如下：

```python
import unittest
from person import person
class Test(unittest.TestCase):
    def  test_init(self):
        p = Person('hanmeimei',20)
        self.asserEqual(p.name,"hanmeimei","属性值有误")
    
    def test_getAge(self):
        p = Person('hanmeimei',22)
        self.assertEqual(p.getAge(),p.age,"getAge函数有误")

if __name__ = "__main__":
    unittest.mian()
```

> 演示，运行text02.py文件，程序正常运行，修改person.py文件中的内容，具体内容如下：

```python
class Person(object):
    #构造方法
    def __init__(self, name, age):
        #给成员变量赋值
        self.name = name
        self.age = age
    
    def getAge(self):
        return self.age+1  
```

> 再次运行会报错
>
> 对类的单元测试：本质上还是对方法的单元测试。

##### 文档测试

> 文档测试的作用：可以提取注释找那个的代码执行
>
> doctest模块可以提取注释中的代码执行
>
> doctest严格按照python的交互模式的输入进行提取

```python
import doctest
def mySum(x,y):
    #第函数进行功能和使用说明
    '''
    求两个数的和
    get The sum from x and y
    :param x:firstNum
    :param y:secondNum
    :return sum
    #注意有空格
    example:
    >>>print(mySum(1,2))
    3
    '''
    return x + y
print(mySum(1，2))
#进行文档测试，在当前文件中进行即可
doctest.testmod()
```

> 注意：演示的时候，主要测试
>
> example:
>
> print(mySum(1,2))
>
> 3
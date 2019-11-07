#### 一  模块

##### 1.1. 模块的概述

> 在计算机程序的开发过程中,随着程序代码越写越多,在一个文件里的代码就会越来越长,越来越不容易维护.
>
> 为了编写可维护的代码,我们把很多函数分组,分别放到不同的文件里,这样每个文件包含的代码就相对较少,很多编程语言都采用这种组织代码的方式,在python中,一个.py文件就称之为一个模块(Module).

##### 1.2. 模块优点

> 1. 大大的提高了代码的可维护性
> 2. 提高了代码的复用性,每当一个模块书写完毕,可以被多个地方引用
> 3. 引用其他模块(包括内置模块和第三方模块与自定义模块)
> 4. 可以避免函数名和变量名冲突

注意:取模块名的时候尽可能不要与内置函数的变量名冲突,查看[python所有内置函数] https://docs.python.org/2/library/functions.html

##### 1.3 模块的引入

> 语法:
>
> import 模块名

##### 1.4  sys模块

>sys 主要是针对于黑屏终端的库

**1.4.1  sys.argv**

>sys.argv 获取当前正在执行的命令行参数的参数列表

```python
import sys
#实现从程序外部向程序传递参数
print(sys.argv)
#当前程序名
sys.argv[0]
#第一个参数
sys.argv[1]
```

**1.4.2  sys.platform**

> 获取当前执行环境的平台

```python
#mac
>>> import sys
>>> sys.platform
'darwin'
```

**1.4.3  sys.path**

> path是一个目录列表,供python从中查找第三方扩展模块,在python启动时,sys.path根据内建规则,PATHPATH变量进行初始化

```python
>>> import sys
>>> sys.path
['', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages']
```



#### 二 自定模块

#####2.1 自定义模块的创建

> 一个.py文件就是一个模块
>
> 创建一个say.py文件

```python
#!/user/bin/env python
#encoding=utf-8
height = 180
weight = 60
def sayHello():
    print("hello, nice to meet you!")
def sayGood():
    print("you are a good  man!")
 def  sayBey():
    print("see you litter")
 
#函数的调用
sayHello()
sayGood()
```

##### 2.2 自定模块的引用之整体引入

> 引入自定义模块
>
> 语法:
>
> import   module1[, module2[,  module3[,…., modulen]]]

```python
#引入内置模块
import time, sys
#引入自定义模块,不用添加.py后缀
import say
#注意:一个模块只会被引入一次,不管你执行了多少次import

#使用模块中的内容
#格式: 模块名.函数名/变量名
say.sayHello()
```

注意: 在这里我们引入了整个say文件,因此say文件中的所有的方法与属性我们都可以访问

##### 2.3 自定义模块的引用之局部引用

> 语法:
>
> from … import 函数名/变量名
>
> 作用:从模块中导入一个指定的部分到当前命名空间
>
> 格式: from  module import name1[, name2[, name3[,...namen]]]
>
> 注意:至少要导入一个

```python
from say import sayGood,sayHello
sayGood()
sayHello()
```

弊端:

```python
from say import sayGood,sayHello
def sayGood():
    print("************")
#注意:程序内容的同名函数可以将模块中的函数覆盖
sayGood()
```

##### 2.3 自定义模块的引用之*

> 语法:
>
> from module  import *
>
> 作用:把一个模块中所有的内容全部导入当前命名空间

```python
from say import *
#直接使用此函数
sayGood()
```

注意:弊端与部分导入的方式相同,不推荐使用这种方式导入.

**注意:使用内置模块的时候,也可以使用上面三种引用的方法**



#### 三  __name__属性

> 模块是一个可执行的.py文件,一个模块被另一个程序引入,若在引用的时候不想让模块中的有些方法执行.这时候我们就需要使用__name__属性去处理.

创建一个say2.py文件

```python
#!/user/bin/env python
#encoding=utf-8

#作为模块执行
height = 180
weight = 60
def sayHello():
    print("hello, nice to meet you!")
def sayGood():
    print("you are a good  man!")
 def  sayBey():
    print("see you litter")
 
#正常执行
#每一个模块都有一个__name__属性,当其值等于"__main__"时,表明该模块自身在执行,否则被引入了其他文件
#若当前文件为程序的入口文件,则__name__属性的值为__main__
if __name__ == "__main__":
	sayHello()
	sayGood()
    print(__name__)
 else:
   
    print(__name__)
   
```

以后的代码可以这么写:

```python
def  main():
    pass

#其他函数

if __name__ == "__main__":
    main()
```

```python
总结:
    1.__name__这个系统变量显示了当前模块执行过程中的名称,如果当前程序运行在当前模块中,则__name__的名称就是__main__,如果不是,则为这个模块的名称.
    2.__name__一般作为函数的入口,尤其在大型工程中,常常有if __name__ == "__mian__":来表明整个工程开始运行的入口.  
```

模块搜索路径:

当导入一个模块时,解释器现在当前包中查找模块,若找不到,然后在内置的built-in模块中查找,找不到则按sys.path给定的路径找对应的模块文件(模块名.py)

#### 四、包

> 思考:上述已经知道模块的用法以及好处,但是如果不同的人编写的模块名相同怎么办?
>
> 解决:为了避免模块名冲突,python又引入按目录来组织模块的方法,称为包.
>
> 特点:引入包以后,只要顶层的包不与其他人发生冲突,那么模块都不会与别人的发生冲突
>
> 注意:目录只有包含一个叫做"_init__.py"的文件,才被认做是一个包,主要为了避免一些滥竽充数的名字,基本上目前这个文件什么也不用写.

通俗一点:包是一个包含____init____.py文件的目录,该目录下一定得有这个____init____.py文件和其它模块或者子包.

注意:每个包目录下都会有一个____init____.py文件,这个文件必须存在,否则python就把这个目录当成普通目录,而不是一个包,____init____.py可以是空文件,也可以有python代码,因为____init____.py本身就是一个模块.

自己创建模块时注意命名,不能和python自带的模块名称冲突,例如系统自带了sys模块,自己的模块就不可命名为sys.py,否则将无法导入系统自带的sys模块.



#### 五 安装第三方模块

> 在python中,安装第三方模块,是通过setuptools这个工具完成的,python有两个封装了setuptools的包管理工具:easy_install 和pip,目前官方推荐pip

注意:

1.若使用的mac或linux,安装pip本身这个步骤就可以跳过了.

2.若正在使用windows,请参考[安装python](https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001374738150500472fd5785c194ebea336061163a8a974000)的内容,确保安装时勾选了pip和add python.exe to path.

在命令提示符窗口下尝试运行pip,如果windows提示未找到命令,可以重新运行安装程序添加pip

```python
#安装包
pip install packagename
#卸载包
pip uninstall packagename
#显示自己安装的包
pip freeze
#显示所有包
pip list
#查看版本
pip -V
#查看包详细信息
pip show packagename
```



> 我们来安装第一个第三方库—Pillow,这是python下非常强大的处理图像的工具库,一般来说,第三方库都会在python官方的pypi.python.org[https://pypi.python.org/pypi] 网站注册,**要安装第三方库必须先知道该库的名称,比如安装Python Imaging Library的名称叫Pillow**,因此安装Pillow的命令就是:

```python
pip install Pillow
'''
若windows如果报错,则输入pip install --upgrade pip
#更新一下pip的版本
#若仍然报错,则换个网络
在pip下载东西,若是出错,则使用命令升级pip,若还是有错,大部分是网络的问题.
window下一般只会使用python3.6的环境
Linux 或者mac下使用一般默认是python2.7环境,若是想使用python3.6,则使用命令python3
'''
```

有了PIL,处理图片易如反掌,随便找个图片生成缩略图

```python
# 引入了第三方库
from PIL import Image
#打开图片,路径需要注意
im = Image.open("test.png")
#查看图片的信息
print(im.format, im.size, im.mode)
# 设置图片的大小,注意:图片的大小给定的是个元组
im.thumbnail((200, 100))
#保存成新的图片
im.save("thum.jpg","JPEG")
```

#### 六 常用的内置模块

#####  关于时间和日期模块

> python程序能用很多方式处理日期和时间,转换日期格式是一种常见的功能.
>
> python提供了一个time和calendar模块可以用于格式化日期和时间.
>
> 时间间隔是以秒为单位的浮点小数
>
> 每个时间戳都以自从1970年1月1日午夜(历元)经过了多长时间来表示.
>
> python的time模块下有很多函数可以转换常见的日期格式

##### 6.2 Time模块

**6.2.1 名词解释**

>UTC :格林威治天文时间,世界标准时间,在中国为UTC+8

> DST:夏令时是一种节约能源而人为规定的时间制度,在夏季调快一小时.

**6.2.2 时间的表示形式**

>1.时间戳
>
>以整数或浮点型表示的是一个秒为单位的时间间隔,这个时间的基础值1970.1.1的零点开始算起
>
>2.元组格式
>
>采用python的数据结构表示,这个元组有9个整型内容,分别表示不同含义
>
>year  month   day  hours  minutes  seconds  weekday  Julia day   flag[1 夏令时  -1 根据当前时间判断   0 正常表示]
>
>3.格式化字符串
>
>%Y 完整年份

**获取当前时间**

```python
#引入第三方库
>>> import time

#返回当前时间的时间戳,浮点数形式,不需要参数
>>> time1 = time.time()
>>> time1
1522159406.3535008

# 时间戳转换为UTC时间
>>> gm = time.gmtime(time1)
>>> gm
time.struct_time(tm_year=2018, tm_mon=3, tm_mday=27, tm_hour=14, tm_min=3, tm_sec=26, tm_wday=1, tm_yday=86, tm_isdst=0)

# 时间戳转为本地时间[把时间戳转为元组]
>>> lt = time.localtime(time1)
>>> lt
time.struct_time(tm_year=2018, tm_mon=3, tm_mday=27, tm_hour=22, tm_min=3, tm_sec=26, tm_wday=1, tm_yday=86, tm_isdst=0)

# 本地时间元组转为时间戳
>>> mt = time.mktime(lt)
>>> mt
1522159406.0

# 时间元组格式转为字符串
>>> st = time.asctime(lt)
>>> st
'Tue Mar 27 22:03:26 2018'

# 将时间戳转换为字符串
>>> ct = time.ctime(time1)
>>> ct
'Tue Mar 27 22:03:26 2018'

# 将本地时间元组转为指定的格式的字符串
>>> strf = time.strftime("%Y-%m-%d %H:%M:%S", lt)
>>> strf
'2018-03-27 22:03:26'

# 将指定时间格式的字符串,转为时间元组
>>> strp = time.strptime('2018-03-27 22:03:26','%Y-%m-%d %X')
>>> strp
time.struct_time(tm_year=2018, tm_mon=3, tm_mday=27, tm_hour=22, tm_min=3, tm_sec=26, tm_wday=1, tm_yday=86, tm_isdst=-1)

	# 休眠 单位s
>>> time.sleep(2)
# 以浮点数计算的秒数返回当前cpu的时间,用来衡量不同的程序的耗时,常用
>>> time.clock()
>>> time.sleep(1)
>>> print("&&&&&")
>>> print("&&&&&")
>>> time.clock()
```

```
格式	含义	备注
%a	本地（locale）简化星期名称	
%A	本地完整星期名称	
%b	本地简化月份名称	
%B	本地完整月份名称	
%c	本地相应的日期和时间表示	
%d	一个月中的第几天（01 - 31）	
%H	一天中的第几个小时（24小时制，00 - 23）	
%I	第几个小时（12小时制，01 - 12）	
%j	一年中的第几天（001 - 366）	
%m	月份（01 - 12）	
%M	分钟数（00 - 59）	
%p	本地am或者pm的相应符	一
%S	秒（01 - 61）	二
%U	一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周。	三
%w	一个星期中的第几天（0 - 6，0是星期天）	三
%W	和%U基本相同，不同的是%W以星期一为一个星期的开始。	
%x	本地相应日期	
%X	本地相应时间	
%y	去掉世纪的年份（00 - 99）	
%Y	完整的年份	
%Z	时区的名字（如果不存在为空字符）	
%%	‘%'字符
```



##### 6.3 datetime模块

**6.3.1 概述**

> datetime比time高级了不少,可以理解为datetime基于time进行了封装,提供了更多的实用的函数,datetime的接口更加的直观,更容易调用

**6.3.2 模块中的类**

> datetime:同时有时间与日期
>
> timedelta:表示时间间隔,即两个时间点的间隔:主要用于计算时间的跨度
>
> tzinfo: 时区相关的信息
>
> date : 只关注日期

##### 6.3.3函数的使用

```python
#导入datetime模块
>>> import datetime
#获取系统当前时间

>>> datetime.datetime.now()
datetime.datetime(2018, 3, 28, 21, 59, 7, 95015)

#  获取指定时间
>>> time2 = datetime.datetime(2018, 3, 28, 21, 59, 7, 95015)
>>> print(time2)
2018-03-28 22:47:11.006712
        
 # 将时间转为字符串       
>>> time3 = time1.strftime("%Y-%m-%d")
>>> time3
'2018-03-28'  
#时间相减,返回一个时间间隔的对象
>>> time4 = datetime.datetime.now()
>>> time4
datetime.datetime(2018, 3, 28, 22, 53, 24, 709216)
>>> time5 = time4 -time1
>>> print(time5)
0:06:13.702504
>>> type(time5)
<class 'datetime.timedelta'>
#间隔天数
>>> print(time5.days)
0
# 间隔天数之外的时间转为秒
>>> print(time5.seconds)
373
 
```

##### Calendar 模块

> calendar模块有很广泛的方法用来处理年历和月历

**函数的使用**

```python
>>> import calendar
#返回指定的某月
>>>>>> calendar.month(2018, 4)
'     April 2018\nMo Tu We Th Fr Sa Su\n                   1\n 2  3  4  5  6  7  8\n 9 10 11 12 13 14 15\n16 17 18 19 20 21 22\n23 24 25 26 27 28 29\n30\n'
# 返回指定某年的日历
>>> calendar.calendar(2018)
#返回当前每周起始日期的设置
>>> calendar.firstweekday()
0
# 判断某一年是否为闰年,如果是返回True,否则返回False
>>> calendar.isleap(2018)
False
# 返回在y1,y2之间闰年的总数
>>> calendar.leapdays(2018, 2080)
15
# 返回某年某月的weekday的第一天和这个月所有的天数   
>>> calendar.monthrange(2018,4)
(6, 30)

#返回某个月以每一周为元素的序列
>>> calendar.monthcalendar(2018, 4)
[[0, 0, 0, 0, 0, 0, 1], [2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22], [23, 24, 25, 26, 27, 28, 29], [30, 0, 0, 0, 0, 0, 0]]

# 返回给定日期的日期码
# 0(周一)到 6(周日)
>>> calendar.weekday(2018,4,2)
6

```

> 1.设计出一个模块，这个模块包含求和（1+...+n），偶数和，奇数和,
>
> 以及任意的倍数之和的功能。

> 2.获取当前时间，并且返回当前时间的下一秒

> 3.分别使用递归与循环计算出n!，并且比较两个程序的运算速度。








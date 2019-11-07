#### 一、list列表

#####1.概述：

> 通过前两天的学习，我们知道变量可以存储数据，但是一个变量只能存储一个数据，现在有一个班级，班级有20个人，现在求班级的平均年龄。

若按照之前的方式来解决

```python
age1 = 10
age2 = 12
...
age20 = 12
average = (age1 + age2 +...+age20)/20
```

> 在这里，很显然这种方法显得很麻烦，而python提供了一种解决方案，就是使用列表
>
> 本质：list列表的本质是一种有序的集合

##### 2.创建列表

> 语法： 列表名 = [元素1，元素2，元素3...说明：列表中的选项被称为元素，跟string类似，下标也是从0开始计数

使用：创建列表

```python
#创建空列表
list1 = []
#创建带有元素的列表
list2 = [10, 20, 30, 10]
print(list2)
```

在列表中元素的数据类型可以不同（灵活性）

```python
list3 = [33, "good", True, 10.32]
print(list3)
```

#####3.列表元素的访问

3.1 列表的取值

> 功能：访问list列表中元素值
>
> 语法：列表名[索引]

```python
list4 = [22, 33, 12, 32, 45]
#下标从0开始，最大值为len(list4)-1
print(list4[0])
```

注意：当索引值大于len(list4)-1的时候，会出现以下错误：

```python
print(list4[5])
IndexError: list index out of range
```

这个错误就是下标越界【下标超出了可表示的范围】

3.2 列表元素的替换

> 功能：更改列表元素的值
>
> 语法：列表名[下标] = 值

```python
list4 = [22, 33, 12, 32, 45]
list4[0] = "hello"
print(list4[0])
```

#####4.列表操作

4.1 列表组合

> 语法： 列表3 = 列表1 + 列表2

```python
list1 = [1, 2, 3]
list2 = ['hello', 'yes', 'no']
list3 = list1 + list2
print(list3)
```

4.2 列表重复

> 语法： 列表2 = 列表1 * n

```python
list1 = [1, 2, 3]
list2 = list1 * n
print(list2)
```

4.3 判断元素是否在列表中

> 语法：元素 in 列表
>
> 若存在则返回True，否则返回False

```python
list1 = [1, 2, 3]
print(1 in list1)
```

4.4 列表截取

> 语法：列表[start: end] 表示获取从开始下标到结束下标的所有元素[start, end)

```python
list1 = [1, 2, 3, 'hello', 'yes', 'no']
print(list1[2:4])
#若不指定start，则默认从0开始截取，截取到指定位置
#若不指定end，则从指定位置开始截取，截取到末尾结束
```

4.5 二维列表

> 语法：列表 =[列表1，列表2，列表3，… ,列表n]

```python
#创建二维列表，即列表中的元素还是列表
list1 = [[1, 2, 3],[2, 3, 4],[5, 4, 9]]
```

4.5 二维列表取值

> 语法：列表名【下标1][下标2]
>
> 注意：下标1代表第n个列表（下标从0开始），下标2代表第n个列表中的第n个元素

```python
list1 = [[1, 2, 3],[2, 3, 4],[5, 4, 9]]
print(list1[0][0])
```



#####5.列表的方法

5.1 list.append(元素/列表)

> 功能：在列表中末尾添加新的元素【在原本的列表中追加元素】
>
> 注意：append()中的值可以是列表也可以是普通元素

```python
>>> list1 = [3, 4, 6]
>>> list1.append(6)
>>> print(list1)
[3, 4, 6, 6]
```

5.2 list.extend(列表)

>功能：在列表的末尾一次性追加另外一个列表中的多个值
>
>注意：extend()中的值只能是列表/元组[一个可迭代对象]，不能是元素
>
>```
>list1.extend(iterable)
>将可迭代对象的元素，打碎追加在末尾
>```

```
list.append(object)
将object作为整体追加在末尾
```

```python
>>> list1 = [1,2,3]
>>> list2 = [3, 4,5]
>>> list1.extend(list2)
>>> print(list1)
[1, 2, 3, 3, 4, 5]
```

```
#  去重，将列表中重复值去除
list4 =[]
list3 = [1, 2, 3, 3, 4, 4, 5, 5, 5]
for x in list3:
    if x not in list4:
        list4.append(x)
print(list4)
```

5.3 list.insert(下标值, 元素/列表)

> 功能：在下标处插入元素，不覆盖原本的数据，原数据向后顺延
>
> 注意：插入的数据可以是元素也可以为列表

```python
>>> list1 = [1,2,3]
>>> list1.insert(1,0)
>>> print(list1)
[1, 0, 2, 3]
>>> list1.insert(1,[2, 4, 8])
>>> print(list1)
[1, [2, 4, 8], 0, 2, 3]
```

5.4 list.pop(下标值)

> 功能：移除列表中指定下标处的元素(默认移除最后一个元素)，并返回移除的数据

```python
>>> list1 = [1, [2, 4, 8], 0, 2, 3]
>>> list1.pop()
3
>>> print(list1)
[1, [2, 4, 8], 0, 2]
>>> list1.pop(2)
0
>>> print(list1)
[1, [2, 4, 8], 2]
```

5.5 list.remove(元素)

不指定元素会报错

> 功能：移除列表中的某个元素第一个匹配结果

```python
>>> list1 = [1, 2, 3]
>>> list1.remove(2)
>>> print(list1)
[1, 3]
```

5.6 list.clear()

> 功能：清除列表中所有的数据

```python
>>> list1 = [1, 2, 3]
>>> list1.clear()
>>> print(list1)
[]
```

del list1

直接将整个列表删除，对象将不能被引用



5.7  list.index(object[, start】[, stop])

> 功能：从指定的范围的列表中找出某个值第一匹配的索引值 
>
> 若不指定范围，则默认是整个列表。

```python
>>> list1 = [1, 2, 3]
>>> list1.index(2)
1
>>> list1.index(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 4 is not in list
```

注意：若在列表中找不到这个元素，则会报错。

5.8 list.count(元素)

​	list.count(object)

> 功能：查看元素在列表中出现的次数

```python
>>> list1 = [1, 2, 3, 1]
>>> list1.count(1)
2
```

5.9 len(list)

> 功能： 获取元素列表个数

```python
>>> list1 = [1, 2, 3, 1]
>>> len(list1)
4
```

5.10 max(list)

> 语法：获取列表中的最大值
>
> 在python字符串进行比较时，比较ASCII码值，再比较第二个
>
> 0的ASCII码 48
>
> A 65
>
> a 97

```python
>>> list1 = [1, 2, 3, 1]
>>> max(list1)
3
```

5.11 min(list) 

> 语法：获取列表中的最小值

```python
>>> list1 = [1, 2, 3, 1]
>>> min(list1)
1
```

5.12 list.reverse()

> 语法： 列表倒叙

```python
>>> list1 = [1, 2, 3, 1]
>>> list1.reverse()
>>> print(list1)
[1, 3, 2, 1]
```

5.13 list.sort()  

对list原列表操作，返回None值

> 语法：列表排序 默认升序
>
> list.sort(reverse=True)降序

```python
>>> list1 = [1, 2, 3, 1]
>>> list1.sort()
>>> print(list1)
[1, 1, 2, 3]
```

5.14 赋值拷贝

> 语法：list1 = [1, 2, 3]
>
> 引用拷贝/赋值拷贝
>
> 	    list2 = list1

```python
>>> list1 = [1, 2, 3, 1]
>>> list2 = list1
>>> print(list2)
[1, 2, 3, 1]
>>> print(id(list1))
4314476424
>>> print(id(list2))
4314476424
```

注意：赋值拷贝为引用拷贝，类似于快捷方式

5.15 浅拷贝

元素分为两种类型：

1 不可变对象: number,bool,tuple,str

2.可变对象：list ,dict,set

> 语法：list1 = [1, 2, 3]
>
> 	    list2 = list1.copy()

```python
>>> list1 = [1, 2, 3, 1]
>>> list2 = list1.copy()
>>> print(list2)
[1, 2, 3, 1]
>>> print(id(list2))
4314525320
>>> print(id(list1))
4314524808
```

注意：浅拷贝为一维内存拷贝，开辟了新的内存空间



```
import copy

list1 = [1, 2, 3, 4, ["hello"]]
list2 = copy.deepcopy(list1)
list1[4][0] = "wrold"
print(list1)
print(list2)
print(id(list1))
print(id(list2)) #完全开辟新的内存空间，包括列表的地址
```

5.16 list(元组)

> 功能：将元组转为列表

```python
>>> list1 = list((1, 2, 3, 4))
>>> print(list1)
[1, 2, 3, 4]
```

#####6.列表的遍历

6.1 使用for循环遍历列表

> 语法：
>
> for  变量名  in  列表 ：
>
> 	语句
>
> 功能：for循环主要用于遍历列表
>
> 遍历：指的是依次访问列表中的每一个元素，获取每个下标对应的元素值

说明：按照顺序获取列表中的每个元素，赋值给变量名，再执行语句，如此循环往复，直到取完列表中所有的元素为止

```python
>>> list1 = ['hello', 78, '你好', 'good']
>>> for item in list1:
...     print(item)
... 
hello
78
你好
good
```

6.2 使用while循环遍历列表[使用下标循环]

> 语法：
>
> 下标 = 0
>
> while  下标 <  列表的长度：
>
> 	语句
>		
> 	下标 += 1

```python
>>> list1 = ['hello', 78, '你好', 'good']
>>> index = 0
>>> while index < len(list1):
...     print(list1[index])
...     index += 1
... 
hello
78
你好
good
```

6.3 同时遍历下标与元素

> 语法：
>
> for   下标，变量    in   enumerate(列表)
>
> 	语句

```python
>>> list1 = ['hello', 78, '你好', 'good']
>>> for index,item in enumerate(list1):
...     print(index, item)
... 
0 hello
1 78
2 你好
3 good
```

```python
enumerate()[枚举]函数用于一个可遍历的数据对象(如列表,元组或者字符串)组合为一个索引序列,同时列出数据与数据下标,一般使用在for循环中
enumerate(obj, [start =0])
obj:一个可迭代对象
start:下标起始位置
```



> 练习:
>
> 1.对一个列表进行冒泡排序【升序】

```
list1 = [12, 3, 56, 45, 76, 34, 13]
for i in range(1, len(list1)):
    for j in range(len(list1)-i):
        if list1[j] > list1[j+1]:
            list1[j] ,list1[j+1] = list1[j+1], list1[j]
print(list1)
```

```
list1 = [12, 3, 56, 45, 76, 34, 13]
len1 = len(list1)
index1, index2 = 0, 0
while index2 < len1:
    while index1 < len1-index2-1:
        if list1[index1] > list1[index1+1]:
            list1[index1], list1[index1+1] = list1[index1+1], list1[index1]
        index1 += 1
    index2 += 1
    index1 = 0
print(list1)

```

> 2.从控制输入一串字符串，要求字符串只能数字字母下划线，并且长度大于等于20，若不符合条件重新输入，输入完毕之后，要求从控制台输入一个字符，使用自己输入的字符，来对字符串进行切片，切片完毕之后，并且去掉空串，删除列表中的重复元素。

```
while True:
    str1 = input("请输入一串字符，长度大于20个字符：")
    if len(str1) >=20:
        for x in str1:
            if x == "_" or x >='0' and x<='9' or x>='a' and x<='z' or x>='A' and x<='Z':
                pass
            else:
                print("输入有误，请重新输入！")
                break #跳出for循环
        else:
            print("输入合法")
            break   #跳出死循环
    else :
        print("输入有误，请重新输入！")

str2 = input("请字符串中包含的一个字符作为分隔符：")
list3 = str1.split(str2)
list2 = []
for x in list3:
    if x not in list2 and x !='':
        list2.append(x)
print(list2)

```

> 3.从控制台输入一串字符串，实现字符串翻转比如:hello => olleh

```
str1 = input("请输入您要翻转的字符串:")
print(str1[::-1])
```



#### 二、turtle模块绘图

#####1.turtle的使用

> turtle是一个简单的绘图工具，他提供了一个小海龟，你也可以把它理解成一个小机器人
>
> 只听得懂有限的指令。
>
> 使用时候需要导入turtle库： import  turtle
>
> 绘图窗口的原点（0，0）在正中间
>
> 默认情况下，海龟向正右方移动

#####2.操作命令

```python
import  turtle

#程序继续执行，也就是代码执行完毕但不关闭窗口
turtle.done()
```

2.1 运动命令

> turtle.forward(d) ：向前移动dpx个长度
>
> turtle.backward(d):向后移动d个长度
>
> turtle.right(d) : 向右转动多少度
>
> turtle.left(d) :向左转动多少度
>
> turtle.goto(x, y) :移动到坐标为(x,y)的位置
>
> turtle.speed(speed) :画笔绘制的速度[0, 10]

2.2 笔画控制命令

> turtle.up() :笔画抬起，在移动的时候不会绘图【只移动画笔】
>
> turtle.down() ：画笔落下，移动绘图
>
> turtle.setheading(d):改变画笔的朝向，多少度
>
> turtle.pensize(d):改变画笔的粗细
>
> turtle.pencolor(color):改变画笔的颜色
>
> turtle.reset():恢复所有设置，清空窗口，重置turtle状态
>
> turtle.clear()：清空窗口

2.3  绘制图形

> turtle.circle(r, steps = n) :默认绘制一个圆形，r为半径，n等于几就是几边行
>
> turtle.begin_fill():开始填充
>
> turtle.fillcolor(color) :填充颜色
>
> turtle.end_fill() :结束填充

2.4 其他命令

> turtle.done() :程序继续执行
>
> turtle.undo() :撤销上一次动作
>
> turtle.hideturtle() :隐藏小海龟
>
> turtle.showturtle():显示小海龟
>
> turtle.screensize(x, y) 设置窗口大小

#### 三、tuple元组

#####1.概述

> 本质上是一种有序的集合，和列表非常的相似，列表使用[]表示，元组使用()表示
>
> 特点：一旦初始化，就不能发生改变

#####2.元组的创建

> 格式：
>
> 元组名 = (元素1， 元素2 ，元素3，...)

```python
#创建空的元组
tuple1 = ()
print(tuple1)
#创建带有元素的元组
tuple2 =(22, 33, 14, 109)
print(tuple2)

#与列表类似，元组中的元素类型可以不同
tuple3 = (23，True，"good")
print(tuple3)

#定义只有一个元素的元组
tuple4 = (1)  #这定义的不是元组而是整数1
tuple4 = (1,) #定义一个元素的元组定义时必须加一个逗号",",用来消除歧义
```

#####3.元组元素的访问

3.1 访问元组中的元素：

> 格式： 元组名[下标]

```python
tuple1 = (20， 40， 201， 401)
print(tuple1[0])
#注意使用下标取值的时候，要注意下标的取值范围，不要下标越界
#获取最后一个元素
print(tuple1[-1])
```

3.2 修改元组

> 在元组定义的时候大家都知道元组一旦初始化就不能改变，但是现在如果我想改变元组怎么办呢？
>
> 元组是不能修改的，但是列表可以，元组中的元素的数据类型可以是不同类型的，因此我们可以通过在元组中添加一个列表，而列表是可以修改的，进而来”修改“我们的元组

```python
tuple1 = ('hello', 'you',[20, 30])
#修改元组
tuple1[0] = 'hi' 
#报错，元组不能修改
tuple1[2][1] = 'good'
```

注意：从表面上看我们的元组确实是改变了，但其实改变的不是我们的元组，而是list的元素，所谓的tuple不变是说，tuple的每个元素的指向永远不变，一旦它指向了这个list，就不能改指向其他的对象，但是指向的list本身是可变的！

3.3 删除元组

> 元组是不可变的，但是我们可以使用del语句删除整个元组

```python
tuple1 = ('hello', 'hi')
del tuple1
print(tuple1)
#此时会报错
```

#####4.元组操作

4.1 元组连接组合

> 语法：
>
> 元组1    元组2
>
> 元组3 = 元组1 + 元组2

```python
tuple1 = (1,  2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2)
#结果
(1, 2, 3, 4, 5, 6)
```

注意：元素连接组合并没有改变原来的元组，而是生成了一个新的元组。

4.2 元组重复

> 语法：
>
> 元组2 = 元组1 * n

```python
tuple1 = (1,  2, 3)
tuple2 = tuple1 * 3
print(tuple2)
#结果
(1, 2, 3, 1, 2, 3, 1, 2, 3)
```

4.3 判断元素是否在元组中

> 语法：
>
> 元素  in  元组
>
> 若存在则返回True，否则返回False

```python
tuple1 = (1,  2, 3)
print( 1 in tuple1)
#结果
True
```

```python
tuple1 = (1,  2, 3)
print( 5 in tuple1)
#结果
False
```

4.4 元组的截取

> 语法：
>
> 元组名[start:end]  
>
> 截取的元组范围[start,end)
>
> 功能：获取开始下标到结束下标之前的所有元素。
>
> 若不指定start则默认是从开头开始截取到指定位置
>
> 若不指定end则默认从指定位置截取到结尾

```python
tuple1 = (1,  2, 3, 8, 'hello', 'good')
tuple2 = tuple1[2:5]
print(tuple2)
#结果
(3, 8, 'hello')
```

```python
tuple1 = (1,  2, 3, 8, 'hello', 'good')
tuple2 = tuple1[:5]
print(tuple2)
#结果
(1, 2, 3, 8, 'hello')
```

```python
tuple1 = (1,  2, 3, 8, 'hello', 'good')
tuple2 = tuple1[3:]
print(tuple2)
#结果
(8, 'hello', 'good')
```

##### 5.元组的方法

5.1  len(tuple)

> 功能：获取元组元素的个数

```python
tuple1 = (1,  2, 3, 8, 'hello', 'good')
print(len(tuple1))
#结果
6
```

5.2 max(tuple)

> 功能：获取元组中元素的最大值

```python
tuple1 = (1,  2, 3, 8, 20, 13)
print(max(tuple1))
#结果
20
```

5.3 min(tuple)

> 功能：获取元组中元素的最小值

```python
tuple1 = (1,  2, 3, 8, 20, 13)
print(min(tuple1))
#结果
1
```

5.4 tuple(list)

> 功能：将列表转换为元组

```python
list1 = [1,  2, 3, 8, 20, 13]
print(tuple(list1))
#结果
(1, 2, 3, 8, 20, 13)
```

**6.二维元组**

> 与二维列表类似，一个元组中的元素依然是元组，则成为二维元组。
>
> 元组名 =（元组1，元组2，...）

```python
tuple1 = ((1, 2, 3),(4, 5, 6),(7, 8, 9))
```

> 二维元组取值
>
> 元组名[下标1]【下标2】

```python
tuple1 = ((1, 2, 3),(4, 5, 6),(7, 8, 9))
#获取第一个元组的第一个元素
print(tuple1[0][0])
#结果
1
```

**练习**

> 1.使用for循环打印图形

```python
'''
  *
 ***
*****
 ***
  *
'''

while True:
    num = int(input("请输入您要打印的*个数，要求为奇数："))
    if num%2 != 0:
        break
str1 = '*'*num
list1 = []
i, j = 1, 1
for x in str1:
    list1.append(x*i)
    if j > num/2:
        i -= 2
    else:
        i += 2
    j +=1
for x in list1:
    print(x.center(num))


```

> 2.写一个双色球彩票系统，系统可以随机产生一组数据，一组彩票数据有六位数，这六位数的的取值范围是0和1。
>
> 一张彩票是两块钱，可以充值金额，用户可以选择继购买张数余额充足开始游戏，用户输入号码，开奖，号码一致的话，打印恭喜中大奖，奖金是购买票数金额的10倍，若没猜中则打印”继续加油！“。，买票和退出的时候要求打印剩余金额。
>
> 

```python
import  time
import  random

print("********游戏开始**********")
time.sleep(1)
print("***********系统开始产生中奖数据*************")

lucyNum = []
for i in range(6):
   num = random.choice([0, 1])
   lucyNum.append(num)
   i += 1
money = int(input("一张彩票五元，请充值您的金额："))

print("您现在的余额为%d元"%money)

print("温馨提示：中奖数据有六位数，每位数为0或者1")
while True:
   if money < 5:
      print("很抱歉，您的余额已不足！")
      break
   money -= 5
   time.sleep(1)
   numC = input("请输入您猜测的中奖数据")
   if numC == str(lucyNum):
      print("恭喜您中大奖了！")
   else:
      print("很抱歉，没有中奖")
   con = input("请问还要继续么？继续请输入yes, 结束请输入no")
   if con == "no":
      break
```

```
import random

print("已进入彩票系统")
while True:
    try:
        money = int(input("请输入您的充值金额："))
    except ValueError:
        print("输入金额有误！")
        continue
    while True:
        if money >= 2 :
            print("您的余额:%d元，一张彩票2元" % (money))
            while True:
                try:
                    num = int(input("请输入您购买的彩票张数："))
                except ValueError:
                    print("输入有误！请输入整数！")
                    continue
                break
            while True:
                try:
                    value1 = input("请输入您的6位数号码1和0组合:")
                    value2 = int(value1)
                    for x in value1:
                        if x != "0" and x != "1" :
                            print("输入有误，请输入您的6位数号码1和0组合:")
                            break # 跳出for循环
                    else:
                        print("输入合法")
                        break   # 跳出while循环
                except ValueError:
                    print("输入有误，请输入您的6位数号码1和0组合:")
                    continue
            if money >= 2 * num:
                print("正在生成系统号码")
                list1 = []
                for x in range(1, 7):
                    list1.append(str(random.choice([0, 1])))
                print("中奖号码已经生成")
                list2 = list(value1)
                while True:
                    kai = input("请输入“开奖”开始:")
                    if kai =="开奖":
                        break
                    else:
                        print("您输入有误")
                        continue
                print("您的号码为：", list2)
                print("中奖号码为：", list1)
                money -= 2 * num
                if list1 == list2:
                    print("恭喜中奖!!奖金%d"%(10*num))
                    money += 10*num
                else:
                    print("没中奖，继续加油！")
                jixu = input("是否继续购买？N/n退出，任意键继续 ")
                if jixu =="n" or jixu =="N":
                    print("您的余额有%d元"%(money))
                    break
        else:
            print("您的余额不足,仅%d元，请充值！"%(money))
            while True:
                try:
                    money += int(input("请输入您的充值金额："))
                    break
                except ValueError:
                    print("输入金额有误！")
                    continue
    break
print("欢迎下次光临！！")
```


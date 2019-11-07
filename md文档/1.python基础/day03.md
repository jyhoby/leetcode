####一、Python的分支（条件）语句2

>计算机之所以能够自动化执行任务，是因为它自己可以做条件判断。
>
>思考1：现有一需求，比如，输入用户年龄，根据年龄打印不同的内容。





![370AA951-25BC-4374-B07E-4D6BA76BC694](/Users/zhangjiao/Library/Containers/com.tencent.qq/Data/Library/Application Support/QQ/Users/1838887021/QQ/Temp.db/370AA951-25BC-4374-B07E-4D6BA76BC694.png)



```python
if 判断条件：
	执行语句...
else:
	执行语句...
```

if语句的判断条件可以用>(大于)、<(小于)、==（等于)、>=(大于等于)、<=(小于等于)来表示关系。

> 需求1：如果年龄大于18，则打印已成年，否则未成年

```python
age = 17
if age> 18：
	print("已成年")
else:
	print("未成年")
```



> 需求3：如果年龄小于等于18，打印少年，年龄大于18且小于等于25，则打印青年，大于25小于等于40，打印壮年，大于40，打印您更年期到了。。。

类似于上面我们需要多重判断的时候，我们则可以使用以下的方式来解决

```python
if 条件判断1：
	语句1
elif 条件判断2：
	语句2
...
elif 条件判断n:
	语句n
else：
   	语句
```

注意：elif是else if的缩写，可以有多个elif。

所以，根据上面的需求，我们的代码则可以这样写

```python
age = 34
if age <= 18:
	print("少年")
elif age <= 25:
	print("青年")
elif age <= 40:
	print("壮年")
else：
	print("更年期到啦")
```

> if语句有个特点，它是从上往下判断，如果在某个判断上是True，把该判断的语句对应执行后，就忽略掉其他的elif和else。

if判断语句还可以简写：

```python
if x：
   print("True")
```

> 只要x是非零数值，非空字符串，非空list，就判断为True，否则为False

#####嵌套的if语句

> 需求：现输入一个数，判断他是否为大于10的偶数

如果要解决上述的需求，可能我们需要两个判断语句，第一个判断输入的数是否大于10，第二个判断是在第一个的基础上来判定这个数是否为偶数。

> 简单的说，就是在if语句中再嵌套一个if语句，效果如下：
>
> 语法：
>
> ​	if 表达式1：
>
> ​		语句1
>
> ​		if 表达式2：
>
> ​			语句2

```python
num = 20
if num > 10:
	if num % 2 == 0:
		print(num)
```

注意：从语法的角度上说，嵌套的层数没有限制，但是，从代码的可读性和可维护性来说，最好的嵌套的层数不要超过三层。

#####if 的神奇用法(三目运算)

> result1  if 判断条件  else  result2
>
> 若条件成立则输出结果result1,否则输出结果result2

```python
>>> x = 10
>>> y = 20
>>> x if x > y else y
20
```



#### 二、循环语句之while

python 不支持 do while

> 思考1：求1+2+3+....+10的值
>
> 解决问题的方法一：使用之前学过的加法运算

```python
>>> num = 1 + 2 + ...+10
>>> print(num)
```

> 思考2：求 1+2 +3+…+100的值

```python
>>> num = 1 + 2 + 3 + ... + 100
>>> print(num)
```

> 这种方法非常的繁琐，为了让计算机计算成千上万次重复的计算，我们就需要循环语句。在python中while语句用于循环执行程序，即在某条件下，循环执行某段程序，以处理需要重复处理的相同任务，其基本形式为：





```python
while 判断条件：
	执行语句...
```

> 执行语句可以是单个语句或语句块，判断条件可以是任何表达式，任何非零，或非空（null）的值均为true，当判断条件为false时，结束循环。
>
> 

![CF7B3BB0-6FFC-4886-AE1D-55AEA44378EE](/Users/zhangjiao/Library/Containers/com.tencent.qq/Data/Library/Application Support/QQ/Users/1838887021/QQ/Temp.db/CF7B3BB0-6FFC-4886-AE1D-55AEA44378EE.png)



> 2.解决方法二：我们使用循环的方式来解决上面的问题

```python
sum = 0
num = 1
while num < 101:
	sum += num
	num += 1
print(sum)
```

在上面的循环中，num < 101判断语句，当这个结果为True的时候，它就继续执行循环体中的代码块，否则就跳出循环语句。

#####while 之死循环

> 死循环出现的契机：当表达式永远为真的时候，会出现死循环

```python
while 1:
	print("I am very good !")
```

#####while 循环之else

> 在python中,while...else在循环条件为false时执行else语句块
>
> **只有在整个循环正常结束时，才执行else语句**
>
>  

```python
count = 0
while count < 5:
    print("%d is less than 5"%count)
    count += 1
else:
    print("%d  is not less than 5"%count)
```

##### while之简单的语句组

> 如果你的while循环体中只有一条语句,你可以将该语句与while写在同一行
>
> 语法:
>
> while 条件: 语句

```python
while True: print("you are a good man")
```



#### 三、结束循环语句

#####1.break语句的使用

> 在循环中，使用break语句可以提前退出循环。

例如：本来循环打印1~100的数字，但是，现在我要提前结束，当数字大于10的时候，打印循环结束。

```python
n = 1
while n <= 100:
	if n > 10:
    #当n = 11时，条件满足，执行break语句
		break
	print(n)
	n += 1
print("循环结束")
```



#####2.continue语句的使用

在循环的过程中，可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。

```python
n =  0
while n < 10:
	n += 1
	print(n)
```

通过上面的程序可以打印出1~10，但是，如果我们只想打印奇数，可以使用continue语句跳过某些循环：

> 思考三：打印1~100以内的奇数

```python
num = 1
while num <= 100:
	if num%2 == 0:
		continue
	print(n)
```

##### 3. pass语句的使用

> pass 语句是空语句,是为了保持程序结构的完整性
>
> pass 不做任何事情,一般用做占位语句

```python
if True:
    pass
else:
    print("hello")
```







#### 四、循环语句之for

>python 的循环有两种，一种是我们之前讲的while循环，另外一种就是for...in循环，依次把list或者tuple中的元素或者字符串迭代出来。

 可迭代对象：str ,list, tuple, dict, set 

```python
name = ['lili','Bob','Tracy']
for name in names:
	print(name)
```

执行这段代码，会依次打印names的每一个元素

```python
lili
Bob
Tracy
```

>所以 for x in … 循环就是把每个元素带入变量x，然后执行缩进块语句。

>计算1~10的整数之和，可以用一个sum变量做累加：

```python
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
	sum = sum + x
print(sum)
```

> 如果要计算1~100的整数之和，从1到100有点困难，在python中提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list，比如range(5)生成的序列是从0开始小于5的整数。
>
> range([start,]stop[,step])    [start,stop）
>
> list()函数，将生成器对象（迭代器）转成列表
>
> list(range(10))  [1,2,...,9]
>
> range(100,0,-1) [100,99,...,1 ]

```python
sum = 0
for x in range(100):
	sum += x
print(sum)
```

#### for 循环使用else语句

> 与while...else类似,else也会在循环正常执行完的情况下执行

```python
for i in range(10):
	print(i)
else:
	print("********")
```



#####range函数

> range函数可创建一个可迭代对象，一般用在for循环中

函数语法：

```python
range([start,] stop[, step])
```

参数说明：

```python
1.start：计数从start开始，默认从0开始，例如：range(5)等价于range(0, 5)
2.stop:计数到stop结束，但不包括stop。例如：range(0，5)的取值为[0，5）
3.step：步长，默认为1，例如range(0，5) 等价于range(0, 5, 1)
```

>函数返回一个可迭代对象，从这个可迭代对象中可以获取一个整数列表

```python 
#使用list函数,可以从可迭代对象中获取整数列表
>>> list(range(5))
[0, 1, 2, 3, 4]
```



#### 嵌套循环

> 我们可以循环体中嵌套循环

> 需求:打印九九乘法表

```python
'''                          行    列
1x1=1                        1     1
1x2=2	2x2=4                2     2
1x3=3	2x3=6	3x3=9        3     3
...

总结：列数随着行数的变化而变化，列数的最大值和行数相等。
'''
i = 1
while i <= 9:
    j = 1
    while j <= i:
        sum = j*i
        print("%dx%d=%d"%(j,i,sum),end="    ")
        j += 1
    print("")
    i += 1
'''
打印结果：
1x1=1    
1x2=2    2x2=4    
1x3=3    2x3=6    3x3=9    
1x4=4    2x4=8    3x4=12    4x4=16    
1x5=5    2x5=10    3x5=15    4x5=20    5x5=25    
1x6=6    2x6=12    3x6=18    4x6=24    5x6=30    6x6=36    
1x7=7    2x7=14    3x7=21    4x7=28    5x7=35    6x7=42    7x7=49    
1x8=8    2x8=16    3x8=24    4x8=32    5x8=40    6x8=48    7x8=56    8x8=64    
1x9=9    2x9=18    3x9=27    4x9=36    5x9=45    6x9=54    7x9=63    8x9=72    9x9=81    
'''
```

拓展：

> 默认情况下使用print("")会自动打印换行符，如果需要更改换行符则需要在print()中添加end属性即print("",end=" "),这样就把换行更改成空格



#### 五、String字符串

#####1.什么是字符串

> 字符串是以单引号或者双引号括起来的任意文本，一个字符串由若干个任意字符组成

#####2.创建字符串

```python
str1 = "hello world"
str2 = 'you are good'
```

#####3.字符串运算

######3.1字符串链接

 3.1.1 使用加号进行链接

```python
#字符串的链接，通过“+”进行链接
s1 = 'welcome'
s2 = 'to guangzhou'
print(s1 + s2)
```

注意：字符串 + 数字，这样会报错，不同类型的不能相加

3.1.2 使用“，”进行链接【tuple类型】

```python
s1 = 'hello'
s2 = 'world'
print(s1, s2)
#使用“，”链接的时候，在“，”的位置会产生一个空格
```

3.1.3 使用%格式化链接

```python
s1 = 'hello'
s2 = 'world'
print("%s %s"%(s1, s2))
```

3.1.4 使用join函数进行链接

```python
s1 = ['hello', 'world']
print("".join(s1))
# 将""作为连接符连接s1的两个元素
```

注意："".join()函数内部只需要传递一个参数。

######3.2 重复输出字符串

```python
#重复输出字符串，通过乘法的方式实现
s3 = 'good'
print(s3 * 3)
```

######3.3 获取字符串中的字符

```python
#通过索引的方式实现
#索引：给一个字符串中的字符从0开始编号，也成为下标
#索引的取值范围：[0，str.length-1]
#访问方式： 变量名称[索引]
str3 = 'good'
print(str3[0])
#索引值还可以从-1开始，-1代表倒数第一个字符
print(str3[-1])
```

######3.3 截取字符串

```python
# 通过下标截取字符串
str1 = "hello world"
print(str1[3:6])
#注意：截取字符串的范围是str[start : end] 它是一个前闭后开的区间[start，end)
#如果n的值超过了字符串的最大长度，则仍然截取原下标的长度

#从开头截取到指定索引之前[0，5）
print(str1[:5])

#从指定截取到结尾[4,str1.length)
print(str1[4:])

#注意在使用str[start : end]来截取字符串的时候，若start不写默认从第一个字符开始
#若end不写，则默认到最后一个字符结束
```

######3.5 判断是否包含指定字符

```python
#判断字符串中是否包含某指定字符串
str4 = "you are a good boy"
print("good" in str4)
#若包含有则返回True否则为False
```

######3.6 格式化输出

```python
#通过%来改变后面的字母或者是符号的含义，%被称为占位符
# %s：打印字符串
print ("His name is %s"%("Aviad"))
# %d：打印整数
print ("He is %d years old"%(25))
# %f：打印浮点数，可指定小数点后的精度
print ("His height is %f m"%(1.83))
# %.2打印浮点数（指定保留小数点位数）
print ("His height is %.2f m"%(1.83))
#指定占位符宽度
print ("Name:%10s Age:%8d Height:%8.2f"%("Aviad",25,1.83))
#指定占位符宽度（左对齐）
print ("Name:%-10s Age:%-8d Height:%-8.2f"%("Aviad",25,1.83))
#指定占位符（只能用0当占位符）
print ("Name:%-10s Age:%08d Height:%08.2f"%("Aviad",25,1.83))


age = 18
name = "丽丽"
weight = 45.5
print("my name is %s , I am %d year old and my weight is %.2f kg"%(name, age, weight))
#注意：%.nf表示精确到小数点后n位，会四舍五入
```





#####4.关于字符串常用函数

######4.1 eval(str)

> 功能：将字符串str当成有效的表达式来求值并返回计算结果。
>
> 可以把list,tuple,dict, set和string相互转化

```python
>>>num1 = eval('123')
>>>print(num1)
123

>>>num2 = eval("[1, 2, 3]")
>>>print(num2)
[1, 2, 3]

>>> num3 = eval("12-3")
>>> print(num3)
9
```

######4.2 len(str)

> 功能：返回当前字符串的长度（字符的个数）

```python
>>> len("you are good")
12
```

######4.3 str.lower()

> 功能：返回一个把字符串中的大写字母转换为小写字母 的字符串

```python
>>> str = "Hello World"
>>> print(str.lower())
hello world
```

注意：此方法不改变原本的字符

######4.4 str.upper()

> 功能：返回一个把字符串中的小写字母转换为大写字母的字符串

```python
>>> str = "Hello World"
>>> print(str.upper())
HELLO WORLD
```

######4.5 str.swapcase()

> 功能：返回一个把字符串中的大写字母转为小写字母，小写字母转换为大写字母的字符串

```python
>>> str = "Hello World"
>>> print(str.swapcase())
hELLO wORLD
```

######4.6 str.capitalize()

> 返回一个首字母大写，其他小写的字符串

```python
>>> str = "Hello World"
>>> print(str.capitalize())
Hello world
```

######4.7 str.title()

> 返回一个每个单词首字母大写的字符串

```python
>>> str = "Hello World"
>>> print(str.title())
Hello World
```

######4.8 str.center(width[, fillchar])

> 功能：返回一个指定宽度的居中字符串，fillchar为填充的字符，默认使用空格

```python
>>> str = "Hello World"
>>> print(str.center(50,"*"))
*******************Hello World********************
```

######4.9 str.ljust(width[, fillchar])

> 功能：返回一个指定宽度的左对齐字符串，fillchar为填充字符。默认使用空格填充

```python
>>> str = "Hello World"
>>> print(str.ljust(50,"*"))
Hello World***************************************
```

######4.10 str.rjust(width[, fillchar])

> 功能：返回一个指定宽度右对齐字符串，fillchar为填充字符，默认使用空格填充

```python
>>> str = "Hello World"
>>> print(str.rjust(50,"*"))
***************************************Hello World
```

######4.11 str.zfill(width)

> 功能：返回一个长度为width字符串，原字符串右对齐，前面补0

```python
>>> str = "Hello World"
>>> print(str.zfill(50))
000000000000000000000000000000000000000Hello World
```



######4.12 str.count(str 【,start】【, end】)

> 功能：返回字符串中str出现的次数，可以指定一个范围，若不指定则默认从头到尾,匹配的时候是区分大小写的。

```python
>>> str = "Hello World"
>>> print(str.count("hello", 0 , 10))
0
```

######4.13 str.find(str1【, start】【, end】)

> 功能：从左到右检测str1字符串是否包含在字符串中，可以指定范围，默认从头到尾。
>
> 返回的是第一次出现的开始的下标，若未查询到，则返回-1

```python
>>> str = "Hello World"
>>> str1 = "llo"
>>> print(str.find(str1, 0 , 10))
2
```

######4.14 str.rfind(str1【, start】【, end】)

> 功能：类似于str.find(),不过是从右边开始查找

```python
>>> str = "Hello World"
>>> str1 = "llo"
>>> print(str.rfind(str1, 0 , 10))
2
```

######4.15 str.index(str1[, start = 0]   ,[ end = len(str)])

> 功能：类似于find(),与find() 不同的是，如果str1不存在的时候会报一个异常

```python
>>> str2 = "Hello World"
>>> str1 = "hello"
>>> print(str2.index(str1, 0 , 10))
ValueError: substring not found
```

######4.16 str.lstrip()

> 功能：截掉字符串左侧指定的字符串，则默认删除空白符（包括'\n', '\r',  '\t',  ' ')

```python
>>> str = '**** you are very good'
>>> print(str.lstrip())
>>> print(str.lstrip())
**** you are very good
>>> print(str.lstrip("*"))
 you are very good
```

######4.17 str.rstrip()

> 功能：截掉字符串右侧指定的字符串，则默认删除空白符（包括'\n', '\r',  '\t',  ' ')

```python
>>> str = '**** you are good****'
>>> print(str.rstrip())
**** you are good****
>>> print(str.rstrip("*"))
**** you are good
```

##### 4.18 str.strip()

> 功能:截掉字符串左右两侧指定的字符串,则默认删除空白符（包括'\n', '\r',  '\t',  ' ')

```python
>>> str1 = "      hello world     "
>>> str1.strip()
'hello world'
```



##### 4.18 string.split(str="", num=string.count(str))

> 功能:以 str 为分隔符切片 string，如果 num有指定值，则仅分隔 num 个子字符串
>
> str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。   num -- 分割次数

```python
>>> str1 = "hello you are good"
>>> str1.split()
['hello', 'you', 'are', 'good']
>>> str1.split(" ",2)
['hello', 'you', 'are good ']
```

**练习题**

1.计算1~100以内所有能被3或者17整除的数的和

```
sum=0
for x in range(1, 101):
    if x%3==0 or x%17==0:
        sum += x
    else: pass
print(sum)
```

2.计算100~999的水仙花数的个数

```
y=0
for x in range(100,1000):
    a=int(str(x)[0])
    b=int(str(x)[1])
    c=int(str(x)[2])
    if x == a**3+b**3+c**3:
        y +=1
        print(x)
print("100~999总共有水仙花数：%d个"%(y))
```

```
y=0
for x in range(100,1000):
    a = x//100
    b = x//10%10
    c = x%10
    if x==a**3+b**3+c**3:
        y +=1
        print(x)
    else: pass
print("100~999总共有水仙花数：%d个"%(y))
```

3.计算200~500以内能被7整除但不是偶数的数的个数。



```
y=0
for x in range(201, 500, 2):
    if x%7==0:
        print(x)
        y +=1
print("共有%d个能被7整除但不是偶数的数"%y)

```

4计算10000~99999回文数个数，并打印回文数

```
y=0
for x in range(10000,100000):
    x2=int(str(x)[::-1])
    if x2==x:
        y +=1
        print(x)
print("共有回文数%d"%y)
```

5.押宝游戏：

开始游戏 -> 投入赌金【一次性投入】 -> 

循环  ：押宝【5块钱一次】 -> 开奖  --》中奖/未中奖 --》用户输入是否继续 【当余额不足则自动退出游戏】

```
import random

money = int(input("请输入你投入的赌金："))
if money>=5:
    while True:
        print("您的资金有%d元" % (money))
        input("按任意键开奖,未中奖将扣除5块")
        value = random.randrange(1,11)
        if value <=3:  #中奖概率30%
            money +=10
            print("恭喜您中了10块！！！")
        else:
            print("很遗憾未中奖！")
            money -= 5
        Back=input("按任意键继续游戏，n/N退出游戏")
        if Back == 'n' or Back == 'N':
            print("欢迎下次光临！！")
            break
        while money<5:
            print("您的余额不足，已退出游戏")
            add =int(input("请输入充值金额："))
            money += add
```



6。百钱买百鸡，现有100文钱，公鸡5文钱一只，母鸡3文钱一只，小鸡一文钱3只。

要求：公鸡，母鸡，小鸡都要有，把100文钱买100只鸡，买的鸡是整数。

问：多少只公鸡，多少只母鸡多少只小鸡？

```
for x in range(101):
    for y in range(101-x):
        for z in range(3,300-x-y,3):
            if x+y+z==100 and 5*x+3*y+z/3 ==100:
                print("%d只公鸡，%d只母鸡,%d只小鸡。%d+%d+%d=100只鸡，%d+%d+%d=100文钱"%(x,y,z,x,y,z,5*x,3*y,z/3))
```



7.倒着打印99乘法表（分别使用while和for循环）

```
for i in range(9, 0, -1):
    for k in range(9-i):
        print("\t",end = "\t")
    for j in range(i, 0, -1):
        print("%dx%d=%d"%(j, i, i*j), end="\t")
    print()
```

```
i,j=9,9
while i:
    a = i
    while 9-a:
        print("", end='\t\t')
        a +=1
    while j:
        print("%dx%d=%d"%(i, j, i*j), end='\t')
        j -=1
    i -=1
    j = i
    print()

```



**什么时候使用while和for**

**当知道循环次数选择for 循环**

**不知道循环次数选择while循环**

 

### 课堂练习###



```
# 求1！+2！+...+n!
n = int(input("请输入n的值："))
ji = 1
i = 1
sum = 0
while i<=n :
    ji *=i
    sum +=ji
    if i<n:
        print("%d" % i, end="!+") #防止末尾多了“!+”字符串
    i += 1
print("%d!=%d"%(n,sum))
```

```
'''
打印：*
	 **
	 ***
'''
n = int(input("请输入打印*的个数："))
i, j = 1, 1
while i<=n:
    while j<=i:
        print("*",end="")
        j +=1
    i +=1
    j =1
    print("")
```

```
n = int(input("请输入打印*的个数："))
i=1
while i<=n:
    print("*"*i)
    i +=1
```
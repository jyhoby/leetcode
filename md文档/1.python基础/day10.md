#### 面向对象思想

##### 面向对象的设计思想

> 面向对象是基于万物皆对象这个哲学观点
>

#####面向对象和面向过程的区别

**面向过程**

> 在生活中:
>
> 它是一种看待问题的思维方式,在思考问题的时候,着眼问题是怎样一步一步解决的,然后亲力亲为去解决问题[类似于公司里的执行者]
>
> 在程序中:
>
> ​	代码是从上而下顺序执行,各个模块之间的关系尽可能简单,在功能上相对独立,程序的流程在写程序的时候就已经决定.

**面向对象**

> 在生活中:
>
> 它是另一种看待问题的方式,它着眼于找到一个具有特殊功能的个体,然后委托这个个体去帮你完成某件事.这是更符合人类思考习惯的思想[指挥者]
>
> 在程序中:
>
> 把数据以及对数据的操作方法放在一起,作为一个相互依存的整体--对象
>
> 把同类的对象进行抽象出其共性,形成类
>
> 类中大多数数据,只能用本类的方法进行处理
>
> 类通过一个简单的外部接口与外界发生关系,对象与对象之间通过消息进行通信
>
> 程序执行的流程由用户在使用的过程中决定
>
> 使用面向对象进行开发,需要先找到具有所需功能更的对象来使用,如果这个对象不存在,那么则需要创建这么一个具有所需功能的对象
>
> 注意:面向对象只是一种思想,并不是一门编程语言.

**区别总结**

> a. 都是看待问题的一种思维方式,都能解决问题
>
> b. 面向过程着眼于所有的事情亲力亲为
>
> c. 面向对象着眼于找到一个具有特殊功能的对象,委托这个对象实现你需要实现的功能.
>
> python语言是面向对象的程序设计语言,类和对象是面向对象的核心

#### 类和对象

##### 类和对象的概念

> 类:一个具有特殊功能的实体的集合[群体]
>
> 对象:在一个类中,一个具有特殊功能的实体,能够帮忙解决特定的问题,对象通常也被称为实例.
>
> 两者之间的关系:类用于描述某一对象的共同特征,而对象则是类的具体存在
>
> 举例:
>
> 学生      张三
>
> 快递      顺丰
>
> 总结: 类与对象的关系
>
> a.类是对象的抽象,对象是类的具体体现
>
> b.类也是一种数据类型,只不过是自己定义的类似与number,string等,它本身并不占用空间,但是它的实例[对象]是占用空间的.

##### 类的定义

> 格式:
>
> class 类名:
>
> ​	类体
>
> 说明:
>
> a.python中使用class关键字定义类
>
> b.类名只要是一个合法的标识符即可,命名规则遵循"驼峰式命名"
>
> c.尽量使用单个或者多个有意义的单词链接而成

演示

```python
# 一个简单的类的实例
class Person():
    print("hello")
```

##### 类的设计

> 只需要关心3样东西
>
> 1.事物名称[类名]: 人类  (Person)
>
> 2.特征: 身高(height)  年龄(age)等 ——>名词
>
> 3.行为: 跑(run) 说话(say)  —————>动词

#### 类中的方法和属性

#####方法和属性的定义

> 生活中描述事物的无非就是描述事物的特征和行为
>
> python中用类来描述事物也是如此,前面已经定义了类,但是,如果只有类单独存在
>
> ,没有任何意义,所以定义类其实就是定义类中的成员[成员变量和成员方法]
>
> 成员变量—>类具有的特征  例如:人—>身高,性别,体重
>
> 成员方法 —>类具有的行为  例如人—>吃喝玩乐
>
> 因此,拥有相同的(或者类似)属性和行为的对象都可以抽取出一个类

```python
class Persion():
    #成员变量,初始值就是相当于默认值
    name = ""
    age = 0
    height = 0
    weight = 0
    #成员方法
    #在类的内部,使用def关键字来定义的一个方法
    #注意:区别于普通方法,类中方法的参数必须包含参数self,且为第一个参数
    #self代表类的实例(某个对象)
    def run(self):
        print("run")
        
    def eat(self, food):
        print("eat",food)
    
    def sleep(self):
        print("sleeping")    
    
```

> 说明:定义了类,并在类中定了成员变量和成员方法,但是成员变量和成员方法是如何使用的呢?

##### 方法和属性的使用

##### 实例化对象:

> 前面说过,对象是实实在在的个体,负责去完成某件指定的事情
>
> 对象的创建的过程又被称作对象的实例化过程
>
> 语法:
>
> 对象名 = 类名()

```python
'''
实例化对象
格式: 对象名 = 类名()
注意: 没有参数的时候,小括号也不能省略
'''

#实例化一个对象
pre1 = Person()
print(pre1)
print(type(per1))
print(id(per1))

per2 = Person()
print(per2)
print(type(per2))
print(id(per2))
```

##### 对象调用方法和属性

```python
per = Preson()
'''
访问属性
格式:对象名.属性名
赋值:对象名.属性名 = 新值
'''
per.name = 'lili'
per.age = 18
per.height = 160
per.weight = 80
print(per.name, per.age, per.height, per.weight)

'''
访问方法
格式:对象名.方法名(参数列表)
'''
per.run()
per.eat("apple")
per.sleep()

#问题:目前来看Person创建的所有对象属性都是一样的
per2 = Person()
print(per2.age)
per3 = Person()
print(per3.age)
```

> 总结:
>
> 访问变量采用:   对象名.属性名
>
> 访问方法采用:  对象名.方法名(参数列表)

##### 内存中的对象

>per = Person()
>
>说明:程序中定义Person类型的变量per实际是一个变量名,它被存放在栈内存中,他指向实际的Person对象,而真正的Person对象则存放在堆内存中.

![存中的对](./内存中的对象.png)

![存中的对象](内存中的对象2.png)

> 综合练习:
>
> 第一天开学,介绍一下你自己其中包括姓名,年龄以及爱好

```python
#学生类
class Student():
    #特征:成员变量
    name = ""
    age = ""
    hobby =""
    
    def introduce(self,name, age, hobby):
        print("大家好,我是%s,今年%d岁,爱好是%s"%(name,age, hobby))
    
    
    def singsong(self):
        print("娘子~啊哈")
    
    def dance(self):
        print("广场舞跳起来...")
    
    def  lie(self):
        print("我家特别穷,我小时候就一直在放牛,只有几万头....")
    
```

#### 构造函数和析构函数

##### 构造方法的使用

```python
	使用上面的方式可以创建对象,但是,很多类都倾向于将对象创建为有初始化状态.因此类可能定义一个名为__init__()的特殊方法(构造方法)
	构造方法也叫做构造器,是指当实例化一个对象(创建一个对象)的时候,第一个被自动调用的方法.
```

> 演示1:构造方法被调动的动机

```python
class Person():
    name = ""
    age = 0
    #构造方法
    def __init__(self):
        print("构造函数被执行了")
    
    #创建对象的过程中构造函数被自动调用
    #得出结论:创建对象的过程中调用了构造函数
    #当未手动添加构造函数时,系统会默认提供一个无参的构造函数
p1 = Person
```

> 演示2:构造函数和普通函数之间的区别和练习

> 说明:构造函数本质上还是一个函数,函数可以有参数,也可以无参,所以同样的道理,构造方法也是如此

```python
class Person():
    name = "stu"
    age = 10
    height = 160
    weight = 90
    def run(self):
        print("run")
    def eat(self, food):
        print("eat "+ food)
        
    #一般情况下,有构造方法的参数和成员变量有关,并且在设置的过程中与成员变量同名
    def __init__(self, name, age, height, weight):
        #print(nname, age, height, weight)
        #因为构造方法是创建对象的过程中被调用的
        #所以构造方法的作用一般是用来定义成员变量并且给成员变量赋值
        #定义属性并给属性赋值
        #通过self来进行区分是成员变量还是形参
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        
        
'''
构造函数: __init__()  在使用类创建对象的时候自动调用
注意: 如果不显式的写出构造函数,默认会自动添加一个空的构造函数,函数体部分什么都不实现
'''
per = Person("hanmeimei", 20, 170, 55)
print(per.name, per.age)
per.run()

per2 = Person("lilei", 21, 175, 70)
print(per2.name, per2.gae)
```

##### 析构函数的使用

> 析构函数: del 释放对象时自动调用

演示:

```python
class Person():
    def run(self):
        print("run")
    
    def eat(self, food):
        print("eat "+food)
    
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        
     def __del__(self):
        print("这里是析构函数")

per = Person("hanmeimei", 20, 170, 55)
#释放对象
del per
#注意:对象释放后就不能再进行访问了

#在函数里定义的对象,会在函数结束时自动释放,这样可以用来减少内存空间的浪费
#其实就是作用域的问题
def func():
    per2 = Person("aa", 1, 1, 1)
    
func() 
```



##### self的使用

> 注意:self代表类的实例[对象],而非类本身
>
> 类的方法与普通的函数只有一个特殊的区别—>他们必须有一个额外的第一个参数名称,按照惯例它的名字是self

```python
class Test():
    def prt(self):
        print(self)
        print(self.__class__)
t = Test
t.prt() 
```

> 演示2:self不是python的关键字

```python
class Person():
    def run(self):
        print("run")
        print(self.__class__)
        #通过这种方式也可以进行对象的初始化
        p = self.__class__("tt", 30, 10, 30)
        
     def eat(self, food)
    	print("eat" + food)
        
     def say(self)
    	print("hello, my name is %s, I am %d year old"%(self.name, self.age))
     
     def play(a)
        print("play",a.name)
        
     def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

#self代表此时正在创建对象,则self.属性表示当前对象的属性 
per1 = Person("tom", 20, 160, 80)
per1.say()

per2 = Person("henmeimei", 21, 160, 80)
per2.say()

per1.say()
per1.run()
```

> 总结：
>
> 1.self在定义的时候需要定义，但是在调用的时候会自动传入
>
> 2.self的名字并不是规定死的，但是最好还是按照约定使用self
>
> 3.self总是指调用时的类的实例

#####拓展

>定义在类中的变量我们又分为成员变量以及类变量(或者称静态成员变量)
>
>类变量定义在类中，且在函数体之外，类变量通常不作为实例变量使用，类变量在整实例化的过程中是公用的。
>
>成员变量：定义在方法中且通过self绑定在实例上的变量，只作用于当前实例。

```python
class Student(object):
    #类变量
    classname = "1802"
    def __init_(self):
        #成员变量
        self.name = "zhang"
        #self.classname = "1888"

#变量的调用
stu = Student()
#成员变量的调用
print(stu.name)
#类变量的调用
print(stu.classname)
print(Student.classname)

#更改变量的值

#通过类名来更改类变量的值
Student.classname = "1804"
#通过对象更改类变量的值
stu.classname = "1803"

#创建一个新的变量
stu2 = Student()
print(stu2.classname)
#"1804"
print(Student.classname)
#"1804"
```

> 结论:
>
> 1.当类变量与成员变量同名时，使用对象来调用时，默认调用的是成员变量的值
>
> 2.当成员变量不存在，并且类变量存在的时候，在使用对象调用属性的时候，会调用类变量
>
> 3.成员变量只能通过对象来调用，而类变量不但可以通过对象调用，还可以通过类名来调用
>
> 4.通过对象来更改成员变量或者是类变量的值的时候，只是改变的当前对象的值，而通过类名来更改类变量的值的时候，更改的则是类变量的初始值。

成员方法：

```python
''' 通常情况下，在类中定义的所有函数（注意了，这里说的就是所有，跟self啥的没关系，self也只是一个再普通不过的参数而已）都是对象的绑定方法，对象在调用绑定方法时会自动将自己作为参数传递给方法的第一个参数。除此之外还有两种常见的方法：静态方法和类方法，二者是为类量身定制的，但是实例非要使用，也不会报错。'''
class Student():
    def say(self):
        print("**********")
```



静态方法：

静态方法是一类特殊的方法，有时你可能需要写一个属于这个类的方法，但是这些代码完全不会使用到实例对象本身，比如：

```python
'''
静态方法是一种普通函数，位于类定义的命名空间中，不会对任何实例类型进行操作，python为我们内置了函数@staticmethod来把类中的函数定义成静态方法
'''
class Student():
    @staticmethod
    def say(self):
        print("**********")
        
     @staticmethod
	def spam(x,y,z): #类中的一个函数，千万不要懵逼，self和x啥的没有不同都是参数名
        print(x,y,z)
        
 Student.say()
 Student.spam(1,23,3)
```

类方法：

> 什么是类方法呢？类方法不是绑定到对象上，而是绑定在类上的方法。

```python
'''
类方法是给类用的，类在使用时会将类本身当做参数传给类方法的第一个参数，python为我们内置了函数@classmethod来把类中的函数定义成类方法
'''
class Test:
    x=1
    @classmethod
    def test(cls):
        print(cls,cls.x)
Test.test()
```

**无论你用哪种方式访问这个方法，它总是绑定到了这个类身上，它的第一个参数是这个类本身**

什么时候使用这种方法呢？类方法通常在以下两种场景是非常有用的：

```python
'''1.工厂方法：它用于创建类的实例，例如一些预处理。如果使用@staticmethod代替，那我们不得不硬编码Pizza类名在函数中，这使得任何继承Pizza的类都不能使用我们这个工厂方法给它自己用。'''
class Pizza():
    price = 20
    def __init__(self,taste):
        self.taste = taste
      
        
    @classmethod
    def getPrice(cls,size):
        return size*cls.price
```

```python
'''
2.调用静态类：如果你把一个静态方法拆分成多个静态方法，除非你使用类方法，否则你还是得硬编码类名。使用这种方式声明方法，Pizza类名明永远都不会在被直接引用，继承和方法覆盖都可以完美的工作。
'''
class Pizza(object):
  def __init__(self, radius, height):
    self.radius = radius
    self.height = height

  @staticmethod
  def compute_area(radius):
     return math.pi * (radius ** 2)

  @classmethod
  def compute_volume(cls, height, radius):
     return height * cls.compute_area(radius)
```

强调，注意注意注意：静态方法和类方法虽然是给类准备的，但是如果实例去用，也是可以用的，只不过实例去调用的时候容易让人混淆，不知道你要干啥

```python
#结论：
区别，实例方法隐含的参数为类实例self，而类方法隐含的参数为类本身cls。 静态方法无隐含参数，主要为了类实例也可以直接调用静态方法。

所以逻辑上，类方法应当只被类调用，实例方法实例调用，静态方法两者都能调用。主要区别在于参数传递上的区别，实例方法悄悄传递的是self引用作为参数，而类方法悄悄传递的是cls引用作为参数。
```





   	

#### 访问限制

##### 概念

> 面向对象语言的三大特征:封装, 继承, 多态
>
> 广义的封装: 类和函数定义本身就是封装的体现
>
> 狭义的封装:一个类的某些属性,不希望外界直接访问,而是把这个属性私有化[只有当前类持有],然后暴露给外界一个访问的方法即可.
>
> 封装的本质:就是属性私有化的过程
>
> 封装的好处:提供了数据的复用性,保证了数据的安全性
>
> 举例:插排



> 在class内部可以有属性和方法，而外部的代码可以通过直接调用实例变量的方法来操作数据，这样就隐藏了内部的复杂逻辑。
>
> 但是从我们之前定义的class来看，外部代码还是可以自由的修改一个实例的name等属性。

##### 使用

> 如果要让内部的属性不被外部访问，可以把属性名前加两个下划线，在python中以双下划线开头的变量就变成了一个私有的变量，只有内部可以访问，而外部不能访问。

```python
class Person(object):
    def __init__(self, name, age, height, money):
        self.name = name
        self.__age__=age
        self.__money = money
```

> 修改完毕之后，对于外部的代码几乎没有变动，但是已经无法从外部访问money变量了

```python
>>>per = Person("hanmeimei", 20, 170, 10000)
>>>per.__money
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute '__money'
```

>这样就确保了外部的代码不能随意的修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。

> 但是，如果外部的代码需要获取money的属性的时候该怎么办呢？
>
> 我们可以通过getMoney与setMoney的方法来操作数据

```python
class Person(object):
    def run(self):
        print(self.__money)
    def eat(self):
        print("eat",food)
    def __init__(self, name, age, height, weight, money):
        self.name = name
        self.__age__=age
        self.weight = weight
        self.__money = money
        
    #通过内部方法,去修改私有属性
    #通过自定义的方法实现对私有属性的赋值与取值
    #set方法:setxxx
    def setMoney(self, money):
        #数据的过滤
        if money < 0:
            money = 0
        self.__money = money
     
    #get方法:getXXX
    def getMoney(self):
        return self.__money

per = Person("hanmeimei", 20, 170, 55, 10000)

#1.属性被私有化之后的访问
#如果要让内部属性不被外部直接访问,在属性前加两个下划线(__),
#在python中如果在属性前面加两个下划线,name这个属性就变成了私有属性[private]
#私有属性的含义:在外界不能像以前那么直接访问
#print(per.__money) #无法在外界直接访问
per.run() #内部可以访问

#2.解决办法: 如何对私有属性取值和赋值
#但是,需要注意的是,在python找那个私有不是绝对的
#属性被私有化之后,可以通过get/set的方法进行访问
per.setMoney(10)
print(per.getMoney())



#4.特殊情况
#在Python中 __xxx__ 属于特殊变量,将不再属于私有变量,可以直接访问
print(per.__age__)

#在python中 _xxx变量,这样的实例变量外部是可以访问的,但是,按照约定的规则
#当我们看到这样的变量时,意思虽然是"虽然我可以被访问,但是请把我视为私有变量,不要直接访问我"
print(per._height)

```

> 双下划线开头的变量是不是一定不能够从外部访问呢？其实也不是。

```python
#不能直接访问per.__money是因为python解释器把__money变成了_Person__money
#仍然可以使用_Person__money去访问,但是强烈不建议这么干,不同的解释器可能存在解释的变量名不一致
per = Person("hanmeimei", 20, 170, 55, 10000)
per._Person__money = 1
print(per.getMoney())
```

> 总的来说，python本身没有任何机制能够阻止你干坏事，一切靠自觉

注意：这种错误的写法

```python
per = Person("hanmeimei", 20, 170, 55, 10000)
per.__money = 1
print(per.__money)
#从表面上看，外部代码“成功的设置了__money”变量，但是实际上这个__money变量和内部的__money变量不是同一个变量，而是外部的代码给per新增了一个变量
#测试一下
print(per.getMoney())
```

##### 单下划线，双下划线，头尾下划线的说明

```python
'''
头尾下划线__foo__()：定义特殊的方法，一般是系统定义名字，类似于__init__()

单下划线：_foo:以单下划线开头的表示是protected类型的变量，即保护类型的变量只允许本身与子类访问，不能用于from module import *

双下划线：__foo:双下划线的表示的是私有类型(private)的变量，只能允许这个类的本身进行访问。
'''
```

> 综合练习

```python
'''
需求:富二代开着骚红色玛莎拉蒂,很自豪的跟朋友炫耀...

分析:
汽车类:
特征:品牌,颜色
行为:在马路上奔驰

富二代类:
特征:姓名
行为:开车,炫耀
'''
form car import Car
from richman import RichMan

#1.创建富二代对象
man = RichMan("王思聪")

#2.创建汽车对象
car = Car("玛莎拉蒂","骚红色")

#富二代的行为
man.dirveCar(car)
man.showCar(car)
```

```python
class Car(object):
    #构造函数
    def __init__(self,brand, color):
        self.__brand = brand
        self.__color = color
    
    #get/set函数
    def setBrand(self, brand):
        self.__brand = brand
    
    def getBrand(self,brand):
        return self.__brand
    
    def setColor(self, color):
        self.__color = color
        
     def getColor(self):
        return self.__color
   	
     #成员函数
      def run(self):
        print("%s在马路上奔驰"%self.__brand)
        
```

```python
class  RichMan(object):
    #构造函数
    def __init__(self, name):
        self.__name = name
        
    #get/set函数
    def setName(self, name):
        self.__name = name
     
    def getName(self):
        return  self.__name
    
    #成员函数
    def driverCar(self,car)
    	print("福二代%s开着他新车%s"%(self.__name, self.getBrand()))
     def showCar(self,car)
    	print("很自豪的炫耀起来,你看这辆%s,你看这%s成色...."%(car.getBrand(), car.getColor()))
```



#### 继承

##### 概念

> 如果两个或者两个以上的类具有相同的属性和方法,我们可以抽取一个类出来,
>
> 在抽取的类中声明公共的部分
>
> ​	被抽取出来的类 ——父类  超类  基类
>
> ​	其他类   — 子类  派生类
>
> ​	他们之间的关系 ——子类  继承自父类
>
> 注意：若一个类没有继承其他类，则它默认继承object类，换句话说，object是一切类的基类。

##### 单继承

> 简单来说,一个子类只能有一个父类,被称为单继承
>
> 演示:test.py 文件
>
> 注意:在使用继承时,尽量一个类存在于一个模块中

> 比如，我们定义了一个Animal的class，有一个run()方法

```python
class Animal(object)：
	def run(self):
        print("Animal is running....")
```

> 当我们需要编写Dog和Cat类时，就可以直接从Animal类继承:

```python
class Dog(Animal):
    pass

class Cat(Animal):
    pass
```

> 对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类，Cat和Dog类似。

> 继承有什么好处？最大的好处就是子类获得了父类的全部功能，由于Animal实现了run()方法，因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()的方法。

```python
dog = Dog()
dog.run()

cat = Cat()
cat.run()
```

> 当然，也可以对子类增加一些方法，比如Dog类：

```python
class Dog(Animal):    
    def eat(self):
        print("Eating meat....")
```

作业：

```python
from person import Person
from student import Student
from worker import Worker

per = Person("aa", 1, 2)
stu = Student("tom", 18, 12345, 110)
print(stu.name, stu.age)
stu.run()

print(stu.stuId)
#私有属性
#print(stu.__money)
print(stu.getMoney())#通过继承过来的共有方法访问私有属性
#stu.stuFunc()

wor = Worker("lilei", 20, 111)
print(wor.name, wor.age)
wor.eat("apple")

#子类对象调用父类同名的函数,则发现优先调用子类中的函数
#本质是子类中的方法覆盖了父类中同名的函数
wor.run()

print(per.getMoney())

#父类对象不能访问子类特有的属性或方法
#print(per.stuId)
```



```python
#以前的写法 class Person(object):
#但是实质上,如果没有显示的写出父类,则这个类的父类默认为object
#object是所有类的父类或者超类
class Person(object):
    #构造方法
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.__money = money
        
     #get/set方法
    def setMoney(self, money):
        self.__money = money
        
    def getMoney(self):
        return self.__money
    
    def run(self):
        print("run")
        
    def eat(self, food):
        print("eat", food)
        
```

```python
from person  import Person
class Student(Person):
    def __init__(self, name, age, money, stuId):
        #调用父类中的构造方法
        #方法1 super(当前类,self).__init__(参数列表)
        #super(Student,self).__init__(name, age, money, stuId)
        #方法2 父类名.__init__(属性列表)
        Person.__init__(self, name, age, money)
        #子类可以有一些自己独有的属性
        self.stuId = stuId
    def setFunc(self):
        print(self.__money)
```

```python
from person import Person

class Worker(Person):
    def __init__(self, name, age, money)
    	super(Worker,self).__init__(name, age, money)
    # 在子类中定义和一个父类中重名的函数
    def run(self):
        print("子类中的run方法被调用了")
```

> 总结:
>
> 继承的特点:
>
> a. 子类对象可以直接访问父类中未私有的对象
>
> b. 子类对象可以调用父类中的方法
>
> c. 父类对象不能访问子类中特有的属性或者方法
>
> 优缺点:
>
> 优点:
>
> 1.可以简化代码,减少冗余
>
> 2.提高代码的维护性
>
> 3.提高了代码的安全性
>
> 缺点:
>
> 耦合和内聚被用来描述类与类之间的关系,耦合性越低,内聚性越高,说明代码越好,
>
> 但是,在继承关系中,耦合性相对比较高,如果修改父类,子类也会随着变化

##### 多继承

> 顾名思义:就是一个子类中可以有多个父类,比如一个孩子有一个爸爸一个妈妈

```python
from  child import Child

def main():
    c = Child(300, 100)
    print(c.money, c.faceValue)
    c.play()
    c.eat()
    #注意:如果多个父类中的方法名相同,默认调用的是子类括号中排前面的父类中的方法
    #此时调用的是Father中func方法
if __name__ == "__mian__":
    main()
```

```python
class Father(object):
    def __init__(self, money):
        self.money = money
    def play(self):
        print("play")
    def func(self):
        print("Father")
```

```python
class Mother(object):
    def __init__(self, faceValue):
        self.faceValue = faceValue
    def eat(self):
        print("eat")
    def  func(self):
        print("Mother")     
```

```python
from father import Father
from mother import Mother

class Child(Father, Mother):
    def __init__(self, money, faceValue):
        #注意:分别调用各个父类中的构造方法
        Father.__init__(self, money)
        Mother.__init__(self, faceValue)
        #子类中同样可以有自己独有的特性
  
```

> 总结:
>
> 1. 子类可以从多个父类中继承属性和方法
> 2. 一个父类可以有多个子类
> 3. 一个子类可以有多个父类

#####多态

> 多态是指一类事物的有多种状态【一个抽象类有很多子类，因而多态的概念依赖于继承。】
>
> 1.序列有多种形态：字符串，列表，元组
>
> 2.动物有多中形态：猫，狗

定义父类：

```python
class Animal(object)：
	def run(self):
        print("Animal is running....")
```

定义子类：

```python
class Dog(Animal):
    def run(self):
        print("Dog is running...")
    
    def eat(self):
        print("Eating meat....")
```

> 继承的第二个好处是，我们可以在自己需要的时候，对我们的代码进行改进。当子类与父类都存在相同的run()方法的时候，子类中的run()覆盖了父类中的run(),在代码运行的时候，总会调用子类中的run().
>
> 这时候我们就获取了继承的另外一个好处：多态。
>
> 若要理解多态，我们首先要对数据类型再进行说明，我们定义一个class的时候，其实就是定义了一种数据类型。

```python
a = list() #a是list类型
b = Animal() #b是Animal类型
c = Dog() #c是Dog类型
```

> 判断一个变量是否是某个类型们可以使用instance()来判断

```python
>>>isinstance(a,list)
True
>>>isinstance(b,Animal)
True
>>>isinstance(c,Dog)
True
#c不仅是Dog还是Animal
>>>isinstance(c,Animal)
True
```

> 在继承的关系中，如果一个实例的数据类型是某个子类，那么它的数据类型也可以被看做是父类。

> 多态的优点：

```python
class Animal(object)：
	#def run(self):
     #   print("Animal is running....")
     
    @staticmethod
    def run2(Animal):
        Animal.run()
        
class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')

Animal.run2(Dog())
Animal.run2(Cat())
#结果
Dog is running...
Cat is running...
```

> 新增子类的时候我们不需要对我们的run2()做任何的修改，任何依赖Animal作为参数的函数都可以不加修饰的正常的运行。
>
> 多态的优点就是，当我们需要传入Dog，Cat，...时我们只需要接收Animal类型的即可,因此，传入的类型只要是Animal类或者是子类，就会自动调用实际类型的run()方法，这就是多态的意思。

##### 获取对象属性

> 使用type()来判断对象类型

```python
>>>type(123)
```

> 若是一个变量指向函数或者是类，依然可以使用type()判断。

> isinstance()可以判断一个对象是否属于某种类型

```python
>>> a = Animal()
>>> b = Dog
>>> isinstance(a,Animal)
True
>>> isinstance(b,Animal)
True
```

>还可以判断一个变量是否是某些类型中的一种，比如下面的代码：

```python
>>> isinstance([1,2,3],(list,tuple))
True
```

> 使用dir()函数可以获取一个对象的所有的属性和方法，它返回一个包含字符串的list

```python
>>> dir(a)
```



##### 函数重写

###### 系统函数

```python
'''
重写:将函数重写一遍
__str__():在调用print打印对象时自动调用,是给用户用的,是一个描述对象的方法.
__repr__():是给机器用的,在python解释器里面直接敲对象名在回车后调用方法
注意:在没有str时,且有repr,__str__=__repr__
'''
class Animal(object):
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
     def __str__(self):
        return "%s-%d-%d-%d"%(self.name, self.age, self.height, self.weight)
ani  = Animal("大黄", 5, 60, 25)
#print(per.name, per.age, per.height, per.weight)
#在打印ani时自动调用str函数
print(ani)

#优点或者使用时机:当一个对象的属性值很多,并且都需要打印,重写__str__方法后,简化了代码,方便查看.

```


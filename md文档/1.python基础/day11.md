#### 成员变量与类变量【静态成员变量】

定义在类中的变量我们又分为成员变量以及类变量(或者称静态成员变量)

类变量定义在类中，且在函数体之外，类变量通常不作为实例变量使用，类变量在整实例化的过程中是公用的。

成员变量：定义在方法中且通过self绑定在实例上的变量，只作用于当前实例。

> 成员变量与类变量的区别
>
> 1.定义的位置不同，类变量直接定义在类中变量，成员变量是定义在方法绑定在self身上的变量
>
> 2.成员变量使用对象来访问，类变量使用类名来访问
>
> 3.在内存中出现的时机不同【类变量随着类的加载而出现，成员变量随着对象的创建而出现】
>
> 4.优先级不同，使用对象调用的时候优先使用成员变量

例如：

```python
class Student(object):
    #定义的位置
    #类变量
    classname = "1802"
    def __init_(self):
        #成员变量
        self.name = "zhang"
        #self.classname = "1888"
```

1.变量的调用

```python
#访问的方式
stu = Student()
#成员变量的调用
print(stu.name)
#类变量的调用
print(stu.classname)
print(Student.classname)
```

2.更改变量的值

```python
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

> 结论：
>
> 1.当类变量与成员变量同名时，使用对象来调用时，默认调用的是成员变量的值
>
> 2.当成员变量不存在，并且类变量存在的时候，在使用对象调用属性的时候，会调用类变量
>
> 3.成员变量只能通过对象来调用，而类变量不但可以通过对象调用，还可以通过类名来调用
>
> 4.通过对象来更改成员变量或者是类变量的值的时候，只是改变的当前对象的值，而通过类名来更改类变量的值的时候，更改的则是类变量的初始值。

#### 动态添加属性和方法

> 正常情况下，我们定义了一个class，创建一个class的实例后，我们可以给该实例绑定任何的属性和方法，这就是动态语言的灵活性。

```python
#python语言的特点:灵活
#这里说的动态加属性和方法主要指的是关于__slots__函数的使用
```

```python
#定义一个空类
class Person():
	pass
# 动态添加属性[体现了动态语言的特点:灵活性]
per = Person()
per.name = "tom"
print(per.name)

#动态添加方法
def say(self):
	print("my name is "+ self.name)
per.speak = say
per.speak()
per.speak(per)
```

但是，给一个实例绑定的方法对另外一个实例是不起作用的。

为了给所有的实例都绑定方法，可以通过给class绑定方法

```python
#动态添加方法
def say(self,name):
    self.name = name
	print("my name is "+ self.name)
Person.speak = say

per = Person()
per.say()
```

> 给class绑定方法后，所有的实例均可调用。
>
> 通常情况下，上面的say方法可以直接定义在class中，但动态绑定允许我们在程序在运行的过程中动态的给class添加功能，这在静态语言中很难实现。



> 如果我们想限制实例的属性怎么办?
>
> 比如，只允许给Person实例添加name，age属性，为了达到限制的目的，Python中允许在定义class的时候，定义一个特殊的变量__slots__变量，来限制该class添加的属性

```python
class Person(object):
    __slots__=("name","age")
#[不想无限制的任意添加属性]
#比如,只允许给对象添加name, age属性
#解决:定义类的时候,定义一个特殊的属性(__slots__),可以限制动态添加的属性范围
per.height = 170
print(per.height)
```

> 使用slots的时候需要注意，slots定义的属性仅仅对当前类的实例起作用，对继承的子类是不起作用的。
>
> 除非在子类中也定义slots，这样子类实例允许定义的属性就是自身的slots加上父类的slots



#### 成员方法

```python
''' 通常情况下，在类中定义的所有函数（注意了，这里说的就是所有，跟self啥的没关系，self也只是一个再普通不过的参数而已）都是对象的绑定方法，对象在调用绑定方法时会自动将自己作为参数传递给方法的第一个参数。除此之外还有两种常见的方法：静态方法和类方法，二者是为类量身定制的，但是实例非要使用，也不会报错。'''
class Student():
    def say(self):
        print("**********")
```

#### 静态方法：

> 静态方法是一类特殊的方法，有时你可能需要写一个属于这个类的方法，但是这些代码完全不会使用到实例对象本身，比如：

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

#### 类方法

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

注意：无论你用哪种方式访问这个方法，它总是绑定到了这个类身上，它的第一个参数是这个类本身。

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
2.调用静态方法：如果你把一个静态方法拆分成多个静态方法，除非你使用类方法，否则你还是得硬编码类名。使用这种方式声明方法，Pizza类名明永远都不会在被直接引用，继承和方法覆盖都可以完美的工作。
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

强调：静态方法和类方法虽然是给类准备的，但是如果实例去用，也是可以用的，只不过实例去调用的时候容易让人混淆，不知道你要干啥。

> 总结：
>
> 1.成员方法隐含的参数为类的实例self，而类方法隐含的参数为类本身cls，静态方法无隐含参数。
>
> 2.类方法只应该被类调用，成员方法被实例/对象调用，而静态方法两者都可以调用。
>
> 3.类方法、静态方法都是给类准备的建议使用类名来调用，但是若执意使用对象来调用，并不会报错。成员方法是给对象准备的，只能使用对象来进行调用，不能使用类名来进行调用。

#### 访问限制—封装

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

> 但是从我们之前定义的class来看，外部代码还是可以自由的修改一个实例的name等属性。

##### 使用

> 如果要让内部的属性不被外部访问，可以把属性名前加两个下划线，在python中以双下划线开头的变量就变成了一个私有的变量，只有内部可以访问，而外部不能访问。

```python
class Person(object):
    def __init__(self, name, age, height, money):
        self.name = name
        self.age=age
        self.__money = money
```

> 修改完毕之后，对于外部的代码几乎没有变动，但是已经无法从外部访问money变量了

> 这样就确保了外部的代码不能随意的修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。

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
        self.age=age
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
    
```

> 更改之后的访问：

```python
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
```

#### 语法糖--@property

```python
class Person(object):
    def run(self):
        print(self.__money)
        
    def eat(self):
        print("eat",food)
    def __init__(self, name, age, height, weight, money):
        self.name = name
        self.age=age
        self.weight = weight
        self.__money = money
     
    #相当于setter方法
   	@money.setter #变量名.setter
    def money(self, money):
        #数据的过滤
        if money < 0:
            money = 0
        self.__money = money
    
    #相当于getter方法
    @property
    def money(self):
        return self.__money
    
```

总结:

> a.装饰器(decorator)可以给函数动态加上功能,对于类的方法,装饰器一样起作用,python内置的@property装饰器就是负责把一个方法变成属性调用的
>
> b.@property的实现比较复杂,我们先考察如何使用,把一个getter方法变成属性,只需要加上@property就可以了,此时@property本身又创建了另一个装饰器@属性.setter,负责把一个setter方法变成属性赋值.
>
> c.@property广泛应用在类的定义中,可以让调用者写出简短的代码,同时保证对参数进行必要的检查,这样,程序运行时就减少了出错的可能性



#### 黑魔法

> 双下划线开头的变量是不是一定不能够从外部访问呢？其实也不是。

```python
#不能直接访问per.__money是因为python解释器把__money变成了_Person__money
#仍然可以使用_Person__money去访问,但是强烈不建议这么干,不同的解释器可能存在解释的变量名不一致
per = Person("hanmeimei", 20, 170, 55, 10000)
per._Person__money = 1
print(per.getMoney())
```

总的来说，python本身没有任何机制能够阻止你干坏事，一切靠自觉



#### 下划线

单下划线，双下划线，头尾下划线的说明

```python
'''
头尾下划线__foo__()：定义特殊的方法，一般是系统定义名字，类似于__init__()

单下划线：_foo:以单下划线开头的表示是protected类型的变量，当我们看到这样的变量时,意思虽然是"虽然我可以被访问,但是请把我视为私有变量,不要直接访问我"

双下划线：__foo:双下划线的表示的是私有类型(private)的变量，只能允许这个类的本身进行访问。
'''

```


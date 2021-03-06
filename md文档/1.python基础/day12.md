#### 继承

##### 概念

> 如果两个或者两个以上的类具有相同的属性和方法,我们可以抽取一个类出来。
>
> 在抽取的类中声明公共的部分
>
> 	被抽取出来的类 ——父类  超类  基类
>		
> 	其他类   — 子类  派生类
>		
> 	他们之间的关系 ——子类  继承自父类
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

当然，也可以对子类增加一些方法，比如Dog类：

```python
class Dog(Animal):    
    def eat(self):
        print("Eating meat....")
```

> 现在，有一个学生类和老师类，同时继承于人类
>
> 人类的特征：name ，age，money

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

> 学生类

```python
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

总结:

object是一切类的基类，也可以省略不写。

继承的特点:

a. 子类对象可以直接访问父类中未私有的属性

b. 子类对象可以调用父类中的方法

c. 父类对象不能访问子类中特有的属性或者方法

优点:

1.可以简化代码,减少冗余

2.提高代码的维护性

3.提高了代码的安全性

缺点:

耦合和内聚被用来描述类与类之间的关系,耦合性越低,内聚性越高,说明代码越好,

但是,在继承关系中,耦合性相对比较高,如果修改父类,子类也会随着变化

#### 多继承

> 顾名思义:就是一个子类中可以有多个父类,比如一个孩子有一个爸爸一个妈妈

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

#### 多态--鸭子模型【依赖于继承】

python中不存在多态，【python动态语言】

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

> 当子类与父类都存在相同的run()方法的时候，子类中的run()覆盖了父类中的run(),在代码运行的时候，总会调用子类中的run().
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

**获取对象属性**

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

还可以判断一个变量是否是某些类型中的一种，比如下面的代码：

```python
>>> isinstance([1,2,3],(list,tuple))
True
```

使用dir()函数可以获取一个对象的所有的属性和方法，它返回一个包含字符串的list

```python
>>> dir(a)
```

#### 函数的重写

系统函数

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

#### 运算符重载

类可以重载加减运算，打印，函数调用，索引等内置运算，运算符重载使我们的对象的行为与内置函数一样，在python调用时操作符会自动的作用于类的对象，python会自动的搜索并调用对象中指定的方法完成操作。

常见的运算符重载方法：


![TIM截图20190510152452](F:\千峰笔记\md文件\TIM截图20190510152452.png)

```python
#举例
#数字和字符串都能相加
print(1 + 2)
print("1" + "2")
#不同的类型用加法会有不同的解释

class Person(object):
    def __init__(self, num):
        self.num = num
     #运算符重载   
    def __add__(self, other):
        return Person(self.num + other.num)
    
    #方法重写
    def __str__(self):
        return "num = " + str(self.num)
    
#如果两个对象相加会怎样?
#对象相加,编译器解释不了,所以就要用到运算符重载
per1 = Person(1)
per2 = Person(2)
print(per1 + per2)
#结果为地址:per1+per2 === per1.__add__(per2),如果想得到num和则重写str方法
#上述打印就等价于:print(per1.__add__(per2)),只不过add方法会自动调用
print(per1)
print(per2)       
```

#### 单例模式

```python
class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(
                Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self, status_number):
        self.status_number = status_number


```





http://user.ihuyi.com/nav/sms.html

#### 发送短信

> 前提:互亿无线账号[上海] 和163邮箱

```python
APIID:C96007594
APIKEY:63dddb423532e74c755637ff759042e2

# SMTP服务器
SMTPServer = "smtp.163.com"
# 发邮件的地址
sender = "zhangjiaojiao_vip@163.com"
```

登录成功之后,互亿无限==>验证码短信==>获取APIID和APIKEY

==>文档中心 ==> 短信验证码/短信通知API接口文档下载,获取到接口文档 ==> 打开文档demo下的python[注意:最好先用记事本打开,复制到pyCharm中]

对原代码的修改如下:

```python
#接口类型:互亿无限触发短信接口,支持发送验证码短信,订单通知短信等.
#账户注册:请通过该地址开通账户
http://sms.ihuyi.com/register.html
#注意事项:
#1.调用期间,请用默认的模板进行测试,默认模板详见接口文档
#2.请使用APIID(查看APIID请登录用户中心-->验证码短信-->产品总览-->APPID)及APIKEY来调用接口.
#3.该代码仅提供接入互亿无线短信接口参考使用,客户可以根据实际需要进行自行编写.
#!/user/local/bin/python
#_*_ coding:utf-8 _*_
import http.client
import urllib

host = "106.ihuiyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

#用户名是登录用户中心-->验证码短信 -->产品总览 -->APPID
account = "C96009595"
#密码 查看密码请登录用户中心 --> 验证码短信 --> 产品总览 -->APIKEY

password ="63dddb423532e74c755637ff759042e2"
def send_sms(text,mobile):
    params = urllib.parse.urlencode({'account':account,'password':password,'content':text,'mobile':mobile,'format':'json'})
    headers = {"Content-type":"application/x-www-form-urlencoded", "Accept":"text/plain"}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str
if __name__ == "__main__":
    moblie = "18388878901"
    text ="您的验证码是: 908078. 请不要把验证码泄露给其他人."
    print(send_sms(text, mobile))
```

740875
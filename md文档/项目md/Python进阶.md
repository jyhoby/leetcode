Python 进阶
===========


### 1. PEP8 编码规范

- 练习: 规范化这段代码

    ```python
    from django.conf import settings
    from user.models import *
    import sys, os
    mod=0xffffffff
    def foo  ( a , b = 123 ):
        c={ 'x' : 111 , 'y' : 222 }#定义一个字典
        d=[ 1 , 3,5 ]
        return a,b , c
    def bar(x):
        if x%2==0 : return True
    ```

- 为什么要有编码规范
    * 编码是给人看的还是给机器看的？
    * 美观是重点吗？
        1. 美观
        2. 可读性
        3. 可维护性
        4. 健壮性
    * 团队内最好的代码状态: 所有人写出的代码像一个人写出来的

- 代码编排:
    * 缩进 4 个空格, 禁止空格与 Tab 混用
    * 行长 80 字符: 防止单行逻辑过于复杂

- import
    * 不要使用 `from xxx import *`
    * 顺序
        1. 标准库
        2. 第三方库
        3. 自定义库
    * 单行不要 import 多个库
    * 模块内用不到的不要去 import

- 空格
    * `: ,` 后面跟一个空格, 前面无空格
    * 二元操作符前后各一个空格, 包括以下几类:
        1. 数学运算符: `+ - * / // = & | `
        2. 比较运算符: `== != > <  >= <= is not in`
        3. 逻辑运算符: `and or not`
        4. 位运算符: `& | ^ << >>`
    * 当 `=` 用于指示关键字参数或默认参数值时, 不要在其两侧使用空格

- 适当添加空行
    * 函数间: 顶级函数间空 2 行, 类的方法之间空 1 行
    * 函数内: 同一函数内的逻辑块之间, 空 1 行
    * 文件结尾: 留一个空行 (Unix 中 \n 是文件的结束符)

- 注释
    * **忌**: 逐行添加注释, 没有一个注释
    * 行尾注释: 单行逻辑过于复杂时添加
    * 块注释: 一段逻辑开始时添加
    * 引入外来算法或者配置时须在注释中添加源链接, 标明出处
    * 函数、类、模块尽可能添加 `docstring`

- 命名
    * 好的变量名要能做到“词能达意”
    * 除非在 lambda 函数中, 否则不要用 **单字母** 的变量名 (即使是 lambda 函数中的变量名也应该尽可能的有意义)
    * 包名、模块名、函数名、方法、普通变量名全部使用小写, 单词间用下划线连接
    * 类名、异常名使用 CapWords (首字母大写) 的方式, 异常名结尾加 `Error` 或 `Wraning` 后缀
    * 全局变量尽量使用大写, 一组同类型的全局变量要加上统一前缀, 单词用下划线连接
    * 函数名最好有动词, 最好是 do_something 的句式, 或者 somebody_do_something 句式

- 语意明确、直白
    * `not xx in yy` *VS* `xx not in yy`
    * `not a is b` *VS* `a is not b`

- 程序的构建
    * 函数是模块化思想的体现
    * 独立的逻辑应该抽离成独立函数，让代码结构更清晰，**可复用度**更高
    * **一个函数只做一件事情, 并把这件事做好**
    * **大的功能用小函数之间灵活组合来完成**
    * 避免编写庞大的程序, **“大” 意味着体积庞大, 逻辑复杂甚至混乱**

- 自定义的变量名、函数名、文件名不要与标准库中的名字冲突

- pip install pycodestyle pylint flake8 autopep8


### 2. * 和 ** 的用法

- 函数定义时接收不定长参数

    ```python
    def foo(*args, **kwargs):
        pass
    ```

- 参数传递

    ```python
    def foo(x, y, z, a, b):
        print(x)
        print(y)
        print(z)
        print(a)
        print(b)
    lst = [1, 2, 3]
    dic = {'a': 22, 'b': 77}
    foo(*lst, **dic)
    ```

- 注意：不建议创建函数时，参数用*args，**kwargs表示

- import * 语法

    - 文件 xyz.py

        ```python
        __all__ = ('a', 'e', '_d')

        a = 123
        _b = 456
        c = 'asdfghjkl'
        _d = [1,2,3,4,5,6]
        e = (9,8,7,6,5,4)
        ```

    - 文件 abc.py

        ```python
        from xyz import *
        print(a)
        print(_b)
        print(c)
        print(_d)
        print(e)
        ```


### 3. Python 的赋值和引用
- `==, is`: `==` 判断的是值, `is` 判断的是内存地址 (即对象的id)
- 小整数对象: [-5, 256], id相同
- 包括字母、数字、下划线的字符串，id相同.  用到了字符串的intern机制
- 可变变量：可以修改的变量
    - list
    - dict
    - set

- 不可变变量：不可以修改的变量
  - 整型
  - 字符串
  - 浮点型
  - 元组

- 练习1: 说出执行结果

    ```python
def extendList(value, lst=[]):
        lst.append(value)
        return lst
    
    list1 = extendList(10)
list2 = extendList(123, [])
    list3 = extendList('a')
    ```
    
- `copy, deepcopy` 的区别

    * `copy`: 只拷贝表层元素
    * `deepcopy`: 在内存中重新创建所有子元素
    
- 练习2: 说出下面执行结果

    ```python
    from copy import copy, deepcopy
    
    a = ['x', 'y', 'z']
    b = [a] * 3
    c = copy(b)
    d = deepcopy(b)
    
    b[1].append(999)
    b.append(777)
    c[1].append(999)
    c.append(555)
    d[1].append(999)
    d.append(333)
    ```

### 4. 迭代器, 生成器

- 可迭代对象：能作用于for循环的对象就是可迭代对象

  - list
  - dict
  - string
  - tuple
  - set
  - 生成器

- 迭代器: 任何实现了 `__iter__` 和 `__next__` 方法的对象都是迭代器，迭代器是需要手动取实现的

  - 注意：可迭代对象不是迭代器

  - 生成器是迭代器

  - 迭代器不是生成器

  - 自定义生成器

    ```python
    class Range():
    
        def __init__(self, num):
            self.num = num
            self.current = 0
    
        # 返回自身的对象
        def __iter__(self):
            return self
    
        def __next__(self):
    
            c = self.current
    
            if c < self.num:
                self.current += 1
                return c
            else:
                raise StopIteration()
    ```

  - 作业：自定义Range生成器，实现内置的range功能 ： range(start, end, step)

- 生成器: 生成器是一种特殊的迭代器, 不需要自定义 `__iter__` 和 `__next__`
  - 生成器函数 (yield)
  
    ```python
    # 函数里面如果有yield关键之，就是一个生成器
    # 生成器是不可以直接执行的
    def foo():
        print(111)
        yield 222
        print(333)
        yield 444
        print(555)
        
    f = foo()
    next(f) # 执行生成器是用next()
    next(f) 
    
    # 如果执行到以后，后抛出StopIteration()的错误
    ```
  
    
  
  - 生成器表达式
  
    ```python
    a = (i for i in range(10))
    ```
  
    
  
- 迭代器的特点：
  
  - 使用`__sizeof__`可以查看对象所占用的内存，迭代器会占用很少的内存
  - `__iter__` 得到一个迭代器。迭代器的`__iter__()`返回自身
  - `__next__` 返回迭代器下一个值
- 如果容器中没有更多元素, 则抛出 `StopIteration` 异常
  
  - Python2中没有 `__next__()`, 而是 `next()`
  
- str / list / tuple / dict / set` 自身不是迭代器，他们自身不具备 `__next__()`, 但是具有 `__iter__()`, `__iter__() 方法用来把自身转换成一个迭代器

  

- 练习1:自定义range的迭代器

```python
class Range:
    def __init__(self, start, end=None, step=1):
        if end is None:
            self.end = start
            self.start = 0
        else:
            self.start = start
            self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            current = self.start
            self.start += self.step
            return current
        else:
            raise StopIteration()
```

- 练习2: 自定义一个迭代器, 实现斐波那契数列

- 练习3: 自定义一个生成器函数, 实现斐波那契数列

- 迭代器、生成器有什么好处？
    * 节省内存
    * 惰性求值 


### 5. 装饰器
- 最简装饰器

    ```python
    def deco(func):
        def wrap(*args, **kwargs):
            return func(*args, **kwargs)
        return wrap

    @deco  # 语法糖
    def foo(a, b):
        return a ** b
    ```

​			

- 还原被装饰器修改的属性

  - 对比被装饰前后的 `foo.__name__` 和 `foo.__doc__`

    ```python
    from functools import wraps
    
    def deco(func):
        '''i am deco'''
        @wraps(func)  # 还原被装饰器修改的原函数属性
        def wrap(*args, **kwargs):
            '''i am wrap'''
            return func(*args, **kwargs)
        return wrap
    ```

    

- 原理
    * 简单过程

        ```python
        fn = deco(func)
    foo = fn
        foo(*args, **kwargs)
        ```
    
* 多个装饰器叠加调用的过程

    ```python
    @deco1
    @deco2
    @deco3
    def foo(x, y):
        return x ** y

    # 过程拆解
    fn3 = deco3(foo)
    fn2 = deco2(fn3)
    fn1 = deco1(fn2)
    foo = fn1
    foo(3, 4)
    ```
- 带参数的装饰器

  ```python
  def deco(n):
      def wrap1(func):
          def wrap2(*args, **kwargs):
              return func(*args, **kwargs)
          return wrap2
      return wrap1
  
  
  # 调用过程
  wrap1 = deco(n)
  wrap2 = wrap1(foo)
  foo = wrap2
  foo()
  ```

  

- 装饰器类和 `__call__`

    - 不带参数

    ```python
    class Deco:
        def __init__(self, func):
            self.func = func
    
        def __call__(self, *args, **kwargs):
            return self.func(*args, **kwargs)
    
    @Deco
    def foo(x, y):
        return x ** y
    
    # 过程拆解
    fn = Deco(foo)
    foo = fn
    foo(12, 34)
    ```

    - 带参数

      ```python
      class Deco:
          def __init__(self, params):
              self.params = params
      
          def __call__(self, func):
            	self.func = func
              return self.wrap
           
          def wrap(self, *args, **kwargs):
              return self.func(*args, **kwargs)
      
      @Deco(10)
      def foo(x, y):
          return x ** y
      
      # 过程拆解
      fn = Deco(10)
      foo = fn(foo)
      foo(12, 34)
      ```



- 练习: 写一个 timer 装饰器, 计算出被装饰函数调用一次花多长时间, 并把时间打印出来

    ```python
    import time
    from functools import wraps

    def timer(func):
        @wraps(func)  # 修正属性
        def wrap(*args, **kwargs):
            time0 = time.time()
            result = func(*args, **kwargs)
            time1 = time.time()
            print(time1 - time0)
            return result
        return wrap
    ```


### 6. 函数闭包
- 三个条件

    - 外层函数中包含一个内层函数
    - 内层函数使用了外层函数中定义的对象
    - 外层函数返回内层函数名

- 说出下面函数返回值

    ```python
    def foo():
        l = []
        def bar(i):
            l.append(i)
            return l
        return bar

    f1 = foo()
    # 说出下列语句执行结果
f1(1)
    f1(2)
    f1(3)
    ```
    
- 作用域

    ```python
    a = 10
    
    def foo1():
        print(a)
    	
    def foo2():
        a = 20
        print(a)
    
    print(a)
    
    def foo3():
        a = a + 5
        print(5)
    ```

​    

* 声明全局变量: `global`

  ```python
  a = 10
  def foo():
    	global a
      a = a + 10
      print(a)
  ```


​      
​    
* 声明非本层的 **局部变量** : `nonlocal`

  ```python
  def foo():
      a = 20
      def inner():
          nonlocal a
          a = a + 20
          print(a)
      inner()
  ```


​      


### 7. 类方法和静态方法
- `method`

    - 通过实例调用
    - 可以引用类内部的**任何属性和方法**

- `classmethod`

    - 无需实例化
    - 可以调用类属性和类方法
    - 无法取到普通的成员属性和方法

- `staticmethod`

    - 无需实例化
    - **无法**取到类内部的任何属性和方法, 完全独立的一个方法

- 练习: 说出下面代码的运行结果

    ```python
    class Test(object):
        x = 123

        def __init__(self):
            self.y = 456

        def bar1(self):
            print('i am a method')

        @classmethod
        def bar2(cls):
            print('i am a classmethod')

        @staticmethod
        def bar3():
            print('i am a staticmethod')

        def foo1(self):
            print(self.x)
            print(self.y)
            self.bar1()
            self.bar2()
            self.bar3()

        @classmethod
        def foo2(cls):
            print(cls.x)
            print(cls.y)
            cls.bar1()
            cls.bar2()
            cls.bar3()

        @staticmethod
        def foo3(obj):
            print(obj.x)
            print(obj.y)
            obj.bar1()
            obj.bar2()
            obj.bar3()

    t = Test()
    t.foo1()
    t.foo2()
    t.foo3()
    ```

### 8. 继承相关问题
- 菱形继承
  
    ```python
class A:
        def run(self):
            print('---A---')
    
    class B(A):
        def run(self):
            print('---B---')
    
    class C(A):
        def run(self):
        print('---C---')
    
    class D(B, C):
        pass
    
    d = D()
    d.run()
    ```
    
    * 菱形继承问题
    
        ```
        继承关系示意
        菱形继承
             A
           /   \
          B     C
           \   /
             D
        ```
    
    - python2版本菱形继承是按深度继承的顺序
- python3版本菱形继承是按广度继承的顺序
  
  * 方法和属性的继承顺序: `Cls.mro()` 或者 `Cls.__mro__`
  * super在菱形继承不是表示父类，而是mro列表的上移级
  
- Mixin: 

    ```python
    class A:
        def run(self):
            print('---A---')
    
    class B:
        def run(self):
            print('---B---')
    
    class C:
        def run(self):
            print('---C---')
    
    class D(A, B, C):
        pass
    
    d = D()
    d.run()
    ```

    - 所有被继承的类都是基类
    - 继承类 的顺序是从左向右继承的


### 9. 垃圾收集 (GC)

- Garbage Collection (GC)

- 引用计数
    * 优点: 简单、实时性高
    
    * ![image-20190825173617751](Python进阶.assets/image-20190825173617751.png)

    * 缺点: 消耗资源、循环引用
    
        ```python
    lst1 = [3, 4]           # lst1->ref_count 1
        lst2 = [8, 9]           # lst2->ref_count 1
        
        # lst1 -> [3, 4, lst2]
        lst1.append(lst2)       # lst2->ref_count 2
        
        # lst2 -> [8, 9, lst1]
        lst2.append(lst1)       # lst1->ref_count 2
        
        del lst1                # lst1->ref_count 1
        del lst2                # lst2->ref_count 1
        ```

- 标记-清除, 分代收集

    * 用来回收引用计数无法清除的内存


### 10. Python 魔术方法
1. `__str__` 格式化输出对象
2. `__init__` 和 `__new__`

    * `__new__` 创建一个实例，并返回类的实例
    * `__init__` 初始化实例，无返回值
    * `__new__` 是一个类方法

        + 单例模式
            ```python
            class A(object):
                '''单例模式'''
                obj = None
                def __new__(cls, *args, **kwargs):
                    if cls.obj is None:
                        cls.obj = object.__new__(cls)
                    return cls.obj
            ```

7. `__setattr__, __getattribute__, __getattr__, __dict__`

    * 内建函数：`setattr(), getattr(), hasattr()`

    * 常用来做属性监听

        ```python
        class User:
            '''TestClass'''
            def __init__(self):
                self.money = 10000
          
            def __setattr__(self, name, value):
                if name == 'money' and value < 0:
                    raise ValueError('money < 0')
                print('set %s to %s' % (name, value))
                object.__setattr__(self, name, value)
        
            def __getattribute__(self, name):
        				print('get %s' % name)
                return object.__getattribute__(self, name)
        
            def __getattr__(self, name):
        				print('not has %s' % name)
                return -1
        
        # 对比
a = A()
        a.money = -10
        ```

8. 槽: `__slots__`
    * 固定类所具有的属性
    * 实例不会分配 `__dict__`
    * 实例无法动态添加属性
    * 优化内存分配

        ```python
        class A:
            __slots__ = ('x', 'y')
        ```

### 11. Python 性能之困

- 编译型语言
  - c
  - c++
  - go
- 半编译型语言
  - java
- 解释型语言
  - python
  - php
  - javascript

1. 计算密集型
    * CPU 长时间满负荷运行, 如图像处理、大数据运算、科学运算等
    * 计算密集型: 用 C 语言或 Cython 补充

2. I/O 密集型
    * 网络 IO, 文件 IO, 设备 IO 等
    * Unix: 一切皆文件

3. 多任务处理
    * 进程、线程、协程调度的过程叫做上下文切换
    * 进程、线程、协程对比
* 进程之间的数据通信一般有三种方式：Pipe Queue Manager
    * 进程和线程的切换是由操作系统来完成
    * 协程的切换是程序员手动完成
    
     名称 | 资源占用 |           数据通信            | 上下文切换 (Context)
    -----|---------|------------------------------|------------------
 进程 |    大   | 不方便 (网络、共享内存、管道等) | 操作系统按时间片切换, 不够灵活, 慢
     线程 |    小   |           非常方便            | 按时间片切换, 不够灵活, 快
     协程 |  非常小 |           非常方便            | 根据I/O事件切换, 更加有效的利用 CPU
    
4. 全局解释器锁 ( GIL )
    * 它确保任何时候一个进程中都只有一个 Python 线程能进入 CPU 执行。
    * 全局解释器锁造成单个进程无法使用多个 CPU 核心
    * 通过多进程来利用多个 CPU 核心，一般进程数与CPU核心数相等，或者CPU核心数两倍
    
      ![image-20190825231228219](Python进阶.assets/image-20190825231228219.png)
6. 协程： gevent / tornado (yield) / asyncio

    - yield实现协程的原理


### 12. 一些技巧和误区

1. 确保能取到有效值 (默认值)
    * `d.get(k, default)`  无值时使用默认值，对原字典无修改
    * `d.setdefault` 无值时使用默认值，并将默认值写入原字典
    * `getattr(a, 'x', 0)`
    * `x = a if foo() else b`
    * `a or b`

2. try...except... 的滥用
    * 不要把所有东西全都包住, 程序错误需要报出来
    * 使用 `try...except` 要指明具体错误, `try` 结构不是用来隐藏错误的, 而是用来有方向的处理错误的

3. 利用 dict 做模式匹配

    ```python
    def do1():
        print('i am do1')

    def do2():
        print('i am do2')

    def do3():
        print('i am do3')

    def do4():
        print('i am do4')

    mapping = {1: do1, 2: do2, 3: do3, 4: do4}
    mod = random.randint(1, 10)
    func = mapping.get(mod, do4)
    func()
    ```

4. 不要用浮点数做条件判断

    ```python
    a = 0.7
    b = 0.3
    c = 0.4
    
    a - b == c
    ```

    - 浮点数都不是精确的，不要用浮点数做判断

5. property: 把一个方法属性化

    ```python
    class C(object):
        @property
        def x(self):
            "I am the 'x' property."
            return self._x
    ```

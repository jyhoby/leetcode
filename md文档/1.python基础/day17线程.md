#### 线程与协程

一、概念

　　1、进程

> 进程是系统进行资源分配和调度的一个独立单位

进程是具有一定独立功能的程序关于某个数据集合上的一次运行活动,进程是系统进行资源分配和调度的一个独立单位。每个进程都有自己的独立内存空间，不同进程通过进程间通信来通信。由于进程比较重量，占据独立的内存，所以上下文进程间的切换开销（栈、寄存器、虚拟内存、文件句柄等）比较大，但相对比较稳定安全。

　　2、线程

> CPU调度和分派的基本单位

线程是进程的一个实体,是CPU调度和分派的基本单位,它是比进程更小的能独立运行的基本单位.线程自己基本上不拥有系统资源,只拥有一点在运行中必不可少的资源(如程序计数器,一组寄存器和栈),但是它可与同属一个进程的其他的线程共享进程所拥有的全部资源。线程间通信主要通过共享内存，上下文切换很快，资源开销较少，但相比进程不够稳定容易丢失数据。

　　3、协程

**协程是一种用户态的轻量级线程，**协程的调度完全由用户控制。协程拥有自己的寄存器上下文和栈。协程调度切换时，将寄存器上下文和栈保存到其他地方，在切回来的时候，恢复先前保存的寄存器上下文和栈，直接操作栈则基本没有内核切换的开销，可以不加锁的访问全局变量，所以上下文的切换非常快。

https://blog.csdn.net/weixin_41254254/article/details/80841806 

####GIL不是Python特性

GIL是Python解释器（Cpython）时引入的概念，在JPython、PyPy中没有GIL。GIL并不是Python的语言缺陷。

####GIL定义

GIL，the Global Interpreter Lock，直译为“全局解释锁”

####GIL存在原因

CPython在执行多线程的时候并不是线程安全的，为了线程间数据的一致性和状态同步的完整性。

####GIL的弊端

- GIL对计算密集型的程序会产生影响。因为计算密集型的程序，需要占用系统资源。GIL的存在，相当于始终在进行单线程运算，这样自然就慢了。

- IO密集型影响不大的原因在于，IO，input/output，这两个词就表明程序的瓶颈在于输入所耗费的时间，线程大部分时间在等待，所以它们是多个一起等（多线程）还是单个等（单线程）无所谓的。

  这就好比，你在公交站等公交时，你们排队等公交（单线程）还是沿着马路一字排开等（多线程）是无所谓的。公交车（即input，即输入的资源）没来，哪种方式都是瞎折腾。

#### 如何解决

```
1、重写python编译器(官方cpython)如使用：PyPy解释器
2、调用C语言的链接库
```

#### 异步

不按照顺序执行，并行执行。

ps：可以理解为在不同的线程执行

串行：类似于同步

并行：类似于异步执行【执行任务的数量小于或者等于cpu的数量】

并发：任务的数量大于cpu的数量

#### 同步：

按顺序执行代码

ps：可以理解成在同一个线程中执行

#### 线程

##### 1.线程的创建【使用此方式创建的线程为守护线程】

```python
import _thread
import threading

def fn1(a,b):
    print(a,b)
    print(threading.current_thread().name)

def create_thread1():
    #参数一：在子线程中要执行的函数
    #参数二：子线程中的函数需要的参数，注意一定要以元组的形式传参
    #使用此种方式创建的线程为守护线程，守护线程的特点是，当主线程结束，守护线程无论执行完毕都会结束
    _thread.start_new_thread(fn1,("hello","yes"))
    
if __name__ == "__main__":
    create_thread1()
	print(threading.current_thread().name)
    #注意此时创建的线程中的代码不会执行，原因是
    #主线程执行的速度非常快，主线程执行结束，就直接退出了，因此我们的子线程根本不会被创建
    #我们可以让主线程阻塞一段时间可以查看一下效果
    #time.sleep(3)  #这时候我们就可以查看打印的数据了
```

守护线程：子线程会随着主线程的结束而结束。

##### 线程创建的方式二

```python
import threading

def func1(*args):
    print(args)
	print(threading.current_thread().name)

def create_thread2():
    #target:在子线程中要执行的函数
    #deamo：是否为守护线程
    #name:线程名称
    t=threading.Thread(target=func1,deamo=False,name="BIG",args=("hello"))
    t.start() #启动线程
	

if __name__ == "__main__":
	create_thread2()

```

##### 创建线程方式三

```python
import threading

class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()
     
    #一定要重写此方法，此方法会自动被调用
    #里面的子线程
    def run(self):
        print("mythread",threading.current_thread().name)

def create_thread3():
    t = MyThread()
    t.start()
    
if __name__ == "__main__":
    create_thread3()
```

**注意**一般情况下使用第二种创建方式比较常用

```python
Thread(group=None, target=None, name=None, args=(), kwargs={}) 
　　group: 线程组，目前还没有实现，库引用中提示必须是None； 
　　target: 要执行的方法； 
　　name: 线程名； 
　　args/kwargs: 要传入方法的参数。

```

```python
实例方法： 
　　isAlive(): 返回线程是否在运行。正在运行指启动后、终止前。 
　　get/setName(name): 获取/设置线程名。 
　　start():  线程准备就绪，等待CPU调度
　　is/setDaemon(bool): 获取/设置是后台线程（默认前台线程（False））。（在start之前设置）

　　　　#如果是后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，主线程和后台线程均停止
       　　#如果是前台线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程也执行完成后，程序停止 
　　join([timeout]): 阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout（可选参数）。
```

#### 多线程

>一个进程运行时产生了多个线程。

```python
import threading,time,random

def fun(*args):
    time.sleep(random.randint(1,4))
    print("子线程",args)
 

if __name__ == "__main__":
    #多个线程同时运行，是异步执行
    t1 = threading.Thread(target=fn,args=("包饺子",))
    t1.start()
    # t1.join()  会阻塞 等待t1线程执行完成后再继续往后执行
     t2 = threading.Thread(target=fn,args=("甜馨",))
    t2.start()
    t3 = threading.Thread(target=fn,args=("嗯哼",))
    t3.start()
    #若多个线程想让其按顺序执行，则可以使用join() 的方法
```

> 循环创建线程

```python
import threading,time,random

def fun(*args):
    time.sleep(random.randint(1,4))
    print("子线程",args)
 

if __name__ == "__main__":
    start = time.time()
    t_list= []
    for x in range(10):
        t1 = threading.Thread(target=fn,args=(x,))
        t1.start()
        t_list.append(t1)
        #当前线程的名称
        print(threading.current_thread().name)
        #线程id
        print(t.ident)
        #线程是否正在执行
        print(t.is_alive())
    #正在运行线程的数量，包括主线程
    print(threading.active_count())
    #列举当前正在运行的所有的线程
    print(threading.enumerate())
    for t in t_list:
        t.join()
    
    print(time.time()-start)
    
```

##### 线程冲突

> 多个线程并发访问同一个变量而相互干扰
>
> 解决方式：线程锁

> 银行存钱问题，买卖包子问题

```python
import threading

def fn():
    global num
    #cpu分配的时间片不足以完成一百万次加法运算
    #因此结果还没有被保存到内存中就可能被其他的线程打断
    for x in range(1000000):
        num += 1

def thread1():
    for i in range(5):
        t = threading.Thread(target=fn)
        t.start()

```

> 解决多线程的冲突问题方式一：
>
> lock = threading.Lock()
>
> 使用 with lock
>
> with内部实现了__enter__()和__exit__()执行语句之前调用enter方法,退出的时候调用exit

```python
import threading

#解决线程冲突问题
#线程锁
lock = threading.Lock()

def fn():
    with lock: #会自动加锁，执行完毕之后才会释放锁
        global num
        #cpu分配的时间片不足以完成一百万次加法运算
        #因此结果还没有被保存到内存中就可能被其他的线程打断
        for x in range(1000000):
            num += 1
        print(num)

def thread1():
    for i in range(5):
        t = threading.Thread(target=fn)
        t.start()

if __name__ == '__main__':
    num = 0
    thread1()
```

> 解决多线程冲突问题，方式二
>
> lock = threading.Lock()
>
> lock.acquire() #锁定
>
> lock.release() #释放锁

```python
import threading

#解决线程冲突问题
#线程锁，创建锁
lock = threading.Lock()

def fn():
    lock.acquire() #锁定
    global num
    #cpu分配的时间片不足以完成一百万次加法运算
    #因此结果还没有被保存到内存中就可能被其他的线程打断
    for x in range(1000000):
        num += 1
    print(num)
    lock.release() #释放锁

def thread1():
    for i in range(5):
        t = threading.Thread(target=fn)
        t.start()

if __name__ == '__main__':
    num = 0
    thread1()
```

作业：售票问题。

#### 死锁

定义：是指一个资源多次调用，而多次调用方都未能释放该资源就会造成一种互相等待的现象，若无外力作用，它们都将无法推进下去，此时称系统处于死锁状态或者系统产生了死锁。

> 若存在两个线程：线程A 与线程B
>
> 若线程A与线程B都 需要资源1与资源2才能执行
>
> 现在线程A拿到了资源1，线程B拿到了资源2，此时就构成了死锁。

若要解决死锁的问题，则此时我们需要使用递归锁。

> 下面以一个关于线程死锁的经典问题：“哲学家就餐问题”，作为本节最后一个例子。题目是这样的：五位哲学家围坐在一张桌子前，每个人 面前有一碗饭和一只筷子。在这里每个哲学家可以看做是一个独立的线程，而每只筷子可以看做是一个锁。每个哲学家可以处在静坐、 思考、吃饭三种状态中的一个。需要注意的是，每个哲学家吃饭是需要两只筷子的，这样问题就来了：如果每个哲学家都拿起自己左边的筷子， 那么他们五个都只能拿着一只筷子坐在那儿，直到饿死。此时他们就进入了死锁状态。 下面是一个简单的使用死锁避免机制解决“哲学家就餐问题”的实现：

```python
import threading,time

class ZheXueJia():
    def __init__(self,left,right):
        self.left = left
        self.right = right

def run(z,name):
    #获取左筷子
    f = z.left.acquire()
    if f:
        print(name,"获取左筷子...")
    #获取右筷子
    ff = z.right.acquire()
    if ff:
        print(name,"获取右筷子...")
        print("哲学家开始就餐",name)
        time.sleep(1)
        print("就餐完毕",name)
    #释放右筷子
    z.right.release()
    #释放左筷子
    z.left.release()


if __name__ == '__main__':
    #每个筷子相当于一把锁
    rlock1 = threading.RLock()
    rlock2 = threading.RLock()
    rlock3 = threading.RLock()
    rlock4 = threading.RLock()
    rlock5 = threading.RLock()
    #必须同时拥有两把锁才能就餐
    z1 = ZheXueJia(rlock5, rlock1)
    z2 = ZheXueJia(rlock1, rlock2)
    z3 = ZheXueJia(rlock2, rlock3)
    z4 = ZheXueJia(rlock3, rlock4)
    z5 = ZheXueJia(rlock4, rlock5)
    #创建五个线程模仿哲学家
    t1 = threading.Thread(target=run,args=(z1,"z1"))
    t2 = threading.Thread(target=run,args=(z2,"z2"))
    t3 = threading.Thread(target=run,args=(z3,"z3"))
    t4 = threading.Thread(target=run,args=(z4,"z4"))
    t5 = threading.Thread(target=run,args=(z5,"z5"))
    #开启线程
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
```

或者使用递归锁来解决

```python
# 解决方案：将所有锁改编成递归锁RLock
# 在Python中为了支持在同一线程中多次请求同一资源，python提供了可重入锁RLock。
# 这个RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，从而使得资源可以被多次require。
# 直到一个线程所有的acquire都被release，其他的线程才能获得资源。上面的例子如果使用RLock代替Lock，则不会发生死锁。
```

```python
import threading
import time

# mutexA = threading.Lock() #资源A
# mutexB = threading.Lock()#资源B
RLock = threading.RLock()


class MyThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    # 当对象调用start的时候会自动执行此方法
    def run(self):
        self.fun1()
        self.fun2()

    def fun1(self):
        RLock.acquire()  # 如果锁被占用,则阻塞在这里,等待锁的释放
        # 获取资源A
        print("I am %s , get res: %s" % (self.name, "ResA"))

        RLock.acquire()
        print("I am %s , get res: %s" % (self.name, "ResB"))
        RLock.release()

        RLock.release()

    def fun2(self):
        RLock.acquire()
        print("I am %s , get res: %s" % (self.name, "ResB"))
        time.sleep(0.2)

        RLock.acquire()
        print("I am %s , get res: %s" % (self.name, "ResA"))
        RLock.release()
        RLock.release()

if __name__ == "__main__":
    for i in range(0, 10):
        my_thread = MyThread()
        my_thread.start()
```

#### 信号量

> **semaphore**是一个内置的计数器
>
> 限制同一时间执行的线程的个数

```python
#每当调用acquire()时，内置计数器-1
#每当调用release()时，内置计数器+1
```

计数器不能小于**0**，当计数器为**0**时，**acquire()**将阻塞线程直到其他线程调用**release()**。 来看下面的代码：

```python
import time
import threading

def foo():
    time.sleep(2)   #程序休息2秒
    print("ok",time.ctime())

for i in range(200):
    t1=threading.Thread(target=foo,args=()) #实例化一个线程
    t1.start()  #启动线程
```

程序会在很短的时间内生成200个线程来打印一句话。

如果在主机执行**IO密集型任务**的时候再执行这种类型的程序时，计算机就有很大可能会宕机。这时候就可以为这段程序添加一个计数器功能，来限制一个时间点内的线程数量。

> 宕机，指操作系统无法从一个严重系统错误中恢复过来，或系统硬件层面出问题，以致系统长时间无响应，而不得不重新启动计算机的现象。它属于电脑运作的一种正常现象，任何电脑都会出现这种情况。

```python
import time
import threading

s1=threading.Semaphore(5)   #添加一个计数器

def foo():
    s1.acquire()    #计数器获得锁
    time.sleep(2)   #程序休眠2秒
    print("ok",time.ctime())
    s1.release()    #计数器释放锁


for i in range(20):
    t1=threading.Thread(target=foo,args=()) #创建线程
    t1.start()  #启动线程   
```

或者使用此方法

```python
import time
import threading

sem=threading.Semaphore(5)   #添加一个计数器

def foo():
    with sem:
        time.sleep(2)   #程序休眠2秒
        print("ok",time.ctime())

for i in range(20):
    t1=threading.Thread(target=foo,args=()) #创建线程
    t1.start()  #启动线程
```


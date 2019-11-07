#### 协程

协程，又称微线程，纤程。

> 协程其实可以认为是比线程更小的执行单元，为啥说他是一个执行单元，因为他自带cpu上下文，这样只要在合适的时机，我们可以把一个协程切换到另一个协程，只要这个过程中保存或者恢复cpu上下文，那么这个程序还是可以运行的。

通俗的理解：在一个线程中的某个函数，可以在任何地方保存当前函数的一些临时变量等信息，然后切换到另一个函数中执行，注意不是通过调用函数的方式做到的，并且切换的次数以及什么时候再切换到原来的函数中都是由开发者自己确定的。

#### 协程与线程的差异

```python
协程的特点在一个线程内部执行，与多线程相比，协程有什么优点？
1.最大的优势就是协程有极高的执行效率，因为子程序切换不是线程切换而是程序自身控制，因此，没有线程切换的开销，和多线程比，线程的数量越多，协程的性能就会越明显
2.第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。
因为协程是一个线程执行，那么怎么利用多核cpu呢？
最简单的方式就是多进程+协程，既充分利用多核，又能充分发挥协程的高效性，可获得极高的性能。

协程的缺点：
它不能同时将cpu的多核用上，只能使用一个核
python对协程的支持是通过generator实现的
在generator中，我们不但能够通过for循环作用，我们还可以不断调用next()函数，获取由yield语句返回的下一个值
```

yield关键字的作用：

> 能过多次进入、多次返回，能够暂停函数体中代码的执行

　　在python的函数（function）定义中，只要出现了yield表达式（Yield expression），那么事实上定义的是一个*generator function*， 调用这个generator function返回值是一个generator

```python

def func():
    yield 1
    yield 2

if __name__ == '__main__':
    g = func()
    print(next(g))
    print(next(g))
    print(next(g)) #报错StopIteration
```

**需求：**使用yield生成斐波那契数列

#### 协程简单的实现

> 协程的实现原理【与yield的方式类似】

```python
import time

def func():
    while True:
        print("====func===")
        yield
        time.sleep(1)

def func2(func):
    while True:
        print("====func2====")
        next(func)
        time.sleep(1)

if __name__ == '__main__':
    #返回了一个生成器对象
    f = func()
    func2(f)
```

##### 使用greenlet来实现协程

```python
from greenlet import greenlet
import time


def  fun1():
    print("协程1...")
    time.sleep(3)
    g2.switch() #切换到协程g2
    print("节日快乐。。。")


def fun2():
    print("协程2...")
    time.sleep(3)
    g1.switch() #切换到协程g1


if __name__ == '__main__':
    g1 = greenlet(fun1)
    g2 = greenlet(fun2)
    g1.switch() #切换到协程1

```

##### 使用gevent实现

```python
'''
使用gevent +　sleep自动将CPU执行权分配给当前未睡眠的协程
'''
import gevent


def func1():
    gevent.sleep(1)
    print("人到中年不得已，保温杯里泡枸杞")
    gevent.sleep(13)
    print("1:over")

def func2():
    gevent.sleep(3)
    print("枸杞难挡岁月催，还得往里加当归")
    gevent.sleep(9)
    print("2:over")

def func3():
    gevent.sleep(5)
    print("当归难挡岁月刀，人参鹿茸泡小烧")
    gevent.sleep(5)
    print("3:over")

def func4():
    gevent.sleep(7)
    print("人参鹿茸不管饱，还得腰子加肾宝")
    gevent.sleep(1)
    print("4:over")


def simpleGevent():
    gr1 = gevent.spawn(func1)
    gr2 = gevent.spawn(func2)
    gr3 = gevent.spawn(func3)
    gr4 = gevent.spawn(func4)
    gevent.joinall([gr1, gr2, gr3, gr4])

if __name__ == '__main__':
    simpleGevent()
```

##### 使用gevent与monkey实现协程

```python
from gevent import monkey;monkey.patch_all()#导入猴子补丁#可以实现协程的自动切换
import requests
import gevent
import threading
import time

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}

def get_data(url):
    print("协程",url)
    response = requests.get(url,headers=headers)
    print(url,"response",response.text)
    time.sleep(3)


if __name__ == '__main__':
    #协程爬取数据
    t1 = time.time()
    url_list = [
        'http://www.baidu.com',
        'http://www.qq.com',
        'http://www.ifeng.com',
        'http://www.sina.com.cn',
        'http://www.taobao.com',
    ]
    g_list = []
    for url in url_list:
        g = gevent.spawn(get_data,url)
        g_list.append(g)

    gevent.joinall(g_list)
    #3.4110121726989746
    #多线程爬取数据
    # t_list = []
    # for url in url_list:
    #     t = threading.Thread(target=get_data,args=(url,))
    #     t.start()
    #     t_list.append(t)
    # for t in t_list:
    #     t.join()
    print(time.time()-t1)
    #4.9332239627838135
```

> 协程爬取链家

```python
import gevent
from gevent import monkey
monkey.patch_all()
import threading

import time
import requests

# 模拟浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}

def get_page(page):
    url = 'https://sz.lianjia.com/ershoufang/pg%d/' % page
    response = requests.get(url, headers=headers)
    print('第%d页' % page, len(response.text))
    # print('第%d页' % page)


if __name__ == '__main__':
    start = time.time()
    g_list=[]
    for i in range(1,200):
        g = gevent.spawn(get_page,i)
        g_list.append(g)
    #执行
    gevent.joinall(g_list)

    #6.445696830749512
    # t_list = []
    # for i in range(1,200):
    #     t = threading.Thread(target=get_page,args=(i,))
    #     t.start()
    #     t_list.append(t)
    #
    # for t in t_list:
    #     t.join()
    print(threading.current_thread().name)
    end = time.time()
    print(end-start)
    #5.983382940292358
```

#### 进程

> 进程是程序的一次性执行的过程，正在进行的一个过程或者任务，而负责执行任务的是cpu。

进程的生命周期：

当操作系统要完成某个任务的时候它会创建一个进程，当进程完成任务之后，系统就会撤销这个进程，收回它所占用的资源，从创建到撤销的时间段就是进程的生命周期。

进程之间存在并发：

在一个操作系统中，同时会存在多个进程，它们就轮流占用cpu资源。

并行与并发的区别：

无论并行还是并发，在用户看来其实都是同时运行的，不管是进程还是线程，都只是一个任务而已，真正干活的是cpu，而一个cpu（单核）同一时刻只能执行一个任务。

并行：多个任务同时运行，只有具备多个cpu才能真正的实现并行，含有几个cpu，也就意味着同一时间可以执行几个任务。

并发：是伪并行，看起来是同时运行的，实际上是单个cpu在多道程序之间的来回切换。

同步与异步的概念：

同步就是指一个进程在执某个请求的时候，若该请求需要一段时间才能返回信息，那么这个进程将会一直等待下去，直到返回信息才能继续执行下去。

异步：是指进程不需要一直等待下去，而是继续执行下面的操作，不管其他进程的状态，当有消息返回的时候，系统会通知进程来进行处理，这样可以提高执行效率。

比如：打电话的过程就是同步通讯，发短信就是异步通讯

多线程和多进程的关系：

对于计算机密集型应用，应该使用多进程

对于IO密集型应用，应该使用多线程，线程的创建比进程的创建开销小的多。

#### 创建进程

```python
import multiprocessing
import time
from time import sleep

def func(*args):
    sleep(3)
    print("子进程",multiprocessing.current_process().name)
    print(args)


if __name__ == '__main__':
    t = time.time()
    p_list = []
    for x in range(300):
        pro = multiprocessing.Process(target=func,args=("hello",))
        pro.start()
        p_list.append(pro)

    for p in p_list:
        p.join()
    print(time.time()-t)

```

##### 进程锁与信号量

```python
import multiprocessing
import time
import random



def func2(i,lock):
    with lock:
        print("加锁",i)
        time.sleep(1)
        print("释放锁",i)




#信号量，控制进程的最大并发数
def func(num,sem):
    with sem:
        print("子进程", num)
        time.sleep(time.time())
        print("结束",num)


if __name__ == '__main__':
    sem = multiprocessing.Semaphore(4)
    lock = multiprocessing.Lock()
    start = time.time()
    p_list = []
    for x in range(1,30):
        p = multiprocessing.Process(target=func2,args=(x,lock))
        p.start()
        p_list.append(p)
    for p in p_list:
        p.join()

    print(time.time()-start)

```

##### 多进程加协程分页爬取链家

```python
import gevent

import time
import requests
import re
import multiprocessing

# 模拟浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}

#获取所有的区与链接
def get_all_area():
    url = 'https://sz.lianjia.com/ershoufang/pg1/'
    response = requests.get(url,headers=headers)
    content = response.text
    pattern = '<div data-role="ershoufang" >(.*?)</div>'
    area_str = re.findall(pattern, content, re.S)[0]
    # print(area_str)

    url_pattern = 'href="(.*?)"'
    url_list = re.findall(url_pattern, area_str, re.S)
    # print(url_list)

    areaname_pattern = '<a(?:.*?)>(.*?)</a>'
    areaname_list = re.findall(areaname_pattern, area_str, re.S)
    # print(areaname_list)

    return url_list, areaname_list

#获取每一页的内容
def get_page(page,url,area):
    url ='%s/pg%d/'%(url,page)
    response = requests.get(url,headers=headers)
    print('{}:第{}页'.format(area,page))

#分区爬取数据使用协程
def get_area(url,area):
    g_list = []
    for i in range(1,101):
        g = gevent.spawn(get_page,i,url,area)
        g_list.append(g)
    gevent.joinall(g_list)

if __name__ == '__main__':
    #获取所有区
    url_list,area_list = get_all_area()
    t = time.time()
    p_list = []
    for i in range(len(url_list)):
        url = 'https://sz.lianjia.com' + url_list[i]
        area = area_list[i]
        p = multiprocessing.Process(target=get_area,args=(url,area))
        p.start()
        p_list.append(p)

    for p in p_list:
        p.join()

    e = time.time()
    print(t-e)
```


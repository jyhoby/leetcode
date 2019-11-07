## Tornado异步化

### 预备知识

#### 并发编程

所谓并发编程就是让程序中有多个部分能够并发或同时执行，并发编程带来的好处不言而喻，其中最为关键的两点是提升了执行效率和改善了用户体验。下面简单阐述一下Python中实现并发编程的三种方式：

1. 多线程：Python中通过`threading`模块的`Thread`类并辅以`Lock`、`Condition`、`Event`、`Semaphore`和`Barrier`等类来支持多线程编程。Python解释器通过GIL（全局解释器锁）来防止多个线程同时执行本地字节码，这个锁对于CPython（Python解释器的官方实现）是必须的，因为CPython的内存管理并不是线程安全的。因为GIL的存在，Python的多线程并不能利用CPU的多核特性。

2. 多进程：使用多进程可以有效的解决GIL的问题，Python中的`multiprocessing`模块提供了`Process`类来实现多进程，其他的辅助类跟`threading`模块中的类类似，由于进程间的内存是相互隔离的（操作系统对进程的保护），进程间通信（共享数据）必须使用管道、套接字等方式，这一点从编程的角度来讲是比较麻烦的，为此，Python的`multiprocessing`模块提供了一个名为`Queue`的类，它基于管道和锁机制提供了多个进程共享的队列。

   ```Python
   
   import multiprocessing
   import time
   
   
   def fun1(name):
       print(multiprocessing.current_process().name)
       time.sleep(5)
       print(name, '进程结束')
   
   
   if __name__ == '__main__':
       print('主进程开始', multiprocessing.current_process().name)
       p_list = []
       for i in range(5):
   
           p = multiprocessing.Process(target=fun1,args=['ccav %d' %i])
           p_list.append(p)
           p.start()
   
   
       print('主进程结束')
   ```

3. 异步编程（异步I/O）：所谓异步编程是通过调度程序从任务队列中挑选任务，调度程序以交叉的形式执行这些任务，我们并不能保证任务将以某种顺序去执行，因为执行顺序取决于队列中的一项任务是否愿意将CPU处理时间让位给另一项任务。异步编程通常通过多任务协作处理的方式来实现，由于执行时间和顺序的不确定，因此需要通过钩子函数（回调函数）或者`Future`对象来获取任务执行的结果。目前我们使用的Python 3通过`asyncio`模块以及`await`和`async`关键字（Python 3.5中引入，Python 3.7中正式成为关键字）提供了对异步I/O的支持。

   ```Python
   import asyncio
   
   
   async def fetch(host):
       """从指定的站点抓取信息(协程函数)"""
       print(f'Start fetching {host}\n')
       # 跟服务器建立连接
       reader, writer = await asyncio.open_connection(host, 80)
       # 构造请求行和请求头
       writer.write(b'GET / HTTP/1.1\r\n')
       writer.write(f'Host: {host}\r\n'.encode())
       writer.write(b'\r\n')
       # 清空缓存区(发送请求)
       await writer.drain()
       # 接收服务器的响应(读取响应行和响应头)
       line = await reader.readline()
       while line != b'\r\n':
           print(line.decode().rstrip())
           line = await reader.readline()
       print('\n')
       writer.close()
   
   
   def main():
       """主函数"""
       urls = ('www.sohu.com', 'www.douban.com', 'www.163.com')
       # 获取系统默认的事件循环
       loop = asyncio.get_event_loop()
       # 用生成式语法构造一个包含多个协程对象的列表
       tasks = [fetch(url) for url in urls]
       # 通过asyncio模块的wait函数将协程列表包装成Task（Future子类）并等待其执行完成
       # 通过事件循环的run_until_complete方法运行任务直到Future完成并返回它的结果
       loop.run_until_complete(asyncio.wait(tasks))
       loop.close()
   
   
   if __name__ == '__main__':
       main()
   ```

   > 说明：目前大多数网站都要求基于HTTPS通信，因此上面例子中的网络请求不一定能收到正常的响应，也就是说响应状态码不一定是200，有可能是3xx或者4xx。当然我们这里的重点不在于获得网站响应的内容，而是帮助大家理解`asyncio`模块以及`async`和`await`两个关键字的使用。

我们对三种方式的使用场景做一个简单的总结。

以下情况需要使用多线程：

1. 程序需要维护许多共享的状态（尤其是可变状态），Python中的列表、字典、集合都是线程安全的，所以使用线程而不是进程维护共享状态的代价相对较小。
2. 程序会花费大量时间在I/O操作上，没有太多并行计算的需求且不需占用太多的内存。

以下情况需要使用多进程：

1. 程序执行计算密集型任务（如：字节码操作、数据处理、科学计算）。
2. 程序的输入可以并行的分成块，并且可以将运算结果合并。
3. 程序在内存使用方面没有任何限制且不强依赖于I/O操作（如：读写文件、套接字等）。

最后，如果程序不需要真正的并发性或并行性，而是更多的依赖于异步处理和回调时，异步I/O就是一种很好的选择。另一方面，当程序中有大量的等待与休眠时，也应该考虑使用异步I/O。

> 扩展：关于进程，还需要做一些补充说明。首先，为了控制进程的执行，操作系统内核必须有能力挂起正在CPU上运行的进程，并恢复以前挂起的某个进程使之继续执行，这种行为被称为进程切换（也叫调度）。进程切换是比较耗费资源的操作，因为在进行切换时首先要保存当前进程的上下文（内核再次唤醒该进程时所需要的状态，包括：程序计数器、状态寄存器、数据栈等），然后还要恢复准备执行的进程的上下文。正在执行的进程由于期待的某些事件未发生，如请求系统资源失败、等待某个操作完成、新数据尚未到达等原因会主动由运行状态变为阻塞状态，当进程进入阻塞状态，是不占用CPU资源的。这些知识对于理解到底选择哪种方式进行并发编程也是很重要的。

#### I/O模式和事件驱动

对于一次I/O操作（以读操作为例），数据会先被拷贝到操作系统内核的缓冲区中，然后从操作系统内核的缓冲区拷贝到应用程序的缓冲区（这种方式称为标准I/O或缓存I/O，大多数文件系统的默认I/O都是这种方式），最后交给进程。所以说，当一个读操作发生时（写操作与之类似），它会经历两个阶段：(1)等待数据准备就绪；(2)将数据从内核拷贝到进程中。

由于存在这两个阶段，因此产生了以下几种I/O模式：

1. 阻塞 I/O（blocking I/O）：进程发起读操作，如果内核数据尚未就绪，进程会阻塞等待数据直到内核数据就绪并拷贝到进程的内存中。
2. 非阻塞 I/O（non-blocking I/O）：进程发起读操作，如果内核数据尚未就绪，进程不阻塞而是收到内核返回的错误信息，进程收到错误信息可以再次发起读操作，一旦内核数据准备就绪，就立即将数据拷贝到了用户内存中，然后返回。
3. 多路I/O复用（ I/O multiplexing）：监听多个I/O对象，当I/O对象有变化（数据就绪）的时候就通知用户进程。多路I/O复用的优势并不在于单个I/O操作能处理得更快，而是在于能处理更多的I/O操作。
4. 异步 I/O（asynchronous I/O）：进程发起读操作后就可以去做别的事情了，内核收到异步读操作后会立即返回，所以用户进程不阻塞，当内核数据准备就绪时，内核发送一个信号给用户进程，告诉它读操作完成了。

通常，我们编写一个处理用户请求的服务器程序时，有以下三种方式可供选择：

1. 每收到一个请求，创建一个新的进程，来处理该请求；
2. 每收到一个请求，创建一个新的线程，来处理该请求；
3. 每收到一个请求，放入一个事件列表，让主进程通过非阻塞I/O方式来处理请求

第1种方式实现比较简单，但由于创建进程开销比较大，会导致服务器性能比较差；第2种方式，由于要涉及到线程的同步，有可能会面临竞争、死锁等问题；第3种方式，就是所谓事件驱动的方式，它利用了多路I/O复用和异步I/O的优点，虽然代码逻辑比前面两种都复杂，但能达到最好的性能，这也是目前大多数网络服务器采用的方式。

> 说明：因为在Python基础阶段讲解过并发编程的知识，但是这部分对学生来说是盲点也是难点，所以此处这里可以根据授课班级学生具体的情况决定讲解的深浅。如果不对这部分知识进行适当的铺垫，后面讲解Tornado框架的设计理念是很难展开的；如果学生完全不理解这些东西，只是能照葫芦画瓢的使用框架，对面试和实际开发也是没有实质性帮助的。

### Tornado

Python的Web框架种类繁多（比Python语言的关键字还要多），但在众多优秀的Web框架中，Tornado框架最适合用来开发需要处理长连接和应对高并发的Web应用。Tornado框架在设计之初就考虑到性能问题，通过对非阻塞I/O和epoll（Linux 2.5.44内核引入的一种多路I/O复用方式，旨在实现高性能网络服务，在BSD和macOS中是kqueue）的运用，Tornado可以处理大量的并发连接，更轻松的应对C10K（万级并发）问题，是非常理想的实时通信Web框架。

> 扩展：基于线程的Web服务器产品（如：Apache）会维护一个线程池来处理用户请求，当用户请求到达时就为该请求分配一个线程，如果线程池中没有空闲线程了，那么可以通过创建新的线程来应付新的请求，但前提是系统尚有空闲的内存空间，显然这种方式很容易将服务器的空闲内存耗尽（大多数Linux发行版本中，默认的线程栈大小为8M）。想象一下，如果我们要开发一个社交类应用，这类应用中，通常需要显示实时更新的消息、对象状态的变化和各种类型的通知，那也就意味着客户端需要保持请求连接来接收服务器的各种响应，在这种情况下，服务器上的工作线程很容易被耗尽，这也就意味着新的请求很有可能无法得到响应。

Tornado框架源于FriendFeed网站，在FriendFeed网站被Facebook收购之后得以开源，正式发布的日期是2009年9月10日。Tornado能让你能够快速开发高速的Web应用，如果你想编写一个可扩展的社交应用、实时分析引擎，或RESTful API，那么Tornado框架就是很好的选择。Tornado其实不仅仅是一个Web开发的框架，它还是一个高性能的事件驱动网络访问引擎，内置了高性能的HTTP服务器和客户端（支持同步和异步请求），同时还对WebSocket提供了完美的支持。

```HTML

```

### 异步化

在前面的例子中，我们并没有对`RequestHandler`中的`get`或`post`方法进行异步处理，这就意味着，一旦在`get`或`post`方法中出现了耗时间的操作，不仅仅是当前请求被阻塞，按照Tornado框架的工作模式，其他的请求也会被阻塞，所以我们需要对耗时间的操作进行异步化处理。

在Tornado稍早一些的版本中，可以用装饰器实现请求方法的异步化或协程化来解决这个问题。

```python



import tornado.web

import asyncio

class MainHandler(tornado.web.RequestHandler):


async def get(self):
    await asyncio.sleep(10)
    self.render('index.html')
```
```Python

或，老的方法

import tornado.web
import asyncio
import tornado.gen

class MainHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def get(self):
        yield from asyncio.sleep(10)
        self.render('index.html')
        
```

去baidu异步获取内容

```python
 class GetUrlHandler(tornado.web.RequestHandler):
    async def get(self):
        wd = self.get_argument('wd')
        client = AsyncHTTPClient()
        response = await client.fetch('http://www.baidu.com/s?wd=%s' %wd)

        self.write(response.body)
        
同步获取内容

class GetUrlHandler(tornado.web.RequestHandler):


    def get(self):
        wd = self.get_argument('wd')
        http_client = HTTPClient()
        response = http_client.fetch('http://www.baidu.com/s?wd=%s' %wd)

        self.write(response.body)




可以用ab来测试服务器的性能

	sudo apt install apache2-utils




```
```Python


```

#### HTML5 WebSocket



WebSocket 是 HTML5 开始提供的一种在单个 TCP 连接上进行全双工通讯的协议。

WebSocket 使得客户端和服务器之间的数据交换变得更加简单，允许服务端主动向客户端推送数据。在 WebSocket API 中，浏览器和服务器只需要完成一次握手，两者之间就直接可以创建持久性的连接，并进行双向数据传输。

在 WebSocket API 中，浏览器和服务器只需要做一个握手的动作，然后，浏览器和服务器之间就形成了一条快速通道。两者之间就直接可以数据互相传送。





#### 聊天室应用



登录



class LoginHanlder(tornado.web.RequestHandler):
    def get(self):

```python
    self.render('login.html',error='')

def post(self):
    username = self.get_body_argument('username')
    password = self.get_body_argument('password')

    if username in ['coco', 'cc','aa'] and password == '123456':
        self.set_secure_cookie('username', username)
        self.render('chat.html', username=username)

    else:

        self.render('login.html', error='password erro
```






websocket





```python
   
class ChatHandler(tornado.websocket.WebSocketHandler):
    user_list = []
    def open(self, *args: str, **kwargs: str):
        self.user_list.append(self)
        for user in self.user_list:
            username = self.get_secure_cookie('username').decode()
            user.write_message('%s enter room' % username)
            
    def on_message(self, message):
        for user in self.user_list:
            username = self.get_secure_cookie('username').decode()
            user.write_message('%s:%s' % (username,message))

    def on_close(self):
        self.user_list.remove(self)
        for user in self.user_list:
            username = self.get_secure_cookie('username').decode()
            user.write_message('%s leave room' % (username))
```




页面



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>登录</title>
</head>
<body>
    <p>登录聊天室界面</p>
    {% if error %}
        {{ error }}
    {% end %}
    <form action="" method="post">
        <p>用户名: <input type="text" name="username"></p>
        <p>密码: <input type="text" name="password"></p>
        <p><input type="submit" value="提交"> </p>
    </form>
</body>
</html>
```



chat

“”“

```
    <title>聊天室</title>
    <script src="https://code.jquery.com/jquery-3.0.0.min.js"></script>
</head>
<body>
    <p>当前账号: {{ username }}</p>
    <div id="chat" style="width:300px; height:300px; border:1px solid #000000;">
        <!--聊天窗口-->

    </div>
    <!--输入信息窗口-->
    <input type="text" name="content" id="content">
    <input type="button" id="btn" value="提交">

    <script>
        <!--建立连接-->
        var websocket = new WebSocket('ws://127.0.0.1:80/chat/')
        <!--获取后端返回的数据-->
        websocket.onmessage = function(e){
            console.log(e.data)
            $('#chat').append('<br>')
            $('#chat').append(e.data)
        }
        $('#btn').click(function(){
            <!--向后端发送数据-->
            var content = $('#content').val()
            websocket.send(content)
        });


    </script>

</body>
```






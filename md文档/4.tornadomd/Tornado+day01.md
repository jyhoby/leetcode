## Tornado基础

### Tornado概述

Python的Web框架种类繁多（比Python语言的关键字还要多），但在众多优秀的Web框架中，Tornado框架最适合用来开发需要处理长连接和应对高并发的Web应用。Tornado框架在设计之初就考虑到性能问题，它可以处理大量的并发连接，更轻松的应对C10K（万级并发）问题，是非常理想的实时通信Web框架。

Tornado框架源于FriendFeed网站，在FriendFeed网站被Facebook收购之后得以开源，正式发布的日期是2009年9月10日。Tornado能让你能够快速开发高速的Web应用，如果你想编写一个可扩展的社交应用、实时分析引擎，或RESTful API，那么Tornado框架就是很好的选择。Tornado其实不仅仅是一个Web开发的框架，它还是一个高性能的事件驱动网络访问引擎，内置了高性能的HTTP服务器和客户端（支持同步和异步请求），同时还对WebSocket提供了完美的支持。

了解和学习Tornado最好的资料就是它的官方文档，在[tornadoweb.org](http://www.tornadoweb.org)上面有很多不错的例子，你也可以在Github上找到Tornado的源代码和历史版本。

### 5分钟上手Tornado

1. 创建并激活虚拟环境。

   ```Shell
   mkvirtualenv tornadoenv -p /usr/bin/python3
   ```

2. 安装Tornado。

   ```Shell
   pip install tornado
   ```

3. 编写Web应用。

   ```Python
   """
   example01.py
   """
   import tornado.ioloop
   import tornado.web
   
   
   class MainHandler(tornado.web.RequestHandler):
   
       def get(self):
           self.write('<h1>Hello, world!</h1>')
   
   
   def main():
       app = tornado.web.Application(handlers=[(r'/', MainHandler), ])
       app.listen(8888)
       tornado.ioloop.IOLoop.current().start()
   
   
   if __name__ == '__main__':
       main()
   ```

4. 运行并访问应用。

   ```Shell
   python example01.py
   ```


在上面的例子中，代码example01.py通过定义一个继承自`RequestHandler`的类（`MainHandler`）来处理用户请求，当请求到达时，Tornado会实例化这个类（创建`MainHandler`对象），并调用与HTTP请求方法（GET、POST等）对应的方法，显然上面的`MainHandler`只能处理GET请求，在收到GET请求时，它会将一段HTML的内容写入到HTTP响应中。`main`函数的第1行代码创建了Tornado框架中`Application`类的实例，它代表了我们的Web应用，而创建该实例最为重要的参数就是`handlers`，该参数告知`Application`对象，当收到一个请求时应该通过哪个类的对象来处理这个请求。在上面的例子中，当通过HTTP的GET请求访问站点根路径时，就会调用`MainHandler`的`get`方法。 `main`函数的第2行代码通过`Application`对象的`listen`方法指定了监听HTTP请求的端口。`main`函数的第3行代码用于获取Tornado框架的`IOLoop`实例并启动它，该实例代表一个条件触发的I/O循环，用于持续的接收来自于客户端的请求。

> 扩展：在Python 3中，`IOLoop`实例的本质就是`asyncio`的事件循环，该事件循环在非Windows系统中就是`SelectorEventLoop`对象，它基于`selectors`模块（高级I/O复用模块），会使用当前操作系统最高效的I/O复用选择器，例如在Linux环境下它使用`EpollSelector`，而在macOS和BSD环境下它使用的是`KqueueSelector`；在Python 2中，`IOLoop`直接使用`select`模块（低级I/O复用模块）的`epoll`或`kqueue`函数，如果这两种方式都不可用，则调用`select`函数实现多路I/O复用。当然，如果要支持高并发，你的系统最好能够支持epoll或者kqueue这两种多路I/O复用方式中的一种。

如果希望通过命令行参数来指定Web应用的监听端口，可以对上面的代码稍作修改。

```Python
"""
example01.py
"""
import tornado.ioloop
import tornado.web

from tornado.options import define, options, parse_command_line


# 定义默认端口
define('port', default=8000, type=int)


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('<h1>Hello, world!</h1>')


def main():
    # python example01.py --port=8888
    parse_command_line()
    app = tornado.web.Application(handlers=[(r'/', MainHandler), ])
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
```

在启动Web应用时，如果没有指定端口，将使用`define`函数中设置的默认端口8000，如果要指定端口，可以使用下面的方式来启动Web应用。

```Shell
python example01.py --port=8888
```

使用 curl 发送POST请求

```
curl -X POST 127.0.0.1:8080/days/2019/07/15/
```



### 路由解析

上面我们曾经提到过创建`Application`实例时需要指定`handlers`参数，这个参数非常重要，它应该是一个元组的列表，元组中的第一个元素是正则表达式，它用于匹配用户请求的资源路径；第二个元素是`RequestHandler`的子类。在刚才的例子中，我们只在`handlers`列表中放置了一个元组，事实上我们可以放置多个元组来匹配不同的请求（资源路径），而且可以使用正则表达式的捕获组来获取匹配的内容并将其作为参数传入到`get`、`post`这些方法中。

```Python
"""
example02.py
"""
import os
import random

import tornado.ioloop
import tornado.web

from tornado.options import define, options, parse_command_line


# 定义默认端口
define('port', default=8000, type=int)


class DaysHandler(tornado.web.RequestHandler):
    # def get(self, year, month, day):
    def get(self, month, day, year):

        self.write('%s年%s月%s日' % (year, month, day))


class Days2Handler(tornado.web.RequestHandler):
    # def get(self, year, month, day):
    def get(self, month, year, day):
        self.write('%s年%s月%s日' % (year, month, day))

    def post(self, month, year, day):
        self.write('post:只负责新增数据')

    def delete(self, month, year, day):
        self.write('delete: 只负责删除')

    def patch(self, month, year, day):
        self.write('patch: 修改部分属性')

    def put(self, month, year, day):
        self.write('put: 修改全部数据')
        
class IndexHandler(tornado.web.RequestHandler):

    def get(self):

        self.render('index.html')

def main():
    """主函数"""
    parse_command_line()
    app = tornado.web.Application(
        # handlers是按列表中的顺序依次进行匹配的
        handlers=[
        	(r'/days/(\d{4})/(\d+)/(\d{2})/', DaysHandler),
        	(r'/days2/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/', Days2Handler),
        ],
        template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'templates'),
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
```

模板页index.html。

```HTML
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<title>Tornado基础</title>
</head>
<body>
	<h1>{{message}}</h1>
</body>
</html>
```



Tornado的模板语法与其他的Web框架中使用的模板语法并没有什么实质性的区别，而且目前的Web应用开发更倡导使用前端渲染的方式来减轻服务器的负担，所以这里我们并不对模板语法和后端渲染进行深入的讲解。

### 请求处理器

通过上面的代码可以看出，`RequestHandler`是处理用户请求的核心类，通过重写`get`、`post`、`put`、`delete`等方法可以处理不同类型的HTTP请求，除了这些方法之外，`RequestHandler`还实现了很多重要的方法，下面是部分方法的列表：

1. `get_argument` / `get_arguments` / `get_body_argument` / `get_body_arguments` / `get_query_arugment` / `get_query_arguments`：获取请求参数。

2. `set_status` / `send_error` ：操作状态码和响应头。

3. `write` / `flush` / `finish` /：和输出相关的方法。

4. `render` / `render_string`：渲染模板。

5. `redirect`：请求重定向。

6. `get_cookie` / `set_cookie` /  `clear_cookie` / `clear_all_cookies`：操作Cookie。

7. reverse_url : url反向解析

   ```python
   from tornado.web import url
   
       return tornado.web.Application(handlers=[
           url(r'/index/', MainHandler, name='index'),
           url(r'/login/', LoginHandler),
           url(r'/user_handler/', UserHander),
           url(r'/days/(\w{4,})/(\d+)/(\d+)/', DaysHandler, name='dd'),
           url(r'/days2/(?P<year>\w{4,})/(?P<month>\d+)/(?P<day>\d+)/', DaysHandler2),
   
       ],
           template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'templates'),
           static_path= os.path.join(os.path.dirname(os.path.abspath(__file__)),'static'),
   
       )
   
   
   print(self.reverse_url('dd','123',111,123))
   ```

我们用上面讲到的这些方法来完成下面的需求，访问页面时，如果Cookie中没有读取到用户信息则要求用户填写个人信息，如果从Cookie中读取到用户信息则直接显示用户信息。

```Python
"""
example03.py
"""
import os
import re

import tornado.ioloop
import tornado.web

from tornado.options import define, options, parse_command_line


# 定义默认端口
define('port', default=8000, type=int)

class UserHander(tornado.web.RequestHandler):
    def get(self):
        username = self.get_query_argument('username')
        password = self.get_query_argument('password')

        if username == 'hule' and password == '123456':
            self.set_cookie('username',username,expires_days=7)

            self.redirect('/index/')
        else:
            self.write('登录失败')

```

```html
<!-- 登录 -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <form action="{{ reverse_url('u_handler') }}">
        用户名：<input type="text" name="username">
        password：<input type="text" name="password">
        <input type="submit" value="登录">
    </form>
</body>
</html>
```

``` 

<!-- 首页 -- >
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <!--<link rel="stylesheet" href="/static/index.css">-->
    <link rel="stylesheet" href="{{ static_url('index.css')}}">
</head>
<body>
    <h3>index</h3>
    <p>{{ message }}</p>
    {% if username %}
        <p>{{username}}</p>
    {% end %}
    <a href="{{ reverse_url('login') }}">登录</a>
</body>
</html>
```


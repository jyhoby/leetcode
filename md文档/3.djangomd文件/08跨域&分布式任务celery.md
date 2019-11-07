# cors跨域&celery

# 一.cors跨域

#### 1. 什么是跨域

```
跨域(跨源)是指浏览器从一个源的网页去请求另一个源，源指的是域名、端口、协议

以下都属于跨域问题
域名： 
    主域名不同: http://www.baidu.com/index.html –> http://www.sina.com/test.js 
    子域名不同: http://www.666.baidu.com/index.html –> http://www.555.baidu.com/test.js 
    域名和域名ip: http://www.baidu.com/index.html –>http://180.149.132.47/test.js 
端口： 
	http://www.baidu.com:8080/index.html–> http://www.baidu.com:8081/test.js 
协议： 
	http://www.baidu.com:8080/index.html–> https://www.baidu.com:8080/test.js 

```

#### 2. 为什么要考虑跨域问题

```python
因为Ajax不能跨域, 一旦客户端和服务端的不在一台服务器, 则需要考虑跨域访问的问题
```

#### 3. 同源策略

```python
同源策略是浏览器的一项最为基本同时也是必须遵守的安全策略。
同源策略的存在，限制了“源”自A的脚本只能操作“同源”页面的DOM，“跨源”操作来源于B的页面将会被拒绝。
所谓的“同源”，必须要求相应的URI的域名、端口、协议均是相同的。
```

#### 4. 使用Ajax发送请求的方式

```javascript
//js
xhr = new XMLHttpRequest();
xhr.open('get', 'http://127.0.0.1:8000/app/getdata/', true);
xhr.send();
xhr.onreadystatechange = function () {
  	if (xhr.readyState==4 && xhr.status==200){
      	console.log(JSON.parse(xhr.responseText))
  	}
}

//jq
$.ajax({
  	type: "get",
  	url: 'http://127.0.0.1:8000/app/getdata/',
    data: {},
    async: true,

    success: function (data) {
      	console.log(data);
    },
    error: function (e) {
      	console.log(e);
    }
})

// get请求
$.get("http://127.0.0.1:8000/app/getdata/", function (data) {
	console.log(data);
});

// post请求 【csrf验证】
$.ajaxSetup({
	data:{csrfmiddlewaretoken:'{{ csrf_token }}'}
});

$.post("http://127.0.0.1:8000/app/getdata/", function (data) {
	console.log(data);
})

```



#### 5. 解决跨域问题	

##### 方式一: 使用 JSONP (一种非Ajax技术,需要前后端同时支持)

```
<script src='http://www.baidu.com/getdata/'></script>
```

##### 方式二: 让服务器支持跨域(推荐) 

##### Django支持跨域 

```python
安装django-cors-headers
	pip install django-cors-headers
配置settings.py文件
	INSTALLED_APPS = [
        'corsheaders'，
     ]

    MIDDLEWARE = (
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware', 
    )
    # 跨域增加忽略
    CORS_ALLOW_CREDENTIALS = True
    CORS_ORIGIN_ALLOW_ALL = True
	
    # 跨域允许的请求方式(可选)
    CORS_ALLOW_METHODS = (
        'DELETE',
        'GET',
        'OPTIONS',
        'PATCH',
        'POST',
        'PUT',
    )
	
    # 跨域允许的头部参数(可选)
    CORS_ALLOW_HEADERS = (
        'XMLHttpRequest',
        'X_FILENAME',
        'accept-encoding',
        'authorization',
        'content-type',
        'dnt',
        'origin',
        'user-agent',
        'x-csrftoken',
        'x-requested-with',
        'Pragma',
    )
```

##### Flask支持跨域

```python
安装flask_cors
	pip install flask-cors
    
使用flask_cors的CORS
	from flask_cors import CORS
	CORS(app, supports_credentials=True)
    
```



# 二.celery

#### 1. celery介绍

```
Celery - 分布式任务队列. Celery 是一个简单、灵活且可靠的, 基于python开发的分布式异步消息任务队列，通过它可以轻松的实现任务的异步处理， 如果你的业务场景中需要用到异步任务，就可以考虑使用celery.
使用场景:
	1.你想执行一个操作，可能会花很长时间，但你不想让你的程序一直等着结果返回，而是想有创建一个任务,这个任务会在其他地方执行,执行完毕后会你拿到结果， 在任务执行过程，你可以继续做其它的事情。 
	2.你想做一个定时任务，比如每个星期五发送一条会议通知.

异步：理解为在不同线程中并发执行
同步：理解为同一个线程中按顺序执行（串行执行）

Celery它是一个专注于实时处理的任务队列，同时也支持任务调度.

Celery是基于Python开发的一个分布式任务队列框架，支持使用任务队列的方式在分布的机器/进程/线程上执行任务调度.
```

#### 2.安装celery

```python
创建虚拟环境
	mkvirtualenv celeryenv
使用pip安装
	pip install celery
```

#### 使用celery

##### 创建python工程, 然后新建tasks.py文件, 写入以下代码

```python
from celery import Celery

# 创建celery对象,设置任务队列使用redis
app = Celery('tasks', broker='redis://localhost:6379')

# 创建任务
@app.task
def add(a, b):    
    time.sleep(5)    
    n = a + b    
    print(n)    
    return n

if __name__ == '__main__':
    # add(10, 5)    
    # 调用任务
    add.delay(10, 5)
    print('程序执行结束')
    
```

#### 启动celery服务

```python
celery -A tasks worker --loglevel=info
```

#### redis操作:

```python
安装redis
	pip install redis
启动redis服务
	redis-server
```



#### Flask中使用celery

##### 在之前创建的虚拟环境celeryenv中安装flask

```
安装flask
	pip install flask
```

##### 创建FlaskProject.py文件,并写入以下代码

```python
from flask import Flask
from tasks import send_email

app = Flask(__name__)

@app.route('/')
def index():
    send_email.delay('111@qq.com')
    return "激活邮件已发送， 请注意查收"

if __name__ == '__main__':
    app.run()

```

##### 在之前的tasks.py文件, 添加以下代码

```python
@app.task
def send_email(receive_addr):
    time.sleep(7)
    print(receive_addr)
    
```

#### Django中使用celery

##### 安装celery

```python
pip install celery
```

##### 安装redis

```
pip install redis
```

##### 安装sqlalchemy

```
pip install sqlalchemy
```

##### 启动celery服务



```
celery 降版本
pip uninstall celery
pip install celery==3.1.24

另一种启动方式：
celery -A Moonbasa worker --pool=solo -l info
```

```
celery -A Moonbasa worker -l info
注意: Moonbasa是工程名称
```

### celery定时任务

启动beat

```
celery -A myproject beat -l info
```



```python

from celery import Celery
from celery.schedules import crontab

app = Celery('tasks', broker='redis://localhost:6379')

# 添加定时任务
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(3.0, test.s("hello"), name='每隔3秒调用一次')
    # sender.add_periodic_task(3.0, test.s("world"), expires=10)
    # sender.add_periodic_task(
    #     crontab(hour=7, minute=30, day_of_week=1),
    #     test.s("Happy Mondays!"),
    # )

@app.task
def test(arg):
    print(arg)

```


















# Django 项目部署

> 思考题
>
> 在浏览器中打开一个网页，都发生了些什么事情？

- 开发模式

  浏览器 <=> 开发服务器(WSGI server) <=> Python应用程序(WSGI Applicaton) <=> 数据库(MySQL)

- 生产模式

  浏览器 <=> **服务器(Nginx) <=> WSGI 服务器(uWSGI/Gunicorn)** <=> Python 应用程序(WSGI Applicaton) <=> 数据库(MySQL)

### Django

settings.py

```python
DEBUG = False    # 生产环境关闭 DEBUG
ALLOWED_HOSTS = ['mysite.com',]  # 设置为你的网站域名

STATIC_ROOT = os.path.join(BASE_DIR, "static")    # DEBUG 为 False 时，需要自己维护静态文件访问，需要将项目中的静态文件收集到 STATIC_ROOT


# 这三个的配置有一定要求
# STATIC_ROOT 为Nginx托管目录，也是 python manage.py collectstatic 的收集目录
STATIC_ROOT = os.path.join(BASE_DIR, "allstatic")

# 这个与网页里的 {% load staticfiles %}标签配合，会将static关键字解析为跟配置的路由
STATICFILES_DIRS = (
    os.path.join(os.path.join(BASE_DIR, 'static')),
)
# 这个为普通今天文件路由，在使用dev环境时最好放在最下面
STATIC_URL = '/static/'
```

静态文件

```
python manage.py collectstatic   # 将项目使用的所有静态文件收集到 STATIC_ROOT
```

### uWSGI

- 安装 `pip install uwsgi`

- 配置

```
--http        # 以 HTTP 方式启动，监听ip及端口：10.10.10.10:8000
--socket      # 以 socket 方式启动，监听ip及端口：10.10.10.10:8000
--chdir       # 项目目录
--wsgi-file   # wsgi 应用程序文件/模块
--callable    # 指定 wsgi 应用程序
--module      # 指定模块及应用
--daemonize   # 指定后台启动的日志文件
--processes   # 指定启动进程数
--threads     # 指定启动线程数
```

- HTTP 方式启动

- ```shell
  uwsgi --http 127.0.0.1:8000 --wsgi-file mysite/wsgi.py --callable application
  ```

- socket 方式启动

- ```shell
  uwsgi --socket 127.0.0.1:8000 --wsgi-file mysite/wsgi.py --callable application
  ```

- 通过配置文件启动 (socket 方式) `uwsgi —ini uwsg.ini`

  ```ini
  [uwsgi]
  module=mysite.wsgi:application
  env=DJANGO_SETTINGS_MODULE=mysite.settings.production
  socket=127.0.0.1:8000
  daemonize=/var/log/uwsgi.log
  ```
  
  socket 方式还可以指定到文件：socket=/tmp/uwsgi.sock

### Nginx

- nginx 转发(TCP)

- 配置文件目录：

  - /etc/nginx/conf.d/*.conf
  - /etc/nginx/sites-enabled/*
  
  ```nginx
  server {
  	listen 80;
  	server_name mysite.com www.mysite.com;
    
    # 通过 nginx 为静态文件提供访问服务，Django 配置文件中 STATIC_ROOT 的目录
  	location /static {	#这里static是关键字 
    	alias /var/www/mysite/static;
  	}
    
    location /media {
    	alias /var/www/mysite/media;
  	}
  	
  	location / {
  		uwsgi_pass 127.0.0.1:8000;
      include uwsgi_params;
  	}
  }
  ```

检查配置是否正确：`nginx -t`

### Gunicorn

安装 `pip install gunicorn`

```
gunicorn -w 4 mysite.wsgi
gunicorn --workers=4 --env DJANGO_SETTINGS_MODULE=mysite.settings.production mysite.wsgi --daemon
```

```nginx
server {
  listen 80;
  server_name mysite.com;

  location / {
      proxy_pass http://127.0.0.1:8000;
      proxy_set_header Host $host;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  }
}
```



### 前后端分离项目

#### 前端部署

- Vue

  修改生产环境 api 访问地址，并编译

  ```
  # 相关命令
  npm run build
  ```

- Nginx

- 配置文件目录：

  - /etc/nginx/conf.d/*.conf
  - /etc/nginx/sites-enabled/*

```nginx
server {
	listen 9998;
	server_name 47.102.96.95;
	
	location / {
		root /home/code/dist;
    		index index.html;
	}
}
```

#### 后端部署

redis 安装：`sudo apt-get install redis-server`

安装好后，第一次需要新建终端启动  `redis-server `

- 生成项目依赖文件，部署时安装依赖包

```shell
pip freeze > requirements.txt
pip install -r requirements.txt
```

- Django
  settings.py

```python
DEBUG = False    # 生产环境关闭 DEBUG
ALLOWED_HOSTS = ['mysite.com',]  # 设置为你的网站域名,通用可以设置为 *

INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]

MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]

CORS_ORIGIN_WHITELIST = [	# 设置跨域白名单
    "https://axf.com",
    "https://m.axf.com",
]
# 也可直接这是全部白名单，与上面二选一
CORS_ORIGIN_ALLOW_ALL = True
```

- UWSGI

```ini
[uwsgi]
module=axf.wsgi:application
env=DJANGO_SETTINGS_MODULE=axf.settings
socket=127.0.0.1:6666
daemonize=/home/logs/uwsgi02.log
```

总结：uwsgi.ini文件最好放在项目根目录下，因为module可能会就近寻找app入口，放在其它地方可能找不到入口模块,env也是如此；其次socket是设置当前运行时的端口号，即通常我们用命令行启动时`python manage.py runserver 0:6666`配置端口号，这个端口应该是接收来自上面vue中ajax请求的端口，然后转发给此端口。

- Nginx
- 配置文件目录：
  - /etc/nginx/conf.d/*.conf
  - /etc/nginx/sites-enabled/*

```nginx
server {
	listen 9999;
	server_name 47.102.96.95;
	
	location / {
		include uwsgi_params;
		uwsgi_pass 127.0.0.1:6666;
    		
	}
}
```

总结：此处是配置后端服务器的nginx,需在阿里云上打开对应的端口，前端的Ajax请求才能经过Nginx转发到服务器响应程序的端口

- 最后总结

请求到转发然后到响应的流程:

浏览器地址(ip加端口号)  >>  阿里云对外开放的端口匹配  >>  根据nginx配置转发到服务器对应应用程序的端口  >>  服务器应用程序作出响应（按原路径返回）

一份比较推荐的uwsgi配置：

```
[uwsgi]
module=fresh_shop_eve7.wsgi:application
env=DJANGO_SETTINGS_MODULE=fresh_shop_eve7.settings
master=true
socket=127.0.0.1:4398
chdir=/home/code/fresh_shop_eve7
pythonpath=/home/env/freshenv/bin/python
callable=app
logto=/home/logs/freshuwsgi.log
```



##### 补充：可能还是个面试题

uWSGI是一个[Web服务器](https://baike.baidu.com/item/Web%E6%9C%8D%E5%8A%A1%E5%99%A8)，它实现了WSGI协议、uwsgi、http等协议。Nginx中HttpUwsgiModule的作用是与uWSGI服务器进行交换。

要注意 WSGI / uwsgi / uWSGI 这三个概念的区分。

- WSGI是一种通信协议。
- uwsgi是一种线路协议而不是通信协议，在此常用于在uWSGI服务器与其他网络服务器的数据通信。
- 而uWSGI是实现了uwsgi和WSGI两种协议的Web服务器。

uwsgi协议是一个uWSGI服务器自有的协议，它用于定义传输信息的类型（type of information），每一个uwsgi packet前4byte为传输信息类型描述，它与WSGI相比是两样东西。
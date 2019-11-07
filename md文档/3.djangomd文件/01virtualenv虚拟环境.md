#Hello Django
#### 1. **创建虚拟环境**(virtualenv 和virtualenvwrapper)

```python
1.1, virtualenv的概述
	virtualenv是用来创建Python的虚拟环境的库，虚拟环境能够独立于真实环境存在，并且可以同时有多个互相独立的Python虚拟环境，每个虚拟环境都可以营造一个干净的开发环境，对于项目的依赖、版本的控制有着非常重要的作用。
	虚拟环境有什么意义？
	比如: 我们要同时开发多个应用程序，应用A需要Django1.11，而应用B需要Django1.8怎么办, 这种情况下，每个应用可能需要各自拥有一套独立的Python运行环境,virtualenv就可以用来为每一个应用创建一套'隔离'的Python运行环境。

1.2, 安装pip
   【请使用普通用户】 
  	a. 查看pip版本
  		查看pip版本: pip -V
		查看pip3版本: pip3 -V
	b. 安装pip(如果存在则不需要安装)
		安装pip3: apt install python3-pip    
         安装pip2: apt install python-pip    
	c. 更新pip
  		更新pip (如果pip版本高于9.0则不需要更新): 
  			更新pip3: pip3 install --upgrade pip
        	更新pip: pip install --upgrade pip
 
         注意: 更新后如出现以下错误（这是pip 10.0.0版本的BUG）：
			Traceback (most recent call last): 
			File “/usr/bin/pip”, line 9, in 
			from pip import main

		    解决方法：修改对应pip文件中的代码(pip和pip3类似)
			  	例如更新pip时报错则需要修改 /usr/bin/pip 文件中的代码，
				使用: sudo vim /usr/bin/pip 打开pip文件
				将：          
					from pip import main
					if __name__ == '__main__':
						sys.exit(main())
				改成：
					from pip import __main__
					if __name__ == '__main__':
						sys.exit(__main__._main())

	d. 让pip默认使用python3, 执行命令：
		sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 150
		
    e. pip命令
  		pip install xxx:安装xxx依赖包
    	pip list:查看所有依赖包
    	pip freeze:查看新安装的包
    	pip uninstall xxx ：卸载xxx包

1.3, virtualenv和virtualenvwrapper 的安装和使用
   【请使用普通用户】 
    a. 安装虚拟环境
  		sudo apt update
  		sudo pip3 install virtualenv virtualenvwrapper
        
  		安装后如果不能使用虚拟环境命令，则需要配置环境变量
            1, 进入家目录: cd ~
            2, 使用vim打开.bashrc, 定位到最后:shift+g，并添加以下2行代码(注意修改自己Ubuntu的用户名)
                	export WORKON_HOME=/home/自己Ubuntu的用户名/.virtualenvs
                	source /usr/local/bin/virtualenvwrapper.sh
            3, 在家目录创建.virtualenvs目录: mkdir .virtualenvs
            4, 加载修改后的设置，使之生效：source .bashrc
  	b. 创建虚拟环境: 
  		mkvirtualenv env  
  		mkvirtualenv env2 -p /usr/bin/python3  (指定python路径)
  	c. 退出虚拟环境
  		deactivate 
    d. 进入虚拟环境: 
  		workon 虚拟环境名称
	f. 删除虚拟环境
    	rmvirtualenv env  
  
```

#### 2. 安装django

**pip install django==1.11**（==1.11是指定版本， 如不写则会安装最新版本）

  ```python
  测试Django是否安装成功 
  进入python环境
  	import django
  	django.get_version()

  课堂练习：在上一步创建的虚拟环境中分别安装django。
  ```

#### 3. 创建一个Django项目

进入到指定要存放项目的目录，执行 **django-admin startproject xxx**  来创建一个名字为xxx的工程

```python
查看默认目录结构:
manage.py:
    是Django用于管理本项目的命令行工具，之后进行站点运行，数据库自动生成等都是通过本文件完成。
HelloDjango/__init__.py:
	告诉python该目录是一个python包，暂无内容，后期一些工具的初始化可能会用到
HelloDjango/settings.py:
    Django项目的配置文件，默认状态其中定义了本项目引用的组件，项目名，数据库，静态资源等。
HelloDjango/urls.py:
    维护项目的URL路由映射，即定义当客户端访问时由哪个模块进行响应。
HelloDjango/wsgi.py:
    定义WSGI的接口信息，主要用于服务器集成，通常本文件生成后无需改动。
    
```

#### 4. 测试服务器的启动

##### **python manage.py runserver [ip:port]**

```python
可以直接进行服务运行 默认执行起来的端口是8000
也可以自己指定ip和端口：
监听机器所有可用 ip （电脑可能有多个内网ip或多个外网ip）：python manage.py runserver 0.0.0.0:8000 或 runserver 0:8000 
同时在settings.py中将ALLOWED_HOSTS=['*']
如果是外网或者局域网电脑上可以用其它电脑查看开发服务器，访问对应的 ip加端口，比如 10.36.132.2:8000
浏览器访问:http://localhost:8000 可以看到服务器启动成功
```

#### 5.**数据迁移**

迁移的概念: 就是将模型映射到数据库的过程

生成迁移文件:**python manage.py makemigrations**

执行迁移:**python manage.py migrate**



#### 6.**创建应用**

**python manage.py startapp XXX** 
创建名称为XXX的应用
使用应用前需要将应用配置到项目中，在settings.py中将应用加入到INSTALLED_APPS选项中

```python
应用目录介绍:
__init__.py:
    其中暂无内容，使得app成为一个包
admin.py:
    管理站点模型的声明文件，默认为空
apps.py:
    应用信息定义文件，在其中生成了AppConfig，该类用于定义应用名等数据
models.py:
    添加模型层数据类文件
views.py:
    定义URL相应函数
migrations包:
    自动生成，生成迁移文件的
tests.py:
    测试代码文件
```

#### 7.**基本视图**

```python
首先我们在views.py中建立一个路由响应函数
from django.http import HttpResponse
def welcome(request):
	return HttpResponse('HelloDjango');

接着我们在urls中进行注册
from App import views
url(r'^welcome/',views.welcome)

基于模块化的设计，我们通常会在每个app中定义自己的urls

在项目的urls中将app的urls包含进来
from django.conf.urls import include
url(r'^welcome/',include('App.urls'))

课堂练习：新建一个应用showtime，每次刷新页面显示不同的当前时间。
```

#### 8.**基本模板**   

```python
模板实际上就是我们用HTML写好的页面
创建模板文件夹templates, 在模板文件夹中创建模板文件
在views中去加载渲染模板, 使用render函数: return render(request,'xxx')

课堂练习：在上一个课堂练习中，使用template显示页面内容。
```

#### 9.**定义模型**

在models.py 中引入models
from django.db import models

创建自己的模型类，但切记要继承自 models.Model

案例驱动: 使用模型定义班级，并在模板上显示班级列表

```
班级table : grade
 	columns: 	
			班级名称 - name
			成立时间 - date
			女生个数 - girlnum
			男生个数 - boynum
			是否删除 - is_delete
```

#### 10.**Admin 后台管理**

在admin.py中将model加入后台管理：

admin.site.register(Grade)

创建超级用户：**python manage.py createsuperuser**

访问admin后台：http://127.0.0.1:8000/admin/

#### 11.**展示班级列表**

在views.py文件中编写班级的视图函数：

```python
def grade_list(request):
    # 获取班级所有数据
    g_list = Grade.objects.all()  
    return render(request, 'grade/grade_list.html', {'g_list': g_list})
```

​	模板文件(html文件)：

```python
{% for grade in g_list %}
	{{ grade.sname }}
{% endfor %}
```

#### 12.**配置url**

在grade App中新建urls.py文件，输入如下代码：

```python
from django.conf.urls import url
from .views import grade_list
urlpatterns = [
	url(r'^grade/$', grade_list),
]
```
​	在工程的urls.py文件中添加如下代码：

```python
url(r'^', include('grade.urls')),
```



#### 练习：

​	1，从创建虚拟环境到显示出所有班级再自己操作2次

​	2，在班级Grade所在项目中创建学生students应用，在admin后台管理系统中添加多条学生数据, 在模板中显示所有学生信息

​	学生table：student
​		columns:	

​			学生姓名 - name
​			学生性别 - gender
​			学生年龄 - age
​			学生简介 - info	
​			是否删除 - is_delete 

 	定义学生类
  		class Student(models.Model):
  			name = models.CharField(max_length=20)
  	  		gender = models.BooleanField(default=True)
  	  		age = models.IntegerField()
  	  		info = models.CharField(max_length=20)
  	  		is_delete = models.BooleanField(default=False)



​	3，学会查看官网: https://docs.djangoproject.com/en/1.11/intro/tutorial01/

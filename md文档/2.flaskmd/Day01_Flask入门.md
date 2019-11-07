# FlaskDay01

## Flask简介 

```python
Flask是一个基于Python实现的Web开发‘微’框架 'MicroFramework'
官方文档: http://flask.pocoo.org/docs/0.12/  
中文文档: http://docs.jinkan.org/docs/flask/
        
Flask是一个基于MVC设计模式的Web后端框架
MTV 
	M: Models  模型（数据）
    T: Templates 模板（界面）
    V: Views 视图（控制器）

Flask依赖三个库
  Jinja2 模板引擎 {% %}  模板：静态html+模板语言{%  %}  
  Werkzeug WSGI工具集
  Itsdangerous 基于Django的签名模块
  
流行的Flask
Flask流行的主要原因:
  1. 有非常齐全的官方文档，上手非常方便
  2. 有非常好的扩展机制和第三方扩展环境，工作中常见的软件都会有对应的扩展。自己动手实现扩展也很容易
  3. 社区活跃度非常高
  4. 微型框架的形式给了开发者更大的选择空间

```



## MVC模式/MTV模式

```python
一种软件设计典范，用一种业务逻辑，使数据，界面显示分离的方法组织代码，将业务逻辑聚集到一个部件里面，在改进和个性化定制界面与用户交互的同时，不需要重新编写业务逻辑。

MVC被独特的发展起来用于映射传统的输入，处理和输出功能在一个逻辑的图形化界面结构中。
  	核心思想：解耦
  	优点：降低各个模块之间的耦合性，方便变更，更容易重构代码，最大程度实现了代码的重用。

MVC（Model，View，Controller）
    Model：用于封装与应用程序的业务逻辑相关的数据及对数据的处理方法，是Web应用程序中用于处理应用程序的数据逻辑部分，Model通常只提供功能性的接口，通过这些接口可以获取Model的所有功能。
    View:负责数据的显示和呈现，View是对用户的直接输出。
    Controller:负责从用户端收集用户的输入，可以看成提供View的反向功能，主要处理用户交互。

MVT模式简介
    本质上与MVC没什么差别，也是各组件之间为了保持松耦合关系，只是定义上有些许不同。
    Model:负责业务对象与数据库（ORM）的对象， models.py： 数据
    View:视图函数，负责业务逻辑，并在适当的时候调用Model和Template， views.py：控制器
    Template:负责把页面展示给用户, html： 界面
        
url：路由， urls.py

```



## 使用Flask

### 虚拟环境-Linux

```python
1, virtualenv的概述
	virtualenv是用来创建Python的虚拟环境的库，虚拟环境能够独立于真实环境存在，并且可以同时有多个互相独立的Python虚拟环境，每个虚拟环境都可以营造一个干净的开发环境，对于项目的依赖、版本的控制有着非常重要的作用。
	虚拟环境有什么意义？
	比如: 我们要同时开发多个应用程序，应用A需要Django1.11，而应用B需要Django1.8怎么办, 这种情况下，每个应用可能需要各自拥有一套独立的Python运行环境,virtualenv就可以用来为每一个应用创建一套'隔离'的Python运行环境。

2, 安装pip
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

3, virtualenv和virtualenvwrapper 的安装和使用
   【请使用普通用户】 
    a. 安装虚拟环境
  		sudo apt update
  		sudo pip3 install virtualenv virtualenvwrapper
        
  		安装后如果不能使用虚拟环境命令，则需要配置环境变量
            1, 进入家目录: cd ~
            2, 使用vim打开.bashrc, 定位到最后:shift+g，并添加以下2行代码(注意修改自己Ubuntu的用户名)
                	export WORKON_HOME=/home/自己Ubuntu的用户名/.virtualenvs
                	source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
            3, 在家目录创建.virtualenvs目录: mkdir .virtualenvs
            4, 加载修改后的设置，使之生效：source .bashrc
        	（如果找不到virtualenvwrapper.sh,
			 则将路径改成/usr/local/bin/virtualenvwrapper.sh
			 然后重试 ）
  	b. 创建虚拟环境: 
  		mkvirtualenv env  
  		mkvirtualenv env2 -p /usr/bin/python3  (指定python路径)
  	c. 退出虚拟环境
  		deactivate 
    d. 进入虚拟环境: 
  		workon 虚拟环境名称
```

### 第一个Flask项目

#### 创建项目

```python
1.创建虚拟环境
	mkvirtualenv flaskenv

2.在虚拟环境中安装flask
	pip install flask
    
3.创建helloFlask.py文件,并写入以下代码:
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello Flask'

    if __name__ == '__main__':
        app.run()

run()启动的时候还可以添加参数:
    debug 是否开启调试模式，开启后修改过python代码会自动重启
    port 启动指定服务器的端口号，默认是5000
    host 主机，默认是127.0.0.1，指定为0.0.0.0代表本机所有ip

```

### 使用Flask插件

```
Flask是一个微型框架，除了Flask自带的核心功能外，其他大部分功能都需要利用Flask提供的插件。
优点：灵活，可以根据项目功能需求灵活使用需要的插件
缺点：核心功能较少，针对稍大的项目每次都需要自己集成插件
```

#### flask-script 插件

```python
flask-script扩展提供向Flask插入外部脚本的功能，包括运行一个开发用的服务器，一个定制的Python shell，设置数据库的脚本及其他运行在web应用之外的命令行任务；使得脚本和系统分开；
1.安装
	pip install  flask-script

2.初始化
	manager = Manager（app）

3.调用
	在run的地方修改，修改manager.run()

4.可以在命令行中使用: python manage.py runserver
  还可以接收参数: python manage.py runserver -p 8000 -h 0 -d -r
	p  端口 port
	h  主机  host
	d  调试模式  debug
	r  重启（重新加载） reload（restart）
    
```

#### 代码结构

```python
static 静态资源文件
templates 模板文件
默认两个都可以直接使用, 直接使用相对路径就好

模板渲染
  render_template（）

  其实也是分为两个过程，加载和渲染
    template = Template(“<h2>呵呵</h2>”)
    template.render()

静态使用，相当于反向解析
  url_for（’static’,filename=‘hello.css’）
    
```

#### 请求流程

![](请求流程.jpeg)

#### 项目拆分

代码全都写在manage.py一个文件中是不现实的, 我们可以对项目进行简单的拆分

将原来的app.py文件重命名为:manage.py

```python
from flask_script import Manager
from App import create_app

# 创建app
app = create_app()

# 创建manager对象
manager = Manager(app)

if __name__ == '__main__':    
	manager.run()
```

新建目录App, 并在App的init文件中创建app对象

```python
from flask import Flask

# 创建app
def create_app():
	app = Flask(__name__)       
	return app

```

##### 蓝图blueprint

```python
1,宏伟蓝图（宏观规划）
2,蓝图也是一种规划，主要用来规划urls（路由）
3,蓝图基本使用    
  在views.py中初始化蓝图
	blue = Blueprint('first', __name__)
    
  在init文件中调用蓝图进行路由注册
    app.register_blueprint(blueprint=blue)
    
```



#### route路由

```python
路由:
   将从客户端发送过来的请求分发到指定函数上

路由通过装饰器对应视图函数，并且可以接收参数,所以我们只需要在视图函数上使用装饰器即可

语法
  @app.route(‘/rule/’)
  def hello():
      return ‘Hello World!’  
      
  @app.route(‘/rule/<id>/’)
  def hello(id):
      return ‘Hello%s’ % id

写法
	<converter:variable_name>
converter类型
	string 	接收任何没有斜杠（‘/’）的文件（默认）
	int	接收整型
	float	接收浮点型
	path	接收路径，可接收斜线（’/’）
	uuid	只接受uuid字符串，唯一码，一种生成规则
	any	可以同时指定多种路径，进行限定
     	
请求方法
	默认支持GET，HEAD，OPTIONS, 如果想支持某一请求方式，需要自己手动指定
	@app.route(‘/rule/’,methods=[‘GET’,’POST’])
	def hello():
		return ‘LOL’
    
methods中指定请求方法
	GET
	POST
	HEAD 
	PUT
	DELETE
    
url_for
	反向解析，根据函数名字，获取反向路径
    url_for("蓝图名.函数名")
	url_for(‘函数名’,参数名=value)

```

#### Request

```python
服务器在接收到客户端的请求后，会自动创建Request对象
由Flask框架创建，Request对象不可修改

属性
  url  完整请求地址
  base_url  去掉GET参数的URL
  host_url  只有主机和端口号的URL
  path  路由中的路径 *
  method  请求方法 *
  remote_addr  请求的客户端地址  
  args  GET请求参数 *
  form  POST请求参数*
  files  文件上传 
  headers  请求头
  cookies  请求中的cookie
    
ImmutableMultiDict: 类似字典的数据结构, 与字典的区别，可以存在相同的键  
	args和form都是ImmutableMultiDict的对象
ImmutableMultiDict中数据获取方式
	dict['uname'] 或 dict.get('uname)
获取指定key对应的所有值
	dict.getlist('uname')
                             
1. args
   - get请求参数的包装，args是一个ImmutableMultiDict对象，类字典结构对象
   - 数据存储也是key-value
   - 外层是列表，列表中的元素是元组，元组中左边是key，右边是value
2. form
   - 存储结构个args一致
   - 默认是接收post参数
   - 还可以接收 PUT，PATCH参数

```

#### Response

```python
服务器返回给客户端的数据
由程序员创建，返回Response对象
  1. 直接返回字符串, 可以返回文本内容，状态码
  2. render_template 渲染模板，将模板转换成字符串
  3. 通过make_response(data,code)
    - data 返回的数据内容
    - code 状态码
  4. 返回Response对象

重定向
  redirect()
  url_for(‘函数名’,参数=value)

终止执行, 抛出异常
	主动终止 abort(code)

捕获异常
	@app.errorhandler(404)
	def hello(e):
		return ‘LOL’

```

### 作业

1. 熟练掌握虚拟环境搭建和使用
2. 熟悉Flask框架的特点，Flask框架的组成
3. 熟练掌握Flask框架中MVT模式开发
4. 掌握flask-script 插件的使用
5. 掌握蓝图Blueprint的使用
6. 掌握路由Router的使用
7. 掌握请求Request和响应Response的使用
8. 自行了解学习Http协议
9. 预习Day02
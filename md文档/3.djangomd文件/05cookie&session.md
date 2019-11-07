#View & Cookie&Session 
##回顾 

```
多表关系
	1 ：N 一对多 models.ForeignKey()
	N ：N 多对多 models.ManyToManyField()
	1 : 1 一对一 models.OneToOneField()

1:N：
	UserType : User = 1: N
	class UserType:
		name = ''
	class User:
		name = ''
		age = ''
		user_type = models.ForeignKey(Type)
	
	使用对象：
		正向： user.user_type  一个对象
		反向： type.user_set.all()  一个查询集
	使用filter(),get()
		正向: User.objects.filter(user_type__name='')
		反向: UserType.objects.filter(user__name='')
```



##一. View视图 

####HttpRequest 和HttpResponse

```python
Django中的视图主要用来接受Web请求，并做出响应。
视图的本质就是一个Python中的函数
视图的响应分为两大类
	1）以Json数据形式返回 （JsonResponse）
	2）以网页的形式返回
		2.1）重定向到另一个网页 （HttpResponseRedirect）
		2.2）错误视图(40X,50X) （HttpResponseNotFound，HttpResponseForbidden，HttpResponseNotAllowed等）
视图响应过程: 浏览器输入 ->  django获取信息并去掉ip:端口，剩下路径 -> urls 路由匹配 - > 视图响应 -> 回馈到浏览器
视图参数:
	1）一个HttpRequest的实例，一般命名为request
	2）通过url正则表达式传递过来的参数
位置:通常在应用下的views.py中定义
	错误视图:	
		1） 404视图 （页面没找到）
		2） 400视图 （客户操作错误）
		3） 500视图（服务器内部错误）
	自定义错误视图
		在工程的templates文件夹下创建对应的错误文件
		在文件中定义自己的错误样式
		注意需要在关闭Debug的情况下,并设置ALLOWED_HOSTS才可以
		没有关闭Debug的情况下会在界面中直接显示log
```

#####HttpRequest
	服务器在接收到Http请求后，会根据报文创建HttpRequest对象
	视图中的第一个参数就是HttpRequest对象
	Django框架接收到http请求之后会将http请求包装为HttpRequest对象，之后传递给视图。
	
	request常用属性和方法：
		属性:	  path		请求的完整路径
			 	method	请求的方法，常用GET,POST	
				encoding	编码方式，常用utf-8
				GET		类似字典的参数，包含了get的所有参数
				POST		类似字典的参数，包含了post所有参数
				FILES		类似字典的参数，包含了上传的文件
				COOKIES	字典，包含了所有COOKIE
				session		类似字典，表示会话	
		方法: is_ajax()		判断是否是ajax()，通常用在移动端和JS中
			  get_full_path()	 返回包含参数字符串的请求路径.
	
	QueryDict： 类字典的对象
		类似字典的数据结构。与字典的区别:可以存在相同的键。
		QueryDict中数据获取方式
			dict['uname'] 或 dict.get('uname)
			获取指定key对应的所有值
			dict.getlist('uname')
#####HttpResponse
```python
服务器返回给客户端的数据
HttpResponse由程序员自己创建：
	1）不使用模板，直接调用HttpResponse()，返回HttpResponse对象。
	2）调用模板，进行渲染。
		使用render
			render(request,template_name[,context])
			request 		请求体对象
			template_name	模板路径
			context		字典参数，用来填坑

属性:	content		   返回的内容
	 charset		编码格式
	 status_code	响应状态码(200,3xx,404,5xx)
方法
	write(xxx)			直接写出文本 
	flush()				冲刷缓冲区
	set_cookie(key,value='xxx',max_age=None)  设置cookie
	delete_cookie(key)	 删除cookie
	
HttpResponse子类
	HttpResponseRedirect
		响应重定向:可以实现服务器内部跳转
		return HttpResponseRedict('/grade/2017')
		使用的时候推荐使用反向解析
	JsonResponse
		返回Json数据的请求，通常用在异步请求上
			JsonResponse（dict）
		返回json数据时,Content-type是application/json
        
```



##二. Cookie 和 Session

  ####Cookie
```python
	理论上，一个用户的所有请求操作都应该属于同一个会话，而另一个用户的所有请求操作则应该属于另一个会话，二者不能混淆. 而Web应用程序是使用HTTP协议传输数据的。HTTP协议是无状态的协议。一旦数据交换完毕，客户端与服务器端的连接就会关闭，再次交换数据需要建立新的连接。这就意味着服务器无法从连接上跟踪会话。要跟踪该会话，必须引入一种机制。
	Cookie就是这样的一种机制。它可以弥补HTTP协议无状态的不足。在Session出现之前，基本上所有的网站都采用Cookie来跟踪会话。
	Cookie实际上是一小段的文本信息。客户端请求服务器，如果服务器需要记录该用户状态，就使用response向客户端浏览器颁发一个Cookie。客户端浏览器会把Cookie保存起来。当浏览器再请求该网站时，浏览器把请求的网址连同该Cookie一同提交给服务器。服务器检查该Cookie，以此来辨认用户状态。服务器还可以根据需要修改Cookie的内容。
	由于HTTP是一种无状态的协议，服务器单从网络连接上无从知道客户身份。怎么办呢？就给客户端们颁发一个通行证吧，每人一个，无论谁访问都必须携带自己通行证。这样服务器就能从通行证上确认客户身份了。这就是Cookie的工作原理。
	
    cookie本身由服务器生成，通过Response将cookie写到浏览器上，下一次访问，浏览器会根据不同的规则携带cookie过来。
	注意：cookie不能跨浏览器
    
    设置cookie（使用response设置）：
		response.set_cookie(key,value[,max_age=None,expires=None)]
			max_age: 整数 单位为秒，指定cookie过期时间
                      设置为None:浏览器关闭失效,默认值
			expires: 指定过期时间，还支持datetime或timedelta，可以指定一个具体日期时间
                  expires=datetime.datetime(2019, 1, 1, 2, 3, 4)
               或 datetime.datetime.now() + datetime.timedelta(days=10)
			
            注意:max_age和expries两个选一个指定
			# response.set_cookie('username', username, max_age=10)	
			# response.set_cookie("username", username1, expires=d)

	获取cookie(使用request获取)：
		request.COOKIES.get('username')
	删除cookie(使用response删除):
		response.delete_cookie('username')
		
   cookie存储到客户端
   优点：
       数据存在在客户端，减轻服务器端的压力，提高网站的性能。
   缺点：
       安全性不高：在客户端机很容易被查看或破解用户会话信息
```

  ####Session 

1.服务器把数据保存在session中

2.生成sessionid指向这个session

3.通过cookie把sessionid传递给浏览器

```python
	服务器端会话技术,依赖于cookie.
	django中启用SESSION
		settings中
			INSTALLED_APPS：
				'django.contrib.sessions'
			MIDDLEWARE:
				'django.contrib.sessions.middleware.SessionMiddleware'
	基本操作
		设置Sessions值（使用request设置）
		      request.session['user_id'] = user.id
		      request.session.set_expiry(86400)  # 设置过期时间
		      
		获取Sessions值	
			  get(key,default=None) 根据键获取会话的值
		      username = request.session.get("user_id")  
		      # 或 session_name = request.session["session_name"]
		      
		删除Sessions值
			  # 获取当前请求的session的key
			  session_key = request.session.session_key
		      del request.session[session_key]
		      # request.session.delete(session_key)
		   
		clear() 清除所有会话
		flush() 删除当前的会话数据并删除会话的cookie

		数据存储到数据库中会进行编码,使用的是Base64
	每个HttpRequest对象都有一个session属性，也是一个类字典对象.
    
```

#static&media&文件上传&分页 
##一. 静态文件和媒体文件

	媒体文件：用户上传的文件，叫做media
	静态文件：存放在服务器的css,js，image等 叫做static
  ####1. 在django中使用静态文件
```python
	1）首先确保django.contrib.staticfiles在 INSTALLED_APPS中
	2）在settings中定义 STATIC_URL
		STATIC_URL = '/static/'
	3）在你app的static目录中存放静态文件，比如：
		my_app/static/my_app/example.jpg.
	4）如果有别的静态资源文件，不在app下的static目录下，可以通过	
STATICFILES_DIRS来指定额外的静态文件搜索目录。
        STATICFILES_DIRS = [
            os.path.join(BASE_DIR, "static"),
            ...
        ]
    5）在模板中使用load标签去加载静态文件
		{% load static %}
		<img src="{% static "my_app/example.jpg" %}" />
```
  ###2. 在django中使用媒体文件
```python
	在settings中配置 MEDIA_ROOT
		MEDIA_ROOT = os.path.join(BASE_DIR, "media")
```



##二. 文件上传

##### 单文件上传

```python
文件上传要求form表单存在enctype="multipart/form-data"属性，并且提交方法是post。
	<form enctype="multipart/form-data" action="/uploadFile/" method="post"> 
	   <input type="file" name="myfile" />  
	   <br/>  
	   <input type="submit" value="upload"/>  
	</form>
    
最简单的文件上传：
	def file_upload(request):
        if request.method == 'POST':
            # 获取上传的文件，如果没有文件，则默认为None
            myFile = request.FILES.get('myfile', None)
            if not myFile:
                return HttpResponse("no files for upload")

            file_path = os.path.join(settings.MEDIA_ROOT, '1.jpg')
            with open(file_path, 'ab') as fp:
                for part in myFile.chunks():
                    fp.write(part)
            return HttpResponse("上传成功！")

        else:
            return render(request, 'index.html')
```

##### 多文件上传

```python
多文件上传和单文件上传类似
    1.需要在模板文件的form表单input中添加multiple
    2.后台获取时使用request.FILES.getlist('myfile', None)
def file_upload2(request):
    if request.method == 'POST':
        # 获取上传的文件，如果没有文件，则默认为None
        myFiles = request.FILES.getlist('myfile', None)
        for myFile in myFiles:
            if not myFile:
                return HttpResponse("no files for upload")
    
            file_path = os.path.join(settings.MEDIA_ROOT, myFile.name)
            with open(file_path, 'ab') as fp:
                for part in myFile.chunks():
                    fp.write(part)
                    
        return HttpResponse("上传成功！")

    else:
        return render(request, 'index.html')
```



## 三.分页

```python
django提供了分页的工具，存在于django.core中	
	Paginator : 数据分页工具
	Page	: 具体的某一页面

导入Paginator： 	
	from django.core.paginator import Paginator

Paginator:	
对象创建: 
	Paginator(数据集，每一页数据数)
属性:	
	count：对象总数
	num_pages：页面总数
	page_range: 页码列表，从1开始
方法:	
	page(整数): 获得一个page对象

常见错误:	
	InvalidPage：page()传递无效页码
	PageNotAnInteger：page()传递的不是整数
	Empty：page()传递的值有效，但是没有数据
    
Page:
	对象获得，通过Paginator的page()方法获得
属性:
	object_list：	当前页面上所有的数据对象
	number：	当前页的页码值
	paginator:	当前page关联的Paginator对象
方法：
	has_next()	:判断是否有下一页
	has_previous():判断是否有上一页
	has_other_pages():判断是否有上一页或下一页
	next_page_number():返回下一页的页码
	previous_page_number():返回上一页的页码	
	len()：返回当前页的数据的个数

```



##四. 中间件&AOP

```python
中间件：是一个轻量级的，底层的插件，可以介入Django的请求和响应过程（面向切面编程）

Django中间件的本质就是一个python类

面向切面编程（Aspect Oriented Programming）简称AOP。AOP的主要实现目的是针对业务处理过程中的切面进行提取，它所面对的是处理过程中的某个步骤或阶段，以获得逻辑过程中各部分之间低耦合的隔离效果。

中间件可实现功能
   - 统计
   - 黑名单
   - 白名单 
   - 反爬
   - 界面友好化（捕获异常）
```
#### 1 中间件的可切入点

![](AOP.png)

#### 2 切入函数

```python
__init__:
    没有参数，服务器响应第一个请求的时候自动调用，用户确定是否启用该中间件
process_request(self,request):
    在执行视图前被调用，每个请求上都会调用，不主动进行返回或返回HttpResponse对象
process_view(self,request,view_func,view_args,view_kwargs)：
	调用视图之前执行，每个请求都会调用，不主动进行返回或返回HttpResponse对象
process_template_response(self,request,response):
    在视图刚好执行完后进行调用，每个请求都会调用，不主动进行返回或返回HttpResponse对象
process_response(self,request,response):
    所有响应返回浏览器之前调用，每个请求都会调用，不主动进行返回或返回HttpResponse对象
process_exception(self,request,exception):
    当视图抛出异常时调用，不主动进行返回或返回HttpResponse对象
```

#### 3 自定义中间件

```python
自定义中间件流程
	1.在工程目录下创建middleware目录
	2.目录中创建一个python文件
	3.在python文件中导入中间件的基类
		from django.utils.deprecation import MiddlewareMixin
	4.在类中根据功能需求，创建切入需求类，重写切入点方法
        class LearnAOP(MiddlewareMixin):
            def process_request(self,request):
                print('request的路径',request.GET.path)
	5.启用中间件，在settings中进行配置，MIDDLEWARE中添加middleware.文件名.类名
   
```
作业： 1, 自己实现完整的登录注册功能

​	     2, 结合bootstrap实现分页功能 
#URL&模板&Admin

##一、URL

#### 路由匹配

```python
使用url给视图函数传参数
在url配置中将正则部分小括号括起来。比如：
	url(r'^time/plus/(\d{1,2})/$', views.hours_ahead)
如果有多个参数则用/隔开，参数需要用分组，比如：
	url(r'^time/plus/(\d{1,2})/(\d{1,2})/$', views.hours_ahead),
给参数命名，使用正则分组的别名，比如：
	url(r'^time/plus/(?P<time1>\d{1,2})/(?P<time2>\d{1,2})/$', views.hours_ahead)
使用分组别名之后，视图函数的参数必须用分组的别名，但是位置可以不固定。

给url取别名，那么在使用此url的地方可以使用别名。比如：
	url(r'^buy/$', views.buy, name='buy'),
	url(r'^login/$', views.login, name='login'),

Django2.0以上
	# 命名空间 
	path('app/', include(('App.urls', "App"), namespace='App'))
	# url
    path('index/', index)
    path('detail/<int:id>/', index)
    re_path(r'^detail/(\d+)/', detail)
```

#### 反向解析

```python
在视图函数中，反向解析url：
    from django.shortcuts import render, redirect
    from django.urls import reverse
    def buy(request):
        return redirect(reverse('index'))
        return redirect(reverse('detail', args=[2]))
        return redirect(reverse('detail', kwargs={"id": 2}))
	
在templates中，使用别名：
	{% url 'detail' stu.id %}

使用命名空间:
    在工程的urls.py文件中，在include时，可以指定命名空间，更加细化的划分url。比如： 
		url(r'^App/', include('App.urls', namespace='App')),
	指定命令空间后，使用反向解析时需要加上命名空间，比如：
		在视图函数中: return redirect(reverse('students:index'))
		在templates中: {% url 'students:detail' %}
```



##二、模板Template

```python
在Django框架中，模板是可以帮助开发者快速生成呈现给用户页面的工具
模板的设计方式实现了我们MVT中VT的解耦，VT有着N:M的关系，一个V可以调用任意T，一个T可以供任意V使用
模板处理分为两个过程
	加载
	渲染
模板主要有两个部分
	HTML静态代码
	模板语言，动态插入的代码段（挖坑，填坑）
模板中的动态代码段除了做基本的静态填充，还可以实现一些基本的运算，转换和逻辑

模板中的变量: 视图传递给模板的数据，遵守标识符规则
	语法： {{ var }}
	如果变量不存在，则插入空字符串
	
方法不能有参数。
	{{ str }} 
    {{ str.upper }}
    {{ str.isdigit }}
	{{ dict.name }}
列表，使用索引，不允许负索引	
	items= ['apples', 'bananas', 'carrots']
	{{ items.2 }}
	
    
模板中的标签
语法 {%  tag  %}
作用	
	1. 加载外部传入的变量  
	2. 在输出中创建文本
	3. 控制循环或逻辑
if 语句：
	格式:	
	if单分支
		{% if  表达式 %}
	    	语句
		{% endif  %}
        
	if双分支
		{%  if 表达式 %}
	    	语句
		{% else  %}
	    	语句
		{% endif %}
        
	if多分支
		{% if 表达式 %}
        	语句	
 		{% elif 表达式 %}
        	语句
        {% else  %}
	    	语句
		{% endif %}
	
	判断true或false
		{% if today_is_weekend %}
			<p>Welcome to the weekend!</p> 
		{% endif %}
        
	使用 and or not
		{% if athlete_list and coach_list %}
	    	<p>Both athletes and coaches are available.</p>
		{% endif %}
	
		{% if not athlete_list %}
	    	<p>There are no athletes.</p>
		{% endif %}
	
		{% if athlete_list or coach_list %}
	    	<p>There are some athletes or some coaches.</p>
		{% endif %}
				
	使用 in和not in，
		{% if "bc" in "abcdef" %}
			This appears since "bc" is a substring of "abcdef"
		{% endif %}
		{% if user not in users %}
			If users is a list, this will appear if user isn't an element of the list.
		{% endif %}

```


```python
for 语句：
	{% for 变量 in 列表 %}
		语句1 
	{% empty %}
		语句2
	{% endfor %}
	当列表为空或不存在时,执行empty之后的语句
	
	{{ forloop.counter }} 表示当前是第几次循环，从1数数
	{% for item in todo_list %}
	    <p>{{ forloop.counter }}: {{ item }}</p>
	{%endfor %}
	
	{{ forloop.counter0}}表示当前是第几次循环，从0数数
	{{ forloop.revcounter}}表示当前是第几次循环，倒着数数，到1停
	{{ forloop.revcounter0}}表示当前第几次循环，倒着数，到0停
	{{ forloop.first }} 是否是第一个  布尔值
	
    {% for object in objects %}
	    {% if forloop.first %}
	        <li class="first">
	    {% else %}
	        <li>
	    {% endif %}
	    {{ object }}</li>
	{% endfor %}
	
	{{ forloop.last }} 是否是最后一个 布尔值
	{% for link in links %}
		{{ link }}{% if not forloop.last %} | {% endif %}
	{% endfor %}
	
	forloop.parentloop
	{% for country in countries %}
	  <table>
	      {% for city in country.city_list %}
	      <tr>
	          <td>Country #{{ forloop.parentloop.counter }}</td>
	          <td>City #{{ forloop.counter }}</td>
	          <td>{{ city }}</td>
	      </tr>
	      {% endfor %}
	  </table>
	 {% endfor %}
	 
注释：
	单行注释
	{#  被注释掉的内容  #}

	多行注释
	{% comment %}
		内容
	{% endcomment %}
	
过滤器: 
	{{ var|过滤器 }}
	作用：在变量显示前修改
	
	add	{{ value|add:2 }}
	没有减法过滤器，但是加法里可以加负数
		{{ value|add:-2 }}
	lower 	
		{{ name|lower }}
	upper
		{{ my_list|first|upper }}
	截断：
		{{ bio|truncatechars:30 }}
	过滤器可以传递参数，参数需要使用引号引起来
	比如join：	{{ students|join:'=' }}
	
	默认值:default，格式 {{var|default:value}}
	如果变量没有被提供或者为False，空，会使用默认值

	根据指定格式转换日期为字符串，处理时间的
	就是针对date进行的转换	
		{{  dateVal | date:'y-m-d' }}
		
HTML转义
	将接收到的数据当成普通字符串处理还是当成HTML代码来渲染的一个问题
	渲染成html:{{ code|safe }}
	
模板继承
	block:
		{% block XXX%}
			code
		{% endblock %}

	extends 继承，写在开头位置
		{% extends '父模板路径' %}

	include: 加载模板进行渲染
         {% include '模板文件' %}

    {{ block.super }} : 获取父模板中block中的内容
    
```



## 三、Admin


####1. django admin后台系统

```python
Django中默认集成了后台数据管理页面，通过简单的配置就可以实现模型后台的Web控制台。
管理界面通常是给系统管理员使用的，用来完成数据的输入，删除，查询等工作。
使用以下models来示范admin后台系统的用法。

创建一个项目, 用来说明出版社, 书籍和作者的关系。
   假定关系：作者：书籍 => 1:n  （一本书由一个作者完成， 一个作者可以创作多本书）
 	  	  出版社：书籍 => n:n  （一个出版社可以出版多本书， 一本书可以由多个出版社出版）

要求:
    1. 创建作者author, 出版社publisher，书籍book三个应用.
    2. 给每个应用分别创建首页index.html,且可以在浏览器打开index页面.
    3. 在书籍的index.html中有一个"查看所有书籍"的超链接按钮，点击进入书籍列表bool_list.html页面.
    4. 在书籍book_list.html中显示所有书名，点击书名可以进入书籍详情book_detail.html
    5. 在书籍book_detail.html中可以点击该书的作者和出版社，进入作者的author_detail.html和出版社的publisher_detail.html页面

models.py内容如下:
	# 出版社
	class Publisher(models.Model):
        name = models.CharField(max_length=30)
        address = models.CharField(max_length=100)
        city = models.CharField(max_length=30)
        state_province = models.CharField(max_length=30)
        country = models.CharField(max_length=20)
        website = models.URLField()
        
	# 作者
	class Author(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        email = models.EmailField()
        gender = models.BooleanField(default=True)

	# 书籍
	class Book(models.Model):
        title = models.CharField(max_length=100)
        publish_date = models.DateField()
        author = models.ForeignKey(Author)  # 外键，book:author = N:1
        publishers = models.ManyToManyField(Publisher)  # 多对多关系，book:publisher=N:N
	
    # author: 是指向Author对象， 不是id
    # publishers.all() : 多个出版社组成的列表(查询集)
    # author.book_set.all() : 反向查找
    # publisher.book_set.all() : 反向查找
        
使用admin后台系统之前，需要先创建一个系统管理员,创建管理员之前需先同步数据库。
	python manager.py createsuperuser
设置为中文
	settings中LANGUAGE_CODE = 'zh-hans'
设置时间，时区
	TIME_ZONE='Asia/Shanghai'

添加自己的数据模型,在admin.py中注册: 
	admin.site.register(Publisher)
	admin.site.register(Author)
	admin.site.register(Book)
在admin中给model添加数据。
给模型加上__str__函数，比如给Author模型添加str函数，让author的显示更加友好：
	def __str__(self):
    	return '%s %s' % (self.first_name, self.last_name)

希望控制admin中添加model数据时的动作，可以修改相应字段的属性。
比如author的email字段运行添加的时候为空，可以在email字段定义中加上 blank=True(可以空白),
比如book的publication_date添加 blank=True, null=True（可以为null）属性。
修改models属性之后记得及时做数据迁移。

使用verbose_name属性指定字段的别名:
    比如给publisher的name字段指定一个中文的别名verbose_name='出版社名称'。
	在models的修改页面，默认显示的是models定义的str函数返回的字符串。
            
```

#### 2. 定制admin

```python
通过定义MoldelAdmin来定制model在admin的表现。比如给Author定义AuthorAdmin。
	class AuthorAdmin(admin.ModelAdmin):
		list_display = ('first_name', 'last_name', 'email')
	相应的注册代码也要变化：
	admin.site.register(Author, AuthorAdmin)

给Author添加一个搜索框：
	search_fields = ('first_name', 'last_name')
给book添加一个过滤器
	list_filter = ('publication_date',)
	过滤器不光可以作用在日期字段上，还可以作用在boolean类型和外键上。
	另一种增加日期过滤的方式：
	date_hierarchy = 'publication_date'
字段排序：
	ordering = ('-publication_date',)
	
修改编辑页面显示的字段及显示顺序，默认按照models中字段的定义顺序显示：
	fields = ('title', 'authors', 'publisher', 'publication_date')
与fields相反的字段是exclude
	exclude = ['publication_date',] 
改善多对多关系中对象选择操作，比如给BookAdmin添加如下属性：
	filter_horizontal = ('authors',)
filter_horizontal和filter_vertical 选项只适用于多对多关系。

一对多的外键关系，admin使用select box下拉菜单来表示。如不想用select box，可添加如下属性，让原来一次性加载所有publisher的select box变成填写publisher的id：
	raw_id_fields = ('publisher',)

让字段分组显示，fieldsets和上面提到的field不能同时出现：
	fieldsets = (
    	('作者', {'fields': ('authors',)}),
    	('出版商', {'fields': ('publisher',)}),
	)

定制list_display字段的显示。比如给Author加一个布尔型gender字段，来表示性别。为了让显示更加人性化：
	# 定制显示属性
    def showgender(self):
        if self.gender:
            return '男'
        else:
            return '女'
    list_display = ('first_name', 'last_name', 'email', showgender)
给该函数设置简短描述，让显示更加友好：
	showgender.short_description = '性别'	

可以将modeladmin的属性简单划分为列表页属性和添加、修改页属性

# 列表页属性
list_display,list_filter,search_fields,list_per_page等

# 添加、修改页属性
fields ,fieldsets, filter_horizontal, raw_id_fields等
```

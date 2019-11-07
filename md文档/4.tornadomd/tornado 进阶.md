## tornado 进阶

### 一，项目优化：

#### 1，目录结构



```bash
├── app
│   ├── __init__.py		
│   ├── urls.py                 #url放的地方
│   └── views.py				#类视图放的地方
├── manager.py					#运行app
├── static						#静态文件
└── templates					#模板
    ├── index.html
    └── login.html
    
```



#### 2,文件，

##### 	urls.py

```python
from tornado.web import url
from app.views import *


urlpatterns = [
        url(r'/index/', IndexHandler, name='index'),
        url(r'/login/', LoginHandler, name='login'),
        url(r'/logout/', LogoutHandler, name='logout'),
    ]
```



##### 	views.py

```python
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_cookie('username')
        print(username,type('username'))
        self.render('index.html', username=username)
```

​	

​	__init__.py



```python
import tornado.web
from app.urls import urlpatterns
import os
from tornado.options import options

def make_app():
    return tornado.web.Application(handlers=urlpatterns,
    template_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates'),
    static_path= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static'),
    debug=options.debug,
    )


```

##### 	manage.py



```python
import tornado.ioloop
from app import make_app
from tornado.options import define, options, parse_command_line


define('port', default=8080)
define('debug', default=True)

parse_command_line()

app = make_app()

app.listen(options.port)

tornado.ioloop.IOLoop.current().start()
```

------



## 二，模板：

​	挖坑

```
        {% block title %}
        {% end %}
    
    继承
    	{% extends 'base.html' %}

        {% block css %}
            <!--第一种加载方式: 直接定义静态文件的路径-->
            <!--<link rel="stylesheet" href="/static/css/style.css">-->
            <!--第二种加载方式-->
            <link rel="stylesheet" href="{{ static_url('css/style.css') }}">

        {% end %}
```

##### 	逻辑：标签: {% 标签名 %}  {% end %}

###### 		if标签: 

​			{%  if  条件%}  

​			{% end %}

​			

​			{% if 条件 %} 

​			 {% elif 条件%} 

​			{% else %} 

​			 {% end %}

###### 		for标签: 

###### 			{% for 变量 in [] %}  {% end %}

​		

##### 	变量：变量: {{ 变量名 }}

​		

##### 	注释：注解: {# 注解内容 #}



### 三，模型：

​	tornado,没有集成orm对象，我们可以调用第三方的库，sqlalchemy

​	安装

​		pip install sqlalchemy



​	使用：

​		初始化：

​		

```python
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker

    # 连接数据库格式
    # mysql+pymysql://root:123456@127.0.0.1:3306/tornado9
    db_url = 'mysql+pymysql://root:123456@127.0.0.1:3306/tornado9'

    # 创建引擎，建立连接
    engine = create_engine(db_url)

    # 模型与数据库表进行关联的基类，模型必须继承于Base
    Base = declarative_base(bind=engine)

    # 创建session会话
    DbSession = sessionmaker(bind=engine)
    session = DbSession()
    
    
    	创建orm类
        
        
    from sqlalchemy import Column, Integer, String

    from utils.conn import Base


    def create_db():
        # 映射模型对应的表
        Base.metadata.create_all()


    def drop_db():
        # 删除模型映射的表
        Base.metadata.drop_all()


    class Student(Base):
        # 主键自增的int类型的id主键
        id = Column(Integer, primary_key=True, autoincrement=True)
        # 定义不能为空的唯一的姓名字段
        s_name = Column(String(10), unique=True, nullable=False)
        s_age = Column(Integer, default=18)

        __tablename__ = 'student'

        # def __repr__(self):
        
        
		
        

```

增

​	

```python

    # 创建单条数据
    # stu = Student()
    # stu.s_name = 'xiaoming'
    # session.add(stu)
    # session.commit()
    # 创建多条数据
    stus = []
    for i in range(10):
        stu = Student()
        stu.s_name = 'xiaoming_%s' % i
        stus.append(stu)

    session.add_all(stus)
    session.commit()

```



删



​	session.query(User).filter_by(age=2).delete()

​	session.query(User).filter(User.id==1).delete()

​	session.commit()

​	对象删

​	user = session.query(User).get(4)

​	session.delete(user)

​	session.commit()



改

​	用filter改

​	session.query(User).filter(User.id<4,User.id>=2).update({'age':2})   #传字典

​	session.commit()

​	用对象改

​	user = session.query(User).get(3)

​	user.name = ‘changjia'

​	session.commit()

查

​	

```python
	#根据id查询，获取一个类的对象

	session.query(User).get(2)

	#批量查询
    #查询所有记录
    session.query(User).all()

	#filter_by

	session.query(User).filter_by(name='lala').all()
    
    #filter
    first() 取到第一个
    count() 总数
    
    session.query(User).filter(User.name=='lala').all()
    session.query(User).filter(User.id >=1).all()
    session.query(User).filter(User.id < 10).all()
    session.query(User).filter(User.id <=1).all()
    
    session.query(User).filter(User.name.startswith('la')).all()
    session.query(User).filter(User.name.endswith('la')).all()
    session.query(User).filter(User.name.contains('y')).all()
    
    session.query(User).filter(User.id<4,User.id>=2).all()
    
   from sqlalchemy import or_, and_,not_ 
```

​	session.query(User).filter(or_(User.id > 3, User.id <2)).all()

​	
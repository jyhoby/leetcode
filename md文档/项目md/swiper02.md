#### 01.定时执行任务

- ##### celery定时执行任务

  - 在worker包中的`__init__`文件中加入如下配置

    ```python
    from celery.schedules import crontab
    from datetime import timedelta
    
    ...
    ...
    ...
    
    celery_app.conf.update(   # 固定写法
        CELERYBEAT_SCHEDULE={ # 固定写法
            'sum-task': {  # 名字随便命名
                'task': 'common.func.add',  # 导入异步任务
                'schedule': timedelta(seconds=5), # 定时时间
                'args': (5, 6)  # 异步任务函数的参数
            }
        }
    )
    
    '''
    schedule中定时时间有两种方式
    - timedelta方法
        days：天
        seconds：秒
        microseconds：微妙
        milliseconds：毫秒
        minutes：分
        hours：小时	
    - crontab方法
    		month_of_year：月份
        day_of_month：日期
        day_of_week：周
        hour：小时
        minute：分钟
        
        例子
        crontab()  每分钟
        crontab(minute=0, hour=0)  每天的0时0分
        crontab(minute=0, hour='*/3')  每三小时
        crontab(day_of_week='sunday')  周日的每一小时
        crontab(minute='*',hour='*', day_of_week='sun') 与上面相同
    '''
    ```

  - 在common包的func.py中定义add异步任务

    ```python
    @celery_app.task
    def add(x,y):
        return x * y
    ```

  - 同时启动worker和定时任务

    ```python
    celery worker -A worker -l info -B
    ```

- ##### Linux定时任务：contrab

  - 判断cron服务有没有启动，命令：

    ps -ef | grep cron

    启动命令：sudo service cron start

    关闭命令：sudo service cron stop

    重启命令：sudo service cron restart

    重新载入配置文件：sudo service cron reload

     

  - 编辑crontab

    命令：sudo crontab -e

    第一次编辑crontab，会让我们选择使用的编辑器，一般选择第三个vim

    如果选错了，可以执行sudo select-editor 重新选择

    进入编辑页面就可以添加执行的任务

   

  - 查看crontab任务

    命令：sudo crontab -l

    会列出当前用户添加的所有任务

   

  - 清空crontab任务

    命令：sudo crontab -r

    删除当前用户设置的所有任务

    

  - 配置说明

    - 1-10   */2   *   *   *   python3 /etc/a.py

    - crontab中的每一行代表一个定期执行的任务，分为6个部分。前5个部分表示何时执行命令，最后一个部分表示执行的命令。

    - 每个部分以空格分隔，除了最后一个部分（命令）可以在内部使用空格之外，其他部分都不能使用空格。

    - 前5个部分分别代表：分钟，小时，天，月，星期，每个部分的取值范围如下：
      - 分钟         0 - 59
      - 小时         0 - 23
      - 天           1 - 31
      - 月           1 - 12
      - 星期         0 - 6       0表示星期天

    - 除了这些固定值外，还可以配合星号（*），逗号（,），短横线（-）和斜线（/）来表示一些其他的含义：

      - 星号：表示任意值，比如在小时部分填写* 代表任意小时（每小时）

      - 逗号：可以允许在一个部分中填写多个值，比如在分钟部分填写1,3 表示一分钟或三分钟

      - 斜线：一般配合* 使用，代表每隔多长时间，比如在小时部分填写*/2 代表每隔两小时。所以*/1 和* 没有区别

      - 短横线：表示范围，比如在分钟部分填写1-10 代表从第一分钟到第十分钟

        

  - 例子: 

    ```python
    #每天早上7点
    0 7 * * * 
    
    #在12 月内, 每天的早上6 点到12 点中，每隔3个小时执行一次
    0 6-12/3  * 12 *
     
    #周一到周五每天下午5:00
    0 17 * * 1-5
    
    #每月每天的午夜0 点20 分, 2 点20 分, 4 点20 分...
    20 0-23/2 * * *
    
    #每小时的第10和第15分钟
    10,15 * * * *
    
    #每分钟执行一次
    * * * * * 
    ```

- ##### django中的定时任务

  - 1.安装 django-crontab

    ```python
    pip install django-crontab
    ```

  - 2.注册 django-crontab 应用

    ```python
    INSTALLED_APPS = [    
        'django_crontab', # 定时任务
    ]
    ```

  - 3.设置定时任务

    ```python
    定时时间基本格式 :
    
    *  *  *  *  *
    
    分 时 日  月  周    命令
    
    M: 分钟（0-59）。每分钟用 * 或者 */1 表示
    H：小时（0-23）。（0表示0点）
    D：天（1-31）。
    m: 月（1-12）。
    d: 一星期内的天（0~6，0为星期天）。
      
      
    在配置文件settings中定义
    CRONJOBS = [
        ('* * * * *', 'common.func.print_info')
    ]
    
    
    解决 crontab 中文问题
    在定时任务中，如果出现非英文字符，会出现字符异常错误
    CRONTAB_COMMAND_PREFIX = 'LANG_ALL=zh_cn.UTF-8'
    ```

  - 4.管理定时任务

    ```python
    # 添加定时任务到系统中
    python manage.py crontab add
    
    # 显示已激活的定时任务
    python manage.py crontab show
    
    # 移除定时任务
    python manage.py crontab remove
    ```



#### 02.个人资料接口规划

- 接口
  1. 获取个人资料接口
  2. 修改个人资料接口
  3. 上传个人头像接口
     - 参数：
     -  （头像的图片）



- Profile 模型设计 (仅作参考)

| Field          | Description              |
| -------------- | ------------------------ |
| location       | 目标城市                 |
| min_distance   | 最小查找范围             |
| max_distance   | 最大查找范围             |
| min_dating_age | 最小交友年龄             |
| max_dating_age | 最大交友年龄             |
| dating_sex     | 匹配的性别               |
| vibration      | 开启震动                 |
| only_matche    | 不让为匹配的人看我的相册 |
| auto_play      | 自动播放视频             |

- 数据库表关系的构建

  - 关系分类
    - 一对一关系
    - 一对多关系
    - 多对多关系

- 外键的优缺点
  - 优点:
    - 由数据库自身保证数据一致性和完整性, 数据更可靠
    - 可以增加 ER 图的可读性
    - 外键可节省开发量
  - 缺点:
    - 性能缺陷, 有额外开销
    - 主键表被锁定时, 会引发外键对应的表也被锁
    - 删除主键表的数据时, 需先删除外键表的数据
    - 修改外键表字段时, 需重建外键约束
    - 不能用于分布式环境
    - 不容易做到数据解耦

- 手动构建关联

  - 一对一: 主表 id 与 子表 id 完全一一对应
  - 一对多: 在 "多" 的表内添加 "唯一" 表 id 字段
  - 多对多: 创建关系表, 关系表中一般只存放两个相关联的条目的 id

- 对子表关联操作

  ```python
  class User(models.Model):
      ...
      demo_id = models.IntegerField()
      ...
  
      @property
      def demo(self):
          if not hasattr(self, '_demo'):
              return self._demo, _ = Demo.objects.get_or_create(id=self.demo_id)
          return self._demo
  
  class Demo(models.Model):
      xxx = models.CharField()
      yyy = models.CharField()
      
  user = User.objects.get(id=123)
  
  print(user.demo.xxx)
  print(user.demo.yyy)
  ```

#### 03.类视图

- 定义

  ```python
  from django.views.generic import View
  
  class RegisterView(View):
      """类视图：处理注册"""
  
      def get(self, request):
          """处理GET请求，返回注册页面"""
          return render(request, 'register.html')
  
      def post(self, request):
          """处理POST请求，实现注册逻辑"""
          return HttpResponse('这里实现注册逻辑')
  ```

- 使用

  ```python
  urlpatterns = [
      url(r'^register/$', views.RegisterView.as_view()),
  ]
  ```

- 添加装饰器

  ```python
  def my_decorator(func):
      def wrapper(request, *args, **kwargs):
          print('自定义装饰器被调用了')
          print('请求路径%s' % request.path)
          return func(request, *args, **kwargs)
      return wrapper
    
  from django.utils.decorators import method_decorator
    
  # 为全部请求方法添加装饰器
  @method_decorator(my_decorator, name='dispatch')
  class DemoView(View):
      def get(self, request):
          print('get方法')
          return HttpResponse('ok')
  
      def post(self, request):
          print('post方法')
          return HttpResponse('ok')
  
  
  # 为特定请求方法添加装饰器
  @method_decorator(my_decorator, name='get')
  class DemoView(View):
      def get(self, request):
          print('get方法')
          return HttpResponse('ok')
  
      def post(self, request):
          print('post方法')
          return HttpResponse('ok')
        
       
  # 为特定请求方法添加装饰器
  class DemoView(View):
  
      @method_decorator(my_decorator)  # 为get方法添加了装饰器
      def get(self, request):
          print('get方法')
          return HttpResponse('ok')
  
      @method_decorator(my_decorator)  # 为post方法添加了装饰器
      def post(self, request):
          print('post方法')
          return HttpResponse('ok')
  
      def put(self, request):  # 没有为put方法添加装饰器
          print('put方法')
          return HttpResponse('ok')
  
  ```

  
#### 01.项目介绍

- 需求分析
    Swiper Social 是一个类似于 “探探” 的社交类程序, 主要包含以下模块：

  - 个人模块
    - 登陆
    - 注册
    - 个人信息
  - 社交模块
    - 喜欢
    - 不喜欢
    - 超级喜欢
  - vip模块
    - 超级喜欢
    - 反悔
    - 查看喜欢我的人
  
- 项目架构设计

    Swiper Social 采用前后端分离，前端采用vue框架，后端采用django框架。使用restful风格的接口

    形式进行数据交互，架构总结：

  - 使用git作为协同开发工具
  - 使用mysql储存数据
  - 使用redis作为数据的缓存工具
  - 使用celery异步处理数据
  - 使用nginx做反向代理
  - 使用gunicorn作为动态服务器
  - 外部接口：云之讯、七牛



#### 02.restful介绍

- 定义：路径中只包含名词(操作的资源名称，也就是表名字)，不能包含动词

- 例子： user表

  - 获取全部用户
    - 旧 ：/getalluser   get
    - 新：/user    get
  - 获取id为1的用户
    - 旧：/getuser/?id=1   get
    - 新:  /user/1    get
  - 增加用户
    - 旧：/adduser    post
    - 新：/user    post
  - 修改id为1的用户
    - 旧：/updateuser/?id=1    post
    - 新：/user/1    put
  - 删除id为1的用户
    - 旧：/deleteuser/?id=1    post
    - 新:   /user/1    delete
  
- http动词

  - get    查询
  - post   增加
  - put    修改
  - delete  删除

- 过滤信息

  - 返回记录的数量    /?limit=10
  - 分页   /?page=5
  - 排序  /?order=id

- 状态码 (请求服务器有没有成功)

  - 200 OK ：服务器成功返回用户请求的数据
  - 403 Forbidden ：表示用户得到授权（与401错误相对），但是访问是被禁止的。
  - 404 NOT FOUND ：用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的。
  - 500 INTERNAL SERVER ERROR ：服务器发生错误，用户将无法判断发出的请求是否成功

- 状态码（逻辑处理有没有成功），需要自定义

  - 0：成功
  - 1000：用户名不能为空
  - 1001：用户名格式不正确
  - 1002：手机格式不正确

  - 1003：用户不存在

    。。。

- 返回json格式

  - 获取全部用户

    ```python
    {
      'code': 0  # 状态码
      'data': [
        {'name':'ben', 'age':20},
        {'name':'ben', 'age':20},
        {'name':'ben', 'age':20},
        {'name':'ben', 'age':20},
      ]
    }
    ```
  
    
  
  - 获取id为1的用户
  
    ```python
    {
      'code': 0  # 状态码
      'data': {
        'id': 1
        'name':'ben', 
        'age':20
      }
    }
    ```
  
    
  
  - 增加用户
  
    ```python
    {
      'code': 0  # 状态码
      'data': '增加成功'
    }
    ```
  
    
  
  - 修改id为1的用户
  
    ```python
    {
      'code': 0  # 状态码
      'data': '修改成功'  # 也可以返回修改用户的信息，但是不是必须的，按照前端的要求
    }
    ```
  
    
  
  - 删除id为1的用户
  
    ```python
    {
      'code': 0  # 状态码
      'data': '删除成功'  # 也可以返回删除用户的信息，但是不是必须的，按照前端的要求
    }
    ```
  
    
  
  - 返回错误信息
  
    ```python
    {
      'code': 0  # 自定义的错误状态码
      'data': '错误信息'
    }
    ```
  
    
  
  

#### 03.git项目协同开发简易流程

1. 项目管理者在码云或者github上面创建项目
   - master:  主干分支, 用来发布项目到线上，只有项目管理员可以操作
   - develop：测试分支，用来测试功能，项目组人员只能把代码推送到该分支
   
2. 项目管理者把项目clone到本地，创建底层代码

   ```python
   git clone http://xxx
   ```

   

3. 项目管理者在本地创建并切换到develop分支，把代码push到码云上面

   ```python
   git checkout -b develop
   git push origin develop
   ```

   

4. 项目组的开发人员初始化代码需要clone项目到本地，以后在修改代码之前，必须先pull以下最新的代码，防止冲突

   ```python
   git clone http://xxx
   ```

   

5. 项目组开发人员创建并切换到develop分支，拉取码云上develop分支上的代码

   ```python
   git checkout -b develop
   git pull origin develop
   ```

   

6. 项目组开发人员开发功能，完成后把代码push到码云的develop分支

   ```python
   git push origin develop
   ```

   

7. 项目完成后，项目管理者从码云的develop分支拉取代码，并测试功能

   ```python
   git pull origin develop
   ```

   

8. 项目管理者测试没问题，切换到本地的master分支，合并develop分支的代码。

   ```python
   git checkout master
   git merge develop
   ```

   

9. 项目管理者把代码推送到码云的master分支

   ```python
   git push
   ```

   

10. 项目管理者操作线上服务器，拉取码云的master分支的代码

   ```python
   git pull
   ```

   

![image-20190820145324569](swiper.assets/image-20190820145324569.png)



#### 04.用户中心模块

- 接口

  - 获取短信验证码

    - 参数： phone:手机号

    - 方式：post

    - 发送短信：用云之讯

    - celery异步发送短信

      - 安装celery和django-redis

      - 在根目录创建一个worker的包

      - 在包的`__init__`实例化celery对象

        ```python
        import os
        
        from celery import Celery
        
        from worker import config
        
        # 加载django的环境
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swiper.settings")
        
        # 实例化celery
        celery_app = Celery('swiper')
        
        # 加载配置文件
        celery_app.config_from_object(config)
        
        # 自动注册任务
        celery_app.autodiscover_tasks()
        
        ```

      - 创建一个配置文件config.py，存放celery的配置

        ```python
        broker_url = 'redis://127.0.0.1:6379/0'
        ```

      - 在封装的异步函数里面用户celery来装饰这个函数

        ```python
        from worker import celery_app
        
        @celery_app.task
        def send_sms_celery(phone):
          pass
        ```

      - 启动celery

        ```python
        celery worker -A worker -l info
        ```

      - 把任务放到异步的celery里面执行

        ```python
        send_sms_celery.delay(phone)
        ```

        

  - 通过验证码登录、注册

    - 参数： phone：手机号    code：验证码
    - 方式：post

  - 获取个人资料

  - 修改个人资料

  - 头像上传

- 模型

  User 模型设计 (**仅作参考**)  # 保存用户的主要信息

  | Field       | Description |
  | ----------- | ----------- |
  | phonenum    | 手机号      |
  | nickname    | 昵称        |
  | sex         | 性别        |
  | birth_year  | 出生年      |
  | birth_month | 出生月      |
  | birth_day   | 出生日      |
  | avatar      | 个人形象    |
  | location    | 常居地      |

  Profile 模型设计 (仅作参考)   # 保存用户设置交友的资料

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

- redis做缓存
  - 安装 `pip install django-redis`

  - settings 配置

    ```python
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379/0",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                "PICKLE_VERSION": -1,
            }
        }，
        "session": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379/2",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                "PICKLE_VERSION": -1,
            }
        }
    }
    ```

- 指定session的保存方案

  ```python
  SESSION_ENGINE = "django.contrib.sessions.backends.cache"
  SESSION_CACHE_ALIAS = "session"
  ```

  

- 模型对象转换成字典

  ```python
  def to_dict(self):
      '''创建模型的属性字典'''
      attr_dict = {}
      for field in self._meta.get_fields():
          name = field.attname
          attr_dict[name] = getattr(self, name)
      return attr_dict
  ```



#### 05.Celery 及异步任务的处理

1. 模块组成

   ![celery](swiper.assets/celery.png)

   - 任务模块 Task

     包含异步任务和定时任务. 其中, 异步任务通常在业务逻辑中被触发并发往任务队列, 而定时任务由 Celery Beat 进程周期性地将任务发往任务队列.

   - 消息中间件 Broker

     Broker, 即为任务调度队列, 接收任务生产者发来的消息（即任务）, 将任务存入队列. Celery 本身不提供队列服务, 官方推荐使用 RabbitMQ 和 Redis 等.

   - 任务执行单元 Worker

     Worker 是执行任务的处理单元, 它实时监控消息队列, 获取队列中调度的任务, 并执行它.

   - 任务结果存储 Backend

     Backend 用于存储任务的执行结果, 以供查询. 同消息中间件一样, 存储也可使用 RabbitMQ, Redis 和 MongoDB 等.

2. 安装

   ```
   pip install celery
   ```

3. 创建实例

   ```python
   import time
   from celery import Celery
   
   broker = 'redis://127.0.0.1:6379'
   backend = 'redis://127.0.0.1:6379/0'
   app = Celery('my_task', broker=broker, backend=backend)
   
   @app.task
   def add(x, y):
       time.sleep(5)     # 模拟耗时操作
       return x + y
   ```

4. 启动 Worker

   ```
   celery worker -A tasks --loglevel=info
   ```

5. 调用任务

   ```python
   from tasks import add
   
   add.delay(2, 8)
   ```

6. 常规配置

   ```python
   broker_url = 'redis://127.0.0.1:6379/0'
   broker_pool_limit = 1000  # Borker 连接池, 默认是10
   
   timezone = 'Asia/Shanghai'
   accept_content = ['pickle', 'json']
   
   task_serializer = 'pickle'
   result_expires = 3600  # 任务过期时间
   
   result_backend = 'redis://127.0.0.1:6379/0'
   result_serializer = 'pickle'
   result_cache_max = 10000  # 任务结果最大缓存数量
   
   worker_redirect_stdouts_level = 'INFO'
   ```

7. 在django环境中执行celery

   ```python
   import os
   
   from celery import Celery
   
   from worker import config
   
   # 加载django的环境
   os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_swiper.settings")
   
   # 实例化celery
   celery_app = Celery('swiper')
   
   # 加载配置文件
   celery_app.config_from_object(config)
   
   # 自动注册任务
   celery_app.autodiscover_tasks()
   
   ```

#### 06.redis保存在硬盘

redis会把数据从内存同步到硬盘里面

- rdb （默认）

  通过配置文件设置，比如说9分钟如果存储的redis有100个，那么就把这100个数据写进硬盘

- aof

  实时把redis的增删改成的语法保存在文件里面，实时去执行这个文件把数据保存在硬盘
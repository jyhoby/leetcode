## Social 模块开发-2

- 反悔 (每天允许返回 3 次)
- 查看喜欢我的人
- 查看好友信息列表



## VIP、权限模块功能

- 增加权限
- 列出所有权限

1. VIP 分类
   - 非会员
   - 一级会员
   - 二级会员
   - 三级会员
2. 权限分类
   - 超级喜欢
   - 每日反悔 3 次
   - 查看喜欢过我的人
3. 权限分配
   - 非会员: 无任何权限
   - 一级会员: 超级喜欢
   - 二级会员: 超级喜欢 + 反悔3次
   - 三级会员: 超级喜欢 + 反悔3次 + 查看喜欢过我的人

#### 开发难点

1. User 与 VIP 的关系
   - 一种 VIP 对应多个 User
   - 一个 User 只会有一种 VIP
   - 结论: 一对多关系
2. VIP 与权限 的关系
   - 一种 VIP 级别对应多种权限
   - 一个权限会属于在多种级别的 VIP
   - 结论: 多对多关系
3. 如何针对每个接口进行相应的权限检查 ?

#### 模型设计

1. VIP (会员)

   | Field | Description |
   | ----- | ----------- |
   | name  | vip分类名称 |
   | level | 等级        |
   | price | 价格        |

2. Permission (权限)

   | Field       | Description |
   | ----------- | ----------- |
   | name        | 权限名称    |
   | description | 权限说明    |

3. VipPermRelation（vip和权限对应表）

   | Field   | Description |
   | ------- | ----------- |
   | vip_id  | vipid       |
   | perm_id | 权限id      |

   

## Redis 的使用

1. [Redis 文档](http://redisdoc.com/)

2. 主要数据类型

   - **String 类**: 常用作普通缓存

     | CMD   | Example                   | Description                    |
     | ----- | ------------------------- | ------------------------------ |
     | set   | set('a', 123)             | 设置值                         |
     | get   | get('a')                  | 获取值                         |
     | incr  | incr('a')                 | 自增                           |
     | decr  | decr('a')                 | 自减                           |
     | mset  | mset(a=123, b=456, c=789) | 设置多个值                     |
     | mget  | mget(['a', 'b', 'c'])     | 获取多个值                     |
     | setex | setex('kk', 21, 10)       | 设置值的时候, 同时设置过期时间 |
     | setnx | setnx('a', 999)           | 如果不存在, 则设置该值         |

   - **Hash 类**: 常用作对象存储    # 一般存储和数据表结构相似的数据

     | CMD     | Example                          | Description                               |
     | ------- | -------------------------------- | ----------------------------------------- |
     | hset    | hset('obj', 'name', 'hello')     | 在哈希表 obj 中添加一个 name = hello 的值 |
     | hget    | hget('obj', 'name')              | 获取哈希表 obj 中的值                     |
     | hmset   | hmset('obj', {'a': 1, 'b': 3})   | 在哈希表中设置多个值                      |
     | hmget   | hmget('obj', ['a', 'b', 'name']) | 获取多个哈希表中的值                      |
     | hgetall | hgetall('obj')                   | 获取多个哈希表中所有的值                  |
     | hincrby | hincrby('obj', 'count')          | 将哈希表中的某个值自增 1                  |
     | hdecrby | hdecrby('obj', 'count')          | 将哈希表中的某个值自减 1                  |

   - **List 类**: 常用作队列(消息队列、任务队列等)

     | CMD   | Example                 | Description                                       |
     | ----- | ----------------------- | ------------------------------------------------- |
     | lpush | lpush(name, *values)    | 向列表左侧添加多个元素                            |
     | rpush | rpush(name, *values)    | 向列表右侧添加多个元素                            |
     | lpop  | lpop(name)              | 从列表左侧弹出一个元素                            |
     | rpop  | rpop(name)              | 从列表右侧弹出一个元素                            |
     | blpop | blpop(keys, timeout=0)  | 从列表左侧弹出一个元素, 列表为空时阻塞 timeout 秒 |
     | brpop | brpop(keys, timeout=0)  | 从列表右侧弹出一个元素, 列表为空时阻塞 timeout 秒 |
     | llen  | llen(name)              | 获取列表长度                                      |
     | ltrim | ltrim(name, start, end) | 从 start 到 end 位置截断列表                      |

   - **Set 类**: 常用作去重

     | CMD       | Example                | Description                         |
     | --------- | ---------------------- | ----------------------------------- |
     | sadd      | sadd(name, *values)    | 向集合中添加元素                    |
     | sdiff     | sdiff(keys, *args)     | 多个集合做差集                      |
     | sinter    | sinter(keys, *args)    | 多个集合取交集                      |
     | sunion    | sunion(keys, *args)    | 多个集合取并集                      |
     | sismember | sismember(name, value) | 元素 value 是否是集合 name 中的成员 |
     | smembers  | smembers(name)         | 集合 name 中的全部成员              |
     | spop      | spop(name)             | 随机弹出一个成员                    |
     | srem      | srem(name, *values)    | 删除一个或多个成员                  |

   - **SortedSet 类**: 常用作排行处理

     | CMD       | Example                                  | Description                            |
     | --------- | ---------------------------------------- | -------------------------------------- |
     | zadd      | zadd(name, a=12)                         | 添加一个 a, 值为 12                    |
     | zcount    | zcount(name, min, max)                   | 从 min 到 max 的元素个数               |
     | zincrby   | zincrby(name, key, 1)                    | key 对应的值自增 1                     |
     | zrange    | zrange(name, 0, -1, withscores=False)    | 按升序返回排名 0 到 最后一位的全部元素 |
     | zrevrange | zrevrange(name, 0, -1, withscores=False) | 按降序返回排名 0 到 最后一位的全部元素 |
     | zrem      | zrem(name, *value)                       | 删除一个或多个元素                     |



## redis集群

#### 为什么要有集群

- 之前我们已经讲了主从的概念，一主可以多从，如果同时的访问量过大(1000w),主服务肯定就会挂掉，数据服务就挂掉了或者发生自然灾难
- 大公司都会有很多的服务器(华东地区、华南地区、华中地区、华北地区、西北地区、西南地区、东北地区、台港澳地区机房)

#### 集群的概念

- 集群是一组相互独立的、通过高速网络互联的计算机，它们构成了一个组，并以单一系统的模式加以管理。一个客户与集群相互作用时，集群像是一个独立的服务器。集群配置是用于提高可用性和可缩放性。当请求到来首先由负载均衡服务器处理，把请求转发到另外的一台服务器上。
- ![image-20190829231557482](day05.assets/image-20190829231557482.png)

#### redis集群

- 分类
  - 软件层面
  - 硬件层面
  
- 软件层面：只有一台电脑，在这一台电脑上启动了多个redis服务。

  ![image-20190829232159306](day05.assets/image-20190829232159306.png)

- 硬件层面：存在多台实体的电脑，每台电脑上都启动了一个redis或者多个redis服务。

  ![image-20190829232132285](day05.assets/image-20190829232132285.png)

#### 参考阅读

- redis集群搭建 http://www.cnblogs.com/wuxl360/p/5920330.html
- [Python]搭建redis集群 http://blog.5ibc.net/p/51020.html



#### 配置机器

- 在桌面创建conf目录

- 在桌面创建6个redis的配置文件，文件名为7000到7005的conf配置文件

- 编辑文件，内容如下

  ```python
  port 7000  # 和文件名相同
  bind 172.16.179.130 # 本机的ip
  daemonize yes
  pidfile 7000.pid  # 和文件名相同 
  cluster-enabled yes
  cluster-config-file 7000_node.conf  # 和文件名相同 
  cluster-node-timeout 15000
  appendonly yes
  ```

- 启动redis服务

  ```python
  redis-server 7000.conf
  redis-server 7001.conf
  redis-server 7002.conf
  redis-server 7003.conf
  redis-server 7004.conf
  redis-server 7005.conf
  ```

#### 创建集群

- redis的安装包中包含了redis-trib.rb，用于创建集群

- 接下来的操作在172.16.179.130机器上进行

- 将命令复制，这样可以在任何目录下调用此命令

  ```python
  sudo cp /usr/share/doc/redis-tools/examples/redis-trib.rb /usr/local/bin/
  ```

- 安装ruby环境，因为redis-trib.rb是⽤ruby开发的

  ```python
  sudo apt-get install ruby
  ```

- 在提示信息处输入y，然后回车继续安装 

  ![image-20190829233131854](day05.assets/image-20190829233131854.png)

- 运⾏如下命令创建集群

  ```python
  redis-trib.rb create --replicas 1 172.16.179.130:7000 172.16.179.130:7001 172.16.179.130:7002 172.16.179.131:7003 172.16.179.131:7004 172.16.179.131:7005
  ```

- 执⾏上⾯这个指令在某些机器上可能会报错,主要原因是由于安装的 ruby 不是最 新版本!

- 天朝的防⽕墙导致无法下载最新版本,所以需要设置 gem 的源

- 解决办法如下

  ```python
  -- 先查看⾃⼰的 gem 源是什么地址
  gem source -l -- 如果是https://rubygems.org/ 就需要更换
  -- 更换指令为
  gem sources --add https://gems.ruby-china.com/ --remove https://rubygems.org/
  -- 通过 gem 安装 redis 的相关依赖
  sudo gem install redis
  -- 然后重新执⾏指令
  ```

  ![image-20190829233302556](day05.assets/image-20190829233302556.png)

  ```python
  redis-trib.rb create --replicas 1 172.16.179.130:7000 172.16.179.130:7001 172.16.179.130:7002 172.16.179.131:7003 172.16.179.131:7004 172.16.179.131:7005
  ```

- 提示如下主从信息，输⼊yes后回⻋

  ![image-20190829233430052](day05.assets/image-20190829233430052.png)

- 提示完成，集群搭建成功

#### 数据验证

- 根据上图可以看出，当前搭建的主服务器为7000、7001、7003，对应的从服务器是7004、7005、7002

- 在172.16.179.131机器上连接7002，加参数-c表示连接到集群

  ```python
  redis-cli -h 172.16.179.131 -c -p 7002
  ```

- 写⼊数据

  ```python
  set name ben
  ```

- ⾃动跳到了7003服务器，并写⼊数据成功 

- 在7003可以获取数据，如果写入数据又重定向到7000(负载均衡) 



## 排行榜功能

全服人气排行功能

- 被左滑 -5 分
- 被右滑 +5 分
- 被上滑 +7 分
- 统计全服人气最高的 10 位用户



## 日志处理

1. 日志的作用

   1. 记录程序运行状态
      1. 线上环境所有程序以 deamon 形式运行在后台, 无法使用 print 输出程序状态
      2. 线上程序无人值守全天候运行, 需要有一种能持续记录程序运行状态的机制, 以便遇到问题后分析处理
   2. 记录统计数据
   3. 开发时进行 Debug (调试)

2. 基本用法

   ```python
   import logging
   
   # 设置日志格式
   fmt = '%(asctime)s %(levelname)7.7s %(funcName)s: %(message)s'
   formatter = logging.Formatter(fmt, datefmt="%Y-%m-%d %H:%M:%S")
   
   # 设置 handler
   handler = logging.handlers.TimedRotatingFileHandler('myapp.log', when='D', backupCount=30)
   handler.setFormatter(formatter)
   
   # 定义 logger 对象
   logger = logging.getLogger("MyApp")
   logger.addHandler(handler)
   logger.setLevel(logging.INFO)
   ```

3. 日志的等级

   - DEBUG: 调试信息
   - INFO: 普通信息
   - WARNING: 警告
   - ERROR: 错误
   - FATAL: 致命错误

4. 对应函数

   - `logger.debug(msg)`
   - `logger.info(msg)`
   - `logger.warning(msg)`
   - `logger.error(msg)`
   - `logger.fatal(msg)`

5. 日志格式允许的字段

   - `%(name)s` : Logger 的名字
   - `%(levelno)s` : 数字形式的日志级别
   - `%(levelname)s` : 文本形式的日志级别
   - `%(pathname)s` : 调用日志输出函数的模块的完整路径名, 可能没有
   - `%(filename)s` : 调用日志输出函数的模块的文件名
   - `%(module)s` : 调用日志输出函数的模块名
   - `%(funcName)s` : 调用日志输出函数的函数名
   - `%(lineno)d` : 调用日志输出函数的语句所在的代码行
   - `%(created)f` : 当前时间, 用 UNIX 标准的表示时间的浮点数表示
   - `%(relativeCreated)d` : 输出日志信息时的, 自 Logger 创建以来的毫秒数
   - `%(asctime)s` : 字符串形式的当前时间。默认格式是“2003-07-08 16:49:45,896”。逗号后面的是毫秒
   - `%(thread)d` : 线程 ID。可能没有
   - `%(threadName)s` : 线程名。可能没有
   - `%(process)d` : 进程 ID。可能没有
   - `%(message)s` : 用户输出的消息

6. Django 中的日志配置

   ```python
   LOGGING = {
       'version': 1,
       'disable_existing_loggers': True,
       # 格式配置
       'formatters': {
           'simple': {
               'format': '%(asctime)s %(module)s.%(funcName)s: %(message)s',
               'datefmt': '%Y-%m-%d %H:%M:%S',
           },
           'verbose': {
               'format': ('%(asctime)s %(levelname)s [%(process)d-%(threadName)s] '
                       '%(module)s.%(funcName)s line %(lineno)d: %(message)s'),
               'datefmt': '%Y-%m-%d %H:%M:%S',
           }
       },
       # Handler 配置
       'handlers': {
           'console': {
               'class': 'logging.StreamHandler',
               'level': 'DEBUG' if DEBUG else 'WARNING'
           },
           'info': {
               'class': 'logging.handlers.TimedRotatingFileHandler',
               'filename': f'{BASE_DIR}/logs/info.log',  # 日志保存路径
               'when': 'D',        # 每天切割日志
               'backupCount': 30,  # 日志保留 30 天
               'formatter': 'simple',
               'level': 'INFO',
           },
           'error': {
               'class': 'logging.handlers.TimedRotatingFileHandler',
               'filename': f'{BASE_DIR}/logs/error.log',  # 日志保存路径
               'when': 'W0',      # 每周一切割日志
               'backupCount': 4,  # 日志保留 4 周
               'formatter': 'verbose',
               'level': 'WARNING',
           }
       },
       # Logger 配置
       'loggers': {
           'django': {
               'handlers': ['console'],
           },
           'inf': {
               'handlers': ['info'],
               'propagate': True,
               'level': 'INFO',
           },
           'err': {
               'handlers': ['error'],
               'propagate': True,
               'level': 'WARNING',
           }
       }
   }
   ```

   使用

   ```python
   import logging
   err_log = logging.getLogger('err')
   ```

   

## 发送邮箱

#### 1.Django发送邮件流程分析

![image-20190830134108040](day05.assets/image-20190830134108040.png)



`send_mall()`方法介绍

- 位置：
  - 在`django.core.mail`模块提供了`send_mail()`来发送邮件。
- 方法参数：
  - `send_mail(subject, message, from_email, recipient_list, html_message=None)`

```python
subject 邮件标题
message 普通邮件正文，普通字符串
from_email 发件人
recipient_list 收件人列表
html_message 多媒体邮件正文，可以是html字符串
```

#### 2.准备发邮件服务器

![image-20190830134241063](day05.assets/image-20190830134241063.png)

![image-20190830134303461](day05.assets/image-20190830134303461.png)

![image-20190830134329297](day05.assets/image-20190830134329297.png)

![image-20190830134345418](day05.assets/image-20190830134345418.png)

```python
6.配置邮件服务器

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # 指定邮件后端
EMAIL_HOST = 'smtp.163.com' # 发邮件主机
EMAIL_PORT = 25 # 发邮件端口
EMAIL_HOST_USER = '290793992zb@163.com' # 授权的邮箱
EMAIL_HOST_PASSWORD = 'abc123' # 邮箱授权时获得的密码，非注册登录密码
EMAIL_FROM = 'louis<290793992zb@163.com>' # 发件人抬头


7.发送邮件
from django.core.mail import send_mail

to_email = '290793992zb@163.com'
verify_url = 'http://www.baidu.com'
subject = "显示标题"
html_message = '<p>尊敬的用户您好！</p>' \
'<p>您的邮箱为：%s 。请点击此链接激活您的邮箱：</p>' \
'<p><a href="%s">%s<a></p>' % (to_email, verify_url, verify_url)

send_mail(subject, "", settings.EMAIL_FROM, [to_email], html_message=html_message)
```


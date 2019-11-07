# 全文检索方案Elasticsearch

### 全文检索和搜索引擎原理

> 商品搜索需求

- 当用户在搜索框输入商品关键字后，我们要为用户提供相关的商品搜索结果。

> 商品搜索实现

- 可以选择使用模糊查询`like`关键字实现。
- 但是 like 关键字的效率极低。
- 查询需要在多个字段中进行，使用 like 关键字也不方便。

> 全文检索方案

- 我们引入**全文检索**的方案来实现商品搜索。
- **全文检索即在指定的任意字段中进行检索查询。**
- **全文检索方案需要配合搜索引擎来实现。**

> 搜索引擎原理

- **搜索引擎**进行全文检索时，会对数据库中的数据进行一遍预处理，单独建立起一份**索引结构数据**。

- 索引结构数据**类似新华字典的索引检索页**，里面包含了关键词与词条的对应关系，并记录词条的位置。

- 搜索引擎进行全文检索时，将**关键字在索引数据中进行快速对比查找，进而找到数据的真实存储位置**。

  ![image-20190904073051866](day08.assets/image-20190904073051866.png)

结论：

- 搜索引擎建立索引结构数据，类似新华字典的索引检索页，全文检索时，关键字在索引数据中进行快速对比查找，进而找到数据的真实存储位置。



### Elasticsearch介绍

> **实现全文检索的搜索引擎，首选的是Elasticsearch。**

- [Elasticsearch](https://www.elastic.co/) 是用 Java 实现的，开源的搜索引擎。
- 它可以快速地储存、搜索和分析海量数据。维基百科、Stack Overflow、Github等都采用它。
- Elasticsearch 的底层是开源库 [Lucene](https://lucene.apache.org/)。但是，没法直接使用 Lucene，必须自己写代码去调用它的接口。

> **分词说明**

- 搜索引擎在对数据构建索引时，需要进行分词处理。
- 分词是指将一句话拆解成**多个单字** 或 **词**，这些字或词便是这句话的关键词。
- 比如：`我是中国人`
  - 分词后：`我`、`是`、`中`、`国`、`人`、`中国`等等都可以是这句话的关键字。
- Elasticsearch 不支持对中文进行分词建立索引，需要配合扩展`elasticsearch-analysis-ik`来实现中文分词处理。



### 使用Docker安装Elasticsearch

> **1.获取Elasticsearch-ik镜像**

```bash
# 从仓库拉取镜像
$ sudo docker image pull delron/elasticsearch-ik:2.4.6-1.0
# 解压本地镜像
$ sudo docker load -i elasticsearch-ik-2.4.6_docker.tar
```

> **2.配置Elasticsearch-ik**

- 修改`elasticsearc-2.4.6/config/elasticsearch.yml`第54行。
- 更改ip地址为本机真实ip地址。

> **3.使用Docker运行Elasticsearch-ik**

```bash
sudo docker run -dti --name=elasticsearch --network=host -v /home/python/Desktop/es/elasticsearch-2.4.6/config:/usr/share/elasticsearch/config delron/elasticsearch-ik:2.4.6-1.0 
```





# Haystack扩展建立索引

> 提示：
>
> - [Elasticsearch](https://www.elastic.co/) 的底层是开源库 [Lucene](https://lucene.apache.org/)。但是没法直接使用 Lucene，必须自己写代码去调用它的接口。
>
> 思考：
>
> - 我们如何对接 Elasticsearch服务端？
>
> 解决方案：
>
> - **Haystack**



### 1. Haystack介绍和安装配置

> **1.Haystack介绍**

- Haystack 是在Django中对接搜索引擎的框架，搭建了用户和搜索引擎之间的沟通桥梁。
  - 我们在Django中可以通过使用 Haystack 来调用 Elasticsearch 搜索引擎。
- Haystack 可以在不修改代码的情况下使用不同的搜索后端（比如 `Elasticsearch`、`Whoosh`、`Solr`等等）。

> **2.Haystack安装**

```bash
$ pip install django-haystack
$ pip install elasticsearch==2.4.1
```

> **3.Haystack注册应用和路由**

```python
INSTALLED_APPS = [
    'haystack', # 全文检索
]

url(r'^search/', include('haystack.urls')),
```

> **4.Haystack配置**
>
> - 在配置文件中配置Haystack为搜索引擎后端

```python
# Haystack
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://172.16.222.152:9200/', # Elasticsearch服务器ip地址，端口号固定为9200
        'INDEX_NAME': 'swiper', # Elasticsearch建立的索引库的名称
    },
}


# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
```

> **重要提示：**
>
> - **HAYSTACK_SIGNAL_PROCESSOR** 配置项保证了在Django运行起来后，有新的数据产生时，Haystack仍然可以让Elasticsearch实时生成新数据的索引



### 2. Haystack建立数据索引

> **1.创建索引类**

- 通过创建索引类，来指明让搜索引擎对哪些字段建立索引，也就是可以通过哪些字段的关键字来检索数据。
- 本项目中对user信息进行全文检索，所以在`user`应用中新建`search_indexes.py`文件，用于存放索引类。

```python
from haystack import indexes

from .models import User


class UserIndex(indexes.SearchIndex, indexes.Indexable):
    """索引数据模型类"""
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        """返回建立索引的模型类"""
        return User

    def index_queryset(self, using=None):
        """返回要建立索引的数据查询集"""
        return self.get_model().objects.all()
```

- 索引类UserIndex说明：
  - 在`UserIndex`建立的字段，都可以借助`Haystack`由`Elasticsearch`搜索引擎查询。
  - 其中`text`字段我们声明为`document=True`，表名该字段是主要进行关键字查询的字段。
  - `text`字段的索引值可以由多个数据库模型类字段组成，具体由哪些模型类字段组成，我们用`use_template=True`表示后续通过模板来指明。

> **2.创建text字段索引值模板文件**

- 在`templates`目录中创建`text字段`使用的模板文件
- 具体在`templates/search/indexes/user/user_text.txt`文件中定义
  - 第一个user是指子应用的名称
  - 第二个user是指模型类的名称小写

```python
{{ object.name }}
```

- 模板文件说明：当将关键词通过text参数名传递时
  - 此模板指明user的`name`作为`text`字段的索引值来进行关键字索引查询。

> **3.手动生成初始索引**

```python
$ python manage.py rebuild_index
```



### 3. 全文检索测试

> **1.准备测试**

- 请求方法：`GET`
- 请求地址：`/search/`
- 请求参数：`q`

> **2.全文检索测试结果**

> 结论：
>
> - 错误提示告诉我们在`templates/search/`目录中缺少一个`search.html`文件
> - **search.html**文件作用就是**接收和渲染全文检索的结果**。

- 模版中接受数据是通过page对象的object属性来获取数据 

  ```python
  {% for foo in page %}
      {{ foo.object.nickname }}
  {% endfor %}
  ```

  







# MySQL主从同步

### 1. 主从同步机制

> **1.主从同步介绍和优点**

- 在多台数据服务器中，分为主服务器和从服务器。一台主服务器对应多台从服务器。
- 主服务器只负责写入数据，从服务器只负责同步主服务器的数据，并让外部程序读取数据。
- 主服务器写入数据后，即刻将写入数据的命令发送给从服务器，从而使得主从数据同步。
- 应用程序可以随机读取某一台从服务器的数据，这样就可以分摊读取数据的压力。
- 当从服务器不能工作时，整个系统将不受影响；当主服务器不能工作时，可以方便地从从服务器选举一台来当主服务器
- 使用主从同步的优点：
  - 提高读写性能
    - 因为主从同步之后，数据写入和读取是在不同的服务器上进行的，而且可以通过增加从服务器来提高数据库的读取性能。
  - 提高数据安全
    - 因为数据已复制到从服务器，可以在从服务器上备份而不破坏主服务器相应数据。

> **2.主从同步机制**

![image-20190903202210668](day08.assets/image-20190903202210668.png)

> MySQL服务器之间的主从同步是基于**二进制日志机制**，主服务器使用二进制日志来记录数据库的变动情况，从服务器通过读取和执行该日志文件来保持和主服务器的数据一致。



### 2. 基于 Docker 来搭建 MySQL 的主从复制

1. 准备两台 MySQL 服务器
2. 配置主服务器（Master）
3. 配置从服务器（Slave）
4. 完成Master和Slave链接
5. 测试配置是否成功

####  2.1.准备两台 MySQL 服务器

- 使用 Docker 创建 MySQL 的master服务器：

  ```bash
  sudo docker run --name mysql_master -p 3307:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7.27
  ```

- 使用同样的方式创建 Slave 服务器：

  ```bash
  sudo docker run --name mysql_slave -p 3308:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7.27
  ```

- 使用 `sudo docker ps` 查看当前运行的容器，如下：

![image-20190903203535964](day08.assets/image-20190903203535964.png)

#### 2.2 配置主服务器（Master）

- 首先，进入到 Master 服务器

  ```bash
  sudo docker exec -it mysql_master /bin/bash
  ```

- 修改配置文件/etc/mysql/mysql.conf.d/mysqld.conf

  ```bash
  # 在末尾加上两个配置
  
  ## 设置server_id，一般设置为IP的最后一位，同一局域网内注意要唯一
  server_id = 3
  
  ## 开启二进制日志功能，可以随便取，最好有含义（关键就是这里了）
  log-bin = edu-mysql-bin
  ```

  > 注意：修改文件的时候，可能没有vi命令，需要安装vim的软件包
  >
  > 方法：apt-get update     apt install vim

- 配置完成后重启 mysql

  ```bash
  service mysql restart
  ```

  > 注意：这个命令会使得容器停止，重新启动就可以了。

- 进入mysql数据库中创建数据同步用户

  ```bash
  mysql -u root -p -h 172.16.222.152 --port=3307
  ```

- 创建数据同步用户

  ```bash
  mysql> CREATE USER 'slave'@'%' IDENTIFIED BY '123456';
  mysql> GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'slave'@'%'; 
  ```

#### 2.3 配置从服务器（Slave）

- 首先，进入到 Master 服务器

  ```bash
  sudo docker exec -it mysql_slave /bin/bash
  ```

- 修改配置文件/etc/mysql/mysql.conf.d/mysqld.conf

  ```bash
  # 在末尾加上两个配置
  
  ## 设置server_id，一般设置为IP的最后一位，同一局域网内注意要唯一
  server_id = 4
  
  ## 开启二进制日志功能，以备Slave作为其它Slave的Master时使用
  log-bin=edu-mysql-slave-bin  
  ```

- 配置完成后重启mysql，和配置 Master 一样，会使容器停止，需要启动容器。

  ```bash
  service mysql restart
  ```

#### 2.4 完成Master和Slave链接

- 在 Master 进入 MySQL， 然后执行命令：

  ```bash
  mysql -u root -p -h 172.16.222.152 --port=3307
  
  mysql> show master status;
  ```

  结果如下：

  ![image-20190903205334801](day08.assets/image-20190903205334801.png)

  记录下 File 和 Position 字段的值，后面会用到。

- 然后到 Slave 中进入 mysql，执行命令：

  ```bash
  mysql -u root -p -h 172.16.222.152 --port=3308
  
  mysql> change master to master_host='172.16.222.152', master_user='slave', master_password='123456', master_port=3307, master_log_file='edu-mysql-bin.000001', master_log_pos=34659, master_connect_retry=30;
  ```

  命令解释：

  ```bash
  master_host: Master 的IP地址
  master_user: 在 Master 中授权的用于数据同步的用户
  master_password: 同步数据的用户的密码
  master_port: Master 的数据库的端口号
  master_log_file: 指定 Slave 从哪个日志文件开始复制数据，即上文中提到的 File 字段的值
  master_log_pos: 从哪个 Position 开始读，即上文中提到的 Position 字段的值
  master_connect_retry: 当重新建立主从连接时，如果连接失败，重试的时间间隔，单位是秒，默认是60秒。
  ```

- 在 Slave 的 MySQL 终端执行查看主从同步状态

  ```bash
  show slave status \G;
  ```

  ![image-20190903205811370](day08.assets/image-20190903205811370.png)

> SlaveIORunning 和 SlaveSQLRunning 是No，表明 Slave 还没有开始复制过程。相反 SlaveIORunning 和 SlaveSQLRunning 是Yes表明已经开始工作了，因为我已经运行过了，所以我的显示的都是 Yes。

- 执行以下命令，开始开启主从同步：

  ```bash
  start slave;
  ```



# Django实现MySQL读写分离

### 1. 增加slave数据库的配置

```python
DATABASES = {
    'default': { # 写（主机）
        'ENGINE': 'django.db.backends.mysql', # 数据库引擎
        'HOST': '172.16.222.152', # 数据库主机
        'PORT': 3307, # 数据库端口
        'USER': 'root', # 数据库用户名
        'PASSWORD': '123456', # 数据库用户密码
        'NAME': 'sz1903' # 数据库名字
    },
    'slave': { # 读（从机）
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '172.16.222.152',
        'PORT': 3308,
        'USER': 'root',
        'PASSWORD': '123456',
        'NAME': 'sz1903'
    }
}
```

### 2. 创建和配置数据库读写路由

> **1.创建数据库读写路由**
>
> - 在`common/db_router.py`中实现读写路由

```python
class MasterSlaveDBRouter(object):
    """数据库读写路由"""

    def db_for_read(self, model, **hints):
        """读"""
        return "slave"

    def db_for_write(self, model, **hints):
        """写"""
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        """是否运行关联操作"""
        return True
```

> **2.配置数据库读写路由**

```python
DATABASE_ROUTERS = ['common.db_router.MasterSlaveDBRouter']
```
# Day03

### 一、回顾

> MySQL介绍：
>
> ​	Oracle公司，关系型数据库
> ​	关系型数据库（表）： MySQL，Oracle, SQL Server， DB2
>
> ​	非关系型数据库（没有表）：Redis, Mongodb
>
> mysql基本操作：
>
> ​	linux : 
>
> ​		启动数据库： sudo service mysql start
>
> ​		关闭数据库： sudo service mysql stop
>
> ​		重启数据库： sudo service mysql restart
>
> ​	windows:
>
> ​		启动： net start mysql57
>
> ​		关闭：net stop mysql57
>
> ​	登录mysql：mysql -u root -p
>
> ​	退出： exit , quit
>
>  数据库SQL语句
>
> ​	database: 
>
> ​		创建数据库： create database mydb charset='utf8';
>
> ​		删除数据库： drop database mydb;
>
> ​		查看数据库： show databases;
>
> ​		进入数据库： use mydb;
>
> ​	table:
>
> ​		alter table  修改表结构
>
> ​		show tables  查看表
>
> ​		drop table user;  删除表
>
> ​		create table user (
>
> ​			id int auto_increment primary key,
>
> ​			name varchar(20)
>
> ​		)
>
> ​		字段约束：
>
> ​			auto_increment : 整数自动增加
>
> ​			 primary key: 主键
>
> ​			unique: 唯一约束
>
> ​			not null : 非空
>
> ​			default: 默认值
> ​		外键约束：
>
> ​			foreign key 
>
> ​		desc user : 查看表的结构
>
> ​		增删改查：
>
> ​			增： insert into user(name) values('zs'), ('lisi');
>
> ​			删：delete from user where name='zs';
>
> ​			改：update user set name='wangwu' where name='lisi';		
>
> ​			查：select * from user;
>
> ​				select id,name from user;
>
> ​				select * from user where name='zs';
>
> ​				select * from user where name like '%z%'
>
> ​				select * from user where name in ('zs', 'lisi', 'wangwu');
>
> ​		分组：
>
> ​			group by : 分组
>
> ​			having： 分组后的条件
>
> ​		排序：
>
> ​			order by
>
> ​			asc (升序), desc（降序）
>
> ​		聚合函数：		
>
> ​			count(*) : 数量
>
> ​			sum(name) 求和
>
> ​			max(id) 最大值
>
> ​			min(id) 最小值
>
> ​			avg(id) 平均值
>
> ​		分页：
>
> ​			limit 3  : 前3个
>
> ​			limit 3, 5 : 从下标第3个开始的5个数据
>
> ​    多表操作：
>
> ​	一对一：1:1
>
> ​	一对多： 1：n
>
> ​	多对多： m : n
>
> ​	inner join on /  join on  ： 内连接
>
> ​	left join on:  左连接 
>
> ​	right join on: 右连接
>
> 索引：
>
> ​	主键索引:  primary key
>
> ​	唯一索引：unique
>
> ​	普通索引： index
>
> 权限：
>
> ​	grant 
>
> ​	revoke
>
> 事务：
>
> ​	保证多个sql语句要么都执行成功， 要么都不成功！
>
> ​	一般用于 insert, update, delete 这三个操作。

### 二、Redis基础

#### 1.概述

> Redis是一个开源，高级的键值存储和一个适用的解决方案，用于构建高性能，可扩展的Web应用程序。
>
> Redis有三个主要特点，使它优越于其它键值数据存储系统 - 
>
> - Redis将其数据库完全保存在内存中，仅使用磁盘进行持久化。
> - 与其它键值数据存储相比，Redis有一组相对丰富的数据类型。
> - Redis可以将数据复制到任意数量的从机中。
> - sql 
> - nosql  
>
>


#### 2.Redis的优点

> - **异常快** - Redis非常快，每秒可执行大约`110000`次的设置(`SET`)操作，每秒大约可执行`81000`次的读取/获取(`GET`)操作。
> - **支持丰富的数据类型** - Redis支持开发人员常用的大多数数据类型，例如列表，集合，排序集和散列等等。这使得Redis很容易被用来解决各种问题，因为我们知道哪些问题可以更好使用地哪些数据类型来处理解决。
> - **操作具有原子性** - 所有Redis操作都是原子操作，这确保如果两个客户端并发访问，Redis服务器能接收更新的值。
> - **多实用工具** - Redis是一个多实用工具，可用于多种用例，如：缓存，消息队列(Redis本地支持发布/订阅)，应用程序中的任何短期数据，例如，web应用程序中的会话，网页命中计数等。
>

#### 3.Redis与其他键值存储系统

> - Redis是键值数据库系统的不同进化路线，它的值可以包含更复杂的数据类型，可在这些数据类型上定义原子操作。
> - Redis是一个内存数据库，但在磁盘数据库上是持久的，因此它代表了一个不同的权衡，在这种情况下，在不能大于存储器(内存)的数据集的限制下实现非常高的写和读速度。
> - 内存数据库的另一个优点是，它与磁盘上的相同数据结构相比，复杂数据结构在内存中存储表示更容易操作。 因此，Redis可以做很少的内部复杂性。

### 二、Redis 的安装

> ##### 第一步：安装Redis，打开终端执行以下命令
>
> ```
> sudo apt-get install redis-server
> ```
>
> 第二步：启动Redis
>
> ```
> redis-server
> ```
>
> 第三步：检查Redis是否正在工作
>
> ```
> redis-cli
> ```
>
> 执行完得到的结果： `127.0.0.1:6379>`则说明正常工作
>
> 说明：`127.0.0.1`是计算机的IP地址，`6379`是运行Redis服务器的端口。 
>
> 第四步：执行`PING`命令。
>
> ```
> redis 127.0.0.1:6379> ping 
> PONG
> ```
>
> 得到结果为PONG表明**Redis**已成功安装
>
> 注意：在redis的server端，维护着多个数据库（默认为16个）
> 　        所有的数据库以数组的形式保存在redisServer结构中

### 三、Redis keys 命令

> 下表给出了与 Redis 键相关的基本命令：
>
> | 序号   | 命令及描述                                    |
> | ---- | ---------------------------------------- |
> | 1    | DEL key该命令用于在 key 存在时删除 key              |
> | 2    | EXISTS key 检查给定 key 是否存在。                |
> | 3    | EXPIRE key seconds为给定 key 设置过期时间。        |
> | 4    | PEXPIRE key milliseconds 设置 key 的过期时间以毫秒计。 |
> | 5    | KEYS pattern 查找所有符合给定模式( pattern)的 key 。 |
> | 6    | MOVE key db 将当前数据库的 key 移动到给定的数据库 db 当中。 |
> | 7    | PERSIST key 移除 key 的过期时间，key 将持久保持。      |
> | 8    | PTTL key 以毫秒为单位返回 key 的剩余的过期时间。          |
> | 9    | TTL key 以秒为单位，返回给定 key 的剩余生存时间(TTL, time to live)。 |
> | 10   | RANDOMKEY 从当前数据库中随机返回一个 key 。            |
> | 11   | RENAME key newkey 修改 key 的名称             |
> | 12   | TYPE key 返回 key 所储存的值的类型。                |

> 查找以 hello 为开头的 key：
>
> ```
> redis 127.0.0.1:6379> KEYS hello*
> 1) "hello3"
> 2) "hello1"
> 3) "hello2"
> ```
>
> 获取 redis 中所有的 key 可用使用 *****。
>
> ```
> redis 127.0.0.1:6379> KEYS *
> 1) "hello3"
> 2) "hello1"
> 3) "hello2"
> ```

### 四、数据类型

> Redis支持`5`种数据类型。
>

#### 1.字符串

> String是redis最基本的类型，最大能存储512MB的数据，String类型是二进制安全的，即可以存储任何数据、比如数字、图片、序列化对象等
>
> 下表列出了一些用于在**Redis**中管理字符串的基本命令。
>
> | 编号   | 命令                            | 描述说明                 |
> | ---- | ----------------------------- | -------------------- |
> | 1    | SET key value                 | 此命令设置指定键的值。          |
> | 2    | GET key                       | 获取指定键的值。             |
> | 3    | GETRANGE key start end        | 获取存储在键上的字符串的子字符串。    |
> | 4    | GETSET key value              | 设置键的字符串值并返回其旧值。      |
> | 5    | MGET key1 key2..              | 获取所有给定键的值            |
> | 6    | SETEX key seconds value       | 使用键和到期时间来设置值         |
> | 7    | SETNX key value               | 设置键的值，仅当键不存在时        |
> | 8    | SETRANGE key offset value     | 在指定偏移处开始的键处覆盖字符串的一部分 |
> | 9    | STRLEN key                    | 获取存储在键中的值的长度         |
> | 10   | MSET key value key value …    | 为多个键分别设置它们的值         |
> | 11   | MSETNX key value key value …  | 为多个键分别设置它们的值，仅当键不存在时 |
> | 12   | PSETEX key milliseconds value | 设置键的值和到期时间(以毫秒为单位)   |
> | 13   | INCR key                      | 将键的整数值增加`1`          |
> | 14   | INCRBY key increment          | 将键的整数值按给定的数值增加       |
> | 15   | INCRBYFLOAT key increment     | 将键的浮点值按给定的数值增加       |
> | 16   | DECR key                      | 将键的整数值减`1`           |
> | 17   | DECRBY key decrement          | 按给定数值减少键的整数值         |
> | 18   | APPEND key value              | 将指定值附加到键             |
>

##### 1.1设置

> 注 ： Redis命令不区分大小写，如`SET`,`Set`和`set`都是同一个命令。字符串值的最大长度为 512MB。
>
> 演示：
>
> ```Python
> #1.设置键值
> set name 'xiaoming'
>
> #2.设置键值及过期时间，以秒为单位
> setex name  10 'xiaoming' 
>
> #3.设置多个键值
> mset name "lili"  age  18  sex 'girl'
> ```

##### 1.2获取

> 演示：
>
> ```Python
> #1.据键获取值，如果键不存在则返回None
> get name
>
> #2.根据多个键获取多个值
> mget name age
> ```

##### 1.3运算

> 要求：值是字符串类型的数字
>
> 演示：
>
> ```Python
> #1.将key对应的值加1
> incr age
>
> #2.key对应的值减1
> decr age
>
> #3.将key对应的值加整数
> incrby age 10
>
> #4.将key对应的值减整数
> decrby age  20
> ```

##### 1.4其他

> 演示：
>
> ```Python
> #1.追加值
> append name "hello"
> get name
>
> #2.获取值长度
> strlen name
> ```

#### 2.哈希

> Redis哈希(Hashes)是键值对的集合。Redis哈希是字符串字段和字符串值之间的映射。因此，它们用于存储对象。
>
> | 序号   | 命令                                       | 说明                  |
> | ---- | ---------------------------------------- | ------------------- |
> | 1    | HDEL key field2 [field2\]                | 删除一个或多个哈希字段。        |
> | 2    | HEXISTS key field                        | 判断是否存在散列字段。         |
> | 3    | HGET key field                           | 获取存储在指定键的哈希字段的值。    |
> | 4    | HGETALL key                              | 获取存储在指定键的哈希中的所有字段和值 |
> | 5    | HINCRBY key field increment              | 将哈希字段的整数值按给定数字增加    |
> | 6    | HINCRBYFLOAT key field increment         | 将哈希字段的浮点值按给定数值增加    |
> | 7    | HKEYS key                                | 获取哈希中的所有字段          |
> | 8    | HLEN key                                 | 获取散列中的字段数量          |
> | 9    | HMGET key field1 [field2\]               | 获取所有给定哈希字段的值        |
> | 10   | [HMSET key field1 value1 field2 value2 \] | 为多个哈希字段分别设置它们的值     |
> | 11   | HSET key field value                     | 设置散列字段的字符串值         |
> | 12   | HSETNX key field value                   | 仅当字段不存在时，才设置散列字段的值  |
> | 13   | HVALS key                                | 获取哈希中的所有值           |
>

##### 2.1设置

> 演示：
>
> ```Python
> #1.设置单个值
> hset ukey name 'zhangsan'
>
> #2.设置多个值
> hmset ukey username "xixi" password "123456"
>
> #用于存储包含用户的基本信息的用户对象，ukey是键的名称
> ```

##### 2.2获取

> 演示：
>
> ```Python
> #1.获取一个属性的值
> hget ukey name
>
> #2.获取多个属性的值
> hmget ukey username password
>
> #3.获取所有属性和值
> hgetall ukey
>
> #4.获取所有属性
> hkeys ukey
>
> #5.获取所有值
> hvals ukey
>
> #6.返回包含数据的个数
> hlen ukey
> ```

##### 2.3其他

> 演示：
>
> ```Python
> #1.判断属性是否存在，存在返回1，不存在返回0
> hexists ukey username
>
> #2.删除属性及值
> hdel ukey username 'xixi'
> ```

#### 3.列表

> Redis列表只是字符串列表，按插入顺序排序。您可以向Redis列表的头部或尾部添加元素。
>
> 列表的最大长度为`2^32 - 1`个元素(`4294967295`，每个列表可容纳超过`40`亿个元素)。
>
> 下表列出了与列表相关的一些基本命令。
>
> | 序号   | 命令                                    | 说明                                 |
> | ---- | ------------------------------------- | ---------------------------------- |
> | 1    | BLPOP key1 [key2 \] timeout           | 删除并获取列表中的第一个元素，会阻塞，直到有一个元素可用       |
> | 2    | BRPOP key1 [key2 \] timeout           | 删除并获取列表中的最后一个元素，会阻塞，直到有一个元素可用      |
> | 3    | BRPOPLPUSH source destination timeout | 从列表中弹出值，将其推送到另一个列表并返回它; 或阻塞，直到一个可用 |
> | 4    | LINDEX key index                      | 通过其索引从列表获取元素                       |
> | 5    | LINSERT key BEFORE/AFTER pivot value  | 在列表中的另一个元素之前或之后插入元素                |
> | 6    | LLEN key                              | 获取列表的长度                            |
> | 7    | LPOP key                              | 删除并获取列表中的第一个元素                     |
> | 8    | LPUSH key value1 [value2\]            | 将一个或多个值添加到列表                       |
> | 9    | LPUSHX key value                      | 仅当列表存在时，才向列表添加值                    |
> | 10   | LRANGE key start stop                 | 从列表中获取一系列元素                        |
> | 11   | LREM key count value                  | 从列表中删除元素                           |
> | 12   | LSET key index value                  | 通过索引在列表中设置元素的值                     |
> | 13   | LTRIM key start stop                  | 修剪列表的指定范围                          |
> | 14   | RPOP key                              | 删除并获取列表中的最后一个元素                    |
> | 15   | RPOPLPUSH source destination          | 删除列表中的最后一个元素，将其附加到另一个列表并返回         |
> | 16   | RPUSH key value1 [value2\]            | 将一个或多个值附加到列表                       |
> | 17   | RPUSHX key value                      | 仅当列表存在时才将值附加到列表                    |
>

##### 3.1设置

> 演示：
>
> ```Python
> #1.在头部插入
> 127.0.0.1:6379> lpush alist redis
> (integer) 1
> 127.0.0.1:6379> lpush alist mongodb
> (integer) 2
> 127.0.0.1:6379> lpush alist mysql
> (integer) 3
> 127.0.0.1:6379> lrange alist 0 10
> 1) "mysql"
> 2) "mongodb"
> 3) "redis"
>
> #2.在尾部插入
> 127.0.0.1:6379> rpush alist aaa
> (integer) 4
> 127.0.0.1:6379> lrange alist 0 10
> 1) "musql"
> 2) "mongodb"
> 3) "redis"
> 4) "aaa"
>
>
> #3.在一个元素的前/后插入新元素
> 127.0.0.1:6379> linsert alist after aaa bbb
> (integer) 5
> 127.0.0.1:6379> lrange alist 0 10
> 1) "musql"
> 2) "mongodb"
> 3) "redis"
> 4) "aaa"
> 5) "bbb"
> 127.0.0.1:6379> linsert alist before aaa ccc
> (integer) 6
> 127.0.0.1:6379> lrange alist 0 10
> 1) "musql"
> 2) "mongodb"
> 3) "redis"
> 4) "ccc"
> 5) "aaa"
> 6) "bbb"
>
>
> #4.设置指定索引的元素值,索引从0开始
> 127.0.0.1:6379> lset alist 3 bbb
> OK
> 127.0.0.1:6379> lrange alist 0 10
> 1) "musql"
> 2) "mongodb"
> 3) "redis"
> 4) "bbb"
> 5) "aaa"
> 6) "bbb"
>
> #注意：索引值可以是负数，表示偏移量是从list的尾部开始，如-1表示最后一个元素
> ```

##### 3.2获取

> 演示：
>
> ```Python
> #1.移除并返回key对应的list的第一个元素  
> 127.0.0.1:6379> lpop alist
> "musql"
>
> #2.移除并返回key对应的list的最后一个元素
> 127.0.0.1:6379> rpop alist
> "bbb"
>
> #3.返回存储在key的列表中的指定范围的元素
> 127.0.0.1:6379> lrange alist 0 10
> 1) "mongodb"
> 2) "redis"
> 3) "bbb"
> 4) "aaa"
> #注意：start end都是从0开始
> ```

##### 3.3其他

> 演示：
>
> ```Python
> #1.裁剪列表，改为原集合的一个子集
> 127.0.0.1:6379> ltrim alist 0 2
> OK
> 127.0.0.1:6379> lrange alist 0 10
> 1) "mongodb"
> 2) "redis"
> 3) "bbb"
> #包头包尾
>
> #2.返回存储在key里的list的长度
> 127.0.0.1:6379> llen alist
> (integer) 3
>
> #3.返回列表中索引对应的值  
> 127.0.0.1:6379> lindex alist 2
> "bbb"
> ```

#### 4.集合

> Redis集合是唯一字符串的无序集合。 唯一值表示集合中不允许键中有重复的数据。
>
> 一个集合中的最大成员数量为`2^32 - 1`(即`4294967295`，每个集合中元素数量可达`40`亿个)个。
>
> 下表列出了与集合相关的一些基本命令。
>
> | 序号   | 命令                                       | 说明               |
> | ---- | ---------------------------------------- | ---------------- |
> | 1    | SADD key member1 [member2\]              | 将一个或多个成员添加到集合    |
> | 2    | SCARD key                                | 获取集合中的成员数        |
> | 3    | SDIFF key1 [key2\]                       | 减去多个集合           |
> | 4    | SDIFFSTORE destination key1 [key2\]      | 减去多个集并将结果集存储在键中  |
> | 5    | SINTER key1 [key2\]                      | 相交多个集合           |
> | 6    | SINTERSTORE destination key1 [key2\]     | 交叉多个集合并将结果集存储在键中 |
> | 7    | SISMEMBER key member                     | 判断确定给定值是否是集合的成员  |
> | 8    | SMOVE source destination member          | 将成员从一个集合移动到另一个集合 |
> | 9    | SPOP key                                 | 从集合中删除并返回随机成员    |
> | 10   | SRANDMEMBER key [count\]                 | 从集合中获取一个或多个随机成员  |
> | 11   | SREM key member1 [member2\]              | 从集合中删除一个或多个成员    |
> | 12   | SUNION key1 [key2\]                      | 添加多个集合           |
> | 13   | SUNIONSTORE destination key1 [key2\]     | 添加多个集并将结果集存储在键中  |
> | 14   | SSCAN key cursor [MATCH pattern\] [COUNT count] | 递增地迭代集合中的元素      |
>

##### 4.1设置

> 演示：
>
> ```Python
> #1.添加元素
> redis 127.0.0.1:6379> sadd aset redis 
> (integer) 1 
> redis 127.0.0.1:6379> sadd aset mongodb 
> (integer) 1 
> redis 127.0.0.1:6379> sadd aset sqlite 
> (integer) 1 
> redis 127.0.0.1:6379> sadd aset sqlite 
> (integer) 0 
> redis 127.0.0.1:6379> smembers aset  
>
> 1) "sqlite" 
> 2) "mongodb" 
> 3) "redis"
> #aset 为键
> #注意 ：如果被添加两次，但是由于集合的唯一属性，所以它只算添加一次。
> ```

##### 4.2获取

> 演示：
>
> ```Python
> #1.返回key集合中所有元素
> redis 127.0.0.1:6379> smembers aset  
>
> #2.返回集合元素个数
> redis 127.0.0.1:6379> scard aset  
> ```

##### 4.3交集

> 演示：
>
> ```Python
> #1.求多个集合的交集  
> 127.0.0.1:6379> sadd aset1 aaa
> (integer) 1
> 127.0.0.1:6379> sadd aset1 mysql
> (integer) 1
> 127.0.0.1:6379> sadd aset1 bbbb
> (integer) 1
> 127.0.0.1:6379> sinter aset aset1
> 1) "mysql"
> 2) "aaa"
>
> #2.求多个集合的差集   
> 127.0.0.1:6379> sdiff aset aset1
> 1) "mongodb"
> 2) "redis"
>
> #3.判断元素是否在集合中，存在返回1，不存在返回0
> 127.0.0.1:6379> sismember aset mysql
> (integer) 1
> ```

##### 4.4有序集合

> Redis 有序集合和集合一样也是string类型元素的集合,且不允许重复的成员。
>
> 不同的是每个元素都会关联一个double类型的分数。redis正是通过分数来为集合中的成员进行从小到大的排序。
>
> 有序集合的成员是唯一的,但分数(score)却可以重复
>
> 下表列出了 redis 有序集合的基本命令:
>
> | 序号   | 命令及描述                                    |
> | ---- | ---------------------------------------- |
> | 1    | ZADD key score1 member1 [score2 member2\]向有序集合添加一个或多个成员，或者更新已存在成员的分数 |
> | 2    | ZCARD key 获取有序集合的成员数                     |
> | 3    | ZCOUNT key min max 计算在有序集合中指定区间分数的成员数    |
> | 4    | ZINCRBY key increment member 有序集合中对指定成员的分数加上增量 increment |
> | 5    | ZINTERSTORE destination numkeys key [key ...\] 计算给定的一个或多个有序集的交集并将结果集存储在新的有序集合 key 中 |
> | 6    | ZLEXCOUNT key min max 在有序集合中计算指定字典区间内成员数量 |
> | 7    | [ZRANGE key start stop [WITHSCORES\]通过索引区间返回有序集合成指定区间内的成员 |
> | 8    | ZRANGEBYLEX key min max [LIMIT offset count\]通过字典区间返回有序集合的成员 |
> | 9    | ZRANGEBYSCORE key min max [WITHSCORES\] [LIMIT]通过分数返回有序集合指定区间内的成员 |
> | 10   | ZRANK key member 返回有序集合中指定成员的索引          |
> | 11   | ZREM key member member...移除有序集合中的一个或多个成员 |
> | 12   | ZREMRANGEBYLEX key min max 移除有序集合中给定的字典区间的所有成员 |
> | 13   | ZREMRANGEBYRANK key start stop 移除有序集合中给定的排名区间的所有成员 |
> | 14   | ZREMRANGEBYSCORE key min max移除有序集合中给定的分数区间的所有成员 |
> | 15   | ZREVRANGE key start stop [WITHSCORES\]返回有序集中指定区间内的成员，通过索引，分数从高到底 |
> | 16   | ZREVRANGEBYSCORE key max min [WITHSCORES\]返回有序集中指定分数区间内的成员，分数从高到低排序 |
> | 17   | ZREVRANK key member 返回有序集合中指定成员的排名，有序集成员按分数值递减(从大到小)排序 |
> | 18   | ZSCORE key member 返回有序集中，成员的分数值          |
> | 19   | ZUNIONSTORE destination numkeys key [key ...\]计算给定的一个或多个有序集的并集，并存储在新的 key 中 |
> | 20   | ZSCAN key cursor [MATCH pattern\] [COUNT count]迭代有序集合中的元素（包括元素成员和元素分值 |
>
> 演示：
>
> a.添加
>
> ```Python
> 127.0.0.1:6379> zadd z1 1 a 3 b 4 c 5 d 2 e
> (integer) 5
> ```
>
> b.获取
>
> ```Python
> #1.返回指定范围的元素
> 127.0.0.1:6379> zrange z1 1 3
> 1) "e"
> 2) "b"
> 3) "c"
>
> #2.返回元素个数
> 127.0.0.1:6379> zcard z1
> (integer) 5
>
> #3.返回有序集合key中，score在min和max之间的元素的个数
> 127.0.0.1:6379> zcount z1 2 5
> (integer) 4
>
> #4.返回有序集合key中，成员member的score值
> 127.0.0.1:6379> zscore z1 b
> "3"
> ```

### 五、与 python 交互

> pip3 install  redis
>
> 引入模块
>
> ##### from redis import StrictRedis
>
> 这个模块中提供了StrictRedis对象(Strict严格)，用于连接redis服务器，并按照不同类型提供 了不同方法，进行交互操作
>
> ##### StrictRedis对象方法:
>
> 通过init创建对象，指定参数host、port与指定的服务器和端口连接，host默认为localhost，port默认为6379，db默认为0
> sr = StrictRedis(host='localhost', port=6379, db=0)
>
> 代码演示：
>
> ```python
> from redis import  *
>
> # 创建一个StrictReids对象，与redis服务器建立连接
> sr = StrictRedis(host='localhost', port=6379, db=0)
>
> #1.增
> try:
>     result = sr.set('py1', 'gj')
>     # result如果为true，则表示添加成功
>     print(result)
> except Exception as e:
>     print(e)
>     
> #2.删
> #result = sr.delete('py1')
> #print(result)
>
> #3.改
> result = sr.set('py1','he')
>
> #4.查
> #如果建不存在，则返回None
> result = sr.get('py1')
>
> #5.获取建
> result = sr.keys()
>
>
> ```
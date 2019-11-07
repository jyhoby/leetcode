# Social 模块开发


## 功能概述

1. 交友模块
    - 获取推荐列表
    
      ```python
      current_year = datetime.date.today().year
  max_year = current_year-request.user.profile.min_dating_age
      min_year = current_year-request.user.profile.max_dating_age
      
      users = User.objects.filter(
        location=request.user.profile.location,
        birth_year__gte=min_year,
        birth_year__lte=max_year,
        sex=request.user.profile.dating_sex
      ).exclude(id=user.id)[:20]
      data = [model_to_dict(user) for user in users]
      ```
    
      
    
    - 喜欢 / 超级喜欢 / 不喜欢
    
    - 反悔 (每天允许返回 3 次)
    
      ```python
      Swiped.objects.filter(uid=user.id).latest('time')
      
      now = datetime.datetime.now()
      remain_second = 86400 - (now.hour * 3600 + now.minute * 60 + now.second)
      ```
    
      
    
    - 查看喜欢过我的人
    
2. 好友模块
    - 查看好友列表
    - 查看好友信息


## 开发中的难点

1. 滑动需有大量用户，如何初始化大量用户以供测试？
2. 推荐算法
3. 如何从推荐列表中去除已经滑过的用户
4. 滑动操作，如何避免重复滑动同一人
5. 如果双方互相喜欢，需如何处理
6. 好友关系如何记录，数据库表结构如何设计？
7. 反悔接口
    1. “反悔”都应该执行哪些操作
    2. 每日只允许“反悔” 3 次应如何处理
    3. 后期运营时，如何方便的修改反悔次数
8. 内部很深的逻辑错误如何比较方便的将错误码返回给最外层接口


## 关系分析

1. 滑动者与被滑动者
    - 一个人可以滑动很多人
    - 一个人可以被多人滑动
    - 结论: 同表之内构建起来的逻辑上的多对多关系

2. 用户与好友
    - 一个用户由多个好友
    - 一个用户也可以被多人加为好友
    - 结论: 同表之内构建起来的逻辑上的多对多关系, Friend 表实际上就是一个关系表


## 模型设计参考

1. Swiped (划过的记录)

    | Field | Description     |
    | ----- | --------------- |
    | uid   | 用户自身 id     |
    | sid   | 被滑的陌生人 id |
    | mark  | 滑动类型        |
    | time  | 滑动的时间      |

2. Friend (匹配到的好友)

    | Field | Description |
    | ----- | ----------- |
    | uid1  | 好友 ID     |
    | uid2  | 好友 ID     |


## 类方法与静态方法

- `method`

    - 通过实例调用
    - 可以引用类内部的 **任何属性和方法**

- `classmethod`

    - 无需实例化
    - 可以调用类属性和类方法
    - 无法取到普通的成员属性和方法

- `staticmethod`

    - 无需实例化
    - **无法**取到类内部的任何属性和方法, 完全独立的一个方法


## 利用 Q 对象进行复杂查询

```python
from django.db.models import Q

# AND
Model.objects.filter(Q(x=1) & Q(y=2))

# OR
Model.objects.filter(Q(x=1) | Q(y=2))

# NOT
Model.objects.filter(~Q(name='kitty'))
```

## redis主从

- ⼀个master可以拥有多个slave，⼀个slave⼜可以拥有多个slave，如此下去，形成了强⼤的多级服务器集群架构
- master用来写数据，slave用来读数据，经统计：网站的读写比率是10:1
- 通过主从配置可以实现读写分离
- ![image-20190829133722242](swiper-social.assets/image-20190829133722242.png)

- master和slave都是一个redis实例(redis服务)





### 主从配置

### 配置主

- 查看当前主机的ip地址

  ```python
  ifconfig
  ```

  

- 修改etc/redis/redis.conf文件

  ```python
  sudo vi redis.conf
  bind 192.168.26.128
  ```

- 重启redis服务

  ```python
  sudo service redis stop
  redis-server redis.conf
  ```

### 配置从

- 复制etc/redis/redis.conf文件

  ```python
  sudo cp redis.conf ./slave.conf
  ```

- 修改redis/slave.conf文件

  ```python
  sudo vi slave.conf
  ```

- 编辑内容

  ```python
  bind 192.168.26.128
  slaveof 192.168.26.128 6379
  port 6378
  ```

- redis服务

  ```python
  sudo redis-server slave.conf
  ```

- 查看主从关系

  ```python
  redis-cli -h 192.168.26.128 info Replication
  ```

### 数据操作

- 在master和slave分别执⾏info命令，查看输出信息 进入主客户端

  ```python
  redis-cli -h 192.168.26.128 -p 6379
  ```

- 进入从的客户端

  ```python
  redis-cli -h 192.168.26.128 -p 6378
  ```

- 在master上写数据

  ```python
  set aa aa
  ```

- 在slave上读数据

  ```python
  get aa
  ```

  
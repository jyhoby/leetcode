# Day09

## Scrapy-Redis

#### Scrapy和Scrapy-Redis的区别

```
Scrapy 是一个通用的爬虫框架，但是不支持分布式，
Scrapy-Redis 是为了更方便地实现Scrapy分布式爬取，而提供了一些以redis为基础的组件(仅有组件)
```

#### 安装Scrapy-Redis

```python
pip install scrapy-redis
```

#### Scrapy-Redis介绍

提供了下面四种组件（components）：(四种组件意味着这四个模块都要做相应的修改)

- `Scheduler`
- `Duplication Filter`
- `Item Pipeline`
- `Base Spider`

#### Scrapy-Redis架构

![](C:\sz1903-clawer\day09\doc\img\scrapy-redis.png)

![img](img/s-redis.jpg)









####Scrapy-Redis分布式策略

假设有四台电脑：Windows 10、Mac OS X、Ubuntu 16.04、CentOS 7.2，任意一台电脑都可以作为 Master端 或 Slaver端，比如：

- `Master端`(核心服务器) ：使用 Windows 10，搭建一个Redis数据库，不负责爬取，只负责url指纹判重、Request的分配，以及数据的存储
- `Slaver端`(爬虫程序执行端) ：使用 Mac OS X 、Ubuntu 16.04、CentOS 7.2，负责执行爬虫程序，运行过程中提交新的Request给Master

![img](img/masterAndslaver.png)

1. 首先Slaver端从Master端拿任务（Request、url）进行数据抓取，Slaver抓取数据的同时，产生新任务的Request便提交给 Master 处理；
2. Master端只有一个Redis数据库，负责将未处理的Request去重和任务分配，将处理后的Request加入待爬队列，并且存储爬取的数据。

Scrapy-Redis默认使用的就是这种策略，我们实现起来很简单，因为任务调度等工作Scrapy-Redis都已经帮我们做好了，我们只需要继承RedisSpider、指定redis_key就行了。

缺点是，Scrapy-Redis调度的任务是Request对象，里面信息量比较大（不仅包含url，还有callback函数、headers等信息），可能导致的结果就是会降低爬虫速度、而且会占用Redis大量的存储空间，所以如果要保证效率，那么就需要一定硬件水平。



## Redis

```python
windows 下载：
	https://github.com/MicrosoftArchive/redis
	点击release.
    https://github.com/MicrosoftArchive/redis/releases/download/win-3.2.100/Redis-x64-3.2.100.msi

Redis使用请参考<redis函数.txt>

redis简单回顾
	配置
	linux redis客户端连接windows的服务器
		redis-cli -h 10.8.153.5
	配置windows的redis服务器可以让其它客户端连接和读写
		第56行，把这个注释掉
			#bind 127.0.0.1
		第75行
			protected-mode no
 设置密码
            
在配置文件中配置requirepass的密码（当redis重启时密码依然有效）。

   redis 127.0.0.1:6379> config set requirepass test123

   查询密码：

   redis 127.0.0.1:6379> config get requirepass
   (error) ERR operation not permitted

   密码验证：

   redis 127.0.0.1:6379> auth test123
   OK

   再次查询：

   redis 127.0.0.1:6379> config get requirepass
   1) "requirepass"
   2) "test123"

   PS：如果配置文件中没添加密码 那么redis重启后，密码失效；

   3、登陆有密码的Redis：

   在登录的时候的时候输入密码：

   redis-cli -p 6379 -a test123

   先登陆后验证：

   redis-cli -p 6379

   redis 127.0.0.1:6379> auth test123
   OK

```



### 源码自带项目说明：

#### 使用scrapy-redis的example来修改

```python
2、分布式部署
	scrapy ： 一个框架，不能实现分布式爬取
	scrapy-redis ： 基于这个框架开发的一套组件，可以让scrapy实现分布式的爬取
	（1）安装： pip install scrapy-redis
	（2）样本查看
		https://github.com/rmax/scrapy-redis
		example-project\example\spiders
		dmoz.py : 普通crawlspider，没有参考价值
		myspider_redis.py ： 分布式的Spider模板
		mycrawler_redis.py ： 分布式的CrawlSpider模板
		Spider       ====》  RedisSpider
		CrawlSpider  ====》  RedisCrawlSpider
		name                 name
		redis_key            start_urls
		__init__()           allowed_domains
		【注】__init__()是一个坑，现在还是使用allowed_domains这种列表的形式
	（3）存储到redis中
		scrapy-redis组件已经写好往redis中存放的管道，只需要使用即可，默认存储到本机的redis服务中
		如果想存储到其它的redis服务中，需要在配置文件中配置
		REDIS_HOST = 'ip地址'
		REDIS_PORT = 6379
         # 也可以使用 REDIS_URL = "redis://10.20.158.2:6379"
            
        #如果有密码
        REDIS_PARAMS = {'password':'999'}
        
	（4）部署分布式
		爬虫文件按照模板文件修改
		配置文件说明：
			# 使用scrapy-redis组件的去重队列
			DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
			# 使用scrapy-redis组件自己的调度器
			SCHEDULER = "scrapy_redis.scheduler.Scheduler"
			# 是否允许暂停，不会清空redis队列
			SCHEDULER_PERSIST = True


		【注】分布式爬取的时候，指令不是scrapy crawl xx
		scrapy runspider xxx.py

		在我的windows中往队列中添加起始url
			lpush nnspider:start_urls "http://www.baike.com/"

```

把原来的项目变成分布式爬虫

修改设置文件 settings.py

```python
# dupefilter: 去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用scrapy_redis的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 在redis中保持scrapy-redis用到的各个队列，从而允许暂停和暂停后恢复，也就是不清理redis queues
SCHEDULER_PERSIST = True


ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,

    # 使用redis管道：自动存入redis,默认存入本机的redis
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

# 配置远程连接redis
# REDIS_HOST = '10.20.158.2'
# REDIS_PORT = 6379
```

练习：抓取baidu百科

修改spider



```python
from scrapy_redis.spiders import RedisCrawlSpider
from example.items import BaikeItem

class MyCrawler(RedisCrawlSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'mycrawler_redis'
    redis_key = 'mycrawler:start_urls'

    rules = (
        # follow all links
        Rule(LinkExtractor('item/.*'), callback='parse_page', follow=True),
    )

    allowed_domains = ['baike.baidu.com']


    def parse_page(self, response):
```

在redis中保存的记录

```
1) "mycrawler_redis:items"  # 抓取到的数据 
2) "mycrawler_redis:requests"  # 所有待爬取的请求
3) "mycrawler_redis:dupefilter"  # 所有重复的url
```

练习：<http://www.521609.com/gaozhongxiaohua/>

### 数据持久化

##### 存入mysql 

```python

import json
import redis
import pymysql

def main():

    redis_cli = redis.Redis(host='localhost',port=6379)

    mysqldb = pymysql.connect(host='localhost', user='root', password='123456',database='xiaohua')

    while True:
        source,data = redis_cli.blpop(['xiaohua_spider:items'])
        item = json.loads(data)
        print(item)
        try:
            cursor = mysqldb.cursor()
            sql = "insert into pics(name, img) values ('%s','%s')" %(item.get('name'), item.get('picture_url'))
            cursor.execute(sql)
            mysqldb.commit()
            cursor.close()

        except mysqldb.Error as e:
            mysqldb.rollback()
            print(e)



if __name__ == '__main__':
    main()

```






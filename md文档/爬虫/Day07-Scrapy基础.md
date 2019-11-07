# Day07

## Scrapy 框架介绍

```
Scrapy是用纯Python实现一个为了爬取网站数据、提取结构性数据而编写的应用框架，用途非常广泛。
Scrapy框架：用户只需要定制开发几个模块就可以轻松的实现一个爬虫，用来抓取网页内容以及各种图片，非常之方便。
Scrapy 使用了Twisted(其主要对手是Tornado)多线程异步网络框架来处理网络通讯，可以加快我们的下载速度，不用自己去实现异步框架，并且包含了各种中间件接口，可以灵活的完成各种需求。
```



#### Scrapy架构图

![image](scrapy数据流向.png)



```python
Scrapy主要包括了以下组件：
	Scrapy Engine(引擎): 
        负责Spider、ItemPipeline、Downloader、Scheduler中间的通讯，信号、数据传递等。

	Scheduler(调度器): 
        它负责接受`引擎`发送过来的Request请求，并按照一定的方式进行整理排列，入队，当`引擎`需要时，交还给`引擎`。

	Downloader（下载器）：
    	负责下载`Scrapy Engine(引擎)`发送的所有Requests请求，并将其获取到的Responses交还给`Scrapy Engine(引擎)`，由`引擎`交给`Spider`来处理，

	Spider（爬虫）：
    	它负责处理所有Responses,从中分析提取数据，获取Item字段需要的数据，并将需要跟进的URL提交给`引擎`，再次进入`Scheduler(调度器)`，

	Item Pipeline(管道)：
    	它负责处理`Spider`中获取到的Item，并进行进行后期处理（详细分析、过滤、存储等）的地方.

	Downloader Middlewares（下载中间件）：
		你可以当作是一个可以自定义扩展下载功能的组件。

	Spider Middlewares（Spider中间件）：
    	你可以理解为是一个可以自定扩展和操作`引擎`和`Spider`中间`通信`的功能组件（比如进入`Spider`的Responses和从`Spider`出去的Requests）
        
```



### 安装Scrapy

```python
Scrapy的安装介绍
	Scrapy框架官方网址：http://doc.scrapy.org/en/latest
	Scrapy中文维护站点：http://scrapy-chs.readthedocs.io/zh_CN/latest/index.html
	
安装：
	pip install pywin32
	pip install scrapy
其它安装方式:   
	1、安装wheel
		pip install wheel
    2、安装lxml
		pip install lxml
    3、安装pyopenssl
		pip install pyopenssl
    4、安装Twisted
		需要我们自己下载Twisted，然后安装。这里有Python的各种依赖包。选择适合自己Python以及系统的Twisted版本：https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
		# 3.6版本（cp后是python版本）
         pip install Twisted-18.9.0-cp36-cp36m-win_amd64.whl
		
    5、安装pywin32
		pip install pywin32
    6、安装scrapy
        pip install scrapy
        
安装后，只要在命令终端输入scrapy来检测是否安装成功

```



### 使用Scrapy

#### 使用爬虫可以遵循以下步骤：

1. 创建一个Scrapy项目
2. 定义提取的Item
3. 编写爬取网站的 spider 并提取 Item
4. 编写 Item Pipeline 来存储提取到的Item(即数据)



#### 1. 新建项目(scrapy startproject)

##### 创建一个新的Scrapy项目来爬取 http://www.meijutt.com/new100.html 中的数据，使用以下命令：

```python
scrapy startproject meiju
```

##### 创建爬虫程序

```python
cd meiju
scrapy genspider meijuSpider meijutt.com

其中：
	meijuSpider为爬虫文件名
	meijutt.com为爬取网址的域名
```

创建Scrapy工程后, 会自动创建多个文件，下面来简单介绍一下各个主要文件的作用：

```python
scrapy.cfg：
	项目的配置信息，主要为Scrapy命令行工具提供一个基础的配置信息。（真正爬虫相关的配置信息在settings.py文件中）
items.py：
	设置数据存储模板，用于结构化数据，如：Django的Model
pipelines：
	数据处理行为，如：一般结构化的数据持久化
settings.py：
	配置文件，如：递归的层数、并发数，延迟下载等
spiders：
	爬虫目录，如：创建文件，编写爬虫规则
    
注意：一般创建爬虫文件时，以网站域名命名
```

#### 2. 定义Item

​	Item是保存爬取到的数据的容器；其使用方法和python字典类似，虽然我们可以在Scrapy中直接使用dict，但是 Item提供了额外保护机制来避免拼写错误导致的未定义字段错误；

​	类似ORM中的Model定义字段，我们可以通过scrapy.Item 类来定义要爬取的字段。

```python
import scrapy

class MeijuItem(scrapy.Item):
    name = scrapy.Field()
```

#### 3. 编写爬虫

```python
# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from meiju.items import MeijuItem

class MeijuspiderSpider(scrapy.Spider):
    # 爬虫名
    name = 'meijuSpider'
    # 被允许的域名
    allowed_domains = ['meijutt.com']
    # 起始爬取的url
    start_urls = ['http://www.meijutt.com/new100.html']

    # 数据处理
    def parse(self, response):
        # response响应对象
        # xpath
        mytree = etree.HTML(response.text)
        movie_list = mytree.xpath('//ul[@class="top-list  fn-clear"]/li')

        for movie in movie_list:
            name = movie.xpath('./h5/a/text()')

            # 创建item(类字典对象)
            item = MeijuItem()
            item['name'] = name
            yield item

```

##### 启用一个Item Pipeline组件

为了启用Item Pipeline组件，必须将它的类添加到 settings.py文件ITEM_PIPELINES 配置修改settings.py，并设置优先级，分配给每个类的整型值，确定了他们运行的顺序，item按数字从低到高的顺序，通过pipeline，通常将这些数字定义在0-1000范围内（0-1000随意设置，数值越低，组件的优先级越高）

```python
ITEM_PIPELINES = {
   'meiju.pipelines.MeijuPipeline': 300,
}
```

##### 设置UA

在setting.py中设置USER_AGENT的值

```python
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'

```

#### 4. 编写 Pipeline 来存储提取到的Item(即数据)

```python
class SomethingPipeline(object):
    def init(self):    
        # 可选实现，做参数初始化等
        
	def process_item(self, item, spider):
        # item (Item 对象) – 被爬取的item
        # spider (Spider 对象) – 爬取该item的spider
        # 这个方法必须实现，每个item pipeline组件都需要调用该方法，
        # 这个方法必须返回一个 Item 对象，被丢弃的item将不会被之后的pipeline组件所处理。
        return item

    def open_spider(self, spider):
        # spider (Spider 对象) – 被开启的spider
        # 可选实现，当spider被开启时，这个方法被调用。

    def close_spider(self, spider):
        # spider (Spider 对象) – 被关闭的spider
        # 可选实现，当spider被关闭时，这个方法被调用
    
```
##### 运行爬虫：

```python
scrapy crawl meijuSpider

# nolog模式
scrapy crawl meijuSpider --nolog  
```

scrapy保存信息的最简单的方法主要有这几种，-o 输出指定格式的文件，命令如下：

```python
scrapy crawl meijuSpider -o meiju.json
scrapy crawl meijuSpider -o meiju.csv
scrapy crawl meijuSpider -o meiju.xml
```



## Scrapy Shell

Scrapy终端是一个交互终端，我们可以在未启动spider的情况下尝试及调试代码

##### 启动Scrapy Shell

```python
scrapy shell "https://hr.tencent.com/position.php?&start=0#a"
```

### Selectors选择器

```python
Scrapy Selectors 内置 XPath 和 CSS Selector 表达式机制
Selector有四个基本的方法，最常用的还是xpath:
	xpath(): 传入xpath表达式，返回该表达式所对应的所有节点的selector list列表
	extract(): 序列化该节点为Unicode字符串并返回list
	css(): 传入CSS表达式，返回该表达式所对应的所有节点的selector list列表，语法同 BeautifulSoup4
	re(): 根据传入的正则表达式对数据进行提取，返回Unicode字符串list列表
	
# 使用xpath
response.xpath('//title')
```

##### 练习： Scrapy爬取新浪新闻存入数据库 http://roll.news.sina.com.cn/news/gnxw/gdxw1/index_1.shtml 



## Spider类

```python
Spider类定义了如何爬取某个(或某些)网站。包括了爬取的动作(例如:是否跟进链接)以及如何从网页的内容中提取结构化数据(爬取item)。 换句话说，Spider就是你定义爬取的动作及分析某个网页(或者是有些网页)的地方。

scrapy.Spider是最基本的类，所有编写的爬虫必须继承这个类。

主要用到的函数及调用顺序为：
__init__(): 
	初始化爬虫名字和start_urls列表
start_requests() 
	调用make_requests_from_url():生成Requests对象交给Scrapy下载并返回response
parse():
	解析response，并返回Item或Requests（需指定回调函数）。
	Item传给Item pipline持久化，而Requests交由Scrapy下载，并由指定的回调函数处理（默认parse())，一直进行循环，直到处理完所有的数据为止。
```

#### Spider类源码参考

```python
#所有爬虫的基类，用户定义的爬虫必须从这个类继承
class Spider(object_ref):
    # 定义spider名字的字符串(string)。
    # spider的名字定义了Scrapy如何定位(并初始化)spider，所以其必须是唯一的。
    # name是spider最重要的属性，而且是必须的。
    # 一般做法是以该网站(domain)(加或不加 后缀 )来命名spider。 例如，如果spider爬取 mywebsite.com ，该spider通常会被命名为 mywebsite
    name = None

    # 初始化，提取爬虫名字，start_urls
    def __init__(self, name=None, **kwargs):
        if name is not None:
            self.name = name
        # 如果爬虫没有名字，中断后续操作则报错
        elif not getattr(self, 'name', None):
            raise ValueError("%s must have a name" % type(self).__name__)

        # python 对象或类型通过内置成员__dict__来存储成员信息
        self.__dict__.update(kwargs)

        #URL列表。当没有指定的URL时，spider将从该列表中开始进行爬取。 因此，第一个被获取到的页面的URL将是该列表之一。 后续的URL将会从获取到的数据中提取。
        if not hasattr(self, 'start_urls'):
            self.start_urls = []

    # 打印Scrapy执行后的log信息
    def log(self, message, level=log.DEBUG, **kw):
        log.msg(message, spider=self, level=level, **kw)

    # 判断对象object的属性是否存在，不存在则断言处理
    def set_crawler(self, crawler):
        assert not hasattr(self, '_crawler'), "Spider already bounded to %s" % crawler
        self._crawler = crawler

    @property
    def crawler(self):
        assert hasattr(self, '_crawler'), "Spider not bounded to any crawler"
        return self._crawler

    @property
    def settings(self):
        return self.crawler.settings

    #该方法将读取start_urls内的地址，并为每一个地址生成一个Request对象，交给Scrapy下载并返回Response
    #该方法仅调用一次
    def start_requests(self):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    #start_requests()中调用，实际生成Request的函数。
    #Request对象默认的回调函数为parse()，提交的方式为get
    def make_requests_from_url(self, url):
        return Request(url, dont_filter=True)

    #默认的Request对象回调函数，处理返回的response。
    #生成Item或者Request对象。用户必须实现这个
    def parse(self, response):
        raise NotImplementedError

    @classmethod
    def handles_request(cls, request):
        return url_is_from_spider(request.url, cls)

    def __str__(self):
        return "<%s %r at 0x%0x>" % (type(self).__name__, self.name, id(self))

    __repr__ = __str__
```

#### 主要属性和方法

- name

  > 定义spider名字的字符串。唯一
  >

- allowed_domains

  > 包含了spider允许爬取的域名(domain)的列表，可选。

- start_urls

  > 初始URL元祖/列表。当没有制定特定的URL时，spider将从该列表中开始进行爬取。

- start_requests(self)

  > 该方法必须返回一个可迭代对象(iterable)。该对象包含了spider用于爬取（默认实现是使用 start_urls 的url）的第一个Request。
  >
  > 当spider启动爬取并且未指定start_urls时，该方法被调用。

- parse(self, response)

  > 当请求url返回网页没有指定回调函数时，默认的Request对象回调函数。用来处理网页返回的response，以及生成Item或者Request对象。

- log(self, message[, level, component])

  > 使用 scrapy.log.msg() 方法记录日志信息。




##### 练习：爬取糗事百科翻页爬取地址： https://www.qiushibaike.com/8hr/page/{}/ 

##### 练习：爬取腾讯招聘网,翻页获取岗位名称，时间，招聘人数，并存入数据库 https://hr.tencent.com/position.php?keywords=&lid=2218&tid=87&start=0#a



# CrawlSpider

CrawlSpider是Spider的派生类，Spider类的设计原则是只爬取start_url列表中的网页，而CrawlSpider类定义了一些规则(rule)来提供跟进link的方便的机制，从爬取的网页中获取link并继续爬取的工作更适合。

#### CrawlSpider类源码参考

```python
class CrawlSpider(Spider):
    rules = ()
    def __init__(self, *a, **kw):
        super(CrawlSpider, self).__init__(*a, **kw)
        self._compile_rules()

    #首先调用parse()来处理start_urls中返回的response对象
    #parse()则将这些response对象传递给了_parse_response()函数处理，并设置回调函数为parse_start_url()
    #设置了跟进标志位True
    #parse将返回item和跟进了的Request对象    
    def parse(self, response):
        return self._parse_response(response, self.parse_start_url, cb_kwargs={}, follow=True)

    #处理start_url中返回的response，需要重写
    def parse_start_url(self, response):
        return []

    def process_results(self, response, results):
        return results

    #从response中抽取符合任一用户定义'规则'的链接，并构造成Resquest对象返回
    def _requests_to_follow(self, response):
        if not isinstance(response, HtmlResponse):
            return
        seen = set()
        #抽取之内的所有链接，只要通过任意一个'规则'，即表示合法
        for n, rule in enumerate(self._rules):
            links = [l for l in rule.link_extractor.extract_links(response) if l not in seen]
            #使用用户指定的process_links处理每个连接
            if links and rule.process_links:
                links = rule.process_links(links)
            #将链接加入seen集合，为每个链接生成Request对象，并设置回调函数为_repsonse_downloaded()
            for link in links:
                seen.add(link)
                #构造Request对象，并将Rule规则中定义的回调函数作为这个Request对象的回调函数
                r = Request(url=link.url, callback=self._response_downloaded)
                r.meta.update(rule=n, link_text=link.text)
                #对每个Request调用process_request()函数。该函数默认为indentify，即不做任何处理，直接返回该Request.
                yield rule.process_request(r)

    #处理通过rule提取出的连接，并返回item以及request
    def _response_downloaded(self, response):
        rule = self._rules[response.meta['rule']]
        return self._parse_response(response, rule.callback, rule.cb_kwargs, rule.follow)

    #解析response对象，会用callback解析处理他，并返回request或Item对象
    def _parse_response(self, response, callback, cb_kwargs, follow=True):
        #首先判断是否设置了回调函数。（该回调函数可能是rule中的解析函数，也可能是 parse_start_url函数）
        #如果设置了回调函数（parse_start_url()），那么首先用parse_start_url()处理response对象，
        #然后再交给process_results处理。返回cb_res的一个列表
        if callback:
            #如果是parse调用的，则会解析成Request对象
            #如果是rule callback，则会解析成Item
            cb_res = callback(response, **cb_kwargs) or ()
            cb_res = self.process_results(response, cb_res)
            for requests_or_item in iterate_spider_output(cb_res):
                yield requests_or_item

        #如果需要跟进，那么使用定义的Rule规则提取并返回这些Request对象
        if follow and self._follow_links:
            #返回每个Request对象
            for request_or_item in self._requests_to_follow(response):
                yield request_or_item

    def _compile_rules(self):
        def get_method(method):
            if callable(method):
                return method
            elif isinstance(method, basestring):
                return getattr(self, method, None)

        self._rules = [copy.copy(r) for r in self.rules]
        for rule in self._rules:
            rule.callback = get_method(rule.callback)
            rule.process_links = get_method(rule.process_links)
            rule.process_request = get_method(rule.process_request)

    def set_crawler(self, crawler):
        super(CrawlSpider, self).set_crawler(crawler)
        self._follow_links = crawler.settings.getbool('CRAWLSPIDER_FOLLOW_LINKS', True)
```

### LinkExtractors

```python
使用LinkExtractors 的目的: 提取链接｡每个LinkExtractor有唯一的公共方法是 extract_links()，它接收一个 Response 对象，并返回一个 scrapy.link.Link 对象。
scrapy.linkextractors.LinkExtractor(
    allow = (),
    deny = (),
    allow_domains = (),
    deny_domains = (),
    deny_extensions = None,
    restrict_xpaths = (),
    tags = ('a','area'),
    attrs = ('href'),
    canonicalize = True,
    unique = True,
    process_value = None
)

主要参数：
	allow：满足括号中“正则表达式”的值会被提取，如果为空，则全部匹配。
	deny：与这个正则表达式(或正则表达式列表)匹配的URL一定不提取。
	allow_domains：会被提取的链接的domains。
	deny_domains：一定不会被提取链接的domains。
	restrict_xpaths：使用xpath表达式，和allow共同作用过滤链接。

```

### rules

```python
在rules中包含一个或多个Rule对象，每个Rule对爬取网站的动作定义了特定操作。如果多个rule匹配了相同的链接，则根据规则在本集合中被定义的顺序，第一个会被使用。

scrapy.spiders.Rule(
        link_extractor, 
        callback = None, 
        cb_kwargs = None, 
        follow = None, 
        process_links = None, 
        process_request = None
)

link_extractor：是一个Link Extractor对象，用于定义需要提取的链接。
callback： 从link_extractor中每获取到链接时，参数所指定的值作为回调函数，该回调函数接受一个response作为其第一个参数。
	注意：当编写爬虫规则时，避免使用parse作为回调函数。由于CrawlSpider使用parse方法来实现其逻辑，如果覆盖了parse方法，crawlspider将会运行失败。
follow：是一个布尔(boolean)值，指定了根据该规则从response提取的链接是否需要跟进。 如果callback为None，follow默认设置为True ，否则默认为False。
process_links：指定该spider中哪个的函数将会被调用，从link_extractor中获取到链接列表时将会调用该函数。该方法主要用来过滤。
process_request：指定该spider中哪个的函数将会被调用， 该规则提取到每个request时都会调用该函数。 (用来过滤request)

```



## robots协议

Robots协议（也称为爬虫协议、机器人协议等）的全称是“网络爬虫排除标准”（Robots Exclusion Protocol），网站通过Robots协议告诉搜索引擎哪些页面可以抓取，哪些页面不能抓取。robots.txt文件是一个文本文件。当一个搜索蜘蛛访问一个[站点](https://baike.baidu.com/item/%E7%AB%99%E7%82%B9)时，它会首先[检查](https://baike.baidu.com/item/%E6%A3%80%E6%9F%A5)该站点[根目录](https://baike.baidu.com/item/%E6%A0%B9%E7%9B%AE%E5%BD%95)下是否存在robots.txt，如果存在，搜索机器人就会按照该文件中的内容来确定访问的范围；如果该文件不存在，所有的搜索蜘蛛将能够访问网站上所有没有被口令保护的页面。

```
User-agent: *  这里的*代表的所有的搜索引擎种类，*是一个通配符
Disallow: /admin/ 这里定义是禁止爬寻admin目录下面的目录
Disallow: /require/ 这里定义是禁止爬寻require目录下面的目录
Disallow: /ABC/ 这里定义是禁止爬寻ABC目录下面的目录
Disallow: /cgi-bin/*.htm 禁止访问/cgi-bin/目录下的所有以".htm"为后缀的URL(包含子目录)。
Disallow: /*?* 禁止访问网站中所有包含问号 (?) 的网址
Disallow: /.jpg$ 禁止抓取网页所有的.jpg格式的图片
Disallow:/ab/adc.html 禁止爬取ab文件夹下面的adc.html文件。
Allow: /cgi-bin/　这里定义是允许爬寻cgi-bin目录下面的目录
Allow: /tmp 这里定义是允许爬寻tmp的整个目录
Allow: .htm$ 仅允许访问以".htm"为后缀的URL。
Allow: .gif$ 允许抓取网页和gif格式图片
Sitemap: 网站地图 告诉爬虫这个页面是网站地图
```

```
实例分析：淘宝网的 robots.txt文件
http://www.taobao.com/robots.txt
```

**禁止robots协议将 ROBOTSTXT_OBEY = True改为False**



## Logging

Scrapy提供了log功能，可以通过 logging 模块使用。

> 可以修改配置文件settings.py，任意位置添加下面两行，效果会清爽很多。

```python
LOG_ENABLED = True  # 开启
LOG_FILE = "TencentSpider.log" #日志文件名
LOG_LEVEL = "INFO" #日志级别
```

#### Log levels

- Scrapy提供5层logging级别:
- CRITICAL - 严重错误(critical)
- ERROR - 一般错误(regular errors)
- WARNING - 警告信息(warning messages)
- INFO - 一般信息(informational messages)
- DEBUG - 调试信息(debugging messages)

#### logging设置

通过在setting.py中进行以下设置可以被用来配置logging:

`LOG_ENABLED`

​	默认: True，启用logging

`LOG_ENCODING`

​	默认: 'utf-8'，logging使用的编码

`LOG_FILE`

​	默认: None，在当前目录里创建logging输出文件的文件名

`LOG_LEVEL`

​	默认: 'DEBUG'，log的最低级别



#### settings.py 设置抓取间隔

```python
DOWNLOAD_DELAY = 0.25   # 设置下载间隔为250ms
```


##### 练习： 抓取电影信息，翻页抓取 http://www.id97.com/movie/?page=1

​	




# Day08

##反反爬虫相关机制

```python
Scrapy官方文档描述：
	Some websites implement certain measures to prevent bots from crawling them, with varying degrees of sophistication. Getting around those measures can be difficult and tricky, and may sometimes require special infrastructure. Please consider contacting commercial support if in doubt.
(有些些网站使用特定的不同程度的复杂性规则防止爬虫访问，绕过这些规则是困难和复杂的，有时可能需要特殊的基础设施，如果有疑问，请联系商业支持。)

```

### 通常反反爬主要有以下几个策略：

##### 动态设置User-Agent（随机切换User-Agent，模拟不同用户的浏览器信息）

```python
添加请求头的多种方式

# 方法1：
# 	修改setting.py中的User-Agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'

# 方法2: 
#	修改setting中的DEFAULT_REQUEST_HEADERS
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
 }


```

##### 禁用Cookies

```
也就是不启用cookies middleware，不向Server发送cookies，有些网站通过cookie的使用发现爬虫行为
可以通过COOKIES_ENABLED控制 CookiesMiddleware 开启或关闭
除非特殊需要，可以禁用cookies，防止某些网站根据Cookie来封锁爬虫。
COOKIES_ENABLED = False
```

##### 设置延迟下载

```python
防止访问过于频繁，设置为 2秒 或更高
DOWNLOAD_DELAY = 3
```

##### 使用IP地址池

```
VPN和代理IP，现在大部分网站都反IP的
```

##### 使用Crawlera

```python
Crawlera： 专用于爬虫的代理组件
正确配置和设置下载中间件后，项目所有的request都是通过crawlera发出。
DOWNLOADER_MIDDLEWARES = {
     'scrapy_crawlera.CrawleraMiddleware': 600
}

CRAWLERA_ENABLED = True
CRAWLERA_USER = '注册/购买的UserKey'
CRAWLERA_PASS = '注册/购买的Password'
```


### 自定义中间件

```
process_request(self, request, spider)
当每个request通过下载中间件时，该方法被调用。

process_response(self, request, response, spider)
当下载器完成http请求，传递响应给引擎的时候调用
```

##### 修改settings.py配置USER_AGENTS和PROXIES

```python
# 添加USER_AGENTS：
USER_AGENTS = [
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
]

# 添加代理IP设置PROXIES：
# 免费代理IP可以网上搜索（免费的不太稳定），或者付费购买一批可用的私密代理IP：
PROXIES = [
    {'ip_port': '111.8.60.9:8123'},
    {'ip_port': '101.71.27.120:80'},
    {'ip_port': '122.96.59.104:80'},
    {'ip_port': '122.224.249.122:8088'},
]
```

##### 创建中间件类

```python
# -*- coding: utf-8 -*-
import random
from settings import USER_AGENTS
from settings import PROXIES


# 随机代理IP
class RandomProxy(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        request.meta['proxy'] = "http://" + proxy['ip_port']
```

##### 配置中间件

```python
# 最后设置setting.py里的DOWNLOADER_MIDDLEWARES，添加自己编写的下载中间件类
DOWNLOADER_MIDDLEWARES = {
    #'mySpider.middlewares.MyCustomDownloaderMiddleware': 543,
    'mySpider.middlewares.RandomUserAgent': 81,
    'mySpider.middlewares.ProxyMiddleware': 100
}
```



## Settings配置

```
Scrapy设置(settings)提供了定制Scrapy组件的方法。可以控制包括核心(core)，插件(extension)，pipeline及spider组件。
```

### BOT_NAME

默认: `'scrapybot'`

Scrapy项目实现的bot的名字(也为项目名称)。 这将用来构造默认 User-Agent，同时也用来log。

当您使用 [`startproject`](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/commands.html#std:command-startproject) 命令创建项目时其也被自动赋值。

### CONCURRENT_ITEMS

默认: `100`

Item Processor(即 [Item Pipeline](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/item-pipeline.html#topics-item-pipeline)) 同时处理(每个response的)item的最大值。

### CONCURRENT_REQUESTS

默认: `16`

Scrapy downloader 并发请求(concurrent requests)的最大值。

### CONCURRENT_REQUESTS_PER_DOMAIN

默认: `8`

对单个网站进行并发请求的最大值。

### CONCURRENT_REQUESTS_PER_IP

默认: `0`

对单个IP进行并发请求的最大值。如果非0，则忽略 [`CONCURRENT_REQUESTS_PER_DOMAIN`](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/settings.html#std:setting-CONCURRENT_REQUESTS_PER_DOMAIN) 设定， 使用该设定。 也就是说，并发限制将针对IP，而不是网站。

该设定也影响 [`DOWNLOAD_DELAY`](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/settings.html#std:setting-DOWNLOAD_DELAY): 如果 [`CONCURRENT_REQUESTS_PER_IP`](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/settings.html#std:setting-CONCURRENT_REQUESTS_PER_IP) 非0，下载延迟应用在IP而不是网站上。

### DEFAULT_REQUEST_HEADERS

```
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}
```

Scrapy HTTP Request使用的默认header。由 [`DefaultHeadersMiddleware`](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/downloader-middleware.html#scrapy.contrib.downloadermiddleware.defaultheaders.DefaultHeadersMiddleware) 产生。

### DEPTH_LIMIT

默认: `0`

爬取网站最大允许的深度(depth)值。如果为0，则没有限制。

### DEPTH_PRIORITY

默认: `0`

整数值。用于根据深度调整request优先级。

如果为0，则不根据深度进行优先级调整。

### DEPTH_STATS

默认: `True`

是否收集最大深度数据。

### DEPTH_STATS_VERBOSE

默认: `False`

是否收集详细的深度数据。如果启用，每个深度的请求数将会被收集在数据中。

### DNSCACHE_ENABLED

默认: `True`

是否启用DNS内存缓存(DNS in-memory cache)。

### DOWNLOADER

默认: `'scrapy.core.downloader.Downloader'`

用于crawl的downloader.

### DOWNLOADER_MIDDLEWARES

默认:: `{}`

保存项目中启用的下载中间件及其顺序的字典。

### DOWNLOADER_MIDDLEWARES_BASE

默认:

```
{
    'scrapy.contrib.downloadermiddleware.robotstxt.RobotsTxtMiddleware': 100,
    'scrapy.contrib.downloadermiddleware.httpauth.HttpAuthMiddleware': 300,
    'scrapy.contrib.downloadermiddleware.downloadtimeout.DownloadTimeoutMiddleware': 350,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': 400,
    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 500,
    'scrapy.contrib.downloadermiddleware.defaultheaders.DefaultHeadersMiddleware': 550,
    'scrapy.contrib.downloadermiddleware.redirect.MetaRefreshMiddleware': 580,
    'scrapy.contrib.downloadermiddleware.httpcompression.HttpCompressionMiddleware': 590,
    'scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware': 600,
    'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware': 700,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 750,
    'scrapy.contrib.downloadermiddleware.chunked.ChunkedTransferMiddleware': 830,
    'scrapy.contrib.downloadermiddleware.stats.DownloaderStats': 850,
    'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware': 900,
}

```

包含Scrapy默认启用的下载中间件的字典。 永远不要在项目中修改该设定.

### DOWNLOADER_STATS

默认: `True`

是否收集下载器数据。

### DOWNLOAD_DELAY

默认: `0`

下载器在下载同一个网站下一个页面前需要等待的时间。该选项可以用来限制爬取速度， 减轻服务器压力。同时也支持小数:

```
DOWNLOAD_DELAY = 0.25    # 250 ms of delay
```



### DOWNLOAD_TIMEOUT

默认: `180`

下载器超时时间(单位: 秒)。

### EXTENSIONS

默认:: `{}`

保存项目中启用的插件及其顺序的字典。

### EXTENSIONS_BASE

默认:

```
{
    'scrapy.contrib.corestats.CoreStats': 0,
    'scrapy.webservice.WebService': 0,
    'scrapy.telnet.TelnetConsole': 0,
    'scrapy.contrib.memusage.MemoryUsage': 0,
    'scrapy.contrib.memdebug.MemoryDebugger': 0,
    'scrapy.contrib.closespider.CloseSpider': 0,
    'scrapy.contrib.feedexport.FeedExporter': 0,
    'scrapy.contrib.logstats.LogStats': 0,
    'scrapy.contrib.spiderstate.SpiderState': 0,
    'scrapy.contrib.throttle.AutoThrottle': 0,
}

```

可用的插件列表。需要注意，有些插件需要通过设定来启用。默认情况下， 该设定包含所有稳定(stable)的内置插件。

### ITEM_PIPELINES

默认: `{}`

保存项目中启用的pipeline及其顺序的字典。该字典默认为空，值(value)任意。 不过值(value)习惯设定在0-1000范围内。

```
ITEM_PIPELINES = {
    'mybot.pipelines.validate.ValidateMyItem': 300,
    'mybot.pipelines.validate.StoreMyItem': 800,
}

```

### ITEM_PIPELINES_BASE

默认: `{}`

保存项目中默认启用的pipeline的字典。 永远不要在项目中修改该设定，而是修改 [`ITEM_PIPELINES`](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/settings.html#std:setting-ITEM_PIPELINES)。



### LOG_ENABLED

默认: `True`

是否启用logging。

### LOG_ENCODING

默认: `'utf-8'`

logging使用的编码。

### LOG_FILE

默认: `None`

logging输出的文件名。如果为None，则使用标准错误输出(standard error)。

### LOG_LEVEL

默认: `'DEBUG'`

log的最低级别。可选的级别有: CRITICAL、 ERROR、WARNING、INFO、DEBUG。更多内容请查看 [Logging](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/logging.html#topics-logging) 。

### LOG_STDOUT

默认: `False`

如果为 `True` ，进程所有的标准输出(及错误)将会被重定向到log中。例如， 执行 `print 'hello'` ，其将会在Scrapy log中显示。



### MEMDEBUG_ENABLED

默认: `False`

是否启用内存调试(memory debugging)。

### MEMDEBUG_NOTIFY

默认: `[]`

如果该设置不为空，当启用内存调试时将会发送一份内存报告到指定的地址；否则该报告将写到log中。

样例:

```
MEMDEBUG_NOTIFY = ['user@example.com']
```

### MEMUSAGE_ENABLED

默认: `False`

Scope: `scrapy.contrib.memusage`

是否启用内存使用插件。当Scrapy进程占用的内存超出限制时，该插件将会关闭Scrapy进程， 同时发送email进行通知。

### MEMUSAGE_LIMIT_MB

默认: `0`

Scope: `scrapy.contrib.memusage`

在关闭Scrapy之前所允许的最大内存数(单位: MB)(如果 MEMUSAGE_ENABLED为True)。 如果为0，将不做限制。

### MEMUSAGE_NOTIFY_MAIL

默认: `False`

Scope: `scrapy.contrib.memusage`

达到内存限制时通知的email列表。

```
MEMUSAGE_NOTIFY_MAIL = ['user@example.com']
```

### MEMUSAGE_REPORT

默认: `False`

Scope: `scrapy.contrib.memusage`

每个spider被关闭时是否发送内存使用报告。

### MEMUSAGE_WARNING_MB

默认: `0`

Scope: `scrapy.contrib.memusage`

在发送警告email前所允许的最大内存数(单位: MB)(如果 MEMUSAGE_ENABLED为True)。 如果为0，将不发送警告。

### NEWSPIDER_MODULE

默认: `''`

使用 [`genspider`](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/commands.html#std:command-genspider) 命令创建新spider的模块。

```
NEWSPIDER_MODULE = 'mybot.spiders_dev'
```

### REDIRECT_MAX_TIMES

默认: `20`

定义request允许重定向的最大次数。超过该限制后该request直接返回获取到的结果。 对某些任务我们使用Firefox默认值。

### REDIRECT_PRIORITY_ADJUST

默认: `+2`

修改重定向请求相对于原始请求的优先级。

### ROBOTSTXT_OBEY

默认: `False`

Scope: `scrapy.contrib.downloadermiddleware.robotstxt`

如果启用，Scrapy将会尊重 robots.txt策略。

### SCHEDULER

默认: `'scrapy.core.scheduler.Scheduler'`

用于爬取的调度器。

### SPIDER_CONTRACTS

默认:: `{}`

保存项目中启用用于测试spider的scrapy contract及其顺序的字典

### SPIDER_CONTRACTS_BASE

默认:

```
{
    'scrapy.contracts.default.UrlContract' : 1,
    'scrapy.contracts.default.ReturnsContract': 2,
    'scrapy.contracts.default.ScrapesContract': 3,
}

```

保存项目中默认启用的scrapy contract的字典。 永远不要在项目中修改该设定，而是修改[`SPIDER_CONTRACTS`](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/settings.html#std:setting-SPIDER_CONTRACTS) 。

### SPIDER_MIDDLEWARES

默认:: `{}`

保存项目中启用的下载中间件及其顺序的字典。 

### SPIDER_MIDDLEWARES_BASE

默认:

```
{
    'scrapy.contrib.spidermiddleware.httperror.HttpErrorMiddleware': 50,
    'scrapy.contrib.spidermiddleware.offsite.OffsiteMiddleware': 500,
    'scrapy.contrib.spidermiddleware.referer.RefererMiddleware': 700,
    'scrapy.contrib.spidermiddleware.urllength.UrlLengthMiddleware': 800,
    'scrapy.contrib.spidermiddleware.depth.DepthMiddleware': 900,
}

```

保存项目中默认启用的spider中间件的字典。 永远不要在项目中修改该设定，而是修改[`SPIDER_MIDDLEWARES`](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/settings.html#std:setting-SPIDER_MIDDLEWARES) 。

### SPIDER_MODULES

默认: `[]`

Scrapy搜索spider的模块列表。

```python
SPIDER_MODULES = ['mybot.spiders_prod', 'mybot.spiders_dev']
```

### STATS_CLASS

默认: `'scrapy.statscol.MemoryStatsCollector'`

收集数据的类。该类必须实现 [状态收集器(Stats Collector) API](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/api.html#topics-api-stats).

### STATS_DUMP

默认: `True`

当spider结束时dump [Scrapy状态数据](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/stats.html#topics-stats) (到Scrapy log中)。

### STATSMAILER_RCPTS

默认: `[]` 

spider完成爬取后发送Scrapy数据。

### TELNETCONSOLE_ENABLED

默认: `True`

表明 [telnet 终端](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/telnetconsole.html#topics-telnetconsole) (及其插件)是否启用的布尔值。

### TELNETCONSOLE_PORT

默认: `[6023, 6073]`

telnet终端使用的端口范围。如果设置为 `None` 或 `0` ， 则使用动态分配的端口。

### TEMPLATES_DIR

默认: scrapy模块内部的 `templates`

使用 [`startproject`](https://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/commands.html#std:command-startproject) 命令创建项目时查找模板的目录。

### URLLENGTH_LIMIT

默认: `2083`

Scope: `contrib.spidermiddleware.urllength`

爬取URL的最大长度。

### USER_AGENT

默认: `"Scrapy/VERSION (+http://scrapy.org)"`

爬取的默认User-Agent，除非被覆盖。

#### REACTOR_THREADPOOL_MAXSIZE

线程池数量，默认10条



# scrapy模拟登录

注意：模拟登录时，必须保证settings.py里的COOKIES_ENABLED(Cookies中间件) 处于开启状态

> `COOKIES_ENABLED = True`或`# COOKIES_ENABLED = False`

#### 一：直接POST数据

```python
# POST请求
# 百度翻译：
url = "http://fanyi.baidu.com/sug"
参数： {'kw': 'wolf'}
```

```python
# 只要是需要提供post数据的，就可以用这种方法。下面示例里post的数据是账户密码：
# 可以使用yield scrapy.FormRequest(url, formdata, callback)方法发送POST请求。
# 如果希望程序执行一开始就发送POST请求，可以重写Spider类的start_requests(self)方法，并且不再调用start_urls里的url。

class mySpider(scrapy.Spider):
    # start_urls = ["http://www.example.com/"]

    def start_requests(self):
        url = 'http://www.renren.com/PLogin.do'
        # FormRequest 是Scrapy发送POST请求的方法
        yield scrapy.FormRequest(
            url = url,
            formdata = {"email" : "18058766787", "password" : "Changeme_123"},
            callback = self.parse_page
        )
    def parse_page(self, response):
        print(response.text)
        # do something
```

#### 二：直接使用保存登录状态的Cookie模拟登录

- 如果实在没办法了，可以用这种方法模拟登录，虽然麻烦一点，但是成功率100%

```python
# -*- coding: utf-8 -*-
import scrapy

class RenrenSpider(scrapy.Spider):
    name = "renren"
    allowed_domains = ["renren.com"]
    start_urls = [
        'http://www.renren.com/111111',
        'http://www.renren.com/222222',
        'http://www.renren.com/333333',
    ]
        cookies = {
            'anonymid':'jsvon3qz-88m55l',
            '_r01_':'1',
            'ln_uact':'18058766787',
            'ln_hurl':'http://head.xiaonei.com/photos/0/0/men_main.gif',
            'depovince':'GW',
            'JSESSIONID':'abc1odayq7GN7_H65hYLw',
            'first_login_flag':'1',
            'wp_fold':'0',
            '_de':'AFF129CA7D7B524FAA9A4DB303A192B0',
            'jebecookies':'c6f9d842-36d9-4e95-98a8-69dd6db04f55|||||',
            'p':'ad876e09a18ef9e0279fc6a2f613c9e11',
            'ap':'969929271',
            't':'837747d73ea20da09fd994d4c85891e81',
            'societyguester':'837747d73ea20da09fd994d4c85891e81',
            'id':'969929271',
            'xnsid':'8ddd65b8',
            'ver':'7.0',
            'loginfrom':'null'
        }
        #重写start_request方法
     def start_requests(self):
        url = 'http://www.renren.com/969929271'
        # FormRequest 是Scrapy发送POST请求的方法

        yield scrapy.Request(url=url,cookies=cookies, callback=self.parse)

    # 处理响应内容
    def parse(self, response):
        print "===========" + response.url
        with open("deng.html", "w") as filename:
            filename.write(response.body)
            
```

#### 三：使用selenium插件

```
options = webdriver.ChromeOptions()
# 设置为开发者模式，防止被各大网站识别出来使用了Selenium
options.add_experimental_option('excludeSwitches', ['enable-automation'])
```

##### 模拟登录知乎




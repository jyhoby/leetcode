胡乐

xmxx@qq.com



# Day01 

### 一、爬虫介绍

#### 什么是爬虫

```
爬虫：网络爬虫又称为网络蜘蛛,网络蚂蚁,网络机器人等,可以自动化浏览网络中的信息,当然浏览信息的时候需要按照我们的规定的规则进行,这些规则称之为网络爬虫算法,使用python可以很方便的写出爬虫程序,进行互联网信息的自动化检索

网 ： 互联网
蜘蛛网： 互联网理解为蜘蛛网
爬虫： 蜘蛛

为什么学习爬虫
	私人定制一个搜索引擎,并且可以对搜索引擎的数采集工作原理进行更深层次地理解
	获取更多的数据源,并且这些数据源可以按我们的目的进行采集,去掉很多无关数据
	更好的进行seo(搜索引擎优化)

网络爬虫的组成
	控制节点： 叫做爬虫中央控制器,主要负责根据URL地址分配线程,并调用爬虫节点进行具体爬行
	爬虫节点： 按照相关算法,对网页进行具体爬行,主要包括下载网页以及对网页的文本处理,爬行后会将对应的爬行结果存储到对应的资源库中
	资源库构成： 存储爬虫爬取到的响应数据,一般为数据库
	
爬虫设计思路
	首先确定需要爬取的网页URL地址
	通过HTTP协议来获取对应的HTML页面
	提取html页面里的有用数据
		如果是需要的数据就保存起来
		如果是其他的URL,那么就执行第二部
	
```

#### Python爬虫的优势

```
PHP: 虽然是世界上最好的语言,但是天生不是干爬虫的命,php对多线程,异步支持不足,并发不足,爬虫是工具性程序,对速度和效率要求较高。

Java: 生态圈完善,是PYthon最大的对手,但是java本身很笨重,代码量大,重构成本比较高,任何修改都会导致大量的代码的变动.最要命的是爬虫需要经常修改部分代码
# 爬虫 -> 反爬 -> 反反爬 -> 反反反爬 .... 

C/C++: 运行效率和性能几乎最强,但是学习成本非常高,代码成型较慢,能用C/C++写爬虫,说明能力很强,但不是最正确的选择.

Python: 语法优美,代码简洁,开发效率高,三方模块多,调用其他接口也方便, 有强大的爬虫Scrapy,以及成熟高效的scrapy-redis分布策略

```

#### Python爬虫需要掌握什么

```
Python基础语法
HTML基础

如何抓取页面: 
	HTTP请求处理,urllib处理后的请求可以模拟浏览器发送请求,获取服务器响应文件
解析服务器响应的内容: 
	re,xpath,BeautifulSoup4,jsonpath,pyquery
	目的是使用某种描述性语法来提取匹配规则的数据
如何采取动态html,验证码处理:
	通用的动态页面采集, Selenium+PhantomJs(无界面浏览器),模拟真实浏览器加载js,ajax等非静态页面数据
Scrapy框架
	国内常见的框架Scrapy,Pyspider
	高定制性高性能(异步网络框架twisted),所以数据下载速度非常快,提供了数据存储,数据下载,提取规则等组件
分布式策略
	scrapy-redis
	在Scrapy的基础上添加了一套以redis数据库为核心的一套组件,让scrapy框架支持分布式的功能,主要在redis里做请求指纹去重,请求分配,数据临时存储
	
```

#### 爬虫与反爬虫与反反爬虫三角之争

```
最头痛的人
	爬虫做到最后, 最头痛的不是复杂的页面, 也不是海量的数据, 而是网站另一头的反爬虫人员
反爬虫技术
	User-Agent
	代理
	验证码
	动态数据加载
	加密数据
是否需要反爬虫
	机器成本+人力成本 >  数据价值,就不反了,一般做到封IP就可以
	服务器压力
	面子的战争
	
爬虫和反爬虫之间的战争,最后一定是爬虫胜利

```

#### 网络爬虫类型

```
通用网络爬虫
	概念： 搜索引擎用的爬虫系统
	用户群体： 搜索引擎用的爬虫系统
	目标： 尽可能把互联网上的所有网页下载下来,放到本地服务器里形成备份,再对这些网页做相关处理(提取关键字,去掉广告等),最后提供一个用户检测接口 
	
	抓取流程： 
		首先选取一部分已有的URL,把这些URL放到待爬队列
		从队列里提取这些URL,然后解析DNS得到主机ip,然后去这个IP对应的服务器里下载HTML页面,保存到搜索引擎的本地服务器里,之后把爬过的URL放入到以爬取队列
		分析这些网页内容,找出网页里的URl连接,继续执行第二步,直到爬取条件结束
	
	搜索引擎如何获取一个新网站的URL：
		主动向搜索引擎提交网址(百度站长平台)：http://zhanzhang.baidu.com/site/index?action=add
		在其他网站里设置网站外连接
		搜索引擎会和DNS服务商合作,可以快速收录新的网站
	
	通用爬虫并不是万物皆可爬的,它需要遵守规则：Robots协议
		协议会指明通用爬虫可以爬取网页的权限
		Robots.txt只是1个建议,并不是所有爬虫都遵守,一般只有大型的搜索引擎才会遵守
	
	通用爬虫工作流程：
		爬取网页
		存储数据
		内容处理
		提供检索/排名服务
	
	搜索引擎排名SEO：
		PageRank值：根据网站的流量(点击量,浏览值,人气)统计,流量越高,网站约值钱,排名越靠前
		竞价排名：谁钱多谁排名靠前
		
	通用爬虫的缺点
		只能提供和文本相关的内容(html,word,pdf)等,但是不能提供多媒体(音乐,图片,视频)和二进制文件(程序,脚本)等
		提供结果千篇一律,不能针对不同人群提供不同搜索结果
		不能理解人类语义上的检索
	
聚集网络爬虫
	概念：爬虫程序员写的针对某种内容的爬虫
	特点：面向主题爬虫,面向需求爬虫，会针对某种特定的内容去爬取信息,而且会保证信息和需求尽可能相关。
	
增量网络爬虫
深层网络爬虫
```



> > > > > > > > > >> > > > > > > > > > 

接下来，让我们真正迈向我们的爬虫开发之路吧！

### 二、Python2中开发爬虫

#### urllib2库的基本使用

```python
所谓网页抓取，就是把URL地址中指定的网络资源从网络流中读取出来，保存到本地。 在Python中有很多库可以用来抓取网页，我们先学习urllib2。

urllib2 是 Python2.7 自带的模块(不需要下载，导入即可使用)
urllib2 官方文档：https://docs.python.org/2/library/urllib2.html
urllib2 源码：https://hg.python.org/cpython/file/2.7/Lib/urllib2.py

urllib2 在 python3.x 中被改为urllib.request
```

##### 示例： 使用urllib2抓取百度网页 ( 第一个爬虫程序 ) 

```python
#!C:\Python36\python.exe
# -*- coding:utf-8 -*-

import urllib2

# url, 统一资源定位符
# data=None,默认为None为get请求,否则设置了data则是post请求
# timeout=超时时间
url = "http://www.baidu.com"
response = urllib2.urlopen(url)
print response  # socket._fileobject object， _fileobject文件对象

# python的文件操作
# print response.read()  # 返回所有内容，字符串
# print response.readline()  # 按行返回

# 读取所有行
# while True:
#     if not response.readline():
#         break
#     print response.readline()

print response.readlines()  # 返回所有行，列表
```

#### 第一个反反爬

##### User-Agent
```python
有一些网站不喜欢被爬虫程序访问，所以会检测连接对象，如果是爬虫程序，也就是非人点击访问，它就会不让你继续访问，所以为了要让程序可以正常运行，需要隐藏自己的爬虫程序的身份。此时，我们就可以通过设置User Agent的来达到隐藏身份的目的，User Agent的中文名为用户代理，简称UA。

User Agent存放于Headers中，服务器就是通过查看Headers中的User Agent来判断是谁在访问。在Python中，如果不设置User Agent，程序将使用默认的参数，那么这个User Agent就会有Python的字样，如果服务器检查User Agent，那么没有设置User Agent的Python程序将无法正常访问网站。

常用消息头(详解http请求消息头)
    Accept:text/html,image/*	 (告诉服务器，浏览器可以接受文本，网页图片)
    Accept-Charaset:ISO-8859-1 	 [接受字符编码：iso-8859-1]
    Accept-Encoding:gzip,compress	[可以接受  gzip,compress压缩后数据]
    Accept-Language:zh-cn	[浏览器支持的语言]   
    Host:localhost:8080		[浏览器要找的主机]
    Referer:http://localhost:8080/test/abc.html		[告诉服务器我来自哪里,常用于防止下载，盗链]
    User-Agent:Mozilla/4.0(Com...)		[告诉服务器我的浏览器内核]
    Cookie：	[会话]
    Connection:close/Keep-Alive 	[保持链接，发完数据后，我不关闭链接]
    Date:	[浏览器发送数据的请求时间]

# 设置请求头的User-Agent
header = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36"
}
# 构造一个请求对象发送请求，伪装浏览器访问
request = urllib2.Request(url, headers=header) 
```

##### 添加更多的Header信息
```python
在 HTTP Request 中加入特定的 Header，来构造一个完整的HTTP请求消息。

可以通过调用Request.add_header() 添加/修改一个特定的header 也可以通过调用Request.get_header()来查看已有的header。

添加一个特定的header
request.add_header("Connection", "keep-alive") # 一直活着

print request.get_header("User-agent")  # 用户代理， 首字母大写，其他小写
print request.get_full_url() # 访问的网页链接
print request.get_host() # 服务器域名
print request.get_method() # get或post
print request.get_type() # http/https/ftp

response = urllib2.urlopen(request)
print response.code # 状态码200, 404，500
print response.read() # 获取内容

data = response.read().decode("utf-8")  # 根据网页编码格式进行解码，常见编码：utf-8, gbk, gb2312...
print response.code # 响应状态码

```

##### url编码：urllib.urlencode()

```python
我们都知道Http协议中参数的传输是"key=value"这种简直对形式的，如果要传多个参数就需要用“&”符号对键值对进行分割。如"?name1=value1&name2=value2"，这样在服务端在收到这种字符串的时候，会用“&”分割出每一个参数，然后再用“=”来分割出参数值。

urllib 和urllib2 区别：
	urllib 和 urllib2 都是接受URL请求的相关模块，但是提供了不同的功能。两个最显著的不同如下：
	urllib 仅可以接受URL，不能创建 设置了headers 的Request 类实例；
	但是 urllib 提供 urlencode 方法用来GET查询字符串的产生，而 urllib2 则没有。（这是 urllib 和 urllib2 经常一起使用的主要原因）
	编码工作使用urllib的urlencode()函数，帮我们将key:value这样的键值对转换成"key=value"这样的字符串，解码工作可以使用urllib的unquote()函数。(注意，不是urllib2.urlencode())

urllib.urlencode(keyWord) # url编码
urllib.parse.quote('吴秀波') #对字符串编码
urllib.unquote(kw) # 解码
```

##### 示例： 模拟百度搜索

```python
#!C:\Python36\python.exe
# -*- coding:utf-8 -*-

import urllib2
import urllib

# 模拟百度搜索
def baiduAPI(params):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    }

    url = "https://www.baidu.com/s?" + params
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    return response.read()

if __name__ == "__main__":
    kw = raw_input("请输入你想查找的内容：")

    wd = {"wd": kw, 'ie': 'utf-8'}
    params = urllib.urlencode(wd)  # url编码：将字典 转换成 参数字符串
    # print wd  # 'wd=aa&ie=utf-8'

    content = baiduAPI(params)
    print content
```



### 三、Python3中开发爬虫

##### 示例： urllib.request爬取百度

```python
import urllib
from urllib import request

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

# 创建请求对象
req = urllib.request.Request("http://www.baidu.com", headers=headers)

response = urllib.request.urlopen(req)
print(response.info())  # 响应信息
print(response.read())  # 二进制
print(response.read().decode('utf-8'))  # 字符串
```

##### 示例：模拟百度搜索

```python
import urllib.request
import urllib.parse

# 模拟百度搜索
def baiduAPI(params):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    }

    url = "https://www.baidu.com/s?" + params
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    return response.read().decode('utf-8')

if __name__ == "__main__":
    kw = input("请输入你要查找的内容:")
    wd = {"wd": kw}
    params = urllib.parse.urlencode(wd)
    # print(params)  # 'wd=aa'

    response = baiduAPI(params)
    print(response)
```

##### 示例： 爬取前程无忧岗位数量

```python
import urllib
from urllib import request
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

# 前程无忧职位网址
url = "https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="

# 开始爬取
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)

html = response.read().decode('gbk')  # HTML源码
# print(html)

jobnum_re = '<div class="rt">(.*?)</div>'

jobnum_comp = re.compile(jobnum_re, re.S)
jobnums = jobnum_comp.findall(html)
print(jobnums[0])
```

#### 抓取ajax数据

##### 示例：抓取豆瓣电影

```python
import urllib
from urllib import request
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

url = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=0"
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
content = response.read().decode()  # json数据

data = json.loads(content)
movie_list = data.get('data')

for movie in movie_list:
    title = movie.get('title')
    casts = movie.get('casts')
    print(title, casts)
    
```

#### GET和POST请求
##### 示例：POST爬取网易云音乐评论

```python
import urllib.request
import urllib.parse
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

# post接口
url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_547976490?csrf_token="

# post提交参数
data = {
    "params": "3u5ErBfSCxBGdgjpJpTQyZVZgmPAv+aisCYZJ9pxk26DoOaS5on9xBjsE65yaS57u9XyxvCJIa78DXJathMsyiClN4LXqhonGNQrAtI2ajxsdW8FosN4kv8psGrRyCBsWrxSJQyfy5pfoeZwxLjB7jHtQkt9hglgZaAfj7ieRWq/XvX3DZtSgLcLrvH/SZOM",
    "encSecKey": "872312d7d8b04d2d5dab69d29c9bde5438337f0b3982887e3557468fe7b397de59e85ab349c07f32ef5902c40d57d023a454c3e1ed66205051264a723f20e61105752f16948e0369da48008acfd3617699f36192a75c3b26b0f9450b5663a69a7d003ffc4996e3551b74e22168b0c4edce08f9757dfbd83179148aed2a344826"}

# post参数为二进制
data = urllib.parse.urlencode(data).encode()
# print(data)

# 爬取（设置data进行POST请求）
req = urllib.request.Request(url, data=data, headers=headers)
response = urllib.request.urlopen(req)
content = response.read().decode()
# print(content)

hotcomments = json.loads(content)
hotcomments_list = hotcomments.get('hotComments')

# 热评
for c in hotcomments_list:
    userid = c['user']['userId']
    nickname = c['user']['nickname']
    content = c['content']
    print(userid, nickname, content)

```
##### 练习： 抓取阿里招聘信息并保存到本地文件

```python
# 抓取阿里招聘信息前5页数据，将每个岗位的信息一行行保存到ali.txt文件中；
# 岗位信息包括：学历degree，部门departmentName，岗位要求description，
#		      类型firstCategory，要求workExperience

url = "https://job.alibaba.com/zhaopin/socialPositionList/doList.json"
for i in range(1, 6):
    params = {
        'pageSize': 10,
        't': '0.15338906034674604',
        'pageIndex': i
    }

```

#### 下载

```python
# 参数1： 需要下载的url
# 参数2： 需要写入的文件路径
request.urlretrieve("http://www.baidu.com", r"baidu.html")
request.urlcleanup()  # 清除缓存

# 下载图片
request.urlretrieve("https://www.baidu.com/img/bd_logo1.png", r"baidu.png")
request.urlcleanup()  # 清除缓存
```

##### 

```python

```

## 作业


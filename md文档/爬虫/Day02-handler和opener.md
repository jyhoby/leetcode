# Day02

## Handler处理器 和 自定义Opener

```python
opener是 urllib2.OpenerDirector 的实例，我们之前一直都在使用的urlopen，它是一个特殊的opener（也就是模块帮我们构建好的）。

但是基本的urlopen()方法不支持代理、cookie等其他的HTTP/HTTPS高级功能。所以要支持这些功能：
1、使用相关的Handler处理器来创建特定功能的处理器对象；
2、然后通过urllib2.build_opener()方法使用这些处理器对象，创建自定义opener对象；
3、使用自定义的opener对象，调用open()方法发送请求。

如果程序里所有的请求都使用自定义的opener，可以使用urllib2.install_opener()将自定义的 opener 对象 定义为 全局opener，表示如果之后凡是调用urlopen，都将使用这个opener（根据自己的需求来选择）

```

### 简单的自定义opener()
```python
import urllib
from urllib import request

# 构建一个HTTPHandler 处理器对象，支持处理HTTP请求
handler = urllib.request.HTTPHandler()  # http

# 构建一个HTTPHandler 处理器对象，支持处理HTTPS请求
# handlers = urllib.request.HTTPSHandler()  # 处理https的处理器

# 调用urllib2.build_opener()方法，创建支持处理HTTP请求的opener对象
opener = urllib.request.build_opener(handler)

# 构建 Request请求
req = urllib.request.Request("http://www.baidu.com", headers=headers)

# 调用自定义opener对象的open()方法，发送request请求
response = opener.open(req)

# 获取服务器响应内容
print(response.read())
```
这种方式发送请求得到的结果，和使用urllib2.urlopen()发送HTTP/HTTPS请求得到的结果是一样的。

```python
如果在 HTTPHandler()增加 debuglevel=1参数，还会将 Debug Log 打开，这样程序在执行的时候，会把收包和发包的报头在屏幕上自动打印出来，方便调试，有时可以省去抓包的工作

# 仅需要修改的代码部分：

# 构建一个HTTPHandler 处理器对象，支持处理HTTP请求，同时开启Debug Log，debuglevel 值默认 0
http_handler = urllib2.HTTPHandler(debuglevel=1)

# 构建一个HTTPSHandler 处理器对象，支持处理HTTPS请求，同时开启Debug Log，debuglevel 值默认 0
https_handler = urllib2.HTTPSHandler(debuglevel=1)
```


## Cookie

```python
Cookie 是指某些网站服务器为了辨别用户身份和进行Session跟踪，而储存在用户浏览器上的文本文件，Cookie可以保持登录信息到用户下次与服务器的会话。

Cookie原理

HTTP是无状态的协议, 为了保持连接状态, 引入了Cookie机制 Cookie是http消息头中的一种属性，包括：
Cookie名字（Name）
Cookie的值（Value）
Cookie的过期时间（Expires/Max-Age）
Cookie作用路径（Path）
Cookie所在域名（Domain），
使用Cookie进行安全连接（Secure）。

前两个参数是Cookie应用的必要条件，另外，还包括Cookie大小（Size，不同浏览器对Cookie个数及大小限制是有差异的）。

Cookie由变量名和值组成，根据 Netscape公司的规定，Cookie格式如下：
Set－Cookie: NAME=VALUE；Expires=DATE；Path=PATH；Domain=DOMAIN_NAME；SECURE

```
### Cookie应用

```python
Cookies在爬虫方面最典型的应用是判定注册用户是否已经登录网站，用户可能会得到提示，是否在下一次进入此网站时保留用户信息以便简化登录手续。

cookielib库 和 HTTPCookieProcessor处理器
在Python处理Cookie，一般是通过cookielib模块和 urllib2模块的HTTPCookieProcessor处理器类一起使用。

cookielib模块：主要作用是提供用于存储cookie的对象

HTTPCookieProcessor处理器：主要作用是处理这些cookie对象，并构建handler对象。

cookielib 库
该模块主要的对象有CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar。

CookieJar：管理HTTP cookie值、存储HTTP请求生成的cookie、向传出的HTTP请求添加cookie的对象。整个cookie都存储在内存中，对CookieJar实例进行垃圾回收后cookie也将丢失。

FileCookieJar (filename,delayload=None,policy=None)：从CookieJar派生而来，用来创建FileCookieJar实例，检索cookie信息并将cookie存储到文件中。filename是存储cookie的文件名。delayload为True时支持延迟访问访问文件，即只有在需要时才读取文件或在文件中存储数据。

MozillaCookieJar (filename,delayload=None,policy=None)：从FileCookieJar派生而来，创建与Mozilla浏览器 cookies.txt兼容的FileCookieJar实例。

LWPCookieJar (filename,delayload=None,policy=None)：从FileCookieJar派生而来，创建与libwww-perl标准的 Set-Cookie3 文件格式兼容的FileCookieJar实例。

其实大多数情况下，我们只用CookieJar()，如果需要和本地文件交互，就用 MozillaCookjar() 或 LWPCookieJar()
```

#### Cookie案例：

##### 1.获取Cookie

```python
import urllib.request
from http import cookiejar  # python3
# import cookiejar  # python2

# 创建一个对象存储cookie
cookies = cookiejar.LWPCookieJar()
# cookie处理器, 提取cookie
cookie_handler = urllib.request.HTTPCookieProcessor(cookies)
# 创建打开器, 处理cookie
opener = urllib.request.build_opener(cookie_handler)

# 使用opener打开url
response = opener.open("http://www.baidu.com/")
# 得到cookies
print(cookies)

```
2. ##### 下载cookie
```python
import urllib.request
from http import cookiejar

filename = "baiducookie.txt"  # 用于保存cookie
# 管理cookie的对象
cookies = cookiejar.LWPCookieJar(filename=filename)
# 创建cookie处理器
cookie_handler = urllib.request.HTTPCookieProcessor(cookies)
# 创建打开器
opener = urllib.request.build_opener(cookie_handler)

# 添加UA，并打开百度，下载cookie
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

req = urllib.request.Request("http://www.baidu.com", headers=headers)

# 打开
response = opener.open(req)

# 保存， 忽略错误
cookies.save(ignore_discard=True, ignore_expires=True)

```
3. ##### 使用下载的cookie
```python
import urllib.request
from http import cookiejar

filename = "baiducookie.txt"
cookies = cookiejar.LWPCookieJar()

# 使用cookie
cookies.load(filename)

cookie_handler = urllib.request.HTTPCookieProcessor(cookies)
opener = urllib.request.build_opener(cookie_handler)

# 添加UA，并打开百度
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

req = urllib.request.Request("http://www.baidu.com", headers=headers)
response = opener.open(req)

```

##### 示例： cookie登录qq空间

```python
1，用自己的账号登录qq空间，将登录成功后的cookie拷贝出来
2，将拷贝出来的cookie保存在HTTP头部信息headers中
3，使用headers发送请求
QQ空间： https://user.qzone.qq.com/27589357
```

##### 练习： 登录 笔趣阁

```python
data = {
    'name': 'douyula',
    'password': 'BA3915F267513EA22FAC9EABB30F2EEA',
    'autoLogin': '1',
    'autologin': '1',
}

url = 'https://www.biquge5200.cc/u/login.htm'

1， 保存登录成功后的cookie
2， 使用保存的cookie进行登录， 登录后获取个人信息
	url = "https://www.biquge5200.cc/home/"

```





###ProxyHandler处理器（代理设置）
```python
使用代理IP，这是爬虫/反爬虫的第二大招，通常也是最好用的。

很多网站会检测某一段时间某个IP的访问次数(通过流量统计，系统日志等)，如果访问次数多的不像正常人，它会禁止这个IP的访问。

所以我们可以设置一些代理服务器，每隔一段时间换一个代理，就算IP被禁止，依然可以换个IP继续爬取。

免费的开放代理获取基本没有成本，我们可以在一些代理网站上收集这些免费代理，测试后如果可以用，就把它收集起来用在爬虫上面。

免费短期代理网站举例：
    西刺免费代理IP
    快代理免费代理
    Proxy360代理
    全网代理IP

代理池： 
	如果代理IP足够多，形成代理池，就可以像随机获取User-Agent一样，随机选择一个代理去访问网站。
	可以自己搭建ip代理池服务器 #推荐
    https://github.com/Germey/ProxyPool
    http://104.160.176.88:5080/
            
安装假的useragent            
pip install fake_useragent



from fake_useragent import UserAgent
from urllib import request
ua = UserAgent()

headers = {
    'user-agent':ua.firefox
}

url = 'http://193.112.219.93:5010/get'
res = request.urlopen(url)
proxy_server = {
    'http':'http://' + res.read().decode()
}
# proxy_server = {
#     'http':'http://193.112.219.93:45457'
# }
print(proxy_server)

#创建代理hanlder
proxy_handler = request.ProxyHandler(proxies=proxy_server)

opener = request.build_opener(proxy_handler)

url = 'http://2019.ip138.com/ic.asp'

req = request.Request(url=url, headers=headers)

res = opener.open(req)

print(res.read().decode('gbk'))

```



```python


```

## HTTP响应状态码参考

```python
1xx:信息

100 Continue
	服务器仅接收到部分请求，但是一旦服务器并没有拒绝该请求，客户端应该继续发送其余的请求。
101 Switching Protocols
	服务器转换协议：服务器将遵从客户的请求转换到另外一种协议。


2xx:成功

200 OK
	请求成功（其后是对GET和POST请求的应答文档）
201 Created
	请求被创建完成，同时新的资源被创建。
202 Accepted
	供处理的请求已被接受，但是处理未完成。
203 Non-authoritative Information
	文档已经正常地返回，但一些应答头可能不正确，因为使用的是文档的拷贝。
204 No Content
	没有新文档。浏览器应该继续显示原来的文档。如果用户定期地刷新页面，而Servlet可以确定用户文档足够新，这个状态代码是很有用的。
205 Reset Content
	没有新文档。但浏览器应该重置它所显示的内容。用来强制浏览器清除表单输入内容。
206 Partial Content
	客户发送了一个带有Range头的GET请求，服务器完成了它。


3xx:重定向

300 Multiple Choices
	多重选择。链接列表。用户可以选择某链接到达目的地。最多允许五个地址。
301 Moved Permanently
	所请求的页面已经转移至新的url。
302 Moved Temporarily
	所请求的页面已经临时转移至新的url。
303 See Other
	所请求的页面可在别的url下被找到。
304 Not Modified
	未按预期修改文档。客户端有缓冲的文档并发出了一个条件性的请求（一般是提供If-Modified-Since头表示客户只想比指定日期更新的文档）。服务器告诉客户，原来缓冲的文档还可以继续使用。
305 Use Proxy
	客户请求的文档应该通过Location头所指明的代理服务器提取。
306 Unused
	此代码被用于前一版本。目前已不再使用，但是代码依然被保留。
307 Temporary Redirect
	被请求的页面已经临时移至新的url。


4xx:客户端错误

400 Bad Request
	服务器未能理解请求。
401 Unauthorized
	被请求的页面需要用户名和密码。
401.1
	登录失败。
401.2
	服务器配置导致登录失败。
401.3
	由于 ACL 对资源的限制而未获得授权。
401.4
	筛选器授权失败。
401.5
	ISAPI/CGI 应用程序授权失败。
401.7
	访问被 Web 服务器上的 URL 授权策略拒绝。这个错误代码为 IIS 6.0 所专用。
402 Payment Required
	此代码尚无法使用。
403 Forbidden
	对被请求页面的访问被禁止。
403.1
	执行访问被禁止。
403.2
	读访问被禁止。
403.3
	写访问被禁止。
403.4
	要求 SSL。
403.5
	要求 SSL 128。
403.6
	IP 地址被拒绝。
403.7
	要求客户端证书。
403.8
	站点访问被拒绝。
403.9
	用户数过多。
403.10
	配置无效。
403.11
	密码更改。
403.12
	拒绝访问映射表。
403.13
	客户端证书被吊销。
403.14
	拒绝目录列表。
403.15
	超出客户端访问许可。
403.16
	客户端证书不受信任或无效。
403.17
	客户端证书已过期或尚未生效。
403.18
	在当前的应用程序池中不能执行所请求的 URL。这个错误代码为 IIS 6.0 所专用。
403.19
	不能为这个应用程序池中的客户端执行 CGI。这个错误代码为 IIS 6.0 所专用。
403.20
	Passport 登录失败。这个错误代码为 IIS 6.0 所专用。
404 Not Found
	服务器无法找到被请求的页面。
404.0
	没有找到文件或目录。
404.1
	无法在所请求的端口上访问 Web 站点。
404.2
	Web 服务扩展锁定策略阻止本请求。
404.3
	MIME 映射策略阻止本请求。
405 Method Not Allowed
	请求中指定的方法不被允许。
406 Not Acceptable
	服务器生成的响应无法被客户端所接受。
407 Proxy Authentication Required
	用户必须首先使用代理服务器进行验证，这样请求才会被处理。
408 Request Timeout
	请求超出了服务器的等待时间。
409 Conflict
	由于冲突，请求无法被完成。
410 Gone
	被请求的页面不可用。
411 Length Required
	"Content-Length" 未被定义。如果无此内容，服务器不会接受请求。
412 Precondition Failed
	请求中的前提条件被服务器评估为失败。
413 Request Entity Too Large
	由于所请求的实体的太大，服务器不会接受请求。
414 Request-url Too Long
	由于url太长，服务器不会接受请求。当post请求被转换为带有很长的查询信息的get请求时，就会发生这种情况。
415 Unsupported Media Type
	由于媒介类型不被支持，服务器不会接受请求。
416 Requested Range Not Satisfiable
	服务器不能满足客户在请求中指定的Range头。
417 Expectation Failed
	执行失败。
423
	锁定的错误。


5xx:服务器错误

500 Internal Server Error
	请求未完成。服务器遇到不可预知的情况。
500.12
	应用程序正忙于在 Web 服务器上重新启动。
500.13
	Web 服务器太忙。
500.15
	不允许直接请求 Global.asa。
500.16
	UNC 授权凭据不正确。这个错误代码为 IIS 6.0 所专用。
500.18
	URL 授权存储不能打开。这个错误代码为 IIS 6.0 所专用。
500.100
	内部 ASP 错误。
501 Not Implemented
	请求未完成。服务器不支持所请求的功能。
502 Bad Gateway
	请求未完成。服务器从上游服务器收到一个无效的响应。
502.1
	CGI 应用程序超时。　·
502.2
	CGI 应用程序出错。
503 Service Unavailable
	请求未完成。服务器临时过载或当机。
504 Gateway Timeout
	网关超时。
505 HTTP Version Not Supported
	服务器不支持请求中指明的HTTP协议版本
```
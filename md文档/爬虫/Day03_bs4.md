# Day03


## Cookies 和 Session

### Cookies
如果一个响应中包含了cookie，那么我们可以利用 cookies参数拿到：
```python
import requests

response = requests.get("http://www.baidu.com/")

# 返回CookieJar对象:
cookiejar = response.cookies

# 将CookieJar转为字典：
cookiedict = requests.utils.dict_from_cookiejar(cookiejar)

print(cookiejar)  # <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
print(cookiedict)  # {'BDORZ': '27315'}
```
### Session
```
在 requests 里，session对象是一个非常常用的对象，这个对象代表一次用户会话：从客户端浏览器连接服务器开始，到客户端浏览器与服务器断开。

会话能让我们在跨请求时候保持某些参数，比如在同一个 Session 实例发出的所有请求之间保持 cookie 。
```

##### 示例：实现笔趣阁登录

```python
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

session = requests.session()  # 保存cookie

# 笔趣阁登录
url = "https://www.biquge5200.cc/u/login.htm"
data = {
    # 用户名： douyula, 密码： B2YYtfkP9N98wYJ
    'name': 'douyula',
    'password': 'BA3915F267513EA22FAC9EABB30F2EEA',
    'autoLogin': '1',
    'autologin': '1',
}

# 登录
response = session.post(url, data=data, headers=headers)
print(response.text)

```
##### 处理HTTPS请求 SSL证书验证

```python
Requests也可以为HTTPS请求验证SSL证书：

import requests

# 要想检查某个主机的SSL证书，你可以使用 verify 参数（也可以不写）
response = requests.get("https://www.baidu.com/", verify=True)

# 忽略验证， 可以省略不写或设置为verify=false
response = requests.get("https://www.baidu.com/")

print（response.text）

```

如果SSL证书验证不通过，或者不信任服务器的安全证书，则会报出SSLError，据说以前 12306 证书是自己做的：
来测试一下：

```python
import requests
response = requests.get("https://www.12306.cn/mormhweb/")
print(response.text)

果然：
SSLError: ("bad handshake: Error([('SSL routines', 'ssl3_get_server_certificate', 'certificate verify failed')],)",)

如果我们想跳过 12306 的证书验证，把 verify 设置为 False 就可以正常请求了。
import requests
response = requests.get("https://www.12306.cn/mormhweb/",verify=False)
print response.text




##Beautiful Soup 4.2.0 文档

https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html

安装：pip install beautifulsoup4

```python
import re

from bs4 import BeautifulSoup

doc_html = '''
<!DOCTYPE html>
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="title">
            One
            <b>The Dormouse's story</b>
        </p>
        <p class="story">
            <a class="box" href="elsie" id="link1">1111</a>bbbb
            <a class="sister" href="lacie" id="link2">2222</a>
            <a class="sister" href="tillie" id="link3">3223</a>
        </p>
        <p class="story">aaa</p>
    </body>
</html>
'''

# fp = open('bs4demo.html', encoding='utf-8')

soup = BeautifulSoup(doc_html, 'lxml')
# print(soup)
# print(type(soup))  # <class 'bs4.BeautifulSoup'>

# print(soup.prettify())  # 格式化输出

# Tag 标签
print(soup.head)
print(soup.head.title)
print(soup.head.name)  # head,标签名

print(soup.p)  # 只会得到第一个p
print()

# 属性
print(soup.p.attrs)  # {'class': ['title']},得到p节点的所有属性
print(type(soup.p.attrs))  # <class 'dict'>
print(soup.a.attrs)  # {'class': ['sister'], 'href': 'elsie', 'id': 'link1'},得到第一个a节点的所有属性
print(soup.a.attrs["class"])  # ['sister']
print(soup.a.attrs.get('href'))  # elsie
print(soup.a['href'])  # elsie
print()

# 文本
# string: 查找最里层元素（叶子节点）的内容
print(soup.p.string)  # None
print(soup.p.b.string)  # 'The Dormouse's story'

# text, get_text(): 获取节点内部的文本内容
print(soup.p.text)  # innerText, 节点内部的所有文本内容
print(soup.p.b.text)  # 'The Dormouse's story'
print(soup.p.b.get_text())  # 'The Dormouse's story'
print()

# 兄弟节点
# print(soup.a.next_sibling)  # 下一个节点（包括文本节点）
# print(soup.a.next_sibling.next_sibling)  # 下一个节点（包括文本节点）
# print(soup.a.previous_sibling)  # 上一个节点（包括文本节点）
print("================" * 3)

# find_all()
print(soup.find('p'))  # 查找到第一个p
print(soup.find_all('p'))  # 所有的p节点, 列表

# 可以使用正则
print(soup.find_all(re.compile('^p$')))

# 或运算： []
print(soup.find_all(['p', 'a']))  # 获取a标签和p标签

# 查找指定属性的标签
print(soup.find_all('a', attrs={'href':'elsie'}))  # 查找指定属性的元素
print(soup.find_all('a', href='elsie'))  # 查找指定属性的元素
print(soup.find_all('a', class_='sister'))  # 查找指定class属性
print(soup.find_all('a', class_='sister', limit=2))  # 前2个
print()

# 根据文本内容查找
print(soup.find_all('a', text="1111"))  # 查找内容为1111的元素，完全一样
print(soup.find_all('a', text=re.compile('22')))  # 查找指定正则匹配的元素
print('\n')


# select(): 选择器
print(soup.select('a'))  # 找到所有a标签
print(soup.select('a.box'))
print(soup.select('a#link3'))
print(soup.select('p > a#link3'))
print(soup.select('p a#link3'))
```



##### 示例：爬取前程无忧招聘岗位数量

```python
from bs4 import BeautifulSoup
import requests

def download(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
	response = requests.get(url, headers=headers)
	html = response.content.decode('gbk')
    
    soup = BeautifulSoup(html, 'lxml')
    # 获取岗位数量的多种查找方式
    # 方式1： 使用find_all
    jobnum = soup.find_all('div', class_='rt')
    print(jobnum[0].text)
    
    # 方式2： 使用select
    jobnum = soup.select('.rt')[0].string
	print(jobnum.strip())  # 去掉首尾空格

	# 方式3：正则匹配re
	# jobnum_re = '<div class="rt">(.*?)</div>'
	# jobnum_comp = re.compile(jobnum_re, re.S)
	# jobnums = jobnum_comp.findall(html)
	# print(jobnums[0])

download(url = "https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=")

```
##### 示例：爬取股票基金

```python
import urllib
from urllib import request
from bs4 import BeautifulSoup

stockList = []

def download(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"}
    request = urllib.request.Request(url, headers=headers)  # 请求，修改，模拟http.
    data = urllib.request.urlopen(request).read()  # 打开请求，抓取数据
    
    soup = BeautifulSoup(data, "lxml", from_encoding="gb2312")
    mytable = soup.select("#datalist")
    for line in mytable[0].find_all("tr"):
        print(line.get_text())  # 提取每一个行业
        print(line.select("td:nth-of-type(3)")[0].text) # 提取具体的某一个

if __name__ == '__main__':
    download("http://quote.stockstar.com/fund/stock_3_1_2.html")

```
##### 练习：爬取腾讯岗位说明

```python

https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1560992491261&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=40001&attrId=&keyword=&pageIndex=1&pageSize=20&language=zh-cn&area=cn

```
##### 

```python

```
### 存入数据库

```python
import pymysql

# 存入数据库
def save_job(tencent_job_list):

    # 连接数据库
    db = pymysql.connect(host="127.0.0.1", port=3306, user='root', password="root",database='tencent1', charset='utf8')
    # 游标
    cursor = db.cursor()

    # 遍历，插入job
    for job in tencent_job_list:
        sql = 'insert into job(name, address, type, num) VALUES("%s","%s","%s","%s") ' % (job["name"], job["address"], job["type"], job["num"])
        cursor.execute(sql)
        db.commit()

    cursor.close()
    db.close()
```


# 作业


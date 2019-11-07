# Day04

## selenium&headless

#### 浏览器驱动下载

```html
IE11的Webdriver下载：
	http://dl.pconline.com.cn/download/771640-1.html
	链接：https://pan.baidu.com/s/13TTyXGNaG5cpSNdl1k9ksQ 密码：2n9n

Chrome65.0.3325.146的webdriver驱动下载：
	多版本：http://chromedriver.storage.googleapis.com/index.html
	或 http://npm.taobao.org/mirrors/chromedriver/2.43/

Firefox58的webdriver驱动下载
	链接：https://pan.baidu.com/s/1RATs8y-9Vige0IxcKdn83w 密码：l41g


下载的驱动chromedriver.exe放到C盘下的window文件夹下
```

#### selenium使用

##### get(url)：打开URL

```python
def openURL():
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    print(driver.page_source)
```

##### clear() ： 清除数据 Clears the text if it’s a text entry element.

##### page_source：获取HTML源码

##### close()：关闭

##### quit()：全部关闭

##### click()：点击，Clicks the element.

##### execute_script(script, *args)： 执行脚本

```python
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# 下拉滚动条，使浏览器加载出动态加载的内容
while True:
    # 可能像这样要拉很多次，中间要适当的延时。
    # 如果说说内容都很长，就增大下拉的长度。
    for i in range(10):
        driver.execute_script("window.scrollBy(0,1000)")
        time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    break
```



#### 查找元素

##### find_element(by='id', value=None)

##### find_element_by_class_name(name)

​	Finds element within this element’s children by class name.

##### find_element_by_css_selector(css_selector)

​	Finds element within this element’s children by CSS selector.

##### find_element_by_id(id_)

​	Finds element within this element’s children by ID.

##### find_element_by_link_text(link_text)

​	Finds element within this element’s children by visible link text.

##### find_element_by_name(name)

​	Finds element within this element’s children by name.

##### find_element_by_tag_name(name)

​	Finds element within this element’s children by tag name.

##### find_element_by_xpath(xpath)

​	Finds element by xpath.

```
myelement.find_element_by_xpath(".//a")
```

​	However, this will select the first link on the page.

```
myelement.find_element_by_xpath("//a")
```



##### find_elements(by='id', value=None)

​	‘Private’ method used by the find_elements_by_* methods.

##### find_elements_by_class_name(name)

​	Finds a list of elements within this element’s children by class name.

##### find_elements_by_css_selector(css_selector)

​	Finds a list of elements within this element’s children by CSS selector.

##### find_elements_by_id(id_)

​	Finds a list of elements within this element’s children by ID. Will return a list of webelements if found, or an empty list if not.

##### find_elements_by_link_text(link_text)

​	Finds a list of elements within this element’s children by visible link text.

##### find_elements_by_name(name)

​	Finds a list of elements within this element’s children by name.

##### find_elements_by_tag_name(name)

​	Finds a list of elements within this element’s children by tag name.

##### find_elements_by_xpath(xpath)

​	Finds elements within the element by xpath.

##### get_attribute(name)

​	Gets the given attribute or property of the element.

示例:

```python
# Check if the "active" CSS class is applied to an element.
is_active = "active" in target_element.get_attribute("class")
```

##### save_screenshot(filename)

​	Saves a screenshot of the current element to a PNG image file. Returns

##### send_keys(*value)

​	Simulates typing into the element.

```python
form_textfield = driver.find_element_by_name('username')
form_textfield.send_keys("admin")

search.send_keys("海贼王", Keys.ARROW_DOWN) # 回车
```

​	This can also be used to set file inputs.

```python
file_input = driver.find_element_by_name('profilePic')
file_input.send_keys("path/to/profilepic.gif")
```



##### 示例：selenium登录知乎

```python
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.zhihu.com/')

# 点击登录按钮
driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[2]/span').click()
time.sleep(2)

# 输入用户名
username = driver.find_element_by_name("username")
username.send_keys('18588403840')
time.sleep(2)

# 输入密码
password = driver.find_element_by_name("password")
password.send_keys('Changeme_123')
time.sleep(8)

# 登录
driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/button').click()

# 登录后获取登录后的信息
driver.get('https://www.zhihu.com/people/zuo-zai-fen-tou-diao-xi-gui-82/activities')
print(driver.page_source)

# 可以登录后的获取cookie
# print(driver.get_cookies())


# 新版知乎设置了反爬了， 如果上面的方式无法登录：可以使用第三方登录
# 进入登陆页面
driver.find_element_by_xpath(".//*[@class='SignContainer-switch']/span").click()

# 点击社交网络账号登陆
driver.find_element_by_xpath(".//*[@class='Login-socialLogin']/button").click()
# 点击QQ登陆
driver.find_element_by_xpath(".//*[@class='Login-socialButtonGroup']/button[3]").click()

time.sleep(15)  # 时间不够的自己加
driver.refresh()  # 15秒后要刷新

# 登录后
# 获取cookie
print(driver.get_cookies())

```



#####  selenium设置代理

```python
from selenium import webdriver
chromeOptions = webdriver.ChromeOptions()

# 设置代理
# 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
chromeOptions.add_argument("--proxy-server=http://10.3.132.6:808")
browser = webdriver.Chrome(chrome_options=chromeOptions)

# 查看本机ip，查看代理是否起作用
browser.get("https://blog.csdn.net/zwq912318834/article/details/78626739")
print(browser.page_source)

# 退出，清除浏览器缓存
# browser.quit()

```

###### 设置为开发者模式，防止被各大网站识别出来使用了Selenium
options.add_experimental_option('excludeSwitches', ['enable-automation'])



##### 练习：selenium登录QQ空间

```python
提示：
	login = driver.find_element_by_id('login_frame')
    # iframe需要转换
  	driver.switch_to_frame(login)
```



##### 

```python


```


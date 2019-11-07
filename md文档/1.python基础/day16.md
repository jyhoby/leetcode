#### TCP/IP

> 计算机为了联网，就必须规定通讯协议，早期的计算机网络是由各个厂商规定的一些协议，他们之间互不兼容。
>
> 为了把全世界的电脑能够连接到一起，那么就必须规定一套全球通用的协议，为了完成这个目标，互联网协议簇就是通讯协议标准，有了internet，任何私有网络，只要支持这个协议就可以联入互联网
>
> 因为互联网协议包含了上百种协议标准，但是最重要的两个协议就是TCP和IP协议，所以大家把互联网协议简称TCP/IP协议。

> 通讯的时候，双方必须都知道对方的标识，并且这些标识必须都是唯一的，互联网上的每个计算机唯一标识就是IP地址【10.2.123.34】，如果一台电脑同时接入多个网络，那么它就有多个IP地址，所以IP地址对应的实际上是计算机的网络接口，通常是网卡。

> IP协议负责把数据从一台电脑通过网络发送到另一台电脑，发送的时候，我们的数据被分割成一小块，一小块的，然后通过IP包发送出去，IP包的特点就是按块发送，它不保证到达也不保证顺序到达。

> IP地址实际上是一个32位整数（称为IPV4）
>
> IPV6地址实际上是一个128位整数，它是IPV4的升级版

> TCP协议则是建立在IP协议的基础之上的，TCP协议负责在两台计算机之间建立可靠连接，保证数据包按顺序到达，TCP协议会通过握手建立连接，然后对每个IP包进行编号，确保对方按顺序收到，若是包丢掉了就自动重发。
>
> 一个TCP报文除了含有要传输的数据外，还包含了本机IP地址和目标IP地址，源端口与目标端口

> 端口：在两台计算机通信时，只发送IP是不够的，因为一台电脑上可能执行多个网络程序，一个TCP报文来了之后，应该交给哪个程序来处理，这个就需要使用端口号来进行区分，每个网络程序都向操作系统申请了一个唯一的端口号。1024

三次握手与四次挥手

掌握：

TCP/IP协议    IP地址      端口    三次握手四次挥手

三次握手刚好能够创建一个可靠连接。

记住: ip协议,TCP协议,端口,网卡,三次握手与四次挥手

#### TCP编程

B/S

C/S

> socket是网络编程的一个抽象的概念，通常我们用一个socket表示打开了一个网络连接，而打开网络连接需要知道目标计算机的IP地址和端口号，再指定协议即可。

##### 客户端

> 大多数连接都是可靠的TCP连接，创建连接时，主动发起连接的是客户端，被动响应连接的叫服务器。

创建一个基于TCP连接的socket

```python
#导入socket库
import socket

#创建一个socket对象
#socket.AF_INET指定使用IPV4，若要使用IPV6则指定为AF_INET6
#SOCK_STREAM指定使用面向流的TCP协议
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#客户端要主动发起TCP连接必须知道服务器的IP地址和端口号
#一般的网络地址可以通过域名转到IP地址，但是服务器的端口号是如何确定的呢？
#作为服务器，提供什么样的服务，其端口号就一定要固定，访问网页的端口号80，STMP的服务端口是25，端口号小于1024的是Internet标准服务端口，大于1024的可以随意使用。
sock.connect(('www.zxxk.com',80))
#注意：在这里使用的是一个tuple，包含地址与端口号
#发送数据
#广泛应用的有HTTP/1.0和HTTP/1.1两个版本，1.1和1.0相比最大的特点就是增加对长连接的支持。
#HTTP/1.1支持长连接，在一个TCP连接上可以传送多个HTTP请求和应答，减少建立和关闭连接的消耗和延迟
'''
完整的HTTP请求包括：一个请求行、若干HTTP头域和可选的实体内容三部分
#请求行，请求行以一个方法符号开头，以空格分开，后面跟着请求的URI和协议版本，格式如下：
#Method  Request-URI  HTTP-Version CRLF
#其中的Method表示请求方法，Request-URI是同一资源标识符，HTTP-Version表示请求的HTTP协议版本，CRLF表示回车换行。
具体：https://blog.csdn.net/wangyin159/article/details/47438875
 '''
sock.send(b'GET / HTTP/1.1\r\nHost:www.zxxk.com\r\nConnection:close\r\n\r\n')
#注意：发送的文本格式必须符合HTTP标准，如果格式没问题，接下来就可以接收数据了

#循环读取接收
buffer = []
while True:
    #每次最多接收1k字节
    d = sock.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b"".join(buffer)
#关闭连接
s.close()
header,html = data.split(b"\r\n\r\n",1)
print(header.decode("utf-8"))

#把接收的数据写入文件
with open('sina.html','wb') as f:
    f.writer(html)  
```

##### 服务器

> 与客户端相比，服务器就要复杂一些
>
> 服务器进程需要先绑定一个端口并且监听来自其他客户端的链接，如果某个客户端链接过来了，服务器就与该客户端建立socket链接，之后的通讯就依赖于这个socket

> 因为一台服务器可以响应多个客户端的请求，这样若是来标识唯一的一个socket，则依赖下面四项：服务器地址，服务器端口，客户端地址，以及客户端端口。
>
> 还有，因为服务器需要同时响应请求，所以，每个连接都需要开启一个新的线程来处理，否则服务器一次就只能服务一个客户端了。

服务器

```python
import socket
import threading

#创建一个socket对象，指定协议
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定地址
s.bind(('127.0.0.1',9999))
#注意：绑定端口的号的时候尽量不要使用小于1024的
#监听端口，传入的参数指等待连接的最大数量
s.listen(6)
def tcpLink(sock,addr):
    #打印连接成功
    print("Accept a new connection %s"% addr)
    #服务器发送数据到客户端
    sock.send(b"Welcome to server")
    #循环接收客户端发来的请求数据
    while True:
 		#接收数据，每次接收1024个字节
        data = sock.recv(1024)
        if not data or data.decode("utf-8") == 'end':
            break
        sock.send(("Server %s"%data.decode("utf-8")).encode("utf-8"))
     sock.close()
    print("end form %s"%addr)
    

#服务器通过一个永久的循环来接受来自客户端的连接
while True:
    #接受一个新的连接
    sock,addr = s.accept()
    #创建一个新的线程来处理TCP连接
    t = threading.Thread(target=tcpLink,args=(sock,addr))
	#开启线程
    t.start()
```

客户端

```python
import socket

#创建一个socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect('127.0.0.1',9999)
#接收欢迎消息
print(s.recv(1024).decode("utf-8"))

for data in [b'Hello',b'Hi',b'nihao']:
    #发送数据
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
#最后发送结束的标识
s.send(b'end')
#关闭连接
s.close()
```

#### UDP编程

> TCP是，建立可靠的连接，并且通讯双方都可以以流的形式发送数据，相对于TCP，UDP则是面向无连接的协议。
>
> 使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发送数据包，但是能不能到达就不知道了
>
> 优点：速度快，对于不要求可靠到达的数据，就可以使用UDP协议
>
> 缺点：不可靠

服务器：

```python
import socket
#创建一个socket对象
#socket.SOCK_DGRAM指定socket的类型是UDP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定ip,端口号
s.bind(("127.0.0.1",9999))
print("bind udp ....")
while True:
    #接收数据，返回数据和客户端的地址与端口
    data,addr = s.recvfrom(1024)
    print("recevied from %s"%addr)
    #参数一：要发送的数据  参数二：发送的地址
	s.sendto(b"udp server %s"%data,addr)
```

客户端：

```python
import socket

#创建一个socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'Hello',b'Hi',b'nihoa']:
    #发送数据
    s.sendto(data,('127.0.0.1',9999))
    #接收数据
    print(s.recv(1024).decode("utf-8"))
#关闭连接
s.close()
```

#### 发邮件

> 登录163邮箱 —> 设置 —>POP3/SMTP/IMAP —>客户端授权密码 —>开启  —> 重置授权码
>
> 注意: 授权码尽量和邮件的登录密码不同[],将下面的password改为授权码
>
> 若要发邮件首先需要知道：
>
> 服务器地址，发送邮箱地址，发送邮箱密码，要发送的内容，对方的邮箱地址
>
> 关于邮件：标题，发送者
>
> 打开服务连接-》登录邮箱-》发送邮件-》退出邮箱

```python
#发邮件的库
import smtplib
#邮件文本
from email.mime.text import MIMEText

#STMP服务器
SMTPServer = 'smtp.163.com'

#发邮箱的地址
sender = 'zhangjiaojiao_vip@163.com'
#发送者邮箱密码：授权码
password = '1q2w3e'
#设置发送文本的内容
message = 'hello world'

#转为邮件文本
msg = MIMEText(message)
#标题
msg['Subject'] = '来自星星的我'
#发送者
msg['From'] = sender

#收件人
msg['To'] ='zhangjiaojiao@163.com'

#打开SMTP服务器，端口号一般为25
mailServer = smtplib.SMTP(SMTPServer,25)
#登录邮箱
mailServer.login(sender,password)
#发送邮件
mailServer.sendmail(sender,['zhangjiaojiao_vip@163.com'],msg.as_string())
#退出邮箱
mailserver.quit()
```

> 说明:有时候会被识别为垃圾邮件[其他邮箱都可以用,只要找到授权码即可]
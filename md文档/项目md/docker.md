#### 1. Docker介绍

- [Docker中文社区文档](http://www.docker.org.cn/index.html)
- Docker 是一个开源的软件部署解决方案。
- Docker 也是轻量级的应用容器框架。
- Docker 可以打包、发布、运行任何的应用。
- Docker 就像一个盒子，里面可以装很多物件，如果需要某些物件，可以直接将该盒子拿走，而不需要从该盒子中一件一件的取。
- Docker 是一个`客户端-服务端(C/S)`架构程序。
  - 客户端只需要向服务端发出请求，服务端处理完请求后会返回结果。

> Docker 包括三个基本概念:

- 镜像（Image）
  - Docker的镜像概念类似于虚拟机里的镜像，是一个只读的模板，一个独立的文件系统，包括运行容器所需的数据，可以用来创建新的容器。
  - 例如：一个镜像可以包含一个完整的 ubuntu 操作系统环境，里面仅安装了MySQL或用户需要的其它应用程序。
- 容器（Container）
  - Docker容器是由Docker镜像创建的运行实例，类似VM虚拟机，支持启动，停止，删除等。
  - 每个容器间是相互隔离的，容器中会运行特定的应用，包含特定应用的代码及所需的依赖文件。
- [仓库（Repository）](https://hub.docker.com/)
  - Docker的仓库功能类似于Github，是用于托管镜像的。

#### 2. Docker安装（ubuntu 16.04）

安装Docker CE需要libltdl7>(>= 2.4.6)，ubuntu16.04默认无更高版本。

下载libltdl7安装包：

wget http://launchpadlibrarian.net/236916213/libltdl7_2.4.6-0.1_amd64.deb

安装：

sudo dpkg -i libltdl7_2.4.6-0.1_amd64.deb

> **1.源码安装Docker CE**

```bash
$ cd docker源码目录
$ sudo apt-key add gpg
$ sudo dpkg -i docker-ce_17.03.2~ce-0~ubuntu-xenial_amd64.deb
```

![image-20190902231659984](01.docker.assets/image-20190902231659984.png)

> **2.检查Docker CE是否安装正确**

```bash
$ sudo docker run hello-world
```

出现如下信息，表示安装成功

![image-20190902231754826](01.docker.assets/image-20190902231754826.png)

> **3.启动与停止**

- 安装完成Docker后，默认已经启动了docker服务。

```bash
# 启动docker
$ sudo service docker start
# 重启docker
$ sudo service docker restart
# 停止docker
$ sudo service docker stop
```

#### 3. Docker镜像操作

> **1.镜像列表**

```bash
$ sudo docker image ls
```

![image-20190902231940983](01.docker.assets/image-20190902231940983.png)

```
* REPOSITORY：镜像所在的仓库名称 
* TAG：镜像标签 
* IMAGEID：镜像ID 
* CREATED：镜像的创建日期(不是获取该镜像的日期) 
* SIZE：镜像大小
```

> **2.从仓库拉取镜像**

```bash
# 官方镜像
$ sudo docker image pull 镜像名称 或者 sudo docker image pull library/镜像名称
$ sudo docker image pull ubuntu 或者 sudo docker image pull library/ubuntu
$ sudo docker image pull ubuntu:16.04 或者 sudo docker image pull library/ubuntu:16.04

# 个人镜像
$ sudo docker image pull 仓库名称/镜像名称
$ sudo docker image pull louis/fastdfs
```

> **3.查看镜像**

        ```bash
$ sudo docker image ls
        ```



> **4.删除镜像**

```bash
$ sudo docker image rm 镜像名或镜像ID
$ sudo docker image rm hello-world
$ sudo docker image rm fce289e99eb9
```



#### 4. Docker容器操作

> **1.容器列表**

```bash
# 查看正在运行的容器
$ sudo docker container ls
# 查看所有的容器
$ sudo docker container ls --all
```

![image-20190902232414886](01.docker.assets/image-20190902232414886.png)

> **2.创建容器**

```bash
$ sudo docker run [option] 镜像名 [向启动容器中传入的命令]
```

```
常用可选参数说明：
* -i 表示以《交互模式》运行容器。
* -t 表示容器启动后会进入其命令行。加入这两个参数后，容器创建就能登录进去。即分配一个伪终端。
* --name 为创建的容器命名。
* -v 表示目录映射关系，即宿主机目录:容器中目录。注意:最好做目录映射，在宿主机上做修改，然后共享到容器上。 
* -d 会创建一个守护式容器在后台运行(这样创建容器后不会自动登录容器)。 
* -p 表示端口映射，即宿主机端口:容器中端口。
* --network=host 表示将主机的网络环境映射到容器中，使容器的网络与主机相同。
```

> **3.交互式容器**

```bash
$ sudo docker run -it --name=ubuntu1 ubuntu /bin/bash
```

![image-20190902232500915](01.docker.assets/image-20190902232500915.png)

```
在容器中可以随意执行linux命令，就是一个ubuntu的环境。
当执行 exit 命令退出时，该容器随之停止。
```

> **4.守护式容器**

```bash
# 开启守护式容器
$ sudo docker run -dit --name=ubuntu2 ubuntu
```

![image-20190902232530544](01.docker.assets/image-20190902232530544.png)

```bash
# 进入到容器内部交互环境
$ sudo docker exec -it 容器名或容器id 进入后执行的第一个命令
$ sudo docker exec -it ubuntu2 /bin/bash
```

![image-20190902232601819](01.docker.assets/image-20190902232601819.png)

```
如果对于一个需要长期运行的容器来说，我们可以创建一个守护式容器。
在容器内部执行 exit 命令退出时，该容器也随之停止。
```

> **5.停止和启动容器**

```bash
# 停止容器
$ sudo docker container stop 容器名或容器id
# kill掉容器
$ sudo docker container kill 容器名或容器id
# 启动容器
$ sudo docker container start 容器名或容器id
```

![image-20190902232632779](01.docker.assets/image-20190902232632779.png)

> **6.删除容器**

- 正在运行的容器无法直接删除。

```bash
$ sudo docker container rm 容器名或容器id
```

![image-20190902232655525](01.docker.assets/image-20190902232655525.png)

> **7.容器制作成镜像**

- 为保证已经配置完成的环境可以重复利用，我们可以将容器制作成镜像。

```bash
# 将容器制作成镜像
$ sudo docker commit 容器名 镜像名
```

![image-20190902232720262](01.docker.assets/image-20190902232720262.png)

```bash
# 镜像打包备份
$ sudo docker save -o 保存的文件名 镜像名
```

![image-20190902232813759](01.docker.assets/image-20190902232813759.png)

```bash
# 镜像解压
$ sudo docker load -i 文件路径/备份文件
```

![image-20190902232840056](01.docker.assets/image-20190902232840056.png)



#### 5.FastDFS介绍

- 用`c语言`编写的一款开源的轻量级分布式文件系统。

- 功能包括：文件存储、文件访问（文件上传、文件下载）、文件同步等，解决了大容量存储和负载均衡的问题。特别适合以文件为载体的在线服务，如相册网站、视频网站等等。

- 为互联网量身定制，充分考虑了冗余备份、负载均衡、线性扩容等机制，并注重高可用、高性能等指标。

- 可以帮助我们搭建一套高性能的文件服务器集群，并提供文件上传、下载等服务。

  ![image-20190903072930291](01.docker.assets/image-20190903072930291.png)

- 
  FastDFS架构包括Client、Tracker server 和 Storage server
  
  - `Client`请求`Tracker`进行文件上传、下载，`Tracker`再调度`Storage`完成文件上传和下载。
- **Client**： 客户端，业务请求的发起方，通过专有接口，使用TCP/IP协议与`Tracker`或`Storage`进行数据交互。FastDFS提供了`upload`、`download`、`delete`等接口供客户端使用。
- **Tracker server**：跟踪服务器，主要做调度工作，起负载均衡的作用。在内存中记录集群中所有存储组和存储服务器的状态信息，是客户端和数据服务器交互的枢纽。
- Storage server：存储服务器（存储节点或数据服务器），文件和文件属性都保存到存储服务器上。Storage server直接利用OS的文件系统调用管理文件。
  
  - Storage群中的**横向可以扩容，纵向可以备份**。

#### 6. FastDFS上传和下载流程

![image-20190903073157690](01.docker.assets/image-20190903073157690.png)

#### 7. FastDFS文件索引

![image-20190903073245552](01.docker.assets/image-20190903073245552.png)

- FastDFS上传和下载流程：可以看出都涉及到一个数据叫文件索引（file_id）
  - **文件索引（file_id）**是客户端上传文件后Storage返回给客户端的一个字符串，是以后访问该文件的索引信息。
- 文件索引（file_id）信息包括：组名、虚拟磁盘路径、数据两级目录、文件名等信息。
  - **组名**：文件上传后所在的 Storage 组名称。
  - **虚拟磁盘路径**：Storage 配置的虚拟路径，与磁盘选项`store_path*`对应。如果配置了`store_path0`则是`M00`，如果配置了`store_path1`则是`M01`，以此类推。
  - **数据两级目录**：Storage 服务器在每个虚拟磁盘路径下创建的两级目录，用于存储数据文件。
  - **文件名**：由存储服务器根据特定信息生成，文件名包含:源存储服务器IP地址、文件创建时间戳、文件大小、随机数和文件拓展名等信息。

![image-20190903073334315](01.docker.assets/image-20190903073334315.png)

#### 8.Docker安装运行FastDFS

**1.获取FastDFS镜像**

```python
# 从仓库拉取镜像
$ sudo docker image pull delron/fastdfs
# 解压教学资料中本地镜像
$ sudo docker load -i 文件路径/fastdfs_docker.tar
```

**2.开启tracker容器**

```python
# 我们将 tracker 运行目录映射到宿主机的 /var/fdfs/tracker目录中。
$ sudo docker run -dit --name tracker --network=host -v /var/fdfs/tracker:/var/fdfs delron/fastdfs tracker
```

**3.开启storage容器**

 ```python
# TRACKER_SERVER=Tracker的ip地址:22122（Tracker的ip地址不要使用127.0.0.1）
# 我们将 storage 运行目录映射到宿主机的 /var/fdfs/storage目录中。
$ sudo docker run -dti --name storage --network=host -e TRACKER_SERVER=192.168.103.158:22122 -v /var/fdfs/storage:/var/fdfs delron/fastdfs storage
 ```

#### 9.FastDFS客户端上传文件

**1.安装FastDFS客户端扩展**

```python
# 安装准备好的fdfs_client-py-master.zip到虚拟环境中
$ pip install fdfs_client-py-master.zip
$ pip install mutagen
$ pip isntall requests
```

**2.准备FastDFS客户端扩展的配置文件**

![image-20190903073844057](01.docker.assets/image-20190903073844057.png)

```python
base_path=FastDFS客户端存放日志文件的目录
tracker_server=运行Tracker服务的机器ip:22122
```

**3.FastDFS客户端实现文件存储**

```python
# 使用 shell 进入 Python交互环境
$ python manage.py shell

# 1. 导入FastDFS客户端扩展
from fdfs_client.client import Fdfs_client
# 2. 创建FastDFS客户端实例
client = Fdfs_client('client.conf')
# 3. 调用FastDFS客户端上传文件方法
ret = client.upload_by_filename('/Users/apple/Desktop/kk.jpeg')


ret = {
'Group name': 'group1',
'Remote file_id': 'group1/M00/00/00/wKhnnlxw_gmAcoWmAAEXU5wmjPs35.jpeg',
'Status': 'Upload successed.',
'Local file name': '/Users/apple/Desktop/kk.jpeg',
'Uploaded size': '69.00KB',
'Storage IP': '192.168.103.158'
 }
ret = {
'Group name': 'Storage组名',
'Remote file_id': '文件索引，可用于下载',
'Status': '文件上传结果反馈',
'Local file name': '上传文件全路径',
'Uploaded size': '文件大小',
'Storage IP': 'Storage地址'
 }
```

#### 10.浏览器下载并渲染图片

思考：如何才能找到在Storage中存储的图片？

- 协议：
  - `http`
- IP地址：172.16.222.151
  - `Nginx`服务器的IP地址。
  - 因为 FastDFS 擅长存储静态文件，但是不擅长提供静态文件的下载服务，所以我们一般会将 Nginx 服务器绑定到 Storage ，提升下载性能。
- 端口：8888
  - `Nginx`服务器的端口。
- 路径：group1/M00/00/00/wKhnnlxw_gmAcoWmAAEXU5wmjPs35.jpeg
  - 文件在Storage上的文件索引。
- 完整图片下载地址
  - `http://172.16.222.151:8888/group1/M00/00/00/wKhnnlxw_gmAcoWmAAEXU5wmjPs35.jpeg`
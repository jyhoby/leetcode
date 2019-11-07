# Day04

### 一、MongoDB简介

#### 1.概述

> ​	MongoDB是一个基于分布式文件存储的数据库，由C++语言编写。旨在为WEB应用提供可扩展的高性能数据存储解决方案。
>
>  	 MongoDB介于关系型数据和非关系型数据库之间，是非关系数据库当中功能最丰富，最像关系数据库的。他支持的数据结构非常松散，类似json格式，因此可以存储比较复杂的数据类型。
> ​	
>  	 MongoDB最大的特点是他支持的查询语言非常强大，其语法有点类似于面向对象的查询语言，几乎可以实现类似关系数据库表单查询的绝大部分功能，而且还支持对数据建立索引。
>

#### 2.和MySQL之间的区别

##### 2.1MySQL

> 关系型数据库。
> 查询语句是使用传统的sql语句，拥有较为成熟的体系，成熟度很高。
> 关系型数据库遵循ACID规则
> 开源数据库的份额在不断增加，mysql的份额页在持续增长。
> 缺点：在海量数据处理的时候效率会显著变慢。

##### 2.2 MongoDB

> 非关系型数据库(nosql ),属于文档型数据库。先解释一下文档的数据库，即可以存放xml、json、bson类型系那个的数据。这些数据具备自述性（self-describing），呈现分层的树状数据结构。数据结构由键值(key=>value)对组成。
> 存储方式：虚拟内存+持久化。
> 查询语句：是独特的Mongodb的查询方式。
> 适合场景：事件的记录，内容管理或者博客平台等等。
> 数据处理：数据是存储在硬盘上的，只不过需要经常读取的数据会被加载到内存中，将数据存储在物理内存中，从而达到高速读写。
> 成熟度与广泛度：新兴数据库，成熟度较低，Nosql数据库中最为接近关系型数据库，比较完善的DB之一，适用人群不断在增长。
> 优势：
> 快速！在适量级的内存的Mongodb的性能是非常迅速的，它将热数据存储在物理内存中，使得热数据的读写变得十分快，
> 高扩展！
> json的存储格式！

##### 2.3二者之间的区别

> | MySQL        | MongoDB     | 解释       |
> | ------------ | ----------- | -------- |
> | database     | database    | 数据库      |
> | table        | collection  | 数据表/集合   |
> | row【一条记录，实体】 | document    | 行/文档     |
> | column       | field       | 列/字段或者属性 |
> | table join   | 不支持         | 表连接      |
> | primary key  | primary key | 主键       |
>
> 解释
>
> 数据库：容器，不管是mysql还是mongodb，一个单一的服务器都可以管理多个数据库
>
> 集合：是一组mongodb的文件，等价于mysql中的table，集合中文档可以有不同的字段，也可以有不同的数据类型
>
> 文档：一组键值对，具有动态模式【不同的数据可以是不同的格式】

### 二、MongoDB安装和卸载

#### 1.卸载

> ```mysql
> 执行命令：
> sudo apt-get autoremove mongodb
> sudo apt-get autoclean mongodb
>
> #清除残留数据
> dpkg -l |grep ^rc|awk '{print $2}' |tr ["\n"] [" "]|sudo xargs dpkg -P 
> ```

#### 2.安装

> ##### 第1步 – 导入公钥**
>
> Ubuntu软件包管理器apt（高级软件包工具）需要软件分销商的GPG密钥来确保软件包的一致性和真实性。 执行此下面的命令将MongoDB密钥导入到您的服务器：
>
> ```
> sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
> ```
>
> **第2步 – 创建源列表文件MongoDB**
>
> 检查URL http://repo.mongodb.org/apt/ubuntu/dists/。 如果您在该网页上看到一个目录“bionic”，则将下述命令中的单词“xenial”替换为“bionic”一词，【原因：MongoDB尚未发布Bionic Beaver软件包，但Xenial软件包在Ubuntu 18.04 LTS上运行良好】
>
> 执行以下命令在/etc/apt/sources.list.d/中创建一个MongoDB列表文件：
>
> ```
> echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list
> ```
>
> **第3步 – 更新存储库**
>
> 使用apt命令更新存储库：
>
> ```
> sudo apt-get update
> ```
>
> 说明：执行完会提示一些失败，不用在意
>
> **第4步 – 安装MongoDB**
>
> 执行以下命令来安装MongoDB：
>
> ```
> sudo apt-get install -y mongodb
> ```
>
> ##### 第5步：启动MongoDB
>
> 执行以下命令启动MongoDB并将其添加为在启动时启动的服务
>
> ```
> systemctl start mongodb
> ```
>
> 如果执行完这一步终端没有任何输出，则说明是正确的
>
> ```python
> 如果启动的时候提示：Failed to start mongod.service: Unit mongodb.service not found.
> 解决办法如下：
> 	1创建配置文件：
> 		在/etc/systemd/system/下
> 		sudo vim mongodb.service
>
> 	2.在里面追加文本：
> 		[Unit]
>  		Description=High-performance, schema-free document-oriented database
>  		After=network.target
>    
>  		[Service]
>  		User=mongodb
>  		ExecStart=/usr/bin/mongod --quiet --config /etc/mongodb.conf
>    
>  		[Install]
>  		WantedBy=multi-user.target
>  	3.按ctrl+X退出
>  	4.启动服务
>  		sudo systemctl start mongodb
> 		sudo systemctl status mongodb
> 	5.让它永久启动
> 		sudo systemctl enable mongodb
> ```
>
> ##### 第6步：检查MongoDB是否已经启动在27017端口号上
>
> 执行下面的命令：
>
> ```
> netstat -plntu
> ```
>
> ##### 第7步：登录MongoDB
>
> ```
> mongo
> ```
>
> ```
> 如果出现错误全局初始化失败：BadValue无效或无用户区域设置。 请确保LANG和/或LC_ *环境变量设置正确，请尝试命令：
> 	export LC_ALL=C 
> 	mongo 
> ```
>

### 三、MongoDB使用

#### 1.创建和删除数据库

##### 1.1创建数据库

> 语法：
>
> ```mysql
> use DATABASE_NAME
> 注意：如果指定的数据库DATABASE_NAME不存在，则该命令将创建一个新的数据库，否则返回现有的数据库
>
> #mysql中
> 创建数据库：create database basename;
> 切换数据库：use basename;
> ```
>
> 数据库命名：
>
> ​	a.不能是空字符串
>
> ​	b.不能包含特殊符号
>
> ​	c.最好全部小写
>
> ​	d.有一些数据库名是保留的，可以直接访问特殊数据库
>
> ​		admin：从权限的角度来说，是root的数据库
>
> ​		local：本地数据
>
> ​		config:配置，用于保存MongoDB的配置信息
>
> 演示：
>
> ```mysql
> #登录MongoDB                                                      
> ijeff@Rock:~$ mongo
> MongoDB shell version: 2.6.10
> connecting to: test
> Welcome to the MongoDB shell.
> For interactive help, type "help".
> For more comprehensive documentation, see
> 	http://docs.mongodb.org/
> Questions? Try the support group
> 	http://groups.google.com/group/mongodb-user
> #创建数据库并切换到该数据库下
> > use mydb1	
> switched to db mydb1
> ```
>
> 其他命令：
>
> ```mysql
> #检查当前选择的数据库
> > db
> mydb1
>
> #检查已经创建好的数据库列表
> > show dbs
> admin  (empty)
> local  0.078GB
>
> #创建的数据库(newdb)不在列表中。要显示数据库，需要至少插入一个文档，空的数据库是不显示出来的
> > db.mydb1.insert({'name':'lisi'})
> WriteResult({ "nInserted" : 1 })
> > show dbs
> admin  (empty)
> local  0.078GB
> mydb1  0.078GB
>
> #退出MongoDB
> > exit
> bye
> ijeff@Rock:~$ mongo
> MongoDB shell version: 2.6.10
> #默认的数据库test
> connecting to: test
>
> #如果数据库已经存在，use表示切换数据库
> > use mydb1
> switched to db mydb1
> ```

###### 1.2删除数据库

> 语法：
>
> ```
> db.dropDatabase()
>
> #注意：默认删除当前正在工作的数据库，如果没有通过use命令切换数据库，则删除的是test
> ```
>
> 演示：
>
> ```mysql
> #删除当前正在工作的数据库
> > db.dropDatabase()
> { "dropped" : "mydb1", "ok" : 1 }
> > show dbs
> admin  (empty)
> local  0.078GB
> ```

#### 2.创建和删除集合

> 类似于MySQL中的表
>
> 集合存在于数据库中，集合没有固定的结构，意味着可以对集合插入不同格式和不同类型的数据，但是尽量插入集合的时候保证数据的关联性
>
> 集合名的规范：
>
> ​	a.不能空字符串
>
> ​	b.集合名不能含有\0【空字符】，表示集合名的结尾
>
> ​	c.集合名不能以"system."开头，为系统集合保留的关键字
>
> ​	d.不能含有保留字符，千万不能含有$

##### 2.1创建集合

> 语法：
>
> ```
> db.createCollection(name, options)
>
> #注意
> name的类型为String，是要创建的集合的名称
> options的类型是Document，是一个文档，指定相应的大小和索引，是可选参数
> ```
>
> 下面是可以使用的选项列表：
>
> 在插入文档时，MongoDB首先检查上限集合`capped`字段的大小，然后检查`max`字段。
>
> | 字段            | 类型        | 描述                                       |
> | ------------- | --------- | ---------------------------------------- |
> | `capped`      | `Boolean` | (可选)如果为`true`，则启用封闭的集合。上限集合是固定大小的集合，它在达到其最大大小时自动覆盖其最旧的条目。 如果指定`true`，则还需要指定`size`参数。 |
> | `autoIndexId` | `Boolean` | (可选)如果为`true`，则在`_id`字段上自动创建索引。默认值为`false`。 |
> | `size`        | 数字        | (可选)指定上限集合的最大大小(以字节为单位)。 如果`capped`为`true`，那么还需要指定此字段的值。 |
> | `max`         | 数字        | (可选)指定上限集合中允许的最大文档数。                     |
>

> 演示：
>
> ```mysql
> > use test
> switched to db test
>
> #没有options选项的集合的创建
> > db.createCollection("myCollection")
> { "ok" : 1 }
>
> #显示当前数据库下的集合列表
> > show collections
> myCollection
> system.indexes
>
> #有options选项的集合的创建
> > db.createCollection("mycol",{capped:true,autoIndexId:true,size:1024,max:10000})
> { "ok" : 1 }
> > show collections
> myCollection
> mycol
> system.indexes
>
> #如果一个集合不存在，直接向其中插入数据，会自动创建
> > db.newcollection.insert({'name':'zhangsan'})
> WriteResult({ "nInserted" : 1 })
> > show collections
> myCollection
> mycol
> newcollection
> system.indexes
> ```

##### 2.2删除集合

> 语法：
>
> ```
> db.COLLECTION_NAME.drop()
>
> 注意：如果选定的集合成功删除，drop()方法将返回true，否则返回false
> ```
>
> 演示：
>
> ```mysql
> > db.newcollection.drop()
> true
> > show collections
> myCollection
> mycol
> ```

#### 3.文档操作

> 文档：相当表中的一条记录【实体】
>
> 是一组键值对，文档不需要设置相同的字段，并且相同的字段不需要相同的数据类型
>
> 注意：
>
> ​	a.文档中的键值对是有序的
>
> ​	b.文档中值除了字符串之外，还可以是其他数据类型【嵌套一个文档】
>
> ​	c.严格区分大小写和数据类型的，mycol    myCol
>
> ​	d.文档中不能有重复的键
>
> ​	e.文档中的键基本都是用字符串表示的
>
> 文档中键的命名：
>
> ​	a.键不能包含\0
>
> ​	b.$和.有特殊含义
>
> ​	c.以下划线开头的键是保留的，尽量不要使用下划线开头

##### 3.1插入文档

> 语法：
>
> ```mysql
> db.COLLECTION_NAME.insert(document)
> ```
>
> 注意：在插入的文档中，如果不指定_id参数，那么 MongoDB 会为此文档分配一个唯一的ObjectId
>
> _id为集合中的每个文档唯一的12个字节的十六进制数。 12字节划分如下 
>
> ```mysql
> _id: ObjectId(4 bytes timestamp, 3 bytes machine id, 2 bytes process id, 
>    3 bytes incrementer)
> ```
>
> 演示：
>
> ```mysql
> #插入单条文档
> > db.mycol.insert({
> ... id:100,
> ... name:'zhangsan',
> ... age:18,
> ... hobby:'sing',
> ... })
> WriteResult({ "nInserted" : 1 })
>
> #查看已经插入的文档
> > db.mycol.find()
> { "_id" : ObjectId("5b3d8c919e00ffe8882d9705"), "id" : 100, "name" : "zhangsan", "age" : 18, "hobby" : "sing" }
> > db.mycol.find().pretty()
> {
> 	"_id" : ObjectId("5b3d8c919e00ffe8882d9705"),
> 	"id" : 100,
> 	"name" : "zhangsan",
> 	"age" : 18,
> 	"hobby" : "sing"
> }
>
> #批量插入文档
> > db.mycol.insert({ id:101, name:"lisi", age:20, hobby:'dance', },{ id:102, name:'jack', age:15, hobby:'write', })
> WriteResult({ "nInserted" : 1 })
> > db.check.insert([
> ...    {
> ...       _id: 101,
> ...       title: 'MongoDB Guide', 
> ...       description: 'MongoDB is no sql database',
> ...       by: 'yiibai tutorials',
> ...       url: 'http://www.yiibai.com',
> ...       tags: ['mongodb', 'database', 'NoSQL'],
> ...       likes: 100
> ...    },
> ... 
> ...    {
> ...       _id: 102,
> ...       title: 'NoSQL Database', 
> ...       description: "NoSQL database doesn't have tables",
> ...       by: 'yiibai tutorials',
> ...       url: 'http://www.yiibai.com',
> ...       tags: ['mongodb', 'database', 'NoSQL'],
> ...       likes: 210, 
> ...       comments: [
> ...          {
> ...             user:'user1',
> ...             message: 'My first comment',
> ...             dateCreated: new Date(2017,11,10,2,35),
> ...             like: 0 
> ...          }
> ...       ]
> ...    },
> ...    {
> ...       _id: 104,
> ...       title: 'Python Quick Guide', 
> ...       description: "Python Quick start ",
> ...       by: 'yiibai tutorials',
> ...       url: 'http://www.yiibai.com',
> ...       tags: ['Python', 'database', 'NoSQL'],
> ...       likes: 30, 
> ...       comments: [
> ...          {
> ...             user:'user1',
> ...             message: 'My first comment',
> ...             dateCreated: new Date(2018,11,10,2,35),
> ...             like: 590 
> ...          }
> ...       ]
> ...    }
> ... ])
> BulkWriteResult({
> 	"writeErrors" : [ ],
> 	"writeConcernErrors" : [ ],
> 	"nInserted" : 3,
> 	"nUpserted" : 0,
> 	"nMatched" : 0,
> 	"nModified" : 0,
> 	"nRemoved" : 0,
> 	"upserted" : [ ]
> })
> > db.check.find().pretty()
> {
> 	"_id" : 101,
> 	"title" : "MongoDB Guide",
> 	"description" : "MongoDB is no sql database",
> 	"by" : "yiibai tutorials",
> 	"url" : "http://www.yiibai.com",
> 	"tags" : [
> 		"mongodb",
> 		"database",
> 		"NoSQL"
> 	],
> 	"likes" : 100
> }
> {
> 	"_id" : 102,
> 	"title" : "NoSQL Database",
> 	"description" : "NoSQL database doesn't have tables",
> 	"by" : "yiibai tutorials",
> 	"url" : "http://www.yiibai.com",
> 	"tags" : [
> 		"mongodb",
> 		"database",
> 		"NoSQL"
> 	],
> 	"likes" : 210,
> 	"comments" : [
> 		{
> 			"user" : "user1",
> 			"message" : "My first comment",
> 			"dateCreated" : ISODate("2017-12-09T18:35:00Z"),
> 			"like" : 0
> 		}
> 	]
> }
> {
> 	"_id" : 104,
> 	"title" : "Python Quick Guide",
> 	"description" : "Python Quick start ",
> 	"by" : "yiibai tutorials",
> 	"url" : "http://www.yiibai.com",
> 	"tags" : [
> 		"Python",
> 		"database",
> 		"NoSQL"
> 	],
> 	"likes" : 30,
> 	"comments" : [
> 		{
> 			"user" : "user1",
> 			"message" : "My first comment",
> 			"dateCreated" : ISODate("2018-12-09T18:35:00Z"),
> 			"like" : 590
> 		}
> 	]
> }
> >
> ```
>
> ##### 其它插入文档的方法【作为了解】
>
> db.collection.insertOne():插入单个文档
>
> db.collection.insertMany()：插入多个文档
>
> a.db.collection.insertOne()方法
>
> db.collection.insertOne()`方法将单个文档插入到集合中。 如果文档没有指定`_id`字段，MongoDB会自动将`_id`字段与`ObjectId`值添加到新文档
>
> 演示：
>
> ```mysql
> #以下示例将新文档插入到库存集合中
> db.invent.insertOne({ 
>        item: "canvas", 
>        num: 100, 
>        tags: ["cotton"], 
>        size: { 
>             h: 20,
>             w: 30, 
>         } 
> })
>
>
> #db.collection.insertOne()方法返回包含新插入的文档的`_id```字段值的文档
>
> 执行结果如下：
> > db.inventory.insertOne(
> ...    { item: "canvas", qty: 100, tags: ["cotton"], size: { h: 28, w: 35.5, uom: "cm" } }
> ... )
> {
>         "acknowledged" : true,
>         "insertedId" : ObjectId("5955220846be576f199feb55")
> }
> >
> ```
>
> b.db.collection.insertMany()方法
>
> db.collection.insertMany()`方法将多个文档插入到集合中，可将一系列文档传递给`db.collection.insertMany()`方法。以下示例将三个新文档插入到库存集合中。如果文档没有指定`_id`字段，MongoDB会向每个文档添加一个ObjectId值的`_id`字段
>
> 演示：
>
> ```mysql
> db.inventory.insertMany([
>    { item: "journal", qty: 25, tags: ["blank", "red"], size: { h: 14, w: 21, uom: "cm" } },
>    { item: "mat", qty: 85, tags: ["gray"], size: { h: 27.9, w: 35.5, uom: "cm" } },
>    { item: "mousepad", qty: 25, tags: ["gel", "blue"], size: { h: 19, w: 22.85, uom: "cm" } }
> ])
>
> #insertMany()返回包含新插入的文档_id字段值的文档。执行结果如下：
> > db.inventory.insertMany([
> ...    { item: "journal", qty: 25, tags: ["blank", "red"], size: { h: 14, w: 21, uom: "cm" } },
> ...    { item: "mat", qty: 85, tags: ["gray"], size: { h: 27.9, w: 35.5, uom: "cm" } },
> ...    { item: "mousepad", qty: 25, tags: ["gel", "blue"], size: { h: 19, w: 22.85, uom: "cm" } }
> ... ])
> {
>         "acknowledged" : true,
>         "insertedIds" : [
>                 ObjectId("59552c1c46be576f199feb56"),
>                 ObjectId("59552c1c46be576f199feb57"),
>                 ObjectId("59552c1c46be576f199feb58")
>         ]
> }
> ```

##### 3.2查询文档

> 语法：
>
> ```mysql
> db.COLLECTION_NAME.find(document)
>
> 注意：
> find（）将以非结构化的方式返回查询结果
>
> 要以格式化的方式返回查询结果，可以结合pretty函数使用
> db.COLLECTION_NAME.find(document).pretty()
>
> findOne():返回一个文档
> ```
>
> ##### MongoDB 与 RDBMS的等效MySQL子句
>
> 要在一些条件的基础上查询文档，可以使用以下操作:
>
> | 操作   | 语法                       | 示例                                       | MySQL等效语句             |
> | ---- | ------------------------ | ---------------------------------------- | --------------------- |
> | 相等   | `{<key>:<value>}`        | `db.mycol.find({"by":"yiibai"}).pretty()` | `where by = 'yiibai'` |
> | 小于   | `{<key>:{$lt:<value>}}`  | `db.mycol.find({"likes":{$lt:50}}).pretty()` | `where likes < 50`    |
> | 小于等于 | `{<key>:{$lte:<value>}}` | `db.mycol.find({"likes":{$lte:50}}).pretty()` | `where likes <= 50`   |
> | 大于   | `{<key>:{$gt:<value>}}`  | `db.mycol.find({"likes":{$gt:50}}).pretty()` | `where likes > 50`    |
> | 大于等于 | `{<key>:{$gte:<value>}}` | `db.mycol.find({"likes":{$gte:50}}).pretty()` | `where likes >= 50`   |
> | 不等于  | `{<key>:{$ne:<value>}}`  | `db.mycol.find({"likes":{$ne:50}}).pretty()` | `where likes != 50`   |
>
> 演示：
>
> a.MongoDB中的AND操作符
>
> 语法：
>
> ```mysql
> #在find()方法中，如果通过使用’，‘将它们分开传递多个键，则 MongoDB 将其视为AND条件。 以下是AND的基本语法
> >db.mycol.find(
>    {
>       $and: [
>          {key1: value1}, {key2:value2}
>       ]
>    }
> ).pretty()
> ```
>
> 演示：
>
> ```mysql
>  db.check.find({$and:[{'by':'yiibai tutorials'},{'title':'Python Quick Guide'}]}).pretty()
> {
> 	"_id" : 104,
> 	"title" : "Python Quick Guide",
> 	"description" : "Python Quick start ",
> 	"by" : "yiibai tutorials",
> 	"url" : "http://www.yiibai.com",
> 	"tags" : [
> 		"Python",
> 		"database",
> 		"NoSQL"
> 	],
> 	"likes" : 30,
> 	"comments" : [
> 		{
> 			"user" : "user1",
> 			"message" : "My first comment",
> 			"dateCreated" : ISODate("2018-12-09T18:35:00Z"),
> 			"like" : 590
> 		}
> 	]
> }
> > 
>
>  db.check.find({'by':'yiibai tutorials','title':'Python Quick Guide'}).pretty()
>
> {
> 	"_id" : 104,
> 	"title" : "Python Quick Guide",
> 	"description" : "Python Quick start ",
> 	"by" : "yiibai tutorials",
> 	"url" : "http://www.yiibai.com",
> 	"tags" : [
> 		"Python",
> 		"database",
> 		"NoSQL"
> 	],
> 	"likes" : 30,
> 	"comments" : [
> 		{
> 			"user" : "user1",
> 			"message" : "My first comment",
> 			"dateCreated" : ISODate("2018-12-09T18:35:00Z"),
> 			"like" : 590
> 		}
> 	]
> }
>
> #等效的SQL的语句
> select * from check where by="" and title="";
> ```
>
> b.MongoDB中的OR操作符
>
> 语法：
>
> ```mysql
> #在要根据OR条件查询文档，需要使用$or关键字。 以下是OR条件的基本语法
> >db.mycol.find(
>    {
>       $or: [
>          {key1: value1}, {key2:value2}
>       ]
>    }
> ).pretty()
> ```
>
> 演示：
>
> ```mysql
>  db.check.find({$or:[{'by':'yiibai tutorials'},{'title':'Python Quick Guide'}]}).pretty()
> ```
>
> c.使用 AND 和 OR 联合使用
>
> 演示：
>
> ```mysql
> > db.check.find({'likes':{$gt:100},$or:[{'title':'NoSQL Database'},{'by':'yiibai tutorials'}]}).pretty()
> {
> 	"_id" : 102,
> 	"title" : "NoSQL Database",
> 	"description" : "NoSQL database doesn't have tables",
> 	"by" : "yiibai tutorials",
> 	"url" : "http://www.yiibai.com",
> 	"tags" : [
> 		"mongodb",
> 		"database",
> 		"NoSQL"
> 	],
> 	"likes" : 210,
> 	"comments" : [
> 		{
> 			"user" : "user1",
> 			"message" : "My first comment",
> 			"dateCreated" : ISODate("2017-12-09T18:35:00Z"),
> 			"like" : 0
> 		}
> 	]
> }
> > 
> select * from check where likes>100 and (title='' or by='')
> ```

##### 3.3更新文档

> 1>update()：更新现有文档中的值
>
> criteria:用于指定一个查询，查询选择将要更新的目标记录
>
> action：用于指定更新信息，也可以使用操作符完成
>
> options:
>
> 语法：
>
> ```mysql
> db.COLLECTION_NAME.update(SELECTION_CRITERIA, UPDATED_DATA)
> ```
>
> 演示：
>
> ```mysql
> #find（）：查询指定列的数据
> #{'_id':1,'title':1}：表示要检索的字段列表
> #注意：当执行find函数的时候，它默认将所有的文档显示，为了限制显示的字段，需要将字段列表的值设置为1，如果不显示可以设置为0
> > db.check.find({'title':'MongoDB Guide'},{'_id':1,'title':1})
> { "_id" : 101, "title" : "MongoDB Guide" }
>
> #注意：update默认只更新一个文档，如果要更新多个文档，则添加参数{multi:true})
> db.check.update({'title':'MongoDB Guide'},{$set:{'title':'aaaaaa'}},{multi:true})
> ```
>
> 2>save()：使用`save()`方法中传递的文档数据替换现有文档
>
> 语法：
>
> ```mysql
> >db.COLLECTION_NAME.save({_id:ObjectId(),NEW_DATA})
> ```
>
> 演示：
>
> ```mysql
> > use mydb1
> switched to db mydb1
> > db.check.save({'_id':102,'titlt':'bbbb','by':'hello'})
> WriteResult({ "nMatched" : 0, "nUpserted" : 1, "nModified" : 0, "_id" : 102 })
> > db.check.find({'_id':102},{'_id':1,'title':1,'by':1})
> { "_id" : 102, "by" : "hello" }
> ```

##### 3.4删除文档

> MongoDB中的 `remove()`方法用于从集合中删除文档。 `remove()`方法接受两个参数。 一个是删除条件，第二个是标志：`justOne`。
>
> ​	criteria - (可选)符合删除条件的集合将被删除。
>
> ​	justOne - (可选)如果设置为`true`或``1``，则只删除一个文档
>
> 语法：
>
> ```mysql
> >db.COLLECTION_NAME.remove(DELLETION_CRITTERIA)
> ```
>
> 演示：
>
> ```mysql
> > db.check.remove({'_id':100})
> WriteResult({ "nRemoved" : 0 })
> > db.check.find({},{'_id':1,'title':1})
> { "_id" : 102 }
>
> ```

#### 4.查询

##### 4.1投影

> 投影：查询过程中，只显示指定的字段
>
> 语法：
>
> ```mysql
> >db.COLLECTION_NAME.find({},{KEY:1})
> ```
>
> 演示：
>
> ```mysql
> #在查询文档时只显示文档的标题
> > db.mycol.find({}, {'title':1,'_id':0})
>
> ##注意，在执行find()方法时，始终都会显示_id字段，如果不想要此字段，则需要将其设置为0
> ```

##### 4.2限制筛选记录

> 1>limit方法
>
> 作用：限制MongoDB要返回的记录数
>
> 根据指定的参数返回记录数
>
> 语法：
>
> ```mysql
> > db.COLLECTION_NAME.find().limit(NUMBER)
> ```
>
> 演示：
>
> ```mysql
> #在查询文档时仅显示两个文档
> > db.mycol.find({},{"title":1,_id:0}).limit(2)
> ```
>
> 2>skip方法
>
> 
>
> 语法：
>
> ```mysql
> >db.COLLECTION_NAME.find().limit(NUMBER).skip(NUMBER)
> ```
>
> 演示：
>
> ```mysql
> > db.mycol.find({},{"title":1,_id:0}).limit(1).skip(2)
>
> #注意：skip()方法中的默认值为0。
> ```

##### 4.3对查询记录排序

> 语法：
>
> ```mysql
> >db.COLLECTION_NAME.find().sort({KEY:1})
> ```
>
> 注意：使用指定顺序进行排序，1表示升序，-1表示降序
>
> 演示：
>
> ```mysql
> > db.mycol.find({},{'_id':1, 'title':1})
> # 按`title`降序排序
> > db.mycol.find({},{"title":1,_id:0}).sort({"title":-1})
> # 按`title`降序排序
> > db.mycol.find({},{"title":1,_id:0}).sort({"title":-1})
> ```

##### 4.4分组与聚合函数查询

> 1>aggregate()方法
>
> 语法：
>
> ```
> >db.COLLECTION_NAME.aggregate(AGGREGATE_OPERATION)
> ```
>
> 以下是可用聚合表达式的列表。
>
> | 表达式         | 描述                                       | 示例                                       |
> | ----------- | ---------------------------------------- | ---------------------------------------- |
> | `$sum`      | 从集合中的所有文档中求出定义的值。                        | `db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$sum : "$likes"}}}])` |
> | `$avg`      | 计算集合中所有文档的所有给定值的平均值。                     | `db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$avg : "$likes"}}}])` |
> | `$min`      | 从集合中的所有文档获取相应值的最小值。                      | `db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$min : "$likes"}}}])` |
> | `$max`      | 从集合中的所有文档获取相应值的最大值。                      | `db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$max : "$likes"}}}])` |
> | `$push`     | 将值插入到生成的文档中的数组中。                         | `db.mycol.aggregate([{$group : {_id : "$by_user", url : {$push: "$url"}}}])` |
> | `$addToSet` | 将值插入生成的文档中的数组，但不会创建重复项。                  | `db.mycol.aggregate([{$group : {_id : "$by_user", url : {$addToSet : "$url"}}}])` |
> | `$first`    | 根据分组从源文档获取第一个文档。 通常情况下，这只适用于以前应用的“`$sort`”阶段。 | `db.mycol.aggregate([{$group : {_id : "$by_user", first_url : {$first : "$url"}}}])` |
> | `$last`     | 根据分组从源文档获取最后一个文档。通常情况下，这只适用于以前应用的“`$sort`”阶段。 | `db.mycol.aggregate([{$group : {_id : "$by_user", last_url : {$last : "$url"}}}])` |
>
> 演示：
>
> ```mysql
>  db.article.aggregate([{$group:{'_id':'$by_user','num_tutorial':{$sum:1}}}])
> { "_id" : "Curry", "num_tutorial" : 1 }
> { "_id" : "Kuber", "num_tutorial" : 1 }
> { "_id" : "Maxsu", "num_tutorial" : 2 }
>
> #等效的sql语句
> select  by_user, count(*) as num_tutorial from article group by by_user
> ```
>
> 管道：
>
> 每一组的输出可以作为另一组的输入，并且生成一组新的文档
>
> $sort
>
> $limit
>
> $skip
>
> $group



### MongoDB与Python的交互

#### 1.安装

> pip3 install pymongo

#### 2.使用

> 演示代码：

```python
import pymongo
from pymongo import  MongoClient
from bson.objectid import ObjectId

#1.建立连接
#创建MongoClient的对象
#方式一
#特点：可以连接默认的主机和端口号
#client = MongoClient()
#方式二
#明确指明主机和端口号
#client = MongoClient('localhost',27017)
#client = MongoClient(host='localhost',port=27017)
#方式三
#使用MongoDB URI的
client = MongoClient('mongodb://localhost:27017')

#2.获取数据库
#MongoDB的一个实例可以支持多个独立的数据库
#可以通过MongoClient的对象的属性来访问数据库
#方式一
db = client.test
print(db)
#方式二
#db = client['test']

#3.获取集合
#集合是存储在MongoDb中的一组文档，可以类似于MySQl中的表
#方式一
collection = db.students
#方式二
#collection = db['students']
"""
注意：
MongoDB中关于数据库和集合的创建都是懒创建
以上的操作在MongoDB的服务端没有做任何操作
当第一个文档被插入集合的时候才会创建数据库和集合
"""

#4.文档
#在pymongo中使用字典来表示文档
student1 = {
    'id':'20180101',
    'name':'jack',
    'age':20,
    'gender':'male'
}

#5.插入文档
#5.1 insert（）
#插入单条数据
#注意：MongoDb会自动生成一个ObjectId,insert函数的返回值为objectid
result = collection.insert(student1)
print(result)

#插入多条数据
student2 = {
    'id':'20180530',
    'name':'tom',
    'age':30,
    'gender':'male'
}
student3 = {
    'id':'20180101',
    'name':'bob',
    'age':18,
    'gender':'male'
}
#result = collection.insert([student2,student3])

#5.2insert_one()
student4 = {
    'id':'20180101',
    'name':'rose',
    'age':25,
    'gender':'female'
}
#result = collection.insert_one(student4)
#print(result)           #InsertOneResult
#print(result.inserted_id)

#5.3insert_many()
#result = collection.insert_many([student2,student3]);
#print(result)           #InsertOneResult
#print(result.inserted_ids)

#6.查询文档
#6.1
#find_one()
result = collection.find_one({'name':'jack'})
print(type(result))    #<class 'dict'>
print(result)

#6.2通过objectid查询
#5b3ed21f2e1016e9ad2dc7b7
#注意：导入模块
result = collection.find_one({'_id':ObjectId('5b3ed21f2e1016e9ad2dc7b7')})
print(result)
#查询不到结果则返回None

#6.3find()
#需求：查询年龄为20的数据
results = collection.find({'age':20})
print(results)
#Cursor相当于是一个生成器，只能通过遍历的方式获取其中的数据
for r in results:
    print(r)

#需求：查询年龄大于20的数据
results = collection.find({'age':{'$gt':20}})

#6.4其他用法
#a.count()
#统计所有数据的条数
count1 = collection.find().count()
#统计制定条件的数据条数
count1 = collection.find({'age':20}).count()

#b.sort()
r0 = collection.find().sort('name',pymongo.ASCENDING)

#c.limit(),skip()
r0 = collection.find().sort('name',pymongo.ASCENDING).skip(2)
r0 = collection.find().sort('name',pymongo.ASCENDING).skip(2).limit(5)
#注意事项：在数据库数量非常庞大的情况下，最好不要使用大的 的偏移量，很可能会导致内存溢出


#7.更新文档
#7.1update()
conditon = {'name':'jack'}
student = collection.find_one(conditon);
student['age'] = 30
result = collection.update(conditon,student)

#7.2update_one()
conditon = {'name':'jack'}
student = collection.find_one(conditon);
student['age'] = 30
result = collection.update_one(conditon,{'$set':student})
print(result.matched_count,result.modified_count)

#7.2update_many()
#查询年龄大于20的数据，然后讲年龄增加1
conditon = {'age':{'$gt':20}}
result = collection.update_one(conditon,{'$inc':{'age':1}})
print(result.matched_count,result.modified_count)

#8.删除文档
#8.1remove()
#将符合条件的所有的数据全部删除
result = collection.remove({'name':'rose'})

#8.2delete_one()
result = collection.delete_one({'name':'rose'})

#8.3delete_many()
result = collection.delete_many({'name':'rose'})
```








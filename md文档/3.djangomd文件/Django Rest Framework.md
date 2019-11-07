# Day10 Django Rest Framework

## RESTful简介

### 一. Web应用模式

##### 在开发Web应用中，有两种应用模式：

```
前后端不分离：渲染
前后端分离
```

#### 1 前后端不分离

```
在前后端不分离的应用模式中，前端页面看到的效果都是由后端控制，由后端渲染页面或重定向，也就是后端需要控制前端的展示，前端与后端的耦合度很高。

这种应用模式比较适合纯网页应用，但是当后端对接App时，App可能并不需要后端返回一个HTML网页，而仅仅是数据本身，所以后端原本返回网页的接口不再适用于前端App应用，为了对接App后端还需再开发一套接口。

```

#### 2 前后端分离

```
在前后端分离的应用模式中，后端仅返回前端所需的数据，不再渲染HTML页面，不再控制前端的效果。至于前端用户看到什么效果，从后端请求的数据如何加载到前端中，都由前端自己决定，网页有网页的处理方式，App有App的处理方式，但无论哪种前端，所需的数据基本相同，后端仅需开发一套逻辑对外提供数据即可。

在前后端分离的应用模式中 ，前端与后端的耦合度相对较低。

在前后端分离的应用模式中，我们通常将后端开发的每个视图都称为一个接口，或者API，前端通过访问接口来对数据进行增删改查。
```

### 二. 认识RESTful

```
即Representational State Transfer的缩写。维基百科称其为“具象状态传输”，国内大部分人理解为“表现层状态转化”。

RESTful是一种开发理念。维基百科说：REST是设计风格而不是标准。 REST描述的是在网络中client和server的一种交互形式；REST本身不实用，实用的是如何设计 RESTful API（REST风格的网络接口）,一种万维网软件架构风格。

我们先来具体看下RESTful风格的url,比如我要查询商品信息，那么
非REST的url：http://.../queryGoods?id=1001&type=t01
REST的url: http://.../t01/goods/1001

可以看出REST特点：url简洁，将参数通过url传到服务器，而传统的url比较啰嗦，而且现实中浏览器地址栏会拼接一大串字符，想必你们都见过吧。但是采用REST的风格就会好很多，现在很多的网站已经采用这种风格了，这也是潮流方向，典型的就是url的短化转换。
```

#### 到底什么是RESTful架构：

```
每一个URL代表一种资源；
客户端和服务器之间，传递这种资源的某种表现层；
客户端通过四个HTTP动词（GET,POST,PUT,DELETE），对服务器端资源进行操作，实现"表现层状态转化"。
```

### 三. RESTful API设计

###### 协议

接口API与用户的通信协议，通常使用HTTP\(S\)协议。  TCP ,  UDP 

###### 域名  应该尽量将API部署在专用域名之下。

```
http://api.hello.com 
```

如果确定API很简单，不会有大规模扩充，可以考虑放在主域名之下。

```
http://www.hello.com/api/
```

###### 版本

应该将API的版本号放入URL。

```
http://api.rock.com/v1/
```

也有做法是将版本号放在HTTP的头信息中，但不如放在URL中方便和直观。GITHUB是这么搞的。

###### 路径（Endpoint）

路径又称”终点“（endpoint），表示API的具体网址。

在RESTful架构中，每个网址代表一种资源（Resource），所以网址中不能有动词，只能有名词，而且所用的名词往往与数据库的表格名对应。一般来说，数据库中的表都是同种记录的”集合“（collection），所以API中的名词也应该使用复数。

###### HTTP动词

对于资源的具体操作类型，由HTTP动词表示。

HTTP常用动词

- GET（SELECT）：从服务器取出资源
- POST（CREATE or UPDATE）：在服务器创建资源或更新资源
- PUT（UPDATE）：在服务器更新资源（客户端提供改变后的完整资源）
- PATCH（UPDATE）：在服务器更新资源（客户端提供改变的属性）
- DELETE（DELETE）：从服务器删除资源
- HEAD：获取资源的元数据
- OPTIONS：获取信息，关于资源的哪些属性是客户端可以改变的、

示例

- GET  /students：获取所有学生
- POST /students：新建学生
- GET  /students/id：获取某一个学生
- PUT /students/id ：更新某个学生的信息（需要提供学生的全部信息）
- PATCH /students/id：更新某个学生的信息（需要提供学生变更部分信息）
- DELETE /students/id：删除某个学生

###### 过滤信息（Filtering）

如果记录数量过多，服务器不可能将它们返回给用户。API应该提供参数，过滤返回结果。

- ?limit=10
- ?offset=10
- ?page=2&per\_page=20
- ?sortby=name&order=desc
- ?student\_id=id

参数的设计允许存在冗余，即允许API路径和URL参数偶尔有重复，比如 GET /students/id 和 ？student\_id=id

###### 状态码

服务器向用户返回的状态码和提示信息，常见的有以下一些地方

- 200 OK - \[GET\]：服务器成功返回用户请求的数据
- 201 CREATED -\[POST/PUT/PATCH\]：用户新建或修改数据成功
- 202 Accepted - \[\*\] ：表示一个请求已经进入后台排队（异步任务）
- 204 NO CONTENT - \[DELETE\]：表示数据删除成功
- 400 INVALID REQUEST - \[POST/PUT/PATCH\]：用户发出的请求有错误
- 401 Unauthorized - \[\*\] ：表示用户没有权限（令牌，用户名，密码错误）
- 403 Forbidden - \[\*\]：表示用户得到授权，但是访问是被禁止的
- 404 NOT FOUND - \[\*\]：用户发出的请求针对的是不存在的记录
- 406 Not Acceptable - \[\*\]：用户请求格式不可得
- 410 Gone - \[GET\] ：用户请求的资源被永久移除，且不会再得到的
- 422 Unprocesable entity -\[POST/PUT/PATCH\]：当创建一个对象时，发生一个验证错误
- 500 INTERNAL SERVER EROR - \[\*\] ：服务器内部发生错误

###### 错误处理

如果状态码是4xx，就应该向用户返回出错信息。一般来说，返回的信息中将error做为键名

###### 返回结果

针对不同操作，服务器想用户返回的结果应该符合以下规范

- GET /sutdents：返回资源对象的列表（数组，集合）
- GET /collection/id：返回单个资源对象
- POST /collection：返回新生成的资源对象
- PUT /collection/id：返回完整的资源对象
- PATCH /collection/id：返回完整的资源对象
- DELETE /collection/id：返回一个空文档

###### 使用链接关联资源

RESTful API可以做到超媒体，即返回结果中提供链接，连向其他API方法，使得用户不查文档，也知道下一步应该做什么。

```
{
    "link": {
        "rel":   "collection https://www.hello.com/zoostudents",
        "href":  "https://api.hello.com/students",
        "title": "List of students",
        "type":  "application/vnd.yourformat+json"
      }
}
```

- rel：表示这个API与当前网址的关系
- href：表示API的路径
- title：表示API的标题
- type：表示返回的类型

###### 其它

- 服务器返回的数据格式，应该尽量使用JSON
- API的身份认证应该使用OAuth2.0框架



### APIView

- 子类
  - generics包中
  - GenericAPIView
    - 增加的模型的获取操作
    - get_queryset
    - get_object
      - lookup_field 默认pk
    - get_serializer
    - get_serializer_class
    - get_serializer_context
    - filter_queryset
    - paginator
    - paginate_queryset
    - get_paginated_response
  - CreateAPIView
    - 创建的类视图
    - 继承自GenericAPIView
    - 继承自CreateModelMixin
    - 实现了post进行创建
  - ListAPIView
    - 列表的类视图
    - 继承自GenericAPIView
    - 继承自ListModelMixin
    - 实现了get
  - RetrieveAPIView
    - 查询单个数据的类视图
    - 继承自GenericAPIView
    - 继承自RetrieveModelMixin
    - 实现了get  
  - DestroyAPIView
    - 销毁数据的类视图，删除数据的类视图
    - 继承自GenericAPIView
    - 继承自DestroyModelMixin
    - 实现了delete
  - UpdateAPIView
    - 更新数据的类视图
    - 继承自GenericAPIView
    - 继承自UpdateModelMixin
    - 实现了 put,patch
  - ListCreateAPIView
    - 获取列表数据，创建数据的类视图
    - 继承自GenericAPIView
    - 继承自ListModelMixin
    - 继承自CreateModelMixin
    - 实现了  get,post
  - RetrieveUpdateAPIView
    - 获取单个数据，更新单个数据的类视图
    - 继承自GenericAPIView
    - 继承自RetrieveModelMixin
    - 继承自UpdateModelMixin
    - 实现了 get, put, patch
  - RetrieveDestroyAPIView
    - 获取单个数据，删除单个数据
    - 继承自GenericAPIView
    - 继承自RetrieveModelMixin
    - 继承自DestroyModelMixin
    - 实现了  get, delete
  - RetrieveUpdateDestroyAPIView
    - 获取单个数据，更新单个数据，删除单个数据的类视图
    - 继承自GenericAPIView
    - 继承自RetrieveModelMixin
    - 继承自UpdateModelMixin
    - 继承自DestroyModelMixin
    - 实现了 get, put, patch, delete
- mixins
  - CreateModelMixin
    - create
    - perform_create
    - get_success_headers
  - ListModelMixin
    - list
      - 查询结果集，添加分页，帮你序列化
  - RetrieveModelMixin
    - retrieve
      - 获取单个对象并进行序列化
  - DestroyModelMixin
    - destroy
      - 获取单个对象
      - 调用执行删除
      - 返回Respon  状态码204
    - perform_destroy
      - 默认是模型的delete
      - 如果说数据的逻辑删除
        - 重写进行保存
  - UpdateModelMixin
    - update
      - 获取对象，合法验证
      - 执行更新
    - perform_update
    - partial_update
      - 差量更新，对应的就是patch
- viewsets
  - ViewSetMixin
    - 重写as_view
  - GenericViewSet
    - 继承自GenericAPIView
    - 继承自ViewSetMixin
  - ViewSet
    - 继承自APIView
    - 继承自ViewSetMixin
    - 默认啥都不支持，需要自己手动实现
  - ReadOnlyModelViewSet
    - 只读的模型的视图集合
    - 继承自RetrieveModelMixin
    - 继承自ListModelMixin
    - 继承自GenericViewSet
  - ModelViewSet
    - 直接封装对象的所有操作
    - 继承自GenericViewSet
    - 继承自CreateModelMixin
    - 继承自RetrieveModelMixin
    - 继承自UpdateModelMixin
    - 继承自DestroyModelMixin
    - 继承自ListModelMixin


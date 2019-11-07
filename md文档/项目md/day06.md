#### 01.购买礼物

- 购买礼物生成订单
- 订单表的设计
- 使用事务保存订单数据
- 使用乐观锁并发下单

#### 02.模型类

- 礼物模型类	

  | Field | Description |
  | ----- | ----------- |
  | name  | 礼物名称    |
  | price | 礼物价格    |
  | stock | 礼物库存    |
  | sales | 礼物销量    |

- 总订单模型类

  | Field        | Description                           |
  | ------------ | ------------------------------------- |
  | uid          | 用户id                                |
  | order_code   | 订单编号                              |
  | total_count  | 总数量                                |
  | total_amount | 总金额                                |
  | status       | 订单状态（1待支付，2待发货、3待签收） |

- 订单详情模型类

  | Field      | Description |
  | ---------- | ----------- |
  | uid        | 用户id      |
  | order_code | 订单编号    |
  | goods_id   | 礼物id      |
  | counts     | 购买数量    |
  | price      | 商品单价    |

#### 03.接口设计

- 参数：json格式 {"商品id": "商品数量"}     例如：{\"1\": 10, \"2\": 10, \"3\":10}
- 请求方式：post

#### 04.使用事务

- 在保存订单数据时，涉及到多张表（礼物表、订单表、订单详情表）据的修改应该是一个整体事务，即要么一起成功，要么一起失败。

- mysql中事务的使用

  ```python
  begin  # 开启事务
  rollback # 回滚事务
  commit  # 提交事务
  ```

-  Django中事务的使用

  - with语句用法

    ```python
    from django.db import transaction
    
    def viewfunc(request):
      # 这部分代码不在事务中，会被Django自动提交
      ......
    
      with transaction.atomic():
          # 创建保存点
          save_id = transaction.savepoint()
          # 这部分代码会在事务中执行
          ......
          # 回滚到保存点
          transaction.savepoint_rollback(save_id)
          ......
          # 提交从保存点到当前状态的所有数据库事务操作
          transaction.savepoint_commit(save_id)
    ```

#### 05.使用乐观锁并发下单

- 在多个用户同时发起对同一个商品的下单请求时，先查询商品库存，再修改商品库存，会出现资源竞争问题，导致库存的最终结果出现异常。

- 解决办法：

  - 悲观锁：

    - 当查询某条记录时，即让数据库为该记录加锁，锁住记录后别人无法操作，使用类似如下语法

      ```python
      # 满足的条件
      # 1、必须在事务中使用
      # 2、select 后面加 for update
      select stock from sp_goods where id=1 for update;
      
      Goods.objects.select_for_update().get(id=1)
      ```

    - 悲观锁类似于我们在多线程资源竞争时添加的互斥锁，容易出现死锁现象，采用不多。
      
    - 比如用户A给表A加了锁，然后查询表B。用户B给表B加了锁，然后查询表A。两个人同时等待对方操作完后，解除锁。这样就产生了死锁
  
- 乐观锁：
  
  - 乐观锁并不是真实存在的锁，而是在更新的时候判断此时的库存是否是之前查询出的库存，如果相同，表示没人修改，可以更新库存，否则表示别人抢过资源，不再执行库存更新。类似如下操作
  
      ```python
      update sp_goods set stock=10 where id=1 and stock=20;
      
      Goods.objects.filter(id=1, stock=20).update(stock=10)
    ```
  
  - 操作条件：
    - 库存大于购买量，
    - 更新库存和销量时原始库存没变。

#### 06.MySQL事务隔离级别

- 事务隔离级别指的是在处理同一个数据的多个事务中，一个事务修改数据后，其他事务何时能看到修改后的结果。

- MySQL数据库事务隔离级别主要有四种：

  - `Serializable`：串行化，一个事务一个事务的执行。
  - `Repeatable read`：可重复读，无论其他事务是否修改并提交了数据，在这个事务中看到的数据值始终不受其他事务影响。
  - `Read committed`：读取已提交，其他事务提交了对数据的修改后，本事务就能读取到修改后的数据值。
  - `Read uncommitted`：读取未提交，其他事务只要修改了数据，即使未提交，本事务也能看到修改后的数据值。
  - MySQL数据库默认使用可重复读（ Repeatable read）。

- linux修改方式：

  ![image-20190901182631928](day06.assets/image-20190901182631928.png)

- mac修改方式

  ```python
  serializable 串行化
  repeatable read 可重复读
  read committed 读取已提交
  read uncommitted 读取未提交
  
  # 修改全局事务隔离级别
  set global transaction isolation level read committed;
  
  # 查看隔离级别
  select @@global.transaction_isolation;
  ```



#### 07.支付宝支付

- 支付宝开放平台入口

  ```python
  https://open.alipay.com/platform/home.htm
  ```

- 登陆后创建沙箱环境

  ![image-20190901192404605](day06.assets/image-20190901192404605.png)

- 沙箱环境

  - 支付宝提供给开发者的模拟支付的环境。跟真实环境是分开的。

  - 沙箱应用：https://openhome.alipay.com/platform/appDaily.htm?tab=info

    ![image-20190901192525607](day06.assets/image-20190901192525607.png)

  - 沙箱账号：https://openhome.alipay.com/platform/appDaily.htm?tab=account

    ![image-20190901192605359](day06.assets/image-20190901192605359.png)

- 支付宝开发文档
  - 文档主页：https://openhome.alipay.com/developmentDocument.htm
  - 电脑网站支付产品介绍：https://docs.open.alipay.com/270
  - 电脑网站支付快速接入：https://docs.open.alipay.com/270/105899/
  - API列表：https://docs.open.alipay.com/270/105900/
  - SDK文档：https://docs.open.alipay.com/270/106291/
  - Python支付宝SDK：https://github.com/fzlee/alipay/blob/master/README.zh-hans.md
    - SDK安装：pip install python-alipay-sdk --upgrade

- 电脑网站支付流程

  ![image-20190901193918155](day06.assets/image-20190901193918155.png)



-  配置RSA2公私钥
  - 商城私钥加密数据，商城公钥解密数据。

  - 支付宝私钥加密数据，支付宝公钥解密数据。

    ![image-20190901194438310](day06.assets/image-20190901194438310.png)

  - 生成商城公私钥

    ```python
    $ openssl
    $ OpenSSL> genrsa -out app_private_key.pem 2048  # 制作私钥RSA2
    $ OpenSSL> rsa -in app_private_key.pem -pubout -out app_public_key.pem # 导出公钥
    
    $ OpenSSL> exit
    ```

  - 配置商城公私钥

    - 配置商城私钥

      - 在根目录新建alipay文件夹用于存储公私钥。
      - 将制作的商城私钥`app_private_key.pem`拷贝到alipay文件夹中。

    - 配置商城公钥

      - 将`app_public_key.pem`文件中内容上传到支付宝。

        ![image-20190901194819062](day06.assets/image-20190901194819062.png)

    - 配置支付宝公钥
      - 将支付宝公钥内容拷贝到`alipay_public_key.pem`文件中。

      ![image-20190901194926147](day06.assets/image-20190901194926147.png)

      ```python
      -----BEGIN PUBLIC KEY-----
      支付宝公钥内容
      -----END PUBLIC KEY-----
      ```

    - 配置公私钥结束后

      ![image-20190901195049308](day06.assets/image-20190901195049308.png)

    

  - 后端接口实现

    ```python
    def pay(request):
        alipay = AliPay(
            appid='2016092700609211',
            app_notify_url=None,  # 默认回调url
            app_private_key_path=os.path.join(settings.BASE_DIR, "alipay/app_private_key.pem"),
            alipay_public_key_path=os.path.join(settings.BASE_DIR, "alipay/alipay_public_key.pem"),
            sign_type="RSA2",
            debug=True
        )
    
        # 生成登录支付宝连接
        order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no='订单号',
            total_amount='订单金额',
            subject='标题',
            return_url='同步回调地址',
        )
    
        alipay_url = 'https://openapi.alipaydev.com/gateway.do?' + order_string
        return redirect(alipay_url)
    ```

  - 同步回调地址验证

    - 注意：验证是否支付成功应该在异步回调接口验证，验证规则和同步的验证规则一样

      ```python
      def alipayback(request):
          query_dict = request.GET
          data = query_dict.dict()
      
          print(data)
          # 获取并从请求参数中剔除signature
          signature = data.pop('sign')
      
          # 创建支付宝支付对象
          alipay = AliPay(
              appid='2016092700609211',
              app_notify_url=None,  # 默认回调url
              app_private_key_path=os.path.join(settings.BASE_DIR, "alipay/app_private_key.pem"),
              alipay_public_key_path=os.path.join(settings.BASE_DIR, "alipay/alipay_public_key.pem"),
              sign_type="RSA2",
              debug=True
          )
          # 校验这个重定向是否是alipay重定向过来的
          success = alipay.verify(data, signature)
          if success:
              #	验证成功
              # 生成支付记录，改变订单状态
              print('yes')
              return render_json('yes')
          else:
            	# 验证失败
              print('no')
              return render_json('no')
      ```

      
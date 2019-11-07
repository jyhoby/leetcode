aiomysql，是一个异步的mysql连接器，就是把pymysql异步化了



```python
import asyncio
import aiomysql

loop = asyncio.get_event_loop()

async def test_example():
    conn = await aiomysql.connect(host='127.0.0.1',port=3306, user='root', password='root', db='mysql', loop=loop)

    cursor = await conn.cursor()

    await cursor.execute('select user,host from user')

    r = await cursor.fetchall()
    print(r)

    await cursor.close()

    conn.close()


loop.run_until_complete(test_example())
```



使用连接池

连接池类是对某一数据库所有连接的“缓冲池”，主要实现以下功能：①从连接池获取或创建可用连接；②使用完毕之后，把连接返还给连接池；③在系统关闭前，断开所有连接并释放连接占用的系统资源；④还能够处理无效连接（原来登记为可用的连接，由于某种原因不再可用，如超时，通讯问题），并能够限制连接池中的连接总数不低于某个预定值和不超过某个预定值。



```python
from aiomysql import create_pool


async def go():
    # 创建链接是耗时的 IO 操作
    async with create_pool(host='127.0.0.1', port=3306,
                           user='root', password='root',
                           db='message', charset="utf8") as pool:
        
        # acquire 也是涉及到 socket 的
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                # execute 是需要等待的
                await cur.execute("SELECT * from message")
                value = await cur.fetchone()
                print(value)
                # 从socket 中取数据 网络耗时 都是需要 await


if __name__ == "__main__":
    from tornado import ioloop
    # 这个 ioloop 是单例模式 我们使用 tornado 的 ioloop

    io_loop = ioloop.IOLoop.current()
    # 上面定义的是协程因此我们需要协程的调用方式
    io_loop.run_sync(go)
```



跟tornado 关联

settings:



```python
async def connect_mysql():

    return await aiomysql.connect(
        host='127.0.0.1',
        user='root',
        password='root',
        db='test'
    )



app_setting = {
    'debug':options.debug,
    "template_path":os.path.join(BASE_DIR, 'templates'),
    "static_path":os.path.join(BASE_DIR, 'static'),
    'mysql':tornado.ioloop.IOLoop.current().run_sync(connect_mysql)
}
```



views:



class IndexHandler(tornado.web.RequestHandler):
    async def get(self):

```python
    async with self.settings['mysql'].cursor() as cur:
        await cur.execute('select user()')

        res = await cur.fetchone()
        self.finish(json.dumps(res))
```
# Day02-Python操作MySQL

#### 1.连接MySQL

```python
import pymysql

# 连接mysql
# 参数1：表示主机或ip地址
# 参数2：表示mysql的用户名
# 参数3：表示mysql的密码
# 参数4：表示mysql的数据库名
# conn = pymysql.connect('localhost', 'root', 'root', 'mydb2')
conn = pymysql.connect('10.36.132.6', 'root', 'root', 'mydb2')
# 创建游标对象: 可以执行sql语句
cursor = conn.cursor()

# sql语句
sql = 'select version()'

# 执行sql语句
cursor.execute(sql)

res = cursor.fetchone()
print(res)

# 关闭游标对象
cursor.close()
# 关闭mysql的连接
conn.close()

```

#### 2.插入数据

```python
import pymysql

conn = pymysql.connect('localhost', 'root', 'root', 'mydb2')
cursor = conn.cursor()

# 插入数据
sql = 'insert into person(name, age) values("aa", 20)'

try:
    cursor.execute(sql)
    # 提交事务
    conn.commit()
except:
    # 回滚
    conn.rollback()

cursor.close()
conn.close()

```

#### 3. 删除数据

```python
import pymysql

conn = pymysql.connect('localhost', 'root', 'root', 'mydb2')
cursor = conn.cursor()

# 删除数据
sql = 'delete from person where id=18'

try:
    cursor.execute(sql)
    # 提交事务
    conn.commit()
except:
    # 回滚
    conn.rollback()

cursor.close()
conn.close()

```

#### 4. 更新数据

```python
import pymysql

conn = pymysql.connect('localhost', 'root', 'root', 'mydb2')
cursor = conn.cursor()

# 更新数据
sql = 'update person set age=30 where id=20'

try:
    cursor.execute(sql)
    # 提交事务
    conn.commit()
except:
    # 回滚
    conn.rollback()

cursor.close()
conn.close()

```

#### 5.查询数据

```python
import pymysql

conn = pymysql.connect('localhost', 'root', 'root', 'mydb2', charset='utf8')
cursor = conn.cursor()

# 查询数据
sql = 'select * from person'
# 执行sql
cursor.execute(sql)

# fetchone() : 每次查询下一条数据
# res = cursor.fetchone()
# print(res)
# res = cursor.fetchone()
# print(res)
# res = cursor.fetchone()
# print(res)

# fetchall() : 所有数据
res = cursor.fetchall()
# res = cursor.fetchmany(3)  # 前3条数据
for row in res:
    print(row)

print(cursor.rowcount)  # 总的数据条数

cursor.close()
conn.close()
```

 

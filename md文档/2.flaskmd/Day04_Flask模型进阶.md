# FlaskDay04

## 模型进阶

### 创建模型

```python
# 模型：类
class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True)
    age = db.Column(db.Integer, default=1)

```

##### 字段类型

| 类型名          | Python类型           | 说 明                             |
| ------------ | :----------------- | ------------------------------- |
| Integer      | int                | 普通整数, 一般是 32 位                  |
| SmallInteger | int                | 取值范围小的整数,一般是 16 位               |
| BigInteger   | int 或 long         | 不限制精度的整数                        |
| Float        | float              | 浮点数                             |
| Numeric      | decimal.Decimal    | 定点数                             |
| String       | str                | 变长字符串                           |
| Text         | str                | 变长字符串,对较长或不限长度的字符串做了优化          |
| Unicode      | unicode            | 变长 Unicode 字符串                  |
| UnicodeText  | unicode            | 变长 Unicode 字符串,对较长或不限长度的字符串做了优化 |
| Boolean      | bool               | 布尔值                             |
| Date         | datetime.date      | 日期                              |
| Time         | datetime.time      | 时间                              |
| DateTime     | datetime.datetime  | 日期和时间                           |
| Interval     | datetime.timedelta | 时间间隔                            |
| LargeBinary  | str                | 二进制文件                           |

##### 常用约束

| 选项名         | 说 明                                      |
| :---------- | :--------------------------------------- |
| primary_key | 如果设为 True ,这列就是表的主键                      |
| unique      | 如果设为 True ,这列不允许出现重复的值                   |
| index       | 如果设为 True ,为这列创建索引,提升查询效率                |
| nullable    | 如果设为 True ,这列允许使用空值;如果设为 False ,这列不允许使用空值 |
| default     | 为这列定义默认值                                 |

### 模型操作

#### 单表操作

```python
增加数据
	a. 一次增加一条数据:
        p = Person()    
        p.name = '小明'    
        p.age = 22

        try:
            db.session.add(p)
            db.session.commit()
        except:
            # 回滚
            db.session.rollback()
            db.session.flush()

	b. 一次添加多条数据
        persons = []
        for i in range(10,30):
            p = Person()
            p.name = '宝强' + str(i)
            p.age = i
            persons.append(p)
        db.session.add_all(persons)
        db.session.commit()

删除数据
	p = Person.query.first()  # 获取第一条数据
    db.session.delete(p)
    db.session.commit()
    
修改数据
    p = Person.query.first()
    p.age = 100
    db.session.commit()
        
查询数据
    过滤器
        filter()	把过滤器添加到原查询上,返回一个新查询
        filter_by()	把等值过滤器添加到原查询上,返回一个新查询
        limit()	  使用指定的值限制原查询返回的结果数量,返回一个新查询
        offset()	偏移原查询返回的结果,返回一个新查询
        order_by()	根据指定条件对原查询结果进行排序,返回一个新查询
        group_by()	根据指定条件对原查询结果进行分组,返回一个新查询

    常用查询
        all()	以列表形式返回查询的所有结果,返回列表
        first()	返回查询的第一个结果,如果没有结果,则返回 None
        first_or_404()	返回查询的第一个结果,如果没有结果,则终止请求,返回 404 错误响应
        get()	返回指定主键对应的行,如果没有对应的行,则返回 None
        get_or_404()	返回指定主键对应的行,如果没找到指定的主键,则终止请求,返回 404 错误响应
        count()	返回查询结果的数量
        paginate()	返回一个 Paginate 对象,它包含指定范围内的结果

        查询属性
            contains
            startswith
            endswith
            in_
            __gt__
            __ge__
            __lt__
            __le__


    逻辑运算
        与 and_
            filter(and_(条件),条件…)
        或 or_
            filter(or_(条件),条件…)
        非 not_
            filter(not_(条件),条件…)

    示例:   
     	查询:
            persons = Person.query.all()  # 获取所有
            persons = Person.query.filter(Person.age>22)

            # filter功能比filter_by强大
            persons = Person.query.filter(Person.age==22)  # filter(类.属性==值)
            persons = Person.query.filter_by(age=22) # filter_by(属性=值)

            persons = Person.query.filter(Person.age.__lt__(22)) # <
            persons = Person.query.filter(Person.age.__le__(22)) # <=
            persons = Person.query.filter(Person.age.__gt__(22)) # >
            persons = Person.query.filter(Person.age.__ge__(22)) # >=

            persons = Person.query.filter(Person.age.startswith('宝'))  # 开头匹配
            persons = Person.query.filter(Person.age.endswith('宝'))  # 结尾匹配
            persons = Person.query.filter(Person.age.contains('宝'))  # 包含
            persons = Person.query.filter(Person.age.in_([11,12,22]))  # in_

            persons = Person.query.filter(Person.age>=20, Person.age<30)  # and_
            persons = Person.query.filter(and_(Person.age>=20, Person.age<30))  # and_
            persons = Person.query.filter(or_(Person.age>=30, Person.age<20))  # or_
            persons = Person.query.filter(not_(Person.age<30))  # not_
        
        排序:
            persons = Person.query.limit(5)  # 取前5个
            persons = Person.query.order_by('age')  # 升序
            persons = Person.query.order_by('-age')  # 降序
            persons = Person.query.order_by(desc('age'))  # 降序
            persons = Person.query.offset(5)  # 跳过前5个
        
        分页:
            # 获取页码page和每页数量num
            page = int(request.args.get('page'))
            num = int(request.args.get('num'))

            # 手动做分页
            persons = Person.query.offset((page-1) * num).limit(num)

            # 使用paginate做分页
            persons = Person.query.paginate(page, num, False).items
       
        paginate对象的属性：
            items：返回当前页的内容列表
            has_next：是否还有下一页
            has_prev：是否还有上一页
            next(error_out=False)：返回下一页的Pagination对象
            prev(error_out=False)：返回上一页的Pagination对象
            page：当前页的页码（从1开始）
            pages：总页数
            per_page：每页显示的数量
            prev_num：上一页页码数
            next_num：下一页页码数
            query：返回创建该Pagination对象的查询对象
            total：查询返回的记录总数	
            
```

#### 多表关联

##### 一对多

```python
# 一对多
class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16))
    # 定义班级标的一对多关系，不是字段, Student为学生表模型， backref为反向查找名称
    students = db.relationship('Student', backref='grade1', lazy=True)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16))
    age = db.Column(db.Integer, default=1)
    # 创建外键,关联到班级表的主键，实现一对多关系，班级表中也要有对应操作
    grade = db.Column(db.Integer, db.ForeignKey(Grade.id))

    查: 
        # 获取学生的所在班级信息(反向)
		stu = Student.query.get(stuid)
    	grade = stu.stus
        
    	# 获取班级的所有学生 (正向)
        grade = Grade.query.get(gradeid)
        students = grade.students
	删:
            # 删除班级后， 学生的grade字段会变为null
            grade = Grade.query.get(id)
            db.session.delete(grade)
            db.session.commit()

```

##### 多对多

```python
用户收藏电影,一个用户可以收藏多部电影, 一部电影可以被不同的用户收藏, 是一个多对多关系.

# 中间表(不是模型)
collects = db.Table('collects',
    # user_id为表字段名称, user.id为外键表的id
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True)
) 

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16))
    age = db.Column(db.Integer, default=1)
    # 多对多  关联的学生表格的模型， 中间表的名称， 反向查找
    movies = db.relationship('Movie',  backref='users', secondary=collects, lazy='dynamic')
    
    lazy属性:
        懒加载,可以延迟在使用关联属性的时候才建立关联
    	lazy='dynamic': 会返回一个query对象(查询集)，可以继续使用其他查询方法，如all().
    	lazy='select': 首次访问到属性的时候，就会全部加载该属性的数据.
        lazy='joined': 在对关联的两个表进行join操作，从而获取到所有相关的对象
        lazy=True:  返回一个可用的列表对象,同select
	    
查：
	# 查询用户收藏的所有电影
	 user = User.query.get(id)
     movies = user.movies
        
	# 查询电影被哪些用户收藏
     movie = Movie.query.get(id)
     users = movie.users
    
删：
	# 中间表的数据会被级联删除
     movie = Movie.query.get(id)
     db.session.delete(movie)
     db.session.commit()
     
增：
	# 用户收藏电影
    user = User.query.get(id)
    movie = Movie.query.get(id)
    user.movies.append(movie)
    db.session.commit()

```



#### 作业:图书馆项目

```python
创建一个项目, 用来说明出版社, 书籍和作者的关系。
假定关系：作者：书籍 => 1:n  （一本书由一个作者完成， 一个作者可以创作多本书）
出版社：书籍 => n:n  （一个出版社可以出版多本书， 一本书可以由多个出版社出版）
要求:
	1.在书籍的book_index.html中有一个"查看所有书籍"的超链接按钮，点击进入书籍列表book_list.html页面.
	2.在书籍的book_list.html中显示所有书名，点击书名可以进入书籍详情book_detail.html
	3.在书籍book_detail.html中可以点击该书的作者和出版社，进入作者详情的author_detail.html和出版社详情的publisher_detail.html页面
	
	# 作者
    class Author(db.Model):
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        name = db.Column(db.String(20), unique=True)
        age = db.Column(db.Integer, default=1)
        sex = db.Column(db.Boolean, default=True)
        email = db.Column(db.String(200))
        # 关系
        books = db.relationship('Book', backref='my_auther', lazy='dynamic')

    # 书籍
    class Book(db.Model):
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        title = db.Column(db.String(100), unique=True)
        date = db.Column(db.DateTime)
        # 1对多，外键
        author = db.Column(db.Integer, db.ForeignKey(Author.id))

    # 中间表（书籍-出版社）
    book_publisher = db.Table('book_publisher',
        db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
        db.Column('publisher_id', db.Integer, db.ForeignKey('publisher.id'), primary_key=True)
    )

    # 出版社
    class Publisher(db.Model):
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        name = db.Column(db.String(20), unique=True)
        address = db.Column(db.String(200))
        city = db.Column(db.String(100))
        province = db.Column(db.String(100))
        country = db.Column(db.String(100))
        website = db.Column(db.String(100))
        # 多对多, 关联book表
        books = db.relationship('Book', backref='publishers', secondary=book_publisher, lazy='dynamic')
```
#### 读写文件

> 读写文件是最常见的IO操作,python内置了读写文件的函数,用法和c是兼容的.
>
> 读写文件前,我们必须了解一下,在磁盘上读写文件的功能都是由操作系统提供的,现代操作系统不允许普通的程序直接操作磁盘,所以读写文件就是请求操作系统打开一个文件对象(文件描述),然后,通过操作系统提供的接口从这个文件对象中读取数据(读文件),或者把数据写入这个文件对象(写文件)

#### 读文件

> 要以读文件的模式打开一个文件对象,使用python内置的open()函数,传入文件名和标识符:

```python
>>> f = open('/user/demo/test.txt','r')
```

> 标识符'r'表示读,这样,我们就成功地打开了一个文件
>
> 如果文件不存在,open()函数就会抛出一个IOError的错误,并且会给出详细的错误码和信息,告诉你文件不存在.

```python
>>> f=open('/Users/michael/notfound.txt', 'r')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '/Users/michael/notfound.txt'
```

> 如果文件打开成功,接下来,调用read()方法可以一次性读取文件的全部内容,python把内容读取到内存,用一个str对象表示

```python
>>> f.read()
'hello world!'
```

> 最后一步调用close()方法关闭文件,文件使用完毕之后必须关闭,因为文件对象会占用操作系统的资源,并且操作系统同一时间能打开的文件数量也是有限制的.

```python
>>> f.close()
```

> 由于文件读写都有可能产生IOError,一旦出错,后面的f.close()就不会调用,所以,为了保证文件是否执行出错都能够正确的关闭文件,我们可以使用try … finally来实现.

```python
try:
    f = open('/path/demo/file','r')
    print(f.read())
finally:
    if f:
        f.close()  
```

> 但是每次都这么写实在太繁琐,所以,引入了with语句来自动帮我们调用close()方法:

```python
with open('/path/demo/file', 'r')  as f:
    print(f.read())
```

> 这和前面的try...finally是一样的,但是代码更加简洁,并且不必调用f.close()方法.

> 注意: 使用read()会一次性读取文件的全部内容,如果你的文件特别大,比如说有5G,那么你的内存就爆了,所以,为了保险起见,我们可以反复调用read(size)方法,每次最多读取size个字节内容,另外调用readline()可以每次读取一行内容,调用readlines()一次性读取所有的内容,并按行返回list,因此,要根据需要决定怎么调用.
>
> 如果文件很小,read()一次读取最方便,如果不能确定文件大小,反复调用read(size)比较保险,如果是配置文件,调用readlines()最方便

```python
for line in f.readlines():
    #把末尾的'\n'删掉
    print(line.strip())
```

#### 二进制文件

> 前面讲的默认都是读取文本文件,并且是UTF-8编码的文本文件,要读取二进制文件,比如图片,视频等等,用'rb'模式打开文件即可:

```python
>>> f = open('/users/demo/test.jpg',"rb")
>>> f.read()
b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节
```

#### 字符编码

> 要读取非UTF-8编码的文本文件,需要给open()函数传入encoding参数,例如,读取GBK编码的文件:

```python
>>> f = open('/user/demo/gbk.txt','r',encoding = 'gbk')
>>> f.read()
'测试'
```

> 遇到有些编码不规范的文件,你可能遇到UnicodeDecodeError,因为在文本文件中可能夹杂了一些非法编码的字符,遇到这种情况,open()函数还接收一个error参数,表示如果遇到编码错误之后如何处理,最简单的办法就是直接忽略.

```python
>>> f = open('/users/demo/gbk.txt','r',encoding = 'gbk',errors = 'ignore')
```

#### 写文件

> 写文件和读文件都是一样的,唯一的区别就是调用open()函数时,传入标识符'w'或者'wb'表示写文件或写二进制文件:

```python
>>> f = open("/users/demo/test.txt",'w')
>>> f.write('hello, world!')
>>> f.close()
```

> 你可以反复调用write()来写入文件,但是务必要调用f.close()来关闭文件.
>
> 当我们写入文件时,操作系统往往不会立刻把数据写入磁盘,而是放到内存缓存起来,空闲的时候再慢慢写入,只有调用close()方法时,操作系统才保证把没有写入的数据全部写入磁盘,忘记调用close()的后果是数据可能只写了一部分到磁盘,剩余的丢失了,所以,还是使用with语句来的保险:

```python
with open('/users/demo/test.txt', 'w') as f:
    f.write('hello, world')
```

> 要写入特定编码的文本文件,请给open()函数传入encoding参数,将字符串自动转成指定编码.

> 以'w'模式写入文件时,如果文件已经存在,直接覆盖(相当于删掉后新写入一个文件),如果我们希望追加到文件的末尾怎么办?可以传入'a'以追加模式写入.

```python
with open('/users/demo/test.txt', 'a') as f:
    f.write('hello, world')
```

#### StringIO

> 很多时候,数据读写不一定是文件,也可以在内存读写.
>
> StringIO顾名思义就是在内存中读写str
>
> 要把str写入StringIO,我们需要先创建一个StringIO,然后,像文件一样写入即可:

```python
from io import StringIO
f = StringIO()
f.write("hello")
f.write("	")
f.write('world')
#获取写入后的str
print(f.getvalue())
```

> 要读取StringIO,可以用一个str初始化StringIO,然后,像读文件一样读取:

```python
from io import StringIO
f = StringIO("Hello\nHi\nGoodBye!")
while True:
    s = f.readline()
    if s == '':
        break
    print(s.trip())
#
Hello
Hi
Goodbye!
```

#### BytesIO

> StringIO操作的只能是str,如果要操作二进制数据,就需要使用BytesIO.
>
> BytesIO实现了在内存中读写bytes,我们创建一个BytesIO,然后写入一些bytes:

```python
from io import BytesIO
f = BytesIO()
f.write("中文".encode('utf-8'))
print(f.getvalue())
```

> 注意:写入的不是str,而是经过UTF-8编码的bytes
>
> 和StringIO类似,可以用一个bytes初始化BytesIO,然后,像读文件一样读取:

```python
from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()
b'\xe4\xb8\xad\xe6\x96\x87'
```

> StringIO和BytesIO是在内存中操作str和bytes的方法,使得读写文件具有一致的接口.

#### 序列化

> 在程序运行的过程中，所有的变量都是在内存中，比如定义一个dict

```python
dict1 = {name:"lili",age:18}
```

> 在这里我把name进行修改，改成”leilei“，但是一旦程序结束，变量所占用的内存就会被操作系统全部回收，如果没有把修改的name存到磁盘上，下次name初始化的时候又是”lili“

> 在这里我们把变量从内存中变成可存储或者传输的过程称之为序列化，在python中叫picking，序列化之后，我们就可以把序列化后的内容写入磁盘，或是通过网络传输到别的机器上。反之，把变量内容从序列化的对象重新读取到内存里称之为反序列化，即unpicking。

> python提供了pickle模块来实现序列化。

```python
import pickle
d = dict({name:"lili",age:18})
#pickle.dumps()方法把任意对象序列化成一个bytes，然后就可以把bytes写入文件
print(pickle.dumps(d))

#把序列化后的对象写入文件
f = open("dump.txt",'wb')
#参数一：要写入的对象， 参数二：写入文件的对象
pickle.dump(d,f)
f.close()

#从文件中读取序列化后的对象
f2 = open("dump.txt","rb")
#pickle.load()反序列化对象
d = pickle.load(f)
f.close()


```

> 注意：pickle只能用于python，并且不同版本的python彼此都不兼容，因此，只能用pickle保存一些不重要的数据，这样即使不能成功的反序列化也没什么关系。

#### Json

> 如果我们需要在不同的编程语言之间传递对象，那么我们必须把对象序列化成标准化格式，比如xml，但是更好的方法是json，因为json表现出来就是一个字符串，可以被所有的语言读取，也方便存储到磁盘或者网络传输，json不仅是标准模式，并且速度也比xml更快，还可以在web中读取，非常方便。

| JSON类型   | Python类型 |
| ---------- | ---------- |
| {} 对象    | dict       |
| [] 数组    | list       |
| "string"   | str        |
| 1234.56    | int或float |
| true/false | True/False |
| null       | None       |

> 把python的dict对象变成一个json

```python
import json

d = dict({name:"lili",age:19})
#使用json.dumps()方法返回一个str，这个str就是标准的json
print(json.dumps(d))

#把json反序列化为一个python对象
jsonStr = '{name:"lili",age:19}'
print(json.loads(jsonStr))
```

> 将一个class对象序列化为json

```python
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        
#将student对象转换为dict        
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }        
s = Student('Bob', 20, 88)
#参数一：要传入的对象  参数二：将对象转为dict的函数
json.dumps(s,default=student2dict)

#将dict转为对象
def dict2student(d):
    return Strdent(d['name'],d['age'],d['score'])
jsonStr ='{"age": 20, "score": 88, "name": "Bob"}'
#json反序列化为一个对象
#参数一：json字符串，参数二：dict转为对象的函数
print(json.loads(jsonStr,object_hook=dict2student))

```



#### 读写csv文件

##### 读csv文件

> csv文件本身就是个纯文本文件,这种文件格式经常用来作为不同程序之间的数据交互的格式.
>
> 演示:
>
> 需求:读取001.scv文件
>
> 说明:可以直接打印,然后定义list

```python
import csv

def readCsv(path):
    #列表
    infoList = []
    #以只读的形式打开文件
    with open(path, 'r')  as f:
        #读取文件的内容
        allFileInfo = csv.reader(f)
        #将获取到的内容逐行追加到列表中
        for row in allFileInfo:
            infoList.append(row)
    return infoList
path = r"C:\Users\xlg\Desktop\001.csv"
info = readCsv(path)
```

##### 写csv文件

演示:

需求:向002.csv文件中写入内容

```python
import csv

#以写的方式打开文件
def writeCsv(path,data)：
	with open(path,'w')  as f:
        writer = csv.writer(f)
        for rowData in data:
            print("rowData =", rowData)
            #按行写入
            writer.writerow(rowData)
path = r"C:\Users\xlg\Desktop\002.csv"
writeCsv(path,[[1,2,3],[4,5,6],[7,8,9]])       
```

##### 读取pdf文件

> pip是一个安装和管理python包的工具
>
> 在进行代码演示之前,首先进行安装和pdf相关的工具
>
> a.在cmd中输入以下命令: pip list [作用:列出pip下安装的所有的工具]
>
> b.安装pdfminer3k,继续输入以下命令:pip install pdfminer3k
>
> c.代码演示

```python
#导入系统库
import sys
import importlib
#对importlib做处理,让其加载sys
importlib.reload(sys)

from pdfminer.pdfparser import PDFParser,pdFDocument
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter#解释器
from pdfminer.converter import PDFPageAggregator#转换器
from pdfminer.layout import LTTextBoxHorizontal,LAParams #布局

from pdfminer.pdfinterp import PDFTextExtractionNotAllowed #是否允许pdf和text转换

#将path文件中的内容读取到topath文件中
def readPDF(path, toPath):
    #以二进制的形式打开pdf文件
    f = open(path, 'rb')
    #创建一个pdf文档分析器
    parser = PDFParser(f)
    #创建pdf文档
    pdfFile = PDFDocument()
    #获取连接分析器
    parser.set_document(pdfFile)
    #获取文档对象
    pdfFile.initialize()
    #检测文档是否提供txt转换
    if not pdfFile.is_extractable:
        #不允许转换
        raise PDFTextExtractionNotAllowed
    else:
        #解析数据
        #数据管理器
        manger = PDFResourceManger()
        #创建一个PDF设备对象
        laparams = PDFPageAggregator(manager,laparams=laparams)
        #解释器对象
        interpreter = PDFPageInterpreter(manger,device)
        #开始循环处理,每次处理一页
        for page in pdfFile.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if(isinstance(x, LTTextBoxHorizontal)):
                    with open(toPath, 'a') as f:
                        str1 = x.get_text()
                        #print(str)
                        f.writer(str1 + "\n")
path = r"C:\Users\xlg\Desktop\001.pdf"
toPath = r"C:\Users\xlg\Desktop\001.pdf"
readPDF(path,toPath)
```

#### 错误处理

> 在程序运行的过程中,如果发生了错误,可以事先约定一个错误代码,这样就可以知道是否有错,以及出错的原因,在操作系统的调用中,返回错误码的非常常见,比如打开文件的函数open,成功时返回文件的描述符[就是一个整数],出错时返回-1,但是使用错误码表示是否出错十分不方便,因为函数本身应该返回的正常结果与错误码混淆在一起,所以调用者要使用大量的代码来判断程序是否出错.

因此,在高级语言通常都内置了一套try...except...finally...错误处理机制,python也不例外.

```python
#try的机制
try:
    print("try...")
    r = 10/0
    print('result', r)
except ZeroDivisionError as e:
    print("except:", e)
finally:
    print("finally...")
print("END")   
```

> 当我们认为某些代码可能会出错时,就可以用try来运行这段代码,如果执行出错,则后续代码不会继续执行,而是直接跳转至错误处理代码,即except语句块,执行完except后,如果有finally语句块则执行finally语句块,至此,执行完毕.

> 从输入可以看到，当错误发生时，后续语句print('result', r)不会执行，except由于捕获到了ZeroDivisionError，因此被执行，最后finally语句被执行。



> 错误应该有很多种类，如果发生了不同类型的错误，应该由不同的except语句块处理，但其实python的错误也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其他的子类也一网打尽
>

> 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用。也就是说，我们不必再每个可能出错的地方都去捕获错误，只要在合适的层次去捕获错误就可以了，这样一来，就大大减少了try...except...finally的麻烦。



##### 调用栈

> 如果错误没有捕获,它就会一直向上抛,最后被python解释器捕获,打印一个错误信息,然后程序退出.

```python
def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s)*2

def main():
    bar('0')
main()
```

> 出错的时候，一定要分析错误的调用栈的信息，这样才能定位错误

#### 记录错误

> 如果不捕获错误，自然可以让python解释器来打印出错误堆栈，但是程序也被结束了，既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误的原因，同时让程序继续执行下去。

> python内置的logging模块可以非常容易的记录错误信息：

```python
import logging

def foo(s)：
	return 10/int(s)
def bar(s)
	return foo(s)*2

def mian():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
main()
print("END")       
```

> 同样是出错，但是程序打印完信息后会继续执行，并且正常退出

#### 抛出错误

> 因为错误是class，捕获一个错误就是捕获到该class的一个实例，因此，错误并不是凭空产生的，而是有意创建并抛出的，pyhton的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
>
> 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例。

```python
class  FooError(valueError)：
	pass
def foo(s)：
	n = int(s)
    if n == 0:
        raise FooError("invalid value :%s"%s)
    return 10/n
foo('0')
```

> 只有在必要的时候才定义我们自己的错误类型，如果可以选择python已有的内置的错误类型，尽量使用python内置的错误类型。


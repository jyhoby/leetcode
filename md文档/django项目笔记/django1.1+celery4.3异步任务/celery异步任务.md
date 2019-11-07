## 1.celery配置文件celery.py



django1.1是老版本，必须配合使用celery3.1版本一下的

celery4.3需要和django1.8以上版本使用



**该项目 是django1.1+ celery4.3配合使用，有警告，但至少定时任务和异步任务能够实现**



**在settings同级下创建celery.py**

![Snipaste_2019-07-27_11-29-13](.\Snipaste_2019-07-27_11-29-13.png)

```
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Moonbasa.settings')

app = Celery('Moonbasa')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

```

## 2.创建的app在init中加载

**init.py**

```
from __future__ import absolute_import, unicode_literals
import pymysql
from .celery import app as celery_app


pymysql.install_as_MySQLdb()
__all__ = ('celery_app')

```

## 3.在项目app下创建该app的任务文件tasks.py

```
from __future__ import absolute_import, unicode_literals
import time
from celery import shared_task
from celery import Celery
import requests

#创建异步任务
@shared_task
def send_sms(phone, vcode):
    print("后台生成的验证码vcode:", vcode)
    url = 'https://open.ucpaas.com/ol/sms/sendsms'

    data = {
        "sid": "621f475b64268d39631a97441de0fc82",
        "token": "4ea074e3ffff6603720c8893637294bb",
        "appid": "0ff18e2133fc40a6b54bfb5933b43b80",
        "templateid": "481975",  # 短信内容的模板
        "param": vcode,  # 验证码
        "mobile": phone,  # 接收验证码的手机号
    }

    response = requests.post(url, json=data)
    print(response.text)
    return response.text


@shared_task
def text():
    print('我是定时任务1')
    return "我是celery4.3"


@shared_task
def text2():
    print('我是定时任务2')
    return "我是celery4.3"

```

## 4.在settings下的配置

```
from celery.schedules import crontab
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/11' # redis作为中间件redis仓库11（可自己选择16个仓库中一个）
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/12' # 数据结果存储地址
from datetime import timedelta #导入时间模块做定时任务的计时

# 这里是定时任务的配置
CELERY_BEAT_SCHEDULE = {
    'task_method1': {  # 定时任务1随便起的名字
        'task': 'app.tasks.text',  # app 下的tasks.py文件中的方法名text
        'schedule': timedelta(seconds=3),  # 名字为task_method1的定时任务, 每3秒执行一次
    },
    'task_method2': {  # 定时任务2随便起的名字
        'task': 'app.tasks.text2',  # app 下的tasks.py文件中的方法名text
        'schedule': timedelta(seconds=4),  # 名字为task_method2的定时任务, 每4秒执行一次
    },
}
```

## 5.启动

1.启动worker（任务执行单元）

```
celery -A worker tasks -l info
```

celery.py放在worker文件夹下

```
celery -A Moonbasa worker --pool=solo -l info
```

**Moonbasa要修改为自己的项目名称**

2.另开一个Terminal窗口启动beat,将定时任务加入任务队列

```
celery -A Moonbasa beat -l info
```

**Moonbasa要修改为自己的项目名称**

启动worker后：

![Snipaste_2019-07-29_19-44-43](.\Snipaste_2019-07-29_19-44-43.png)

启动beat后：

![Snipaste_2019-07-29_19-46-26](.\Snipaste_2019-07-29_19-46-26.png)

执行异步任务查看打印信息，定时任务启动后会自动执行

![Snipaste_2019-07-29_19-49-15](.\Snipaste_2019-07-29_19-49-15.png)




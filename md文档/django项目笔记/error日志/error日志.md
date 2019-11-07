## 1.在工程目录下创建logs文件夹存放日志文件

![1564195718(1)](.\1564195718(1).jpg)

## 2.在logs文件夹下添加log.py文件

log.py:

```
import logging
from logging import handlers


# 设置日志格式
fmt = '%(asctime)s %(levelname)7.7s %(funcName)s: %(message)s'
formatter = logging.Formatter(fmt, datefmt="%Y-%m-%d %H:%M:%S")

# 设置 handler
handler = logging.handlers.TimedRotatingFileHandler('myapp.log', when='D', backupCount=30)
handler.setFormatter(formatter)

# 定义 logger 对象
logger = logging.getLogger("MyApp")
logger.addHandler(handler)
logger.setLevel(logging.INFO)

logger.info('这是Info日志级别')
# 2019-07-13 15:43:39    INFO <module>: 这是Info日志级别
logger.error('我是ERROR')

```

## 3.在settings里设置日志参数

```

# 日志配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    # 格式配置
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(module)s.%(funcName)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'verbose': {
            'format': ('%(asctime)s %(levelname)s [%(process)d-%(threadName)s] '
                    '%(module)s.%(funcName)s line %(lineno)d: %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S',
        }
    },
    # Handler 配置
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG' if DEBUG else 'WARNING'
        },
        'info': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            # 'filename': f'{BASE_DIR}/logs/info.log',  # 日志保存路径
            'filename': '%s/logs/info.log' % BASE_DIR,  # 日志保存路径
            'when': 'D',        # 每天切割日志
            'backupCount': 30,  # 日志保留 30 天
            'formatter': 'simple',
            'level': 'INFO',
        },
        'error': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': f'{BASE_DIR}/logs/error.log',  # 日志保存路径
            'when': 'W0',      # 每周一切割日志
            'backupCount': 4,  # 日志保留 4 周
            'formatter': 'verbose',
            'level': 'ERROR',
        }
    },
    # Logger 配置
    'loggers': {
        'django': {
            'handlers': ['console'],
        },
        'inf': {
            'handlers': ['info'],
            'propagate': True,
            'level': 'INFO',
        },
        'err': {
            'handlers': ['error'],
            'propagate': True,
            'level': 'ERROR',
        }
    }
}
```

## 4.在Middleware中间件文件夹里创建ErrorMiddleware.py用来存放错误日志代码

![1564195865(1)](.\1564195865(1).jpg)

```
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

import logging
err_logger = logging.getLogger('err')

# 捕获异常
class ErrorMiddleware(MiddlewareMixin):

    def process_exception(self, request, exception):
        ''' 自动捕获程序中所有异常 '''
        # print('Exception:')
        # print(exception)
        # print(type(exception))

        # 记录错误日志
        err_logger.error(exception)
```

**class ErrorMiddleware(MiddlewareMixin):中间件当遇到错误会自动执行，但是登录日志需要手动添加**



**在views.py添加登录日志，导入模块**

```
# 日志
import logging
inf_logger = logging.getLogger('inf')
```

在登录的视图函数里，登录成功后添加：

```
# 记录登录日志
inf_logger.info('id:%d,user:%s login' % (user_id, username))
```

这里我存了**用户id**和**用户名**两个登录信息
import os
from datetime import timedelta

from celery import Celery

from worker import config

# 加载django的环境
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swiper.settings")

# 实例化celery
celery_app = Celery('swiper')

# 加载配置文件
celery_app.config_from_object(config)

# 自动注册任务
celery_app.autodiscover_tasks()


celery_app.conf.update(   # 固定写法
    CELERYBEAT_SCHEDULE={ # 固定写法
        'sum-task': {  # 名字随便命名
            'task': 'common.func.add',  # 导入异步任务
            'schedule': timedelta(seconds=5), # 定时时间
            'args': (5, 6)  # 异步任务函数的参数
        }
    }
)

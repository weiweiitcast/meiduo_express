# encoding: utf-8
# Author: Timeashore

# celery
BROKER_URL = 'redis://192.168.203.151:6379/0'                 # 使用Redis作为消息代理
CELERY_RESULT_BACKEND = 'redis://192.168.203.151:6379/0'      # 把任务结果存在了Redis

CELERY_TIMEZONE='Asia/Shanghai'                         # 指定时区，默认是 UTC

CELERY_TASK_SERIALIZER = 'pickle'                       # 任务序列化和反序列化使用pickle方案
CELERY_RESULT_SERIALIZER = 'json'                       # 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24               # 任务过期时间，不建议直接写86400，应该让这样的magic数字表述更明显
CELERY_ACCEPT_CONTENT = ['json','pickle']               # 指定接受的内容类型

CELERY_IMPORTS = (                                  # 指定导入的任务模块
    'tasks'
)
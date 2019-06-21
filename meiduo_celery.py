from celery import Celery

app = Celery('task',   # 是当前模块的名称，这个参数是必须的，这样的话名称可以自动生成
             broker = "redis://192.168.203.151:6379/0",  # 中间人的地址
             backend = "redis://192.168.203.151:6379/1" # 结果数据存放地址
)


app.config_from_object('main')
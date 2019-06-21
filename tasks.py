from meiduo_express import MeiduoExp
from meiduo_celery import app

@app.task
def meiduo_cancle_order(data):
    return MeiduoExp.cancle_order(data)
from meiduo_express import cancle_order
from meiduo_celery import app

data = {
"ShipperCode": "UC",
"OrderCode": "TEST201209211045",
"ExpNo": "900008664480",
"CustomerName": "80238728",
"CustomerPwd": "c0bfe0ba86b66bae5426303c53db0a8b"
}

@app.task
def meiduo_cancle_order(data):
    return cancle_order(data)
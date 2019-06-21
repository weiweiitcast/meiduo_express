

from tasks import meiduo_cancle_order


data = {
"ShipperCode": "UC",
"OrderCode": "TEST201209211045",
"ExpNo": "900008664480",
"CustomerName": "80238728",
"CustomerPwd": "c0bfe0ba86b66bae5426303c53db0a8b"
}

import time

a = meiduo_cancle_order.delay(data)

if a.ready():
    print(a.get(timeout=1))
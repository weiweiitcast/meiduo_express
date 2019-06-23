

from meiduo_celery.express.tasks import meiduo_place_order
from meiduo_express import MeiduoExp

data = {'Sender': {'ExpAreaName': '青浦区', 'Address': '明珠路', 'Name': 'Taylor', 'Company': 'LV', 'ProvinceName': '上海', 'CityName': '上海市', 'Mobile': '15018442396'}, 'OrderCode': '20190406122652000000001', 'Receiver': {'ExpAreaName': '襄垣县', 'Name': 'python', 'Address': 'asdasd', 'ProvinceName': '山西省', 'Mobile': '13711111111', 'CityName': '长治市'}, 'Quantity': 1, 'Commodity': [{'Goodsquantity': 1, 'GoodsName': 'Apple iPhone 8 Plus (A1864) 256GB 深空灰色 移动联通电信4G手机'}], 'ExpType': 1, 'PayType': 1, 'ShipperCode': 'SF', 'IsReturnSignBill': 1}

print(MeiduoExp.place_order(data))

a = meiduo_place_order.delay(data)
print(a.task_id)
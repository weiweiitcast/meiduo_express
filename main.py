from meiduo_express import *

data = {
    "OrderCode": "012657018199", "ShipperCode": "SF", "PayType": 1,"ExpType": 1,
    "Cost": 1.0,
    "OtherCost": 1.0,
    "Sender": {
        "Name": "Taylor",
        "Mobile": "15018442396",
        "ProvinceName": "上海",
        "CityName": "上海市",
        "ExpAreaName": "青浦区",
        "Address": "明珠路"
    },
    "Receiver": {
        "Name": "Yann",
        "Mobile": "15018442396",
        "ProvinceName": "北京",
        "CityName": "北京市",
        "ExpAreaName": "朝阳区",
        "Address": "三里屯街道"
    },
    "Commodity": [
        {"GoodsName": "鞋子", "Goodsquantity": 1, "GoodsWeight": 1.0},
        {"GoodsName": "鞋子2", "Goodsquantity": 1, "GoodsWeight": 1.0},
    ],

    "Quantity": 1,
}

a = place_order(data)

print(a)
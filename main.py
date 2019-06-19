
from meiduo_express import meiduo_prompt_check,\
        meiduo_tracking_subscribe,\
        identify_logistic_code,\
        ordering_pick_up

from meiduo_express import ZHONG_TONG,SHUN_FENG


ordering_pick_up_request_data = {
                "OrderCode": "012657018199", "ShipperCode": "SF", "PayType": 1,
                "MonthCode": "1234567890", "ExpType": 1,
                "Cost": 1.0,
                "OtherCost": 1.0,
                "Sender": {
                        "Company": "LV", "Name": "Taylor", "Mobile": "15018442396", "ProvinceName": "上海","CityName": "上海市", "ExpAreaName": "青浦区", "Address": "明珠路"
                },
                "Receiver": {
                        "Company": "GCCUI", "Name": "Yann",
                        "Mobile": "15018442396", "ProvinceName": "北京", "CityName": "北京市", "ExpAreaName": "朝阳区", "Address": "三里屯街道"
                },
                "Commodity": [
                                {
                                        "GoodsName": "鞋子", "Goodsquantity": 1, "GoodsWeight": 1.0
                                } ],
                "AddService": [ {
                                        "Name": "COD",
                                        "Value": "1020",
                                        "CustomerID": "1234567890",
                                } ],
                "Weight": 1.0, "Quantity": 1, "Volume": 0.0, "Remark": "小心轻放"
}
print(ordering_pick_up(ordering_pick_up_request_data))

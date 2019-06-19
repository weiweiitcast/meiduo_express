
from .meiduo_express import MeiduoExpress
from .dkniao_express.exp_company_abbr import *


__all__ = ["meiduo_prompt_check", "meiduo_tracking_subscribe", "identify_logistic_code"]



# 初始化单例对象
__meiduo_exp = MeiduoExpress()


# 即时查询接口
def meiduo_prompt_check(request_data):
    """
    查询快递信息
    :param request_data:
    {
        "OrderCode": 订单号,
        "ShipperCode": 快递公司代码,
        "LogisticCode": 运单号,
    }
    """
    return __meiduo_exp.prompt_check(request_data)


# 轨迹订阅接口
def meiduo_tracking_subscribe(request_data):
    """
    订阅物流轨迹
    :param request_data:
    {
            "ShipperCode": 快递公司代码,
            "LogisticCode": 运单号,
            "Receiver": {
                "Name": 收件人姓名,
                "Tel": 收件人手机,
                "Mobile": 收件人电话,
                "ProvinceName": 省,
                "CityName": 市,
                "ExpAreaName": 区/县(具体名称中不要缺少"区"或"县"),
                "Address": 详细地址
            },
            "Sender": {
                "Name": sender_name,
                "Tel": sender_tel,
                "Mobile": sender_mobile,
                "ProvinceName": sender_province,
                "CityName": sender_city,
                "ExpAreaName": sender_area,
                "Address": sender_detail_addr
            }
    }
    :return:
    """
    return __meiduo_exp.tracking_subscribe(request_data)


# 识别快递单所属公司
def identify_logistic_code(request_data):
    """
    用户识别快递单所属快递公司
    :param request_data:
    {
        "LogisticCode": "3967950525457"
    }
    """
    return __meiduo_exp.identify_logistic_code(request_data)


# 预约取件
def ordering_pick_up(request):
    """
    预约取件
    :param request:
    :return:
    """
    return __meiduo_exp.ordering_pick_up(request)
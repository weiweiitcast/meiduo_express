
from .meiduo_express import MeiduoExpress
from .dkniao_express.exp_company_abbr import *

# 初始化单例对象
__meiduo_exp = MeiduoExpress()


# 即时查询
def prompt_check(request_data):
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


# 轨迹订阅
def tracking_subscribe(request_data):
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


# 单号识别
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
def ordering_pick_up(request_data):
    """
    预约取件
    请求报文中不能出现字符：' " # & + < > % \
    :param request:
    {
        "ShipperCode": 快递公司代码,
        "OrderCode": 订单编号(自定义，不可重复)
        "PayType": 运费支付方式(1-现付，2-到付，3-月结，4-第三方付(仅 SF 支持))
        "ExpType": 详细快递类型
        "Receiver": {
            "Name": 收件人姓名,
            "Tel": 收件人手机,
            "Mobile": 收件人电话,
            "ProvinceName": 省,
            "CityName": 市,
            "ExpAreaName": 区/县(具体名称中不要缺少"区"或"县"),
            "Address": 详细地址,
            "PostCode": 收件地邮编(ShipperCode为EMS、YZPY、YZBK 时必填)
        },
        "Sender": {
            "Name": 发件人姓名,
            "Tel": 发件人手机,
            "Mobile": 发件人电话,
            "ProvinceName": 省,
            "CityName": 市,
            "ExpAreaName": 区/县(具体名称中不要缺少"区"或"县"),
            "Address": 详细地址,
            "PostCode": 发件地邮编(ShipperCode为EMS、YZPY、YZBK 时必填)
        },
        "Quantity": 包裹数，一个包裹对应一个运单号，如果是大于1个包裹，返回则按照子母件的方式返回母运单号和子运单号
        "PackingType": 包装类型，(快运字段)默认为 0; 0-纸，1-纤，2-木，3-托膜，4-木托，99-其他
        "DeliveryMethod": 送货方式(快运字段)默认为 0; 0-自提，1-送货上门(不含上楼)， 2-送货上楼
    }
    :return:
    """

    return __meiduo_exp.ordering_pick_up(request_data)


# 取消预约取件
def cancle_ordering_pick_up(request_data):
    """
    取消预约订单
    :param request:
    {
        "OrderCode": 订单号,
        "ShipperCode": 快递公司代码,
        "LogisticCode": 运单号,
    }
    :return:
    """

    return __meiduo_exp.cancle_ordering_pick_up(request_data)


# 下单
def place_order(request_data):
    """
    下单
    请求报文中不能出现字符：' " # & + < > % \
    自动订阅
    订单编号 OrderCode 可自定义，不可重复
    :param request_data:
    {
        "ShipperCode": 快递公司编码，
        "OrderCode": 订单编号(自定义，不可重复)
        "PayType": 运费支付方式, 1-现付，2-到付，3-月结，4-第三方付(仅SF支持)
        "ExpType": 快递类型,默认为1-标准快递
        "Receiver": {
            "Name": 收件人姓名,
            "Tel": 收件人手机,
            "Mobile": 收件人电话,
            "ProvinceName": 省,
            "CityName": 市,
            "ExpAreaName": 区/县(具体名称中不要缺少"区"或"县"),
            "Address": 详细地址,
            "PostCode": 收件地邮编(ShipperCode为EMS、YZPY、YZBK 时必填)
        },
        "Sender": {
            "Name": 发件人姓名,
            "Tel": 发件人手机,
            "Mobile": 发件人电话,
            "ProvinceName": 省,
            "CityName": 市,
            "ExpAreaName": 区/县(具体名称中不要缺少"区"或"县"),
            "Address": 详细地址,
            "PostCode": 发件地邮编(ShipperCode为EMS、YZPY、YZBK 时必填)
        },
        "Quantity": 包裹数，一个包裹对应一个运单号，如果是大于1个包裹，返回则按照子母件的方式返回母运单号和子运单号
        "Commodity": [
                { "GoodsName": 商品名称 }
                ...
        ]
    }
    :return:
    """

    return __meiduo_exp.place_order(request_data)


# 取消下单
def cancle_order(request_data):
    """
    取消下单，电子面单
    :param request_data:
    {
        "ShipperCode": 快递公司编码
        "OrderCode": 订单编号
        "ExpNo": 快递单号
        "CustomerName": 电子面单客户号
        "CustomerPwd": 电子面单密码
    }
    :return:
    """

    return __meiduo_exp.cancle_order(request_data)
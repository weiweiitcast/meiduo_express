
import json,hashlib,base64,urllib,abc,requests

from .api_settings import KDNIAO_GLOBAL_SETTINGS,DATA_TYPE,KDNIAO_URL
from .request_type import *
from .exceptions import RequiredDataMissing


class DKNiaoExpress(metaclass=abc.ABCMeta):
    __key_value = KDNIAO_GLOBAL_SETTINGS.get("KEY_VALUE")
    __ebusiness_id = KDNIAO_GLOBAL_SETTINGS.get("EBUSINESS_ID")
    __char_set = KDNIAO_GLOBAL_SETTINGS.get("CHAR_SET")

    def __init__(self):

        assert self.__key_value, "please set KEY_VALUE in global setting"
        assert self.__ebusiness_id, "please set EBUSINESS_ID in global setting"
        assert self.__char_set, "please set CHAR_SET in global setting"

        self.__data_type = DATA_TYPE.get("json")
        self.__request_data = {}
        self.__request_type = None

        # 沙箱调试url，生还环境需要在调用接口时指明
        self.__url = KDNIAO_URL

    @property
    def char_set(self):
        return self.__char_set

    @property
    def url(self):
        """请求url，默认为沙箱调试url"""
        return self.__url

    @url.setter
    def url(self, request_url):
        """生产环境，设置具体请求url"""
        self.__url = request_url

    @property
    def request_data(self):
        return self.__request_data

    @request_data.setter
    def request_data(self, request_data):
        self.__request_data = request_data

    @property
    def __json_request_data(self):
        """
        获取查询信息json数据
        :param kwargs: 字典数据，快递查询信息
        :return: 序列化成json数据返回
        """
        return json.dumps(self.__request_data)

    @property
    def __datasign(self):
        return self.__get_datasign()

    def __get_datasign(self):
        # 拼接加密数据: 物流查询信息json格式+keyvalue
        msg = (self.__json_request_data + self.__key_value)

        # md5加密
        md5_str = hashlib.md5(
            msg.encode(encoding=self.__char_set)
        ).hexdigest()

        # URL_Base64编码
        datasign = base64.urlsafe_b64encode(
            md5_str.encode(encoding=self.__char_set)
        ).decode()

        return datasign

    @property
    def __form_params(self):
        return urllib.parse.urlencode({
            "EBusinessID": self.__ebusiness_id,
            "RequestType": self.__request_type,
            "DataType": self.__data_type,
            "RequestData": self.__json_request_data,
            "DataSign": self.__datasign
        })

    @property
    def __http_request_header(self):
        return {
            "Accept": "*/*",
            "Connection": "Keep-Alive",
            "Accept-Charset": "utf-8",
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
        }

    @property
    def request_type(self):
        return self.__request_type

    @request_type.setter
    def request_type(self, request_type):
        self.__request_type = request_type

    def __send_request(self):
        response = requests.post(self.url,
                                 data=self.__form_params,
                                 headers=self.__http_request_header)
        return json.loads(response.content.decode(encoding=self.char_set))

    def send_request(self, request_data):
        assert self.__request_type, "必须指明该请求的接口指令！例如：self.request_type=PROMPT_CHECK"
        assert self.url, "必须指明该请求的url！例如：self.url=PROMTE_CHECK_URL 或 apisetting.KDNIAO_URL设置沙盒url"
        self.request_data = request_data
        return self.__send_request()




    @abc.abstractmethod
    def prompt_check(self, *args, **kwargs):
        """即时查询"""
        pass

    @abc.abstractmethod
    def tracking_subscribe(self, *args, **kwargs):
        """轨迹订阅"""
        pass

    @abc.abstractmethod
    def identify_logistic_code(self, *args, **kwargs):
        """订单识别"""
        pass

    @abc.abstractmethod
    def ordering_pick_up(self, *args, **kwargs):
        """预约取件"""
        pass

    @abc.abstractmethod
    def cancle_ordering_pick_up(self, *args, **kwargs):
        """取消预约取件"""
        pass

    @abc.abstractmethod
    def place_order(self, *args, **kwargs):
        """下发物流订单"""
        pass

    @abc.abstractmethod
    def cancle_order(self, *args, **kwargs):
        """取消物流订单"""
        pass
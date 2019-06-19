
"""
定义快递鸟各类请求接口，用于具体的生产环境
"""

# 即时查询
PROMTE_CHECK_URL = "http://api.kdniao.com/Ebusiness/EbusinessOrderHandle.aspx"

# 单号识别
IDENTIFY_LOGISTICCODE_URL = PROMTE_CHECK_URL

# 轨迹订阅
TRACKINNG_SUBSCRIBE_URL = "http://api.kdniao.com/api/dist"

# 预约取件
ORDERING_PICKUP_URL = "http://api.kdniao.com/api/OOrderService"


from .meiduo_express import MeiduoExpress
from .dkniao_express.exp_company_abbr import *

# 初始化单例对象
MeiduoExp = MeiduoExpress()


__all__ = ['MeiduoExp']
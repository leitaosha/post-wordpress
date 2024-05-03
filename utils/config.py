# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/19
from utils.myLog import log_to_file

try:
    from private_settings import *
except ImportError:
    from settings import *

log = log_to_file()
# log = log_to_file(log_console=True)

# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/19
import utils.util as util


try:
    from private_settings import *
except ImportError:
    from settings import *

# root path of project
BASE_PROJECT_PATH = util.getRootPath()

# The following settings cannot be modified！！！
# 以下内容不可修改！！！
AUTHORIZATION = (USERNAME, PASSWORD)
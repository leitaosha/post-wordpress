# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/5/2

def check_params(yaml_dict: dict) -> dict:
    if "wp" not in yaml_dict:
        yaml_dict['wp'] = {}
    return yaml_dict

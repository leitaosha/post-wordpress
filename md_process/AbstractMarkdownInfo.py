# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/19

from abc import ABC, abstractmethod


class AbstractMarkdownInfo(ABC):
    def __init__(self):
        # yaml信息
        self.title = None
        self.tags = None
        # 初始化yaml和content
        self.md_content = None
        self.md_yaml = None

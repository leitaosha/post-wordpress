# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/19

from md_process.MarkdownParse import MarkdownInfo
from abc import ABC, abstractmethod


class MDProcessor(ABC):
    def __init__(self, markdown: MarkdownInfo):
        self.markdown = markdown

    @abstractmethod
    def preprocess(self):
        pass

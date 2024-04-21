# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/19

from md_processors.WPMarkdown import WPMarkdown
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor


class MDProcessor(ABC):
    def __init__(self, markdown: WPMarkdown, thread_pool_executor: ThreadPoolExecutor):
        self.markdown = markdown
        self.thread_pool_executor = thread_pool_executor

    @abstractmethod
    def preprocess(self):
        pass

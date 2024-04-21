# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/19
from concurrent.futures import ThreadPoolExecutor

from md_processors.AbstractMDProcessor import MDProcessor
from md_processors.WPMarkdown import WPMarkdown


class AttachmentProcessor(MDProcessor):

    def __init__(self, markdown: WPMarkdown, thread_pool_executor: ThreadPoolExecutor):
        super().__init__(markdown, thread_pool_executor)

    # attachment process
    def preprocess(self):
        pass
    # TODO

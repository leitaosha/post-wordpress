# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/21
from concurrent.futures import ThreadPoolExecutor

from md_processors.AbstractMDProcessor import MDProcessor
from md_processors.WPMarkdown import WPMarkdown


class ContentProcessor(MDProcessor):

    def __init__(self, markdown: WPMarkdown, thread_pool_executor: ThreadPoolExecutor):
        super().__init__(markdown, thread_pool_executor)

    def preprocess(self):
        """
        do not convert content
        :return:
        """
        self.markdown.wp.content = self.markdown.md_content
        return

    def convertHtml(self):
        pass

    def convertAttachments(self):
        pass

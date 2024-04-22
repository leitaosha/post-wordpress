# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/21
from concurrent.futures import ThreadPoolExecutor

from markdown import markdown
from markdown.extensions.codehilite import CodeHiliteExtension

from md_processors.AbstractMDProcessor import MDProcessor
from md_processors.CustomMDExtensions import HighLightExtension
from md_processors.WPMarkdown import WPMarkdown


class ContentProcessor(MDProcessor):

    def __init__(self, wp_markdown: WPMarkdown, thread_pool_executor: ThreadPoolExecutor):
        super().__init__(wp_markdown, thread_pool_executor)
        self.Extensions = [HighLightExtension(),
                           'markdown.extensions.extra',
                           'markdown.extensions.codehilite', #代码高亮扩展
                           'markdown.extensions.toc',
                           'markdown.extensions.tables',
                           'markdown.extensions.fenced_code',
                           ]

    def preprocess(self):
        """
        do not convert content
        :return:
        """
        self.markdown.wp.content = self.convertHtml()
        self.markdown.wp.title = self.markdown.title
        self.markdown.wp.excerpt = self.markdown.excerpt
        return

    def convertAttachments(self):
        pass

    def convertHtml(self):
        htmlText = markdown(self.markdown.md_content, extensions=self.Extensions)
        return htmlText

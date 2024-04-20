# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/19

from md_process.MDProcessor import MDProcessor
from md_process.MarkdownParse import MarkdownInfo


class AttachmentProcessor(MDProcessor):

    def __init__(self, markdown: MarkdownInfo):
        super().__init__(markdown)

    # attachment process
    def preprocess(self):
        pass
    # TODO

# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/22
from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagInlineProcessor


class HighLightExtension(Extension):
    """
    Highlight ==(content)==
    """

    def extendMarkdown(self, md):
        md.inlinePatterns.register(SimpleTagInlineProcessor(r'()==(.*?)==', 'mark'), 'mark', 175)




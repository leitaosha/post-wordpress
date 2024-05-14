# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/22
from markdown.inlinepatterns import SimpleTagInlineProcessor
from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension
import xml.etree.ElementTree as etree


class HighLightExtension(Extension):
    """
    Highlight ==(content)==
    """

    def extendMarkdown(self, md):
        md.inlinePatterns.register(SimpleTagInlineProcessor(r'()==(.*?)==', 'mark'), 'mark', 175)


class CustomInlineProcessor(InlineProcessor):
    def __init__(self, tagName, pattern, md):
        super().__init__(pattern)
        self.tagName = tagName
        self.md = md

    def handleMatch(self, m, data):
        el = etree.Element(f'{self.tagName}')
        el.text = m.group(1)
        return el, m.start(0), m.end(0)


class SupExtension(Extension):
    def extendMarkdown(self, md):
        DEL_PATTERN = r'(?<!\$)\^(.*?)\^(?!.*?\$)'
        md.inlinePatterns.register(CustomInlineProcessor('sup', DEL_PATTERN, md), 'sup', 175)


class SubExtension(Extension):
    def extendMarkdown(self, md):
        DEL_PATTERN = r'(?<!\$)\~(.*?)\~(?!.*?\$)'
        md.inlinePatterns.register(CustomInlineProcessor('sub', DEL_PATTERN, md), 'sub', 175)

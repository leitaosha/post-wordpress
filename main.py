# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/18
import time
from concurrent.futures import ThreadPoolExecutor

from md_processors.WPMarkdown import getMarkdown
from md_processors import md_process
from posts.tag import Tag
from concurrent.futures import as_completed


mdPath = r'E:\Project\PythonProject\postWordpress\测试.md'
# 原生md
md = getMarkdown(mdPath)
# 处理md
md2 = md_process.process(md)
# print(md.wp)
# starttime = time.time()

# endtime = time.time()
# print(md.wp.tags, md.wp.categories)
# print(md2.wp)
# print(endtime-starttime)

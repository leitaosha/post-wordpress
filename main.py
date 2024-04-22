# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/18
import time
from concurrent.futures import ThreadPoolExecutor

from md_processors.WPMarkdown import getMarkdown
from md_processors import md_process
from md_processors.md_process import process
from posts.tag import Tag
from concurrent.futures import as_completed


mdPath = r'E:\笔记\博客\分享\实用工具\推荐一款Win版流畅、便捷、好看的快速启动器—DawnLauncher.md'
# 原生md
md = getMarkdown(mdPath)
# 处理md
md2 = process(md)
print(md2.wp)
print(md2.wp.create())


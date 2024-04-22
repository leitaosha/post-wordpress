# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/19
import os.path
import sys
import time

import frontmatter

from error.CustomeError import CustomError
from md_processors.WPMarkdown import getMarkdown
from md_processors.md_process import process

from urllib.parse import unquote

def ob_push_wp(mdPath):
    # 原生md
    mdOrigin = getMarkdown(mdPath)
    mdOrigin2 = mdOrigin
    clearConsole()
    try:
        console("# 这里将暂时作为控制台")
        console("## 正在推送中...")
        # 处理md
        mdProcessed = process(mdOrigin)
        # markdown推送
        post = mdProcessed.wp
        text = post.create()
        if text.status:
            console("## 推送成功")
        else:
            console("## 推送失败")
            raise CustomError('## 推送失败')
        console("### " + text.msg)
        console("## 即将返回...")
        backNum()
        # 获取返回数据
        new_attributes = {
            'id': post.id,
            "link": unquote(post.link),
        }
        # 仅修改wp字段
        mdOrigin.post.metadata['wp'].update(new_attributes) if 'wp' in mdOrigin.post.metadata else ''
        # 写入markdown
        with open(mdPath, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(mdOrigin.post))
    except Exception as e:
        console(e.__str__())
        console('出错了，不要担心，文档不会丢失！！')
        backNum()
        # 写入markdown
        with open(mdPath, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(mdOrigin2.post))


def console(msg: str):
    with open(MD_PATH, 'a', encoding='utf-8') as f:
        f.write(msg + "\n\n")


def clearConsole():
    with open(MD_PATH, 'w', encoding='utf-8') as f:
        f.write('')


def backNum():
    for i in range(3):
        time.sleep(1)
        console(f'## {3 - i}')
    time.sleep(1)


if __name__ == '__main__':
    MD_PATH = sys.argv[1]
    # MD_PATH = r'E:\笔记\博客\分享\实用工具\测试推送.md'
    if os.path.exists(MD_PATH):
        ob_push_wp(MD_PATH)

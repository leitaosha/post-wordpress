# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/19
import sys

import frontmatter
from frontmatter.default_handlers import YAMLHandler
from markdownInfo import MarkdownInfo


def ob_push_wp():
    path = sys.argv[1]
    post = frontmatter.load(path, handler=YAMLHandler())
    markdown = MarkdownInfo(post)
    # markdown预处理
    markdownProcess = markdown

    # markdown推送

    # 获取返回数据
    new_attributes = {}

    # 写入markdown
    post.metadata.update(new_attributes)
    updated_content = frontmatter.dumps(post)
    print(updated_content)
    with open(path, 'w') as f:
        f.write(updated_content)
    return "hello"


if __name__ == '__main__':
    ob_push_wp()

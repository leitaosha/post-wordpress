# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/18
import frontmatter
from frontmatter.default_handlers import YAMLHandler


def updateMarkdownYaml(path, new_attributes):
    path = r'E:\笔记\博客\未命名.md'
    post = frontmatter.load(path, handler=YAMLHandler())
    post.metadata.update(new_attributes)
    updated_content = frontmatter.dumps(post)
    with open(path, 'w') as f:
        f.write(updated_content)
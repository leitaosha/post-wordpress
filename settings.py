# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/20


# Your account of WordPress REST API.
# 你的wordpress账户
USERNAME = ''
PASSWORD = ''
WORDPRESS_SITE = ''

# Post Default Options
# 推送默认设置
WP_OPTIONS = {
    # article status in wordpress : draft(suggest), publish(suggest), private, future, pending
    # 文章发布状态
    'status': 'publish',

    # article comment status in WordPress : open, closed
    # 文章的是否可以评论
    'comment_status': 'open',

    # Whether to pin this article to the top
    # 置顶文章
    'sticky': 'false',

    # 是否可以ping（建议不做更改）
    'ping_status': 'closed',

    # 文章形式
    'format': 'standard',
}

# Markdown process.
# Markdown 处理

# Whether to handle text highlighting in Obsidian
# 是否处理Obsidian中的文本高亮
# eg: "==content==" ---> "<mark>content</mark>"
HIGH_LIGHT_TEXT = True

# In development
# HIGH_LIGHT_CODE = True
# CONVERT_ATTACHMENTS = True


# Thread Pool，When you have a lot of local images or labels, you can modify this value appropriately.
# 线程池，当你有较多的本地图片或标签时，可适当修改该值
THREAD_POOL_MAX_WORKER = 8


# The following settings cannot be modified！！！
# 以下内容不可修改！！！
AUTHORIZATION = (USERNAME, PASSWORD)



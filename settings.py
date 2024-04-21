# -*- coding UTF-8 -*-
# python 3.11
# Author: leitaosha
# Email: 473153250@qq.com
# CreateTime: 2024/4/20


# User
USERNAME = ''
PASSWORD = ''
WORDPRESS_SITE = ''

# Post Default Options
WP_OPTIONS = {'status': 'publish',
              # article status in wordpress : draft(suggest), publish(suggest), future, pending, private
              'comment_status': 'open',
              'slug': '',
              'sticky': 'false',
              }

# Markdown process
CONVERT_TO_HTML = False

# Attachment process
CONVERT_ATTACHMENTS = True

# ELSE
AUTHORIZATION = (USERNAME, PASSWORD)
THREAD_POOL_MAX_WORKER = 5

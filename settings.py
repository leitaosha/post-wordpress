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
              # article comment status in wordpress : open, closed
              'sticky': 'false',
              # Whether to pin this article to the top
              'ping_status': 'closed',
              'format': 'standard',
              }

# Markdown process.
HIGH_LIGHT_TEXT = True  # Convert "==content==" to "<mark>content</mark>"

# In development
# HIGH_LIGHT_CODE = True
# CONVERT_ATTACHMENTS = True


# ELSE
AUTHORIZATION = (USERNAME, PASSWORD)

# Thread Pool
THREAD_POOL_MAX_WORKER = 8

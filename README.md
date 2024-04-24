# Introduction

[![GitHub Repo stars](https://img.shields.io/github/stars/leitaosha/post-wordpress?label=⭐post-wordpress)](https://github.com/leitaosha/post-wordpress)  [![License](https://img.shields.io/github/license/leitaosha/post-wordpress?label=🧾License)](https://github.com/leitaosha/post-wordpress/LICENSE)     ![Download](https://img.shields.io/github/downloads/leitaosha/post-wordpress/total?label=⏬Download)

This is a python project that works with [Obsidian](https://obsidian.md/) to push Markdown to [WordPress](https://wordpress.com/). Specifically, it works with the [Templater](https://github.com/SilentVoid13/Templater) plugin. 
 ![](https://s2.loli.net/2024/04/23/GrRa5p8BeC9j4KL.gif)

# Schedule  
  
 - [x] Parsing Markdown   
 - [x] Push Markdown to WordPress  (If your article don't have any local attachments. It can push now)
 - [x] Custom settings  
 - [ ] Upload attachments
 - [ ] User parameter verification
 - [ ] Optimize some details
  
# Usage  
  
## 1. Install required programs.
### Python

The python3.11 used during the development of this project, it is recommended to use this version.  
  
If you don't know how to install python and add environment path. Please see this [documents]().  

### WordPress plugin - WordPress REST API Authentication

1. Add plug-in -  `WordPress REST API Authentication` in your WordPress.  ![](https://s2.loli.net/2024/04/23/1WXLUgPyTBnDe4u.png)

2. Open the plug-in and follow the prompts to create a **BASIC AUTHENTICATION.** ![](https://s2.loli.net/2024/04/23/x8KGhLWyUpVXmMv.png)
### Install Templater in obsidian 

Install **Templater** plugin in third-party community. ![](https://s2.loli.net/2024/04/23/Cv3f2jsAWQUJxIB.png)


## 2. Clone and Edit Config 

### Download

`git clone https://github.com/leitaosha/post-wordpress.git` （Recommend）

or

Download source code. [Click to download](https://github.com/leitaosha/post-wordpress/archive/refs/heads/master.zip)

Enter the project root directory and execute `pip install -r requirements.txt`

### Edit Config  

1. Open the root directory of the project and edit `settings.py`。It is highly recommended that you create a copy of `settings.py` and name it `private_settings.py`. Then edit `private_settings.py` for protecting your password.
2. Set up **Templater** plug-in to run python scripts. You need `python.exe` path, `push_wp.py` path and a template, see [push wp template](./doc/push wp template.md). 
	- Put the `push wp template.md` into the template folder. ![](https://s2.loli.net/2024/04/23/i2y3a1trhLqbvdX.png)
	- Add a function named `pushWordpress`, add command as follows:![](https://s2.loli.net/2024/04/23/lucdXVorhNbkG75.png)
	```cmd
	<your python path> <path of push_wp.py> <% tp.file.path() %>
	```

	For example:
	```cmd
	E:\venv\Scripts\python.exe E:\postWordpress\push_wp.py <% tp.file.path() %>
	```


#### Required  Parameters
  
```python  
# Your BASIC AUTHENTICATION.  
# 你的 BASIC AUTHENTICATION  
USERNAME = ''  
PASSWORD = ''  
WORDPRESS_SITE = ''  
```  

#### Optional Parameters

```python
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
```

#### Markdown frontmatter 

`title`, `categories`, and `tags` need to be written separately under the first-level fields, and other setting fields are placed in the `wp` field.

Settings in markdown file take precedence over `settings.py`

Example: 

```yaml
---
title: # your article title
tags: 
 - tag1
categories: # which categories of WordPress you want to push
  - category1
excerpt: # excerpt or abstract
wp:
 status: publish
 slug: # For friendly links, pure English numbers and underlines are recommended.
 # there are many params, please see https://developer.wordpress.org/rest-api/reference/posts/ ....
---

```
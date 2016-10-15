#!/usr/bin/python
#-*- coding:utf-8 –*-
from bs4 import BeautifulSoup
import urllib2

html_doc =  """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title1 title2"><b>The Dormouse's story</b></p>
<p class="story1">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story1">...</p>
"""

#Python对象: Tag , NavigableString , BeautifulSoup , Comment .

soup = BeautifulSoup(html_doc)
#soup = BeautifulSoup(open("index.html"))
#soup = BeautifulSoup(urllib2.urlopen("http://www.baidu.html/s"))

print(soup.prettify())
# 格式化之后的全文
print(soup.title)
# 标题 <title>The Dormouse's story</title>
print(soup.title.name)
# 标题标签名 u'title'
print(soup.title.string)
# 标题字段 u'The Dormouse's story'
print(soup.title.parent.name)
# 标题的父标签名 u'head'
print(soup.p)
# 第一个<p> <p class="title1 title2"><b>The Dormouse's story</b></p>
print(soup.p['class'])
# 以数组形式输出第一个<p>的所有class名 
# [u'title1',u'title2']
print(soup.find_all('a'))
# 以数组形式输出所有<a>
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
print(soup.find(id="link3"))
# 符合条件的完整标签 <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
for link in soup.find_all('a'):
    print(link.get('href'))
    print(link.contents[0])
# 文档中所有<a>的href值（超链接）+ 字段
    # http://example.com/elsie
    # Elisie
    # http://example.com/lacie
    # Lacie
    # http://example.com/tillie
    # Tillie
print(soup.get_text())
# 文档中所有文字信息
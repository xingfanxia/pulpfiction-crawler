#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-25 23:03:20
# @Author  : Xingfan Xia (xiax@carleton.edu)
# @Link    : http://xiax.tech
# @Version : $Id$

import os, re, time, urllib2, urllib, sys, requests
from easygui import *
from cookielib import CookieJar
from lxml import html, etree
reload(sys) 
sys.setdefaultencoding('utf-8')

cookies = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

def bookLookup(key):
	query = urllib.urlencode( {'q' : key } )
	url = "http://www.google.com/search?" + query
	print url
	source = opener.open(url).read()
	doc = html.fromstring(source)
	book_url = doc.cssselect(".r>a")[0].attrib['href']
	match = re.findall(r'\d*\b\.htm\b', book_url)
	if match:
		bookNumber = match[0][:-4]
		return bookNumber
	return None

if __name__ == '__main__':
	book_ls = []
	# book_ls = ["绝世唐门", "庆余年", "英雄志", "完美世界", "极品公子", "诛仙", "亵渎", "紫川", "佣兵天下", "新宋", "流氓高手", "流氓仙厨"]
	while True:
		bookname = raw_input("Please enter a bookname to add it to download list, enter a q to finish adding: \n")
		# bookname = enterbox(u"输入书名加入下载列表，输入q停止输入开始下载")
		if bookname == 'q':
			break		
		book_ls.append(unicode(bookname, "utf-8"))
	for book in book_ls:
		book_NO = bookLookup("site:bxwx8.org {name}全文完整版txt".format(name=book))
		if book_NO:
			download_url = "http://txt.bxwxtxt.com/packdown/fulltxt/{cat}/{no}.txt".format(cat = book_NO[:-3], no = book_NO)
			if not os.path.exists("downloads"):
				os.makedirs("downloads") 
			urllib.urlretrieve(download_url, u"downloads/{name}.txt".format(name=book))
			print u"{name} downloaded!".format(name="book")
		else:
			print "book not found"

	print "Download finished!"
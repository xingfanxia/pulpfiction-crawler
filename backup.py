#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-25 23:03:20
# @Author  : Xingfan Xia (xiax@carleton.edu)
# @Link    : http://xiax.tech
# @Version : $Id$



from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time, sys, os, getopt, argparse, urllib, re, urllib2

def bookLookup(keyword):
	url = "https://www.google.com/search?q=" + keyword
	driver = webdriver.Firefox()
	driver.get(url)
	time.sleep(3)
	try:
		result = driver.find_element_by_css_selector(".r>a")
		book_url = result.get_attribute('href')
		re1='.*?'	# Non-greedy match on filler
		re2='\\d+'	# Uninteresting: int
		re3='.*?'	# Non-greedy match on filler
		re4='\\d+'	# Uninteresting: int
		re5='.*?'	# Non-greedy match on filler
		re6='(\\d+)'	# Integer Number 1
		rg = re.compile(re1+re2+re3+re4+re5+re6,re.IGNORECASE|re.DOTALL)
		m = rg.search(book_url)
		if m:
			int1=m.group(1)
			print int1
		driver.quit()
	except:
		print "can't find element"
		driver.quit()
if __name__ == '__main__':
	bookLookup("site:bxwx8.org 斗罗大陆")
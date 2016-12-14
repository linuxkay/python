#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
from lxml import html
import requests
page = requests.get('http://www.eboshi.co.jp/')
tree = html.fromstring(page.content)
info = tree.xpath('//span[@class="gondora01"]/text()')
for i in info:
	    print "Eboshi Ski", i.encode(page.encoding)

#!/usr/bin/env/python
## objective is to scrape table from a website and save it as csv file
##reference http://qiita.com/kitsuyui/items/4906bb457af4d0e2d0a5
# -*- coding: utf-8 -*-
import pandas as pd
urlString = "http://typhoon.yahoo.co.jp/weather/jp/earthquake/list/?sort=1&key=1&b=15001"
import lxml.html as LH
result = pd.io.LH.read_html(urlString)

print (result)

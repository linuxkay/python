#!/usr/bin/env/python
## objective to scrape table from a website and save it as csv file
##reference http://qiita.com/kitsuyui/items/4906bb457af4d0e2d0a5
import pandas
url = 'http://typhoon.yahoo.co.jp/weather/jp/earthquake/list/?sort=1&key=1&b=15001'
fetched_dataframes = pandas.io.html.read_html(url)
fetched_dataframes[0]
fetched_dataframes[0].to_csv('apollo.csv')

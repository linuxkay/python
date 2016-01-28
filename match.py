#!/usr/local/env/python
import re
import os
file = open('word.txt', 'r')

for line in file.readlines():
    if re.search('^findsomemotion$', line, re.I):
          os.system('vlc "http://192.168.11.4/cgi-bin/hi3510/snap.cgi?&-getstream"') 

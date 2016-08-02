#!/usr/bin/env python
#  -*- coding:utf-8 -*-
# File http_post.py

import urllib
import urllib2
import json

# HTTP GET: access token
def http_get():
    # public test account
    # temporary
    # ticket = 'gQFj8ToAAAAAAAAAASxodHRwOi8vd2VpeGluLnFxLmNvbS9xLzAwUlZlQzNsNlppUWltdGQ1MnBXAAIEk2igVwMEgDoJAA=='

    # eternal
    ticket = 'gQFf7zoAAAAAAAAAASxodHRwOi8vd2VpeGluLnFxLmNvbS9xL3FFVGdkRTNsYnBnWG54SmpVbWhXAAIEXHagVwMEAAAAAA=='
    # ticket = 'gQFf7zoAAAAAAAAAASxodHRwOi8vd2VpeGluLnFxLmNvbS9xL3FFVGdkRTNsYnBnWG54SmpVbWhXAAIEXHagVwMEAAAAAA=='

    # eternal string

    params = urllib.urlencode({'ticket': ticket})
    f = urllib.urlopen("https://mp.weixin.qq.com/cgi-bin/showqrcode?%s" % params)
    return f.read()

# resp = http_post()
resp = http_get()
print resp
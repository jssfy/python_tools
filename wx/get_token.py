#!/usr/bin/env python
#  -*- coding:utf-8 -*-
# File http_post.py

import urllib
import urllib2
import json

# HTTP GET: access token
def http_get():
    # public test account
    appid = 'wxc0f1b124629429c4'
    secret = 'da83a792f6df9fb0ee695e4a3335e542'
    params = urllib.urlencode({'grant_type': 'client_credential', 'appid': appid, 'secret': secret})
    f = urllib.urlopen("https://api.weixin.qq.com/cgi-bin/token?%s" % params)
    return f.read()


# resp = http_post()
resp = http_get()
print resp
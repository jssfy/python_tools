#!/usr/bin/env python
#  -*- coding:utf-8 -*-
# File http_post.py

import urllib
import urllib2
import json

# HTTP POST: qrcode
def http_post():
    at = 'RQdT3CyCHDfu6I8bD4-e1TcuCibiNL0Iy1YK7ME0E-z4uezzptbMM-Dr0l7ffwS7dLABcG7O_67cf7BU1TIFXmsMYFsFi5VM-xNluUwmpW-W7CFgFzbfTqZ2K13e-ZkHYHIjACAUDE'
    url = 'https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=' + at
    # to get temporary ticket
    # values = {"expire_seconds": 604800, "action_name": "QR_SCENE", "action_info": {"scene": {"scene_id": 123}}}

    # to get eternal ticket
    # values = {"action_name": "QR_LIMIT_SCENE", "action_info": {"scene": {"scene_id": 321}}}
    # to get string form eternal qrcode
    values = {"action_name": "QR_LIMIT_STR_SCENE", "action_info": {"scene": {"scene_str": "kidd"}}}

    jdata = json.dumps(values)             # 对数据进行JSON格式化编码
    req = urllib2.Request(url, jdata)       # 生成页面请求的完整数据
    response = urllib2.urlopen(req)       # 发送页面请求
    return response.read()                    # 获取服务器返回的页面信息

resp = http_post()
print resp
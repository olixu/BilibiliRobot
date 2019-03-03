#coding:utf-8
import urllib
import urllib.request
import http.cookiejar
import json
import time
import os
import sys
import datetime
import time
import var_set
import random

cookie = var_set.cookie
roomid = var_set.roomid
csrf_token = var_set.csrf_token

#发送弹幕函数，通过post完成，具体可以自行使用浏览器，进入审查元素，监控network选项卡研究
def send_dm(s):
    global cookie
    global roomid
    global dm_lock
    global csrf_token

    try:
        url = "https://api.live.bilibili.com/msg/send"
        postdata =urllib.parse.urlencode({
        'color':'16777215',
        'fontsize':'25',
        'mode':'1',
        'msg':s,
        'rnd':str(int(time.time())),
        'roomid':roomid,
        'csrf_token':csrf_token,
        'csrf':csrf_token
        }).encode('utf-8')
        header = {
        "Accept":"application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding":"utf-8",
        "Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
        "Connection":"keep-alive",
        "Cookie":cookie,
        "Host":"api.live.bilibili.com",
        "Referer":"http://live.bilibili.com/"+roomid,
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 Vivaldi/2.2.1388.37"
        }
        req = urllib.request.Request(url,postdata,header)
        dm_result = json.loads(urllib.request.urlopen(req,timeout=3).read().decode('utf-8'))
        if len(dm_result['msg']) > 0:
            print('[error]弹幕发送失败：'+s)
            print(dm_result)
        else:
            print('[log]发送弹幕：'+s)
    except Exception as e:
        print('[error]send dm error')
        print(e)
    time.sleep(1.5)

def send_dm_long(s):
    n=var_set.dm_size
    for i in range(0, len(s), n):
        send_dm(s[i:i+n])
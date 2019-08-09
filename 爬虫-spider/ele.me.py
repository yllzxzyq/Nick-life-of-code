# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 20:10:12 2019

@author: yllzxzyq
"""

import requests as re
from bs4 import BeautifulSoup
import json

def GetHtml(url):
    try:
        mycookie={'utrace':'4dcb75b0c1bf8ea969230e499787ae7c_2019-04-09',
                  'cna':'QHkzFdRzdgkCAdrFmT4oHQVK',
                  'eleme__ele_me':'ce8c98ac83120a5c38a69eb4b69b75b9:86eb6e05c2d975bd692c662d531f63d18ba17da9',
                  'isg':'BA8PVt2hj6pi-YtWmg3746-rnaMTsU4-TZOdaSEcZ36F8CvyOwfrp7vh9uBrkzvO',
                  'pizza73686f7070696e67':'CPuz42fVoxnRVcVQ1x33fSZUPyvQ5O36IWBpRTDKLLJiy6zJ74G-A7ivujLSOUau',
                  'SID':'skJEaBKJPxdI2tRHKjKEe9K074mOanmpfy2A',
                  'track_id':'1554811735|089ef2e642a72fe2a2bf36198f8cfd92d73351009eb6393f1b|a28990fe799f198c19f9536501d86028',
                  'ubt_ssid':'ujx7kvy2wjw4wm3d0o59168pgjdjkbff_2019-04-09',
                  'USERID':'233155727',
                  'UTUSER':'233155727'}
        kv={'Host':'www.ele.me',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www.ele.me/place/wt3mdmd32t3t?latitude=30.528503&longitude=114.359803',
            'x-shard': 'loc=114.359803,30.528503',
            'Connection':'keep-alive'}
        r=re.get(url,headers=kv,cookies=mycookie)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

url="https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=wt3mdmd32t3t&latitude=30.528503&limit=24&longitude=114.359803&offset=24&terminal=web"
d=GetHtml(url)
print(d)
Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
>>> kv={'wd':'python'}
>>> r=requests.get("http://www.baidu.com/s",params=kv)
>>> r.status_code
200
>>> r.request.url
'http://www.baidu.com/s?wd=python'
>>> len(r.text)
457351
>>> 

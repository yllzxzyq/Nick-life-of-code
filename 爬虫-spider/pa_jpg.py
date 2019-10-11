Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
>>> import os
>>> url="http://img0.dili360.com/pic/2019/02/26/5c74d8ef1514c3783316499.jpg"
>>> root="D://pics//"
>>> path=root+url.split('/')[-1]
>>> try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r=requests.get(url)
		with open(path,'wb') as f:
			f.write(r.content)
			f.close()
			print("文件保存成功")
	else:
		print("文件保存失败")
except:
	print("爬取失败")

	
344009
文件保存成功
>>> 

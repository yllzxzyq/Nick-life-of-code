import requests
import bs4
from bs4 import BeautifulSoup
import re
import os

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def getimgURL(html):
    soup = BeautifulSoup(html , "html.parser")
    adlist=[]
    for i in soup.find_all("img"):
        try:
            ad= re.findall(r'.*src="(.*?)?" .*',str(i))
            if ad :
                adlist.append(ad)
        except:
            continue
    return adlist

def download(adlist):
    root="C:\\Users\yllzxzyq\Desktop\图片\\"
    for i in range(len(adlist)):
        l=re.findall(r'.*=(.*)',adlist[i][0])[0]
        path=root+str(i)+"."+l
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r=requests.get(adlist[i][0])
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()

def main():
    url = 'https://mp.weixin.qq.com/s?__biz=MzIzODA0MjQ4Mw==&mid=2660510707&idx=1&sn=109d344f4e3f08171a948ed68d4ff3cd&chksm=f25fe7efc5286ef96ffa31e4a7649aec5f87b9736218de15217c26b679354d4a9e9ad6cbb6cd&scene=0&xtrack=1&key=423b110d1f6c9d41944865a4e8f28c2de7e6af54e4817f74a6ce8e4493fb0c7a93193cd6f32f98c9c19290255559514c76032dbe7fd5f25302fb34777bf05b8555335062e0f2e002a219568647765b57&ascene=1&uin=MzE2NTMzNzc1OA%3D%3D&devicetype=Windows+10&version=62060739&lang=zh_CN&pass_ticket=pAmsqK%2BPBeCYcfWtNWhnL5d3VDzpBrJSm6Vy9G67seYpe%2FGc5267%2F9SnT5ZX7rZe'
    html=getHTMLText(url)
    list=getimgURL(html)
    download(list)

main()
    

import requests
from bs4 import BeautifulSoup
import re
import os

#获取网页信息
header = {'Host': 'seat.lib.whu.edu.cn',
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0',
          'Accept': 'application/json, text/javascript, */*; q=0.01',
          'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
          'Accept-Encoding': 'gzip, deflate, br',
          'Referer': 'https://seat.lib.whu.edu.cn//simpleCaptcha/chCaptcha',
          'X-Requested-With': 'XMLHttpRequest',
          'Connection': 'keep-alive',
          'Cookie': 'JSESSIONID=3FD23C8DCBF9F4627B759F392FEFC336'}
def getHTMLText(url):
    try:
        r=requests.get(url,headers = header,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

#解析网页，获取所有图片url
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

#新建文件夹pic，下载并保存爬取的图片信息
def download(adlist):
    #注意更改文件目录
    root="C:\\Users\yllzxzyq\Desktop\图片\\"
    for i in range(len(adlist)):
        path=root+str(i)+"."+'gif'
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r=requests.get(adlist[i][0])
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()

def main():
    url = 'https://mp.weixin.qq.com/s/iX-6WDd21W4k21MDp0RYDA'
    html=getHTMLText(url)
    list=getimgURL(html)
    download(list)
main()
    

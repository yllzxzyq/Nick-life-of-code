import requests
import re

#爬取网页数据并解码得到文本
def getHTML(url):
    try:
        kv={'user-agent':'Mozilla/5.0'}
        r=requests.get(url,headers=kv,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

#将网页文本按正则表达式查找得到书名和价格并存入列表ilt
def parsePage(ilt, html):
    try:
        plt= re.findall(r'price="(\d.*)"',html)
        tlt= re.findall(r'alt="<b>(.*)</b>(.*)" error="0"',html)
        for i in range(len(plt)):
            ilt.append([plt[i],tlt[i][0]+tlt[i][1]])
    except:
        return ""

#遍历列表，逐行打印
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count = count+1 
        print(tplt.format(count,g[0],g[1]))
        
def main():
    depth = 3
    start_url= 'http://search.kongfz.com/product_result/?key=%E6%B5%8B%E7%BB%98&status=0&_stpmt=eyJzZWFyY2hfdHlwZSI6ImFjdGl2ZSJ9&pagenum='
    infoList=[]
    for i in range(1,depth):
        try:
            url= start_url+str(i)
            html = getHTML(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)

main()

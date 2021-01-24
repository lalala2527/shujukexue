import urllib.request as ur
import re
from bs4 import BeautifulSoup

def saveFile(name,text):
    path="F:\\爬虫\\新闻资料_四阶段\\"
    rstr=r"[\/\\\:\*\?\"\<\>|]"
    name=re.sub(rstr,"_",name)
    path=path+name
    try:
        with open(path,'wb')as f:
            f.write(text.encode('utf8'))
            print("保存成功")
    except Exception as e:
        print("保存失败",e)

        
url='https://www.baidu.com/s?ie=utf-8&medium=0&rtt=1&bsst=1&rsv_dl=news_b_pn&cl=2&wd=%E6%9C%89%E5%BA%8F%E5%A4%8D%E5%B7%A5&tn=news&rsv_bp=1&rsv_sug3=7&rsv_sug1=2&rsv_sug7=100&oq=&rsv_sug2=\
0&rsv_btype=t&f=8&inputT=879&rsv_sug4=1878&x_bfe_rqs=03E80&x_bfe_tjscore=0.000000&tngroupname=organic_news&newVideo=12&pn='
num=190
proxy_support=ur.ProxyHandler({'http':'120.229.11.39:80'})
opener=ur.build_opener(proxy_support)
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0')]
for i in range(1,17):
    response=opener.open(url+str(num))
    html=response.read().decode('utf-8')
    soup=BeautifulSoup(html,'html.parser')
    num=num-10*i
    i+1
    for link in soup.find_all('a'):  
        if("有序复工"in link.text):
            print(link.text,'\n')
            name=str(link.text)+'.txt'
            try:
                url2=link.get('href')
                opener=ur.build_opener(proxy_support)
                opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0')]
                response=opener.open(url2,timeout=1)
                html=response.read().decode('utf-8')
                soup=BeautifulSoup(html,'html.parser')
                try:
                    content=soup.find("div",class_="article-content").text
                    #print(content,'\n')
                    text=str(content)
                    saveFile(name,text)
                except:
                    print("内容打开失败\n")
                        
            except:
                print("网页加载超时\n")

import urllib.request as ur
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def saveFile(name,text):
    path="F:\\爬虫\\新闻资料_四阶段_荔枝\\"
    rstr=r"[\/\\\:\*\?\"\<\>|]"
    name=re.sub(rstr,"_",name)
    path=path+name
    try:
        with open(path,'wb')as f:
            f.write(text.encode('utf8'))
            print("保存成功")
    except Exception as e:
        print("保存失败",e)

driver= webdriver.Chrome()
url='https://so.jstv.com/?keyword=%E5%A4%8D%E5%B7%A5&page='
num=273
proxy_support=ur.ProxyHandler({'http':'120.229.11.39:80'})
opener=ur.build_opener(proxy_support)
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0')]
for i in range(1,24):
    response=opener.open(url+str(num))
    html=response.read().decode('utf-8')
    soup=BeautifulSoup(html,'html.parser')
    num=num-i
    i+1
    
    for link in soup.find_all('a'):  
        if("复工"in link.text):
            print(link.text,'\n')
            name=str(link.text)+'.txt'
                       
            try:
                url2=link.get('href')
                driver.get(url2)
                soup=BeautifulSoup(driver.page_source,'html.parser')
                try:
                    content=""
                    for c in soup.find_all('p',class_=""):
                      if(str(c.find_all('a'))!="[]"):
                           break
                      content+=str(c.text)
                      content+='\n'
                            
                    #print(content,'\n')
                    text=str(content)
                    saveFile(name,text)
                except:
                    print("内容打开失败\n")
                        
            except:
                print("网页加载超时\n")
            

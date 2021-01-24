import urllib.request as ur
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def saveFile(name,text):
    path="F:\\爬虫\\一阶段评论\\4\\"
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
url='https://weibo.com/2656274875/InjmYsLSS?filter=hot&root_comment_id=0&type=comment#_rnd1608645321782'
driver.get(url)
num=1
proxy_support=ur.ProxyHandler({'http':'120.229.11.39:80'})
opener=ur.build_opener(proxy_support)
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0')]

soup=BeautifulSoup(driver.page_source,'html.parser')
for a in soup.find_all("div",class_="WB_text"):
	for i in range(2,6):
		try:
			if(a.contents[i].find('a')):
				b=str(a.contents[i])
				c=b.replace("：","")
				d=c.replace("等人","")
				e=d.replace("\n","")
				e=re.sub(" ","",e)
				if(e!=""):
					print(e)
					name=str(num)+".txt"
					num=num+1
					saveFile(name,str(e))
		except:
			print("超范围")

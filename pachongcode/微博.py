import requests
import re
import time
def get_one_page(url):#请求函数：获取某一网页上的所有内容
    headers = {
    'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0t',
    'Host' : 'weibo.cn',
    'Accept' : 'application/json, text/plain, */*',
    'Accept-Language' : 'zh-CN,zh;q=0.9',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Cookie' : 'SUB=_2A25NDT_sDeThGeNM6FEW-CjLyDqIHXVuDkGkrDV6PUJbktANLXTkkW1NTj_QKV-vu5RbdPf5FzI9P_KEfufUtL-U; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5T0Zu7sBCSmgzjD-X8qkjT5NHD95Qfeoe0S0ncS0ecWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNSKz0e0MRSoM0Sntt; SSOLoginState=1611222971; _T_WM=9cf87eed2d6541270bda146c507ac37e',
    'DNT' : '1',
    'Connection' : 'keep-alive'
     }#请求头的书写，包括User-agent,Cookie等
    response = requests.get(url,headers = headers,verify=False)#利用requests.get命令获取网页html
    if response.status_code == 200:#状态为200即为爬取成功
        return response.text#返回值为html文档，传入到解析函数当中
    return None
def parse_one_page(html):#解析html并存入到文档result.txt中
    pattern = re.compile('<span class="ctt">.*?</span>', re.S)
    items = re.findall(pattern,html)
    result = str(items)
    with open('test.txt','a',encoding='utf-8') as fp:
        fp.write(result)

for i in range(2,23):
    url ="https://weibo.cn/comment/IqvWOciIr?uid=2656274875&rl=1&page="+str(i)
    html = get_one_page(url)
    #print(html)
    print('正在爬取第 %d 页评论' % (i))
    parse_one_page(html)
    time.sleep(1)

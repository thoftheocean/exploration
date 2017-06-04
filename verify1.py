#coding：utf-8

import sys
reload(sys)  
sys.setdefaultencoding('utf-8')  
 
import requests as rqs
import urllib2
from HTMLParser import HTMLParser
import lxml.html
 
ORG_URL = 'http://jw.tsu.edu.cn'
 
class MyHtmlParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.imgurl = 'http://jw.tsu.edu.cn'
         
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            if len(attrs) == 0:
                pass
            else:
                for (attr, value) in attrs:
                    if attr == 'id':
                        dic = dict(attrs)
                        self.imgurl = dic['src']
                     
 
 
def SaveToFile(filename, content):
    f = open(filename, 'w+')
    try:
        f.write(content)
    except Exception, e:
        print Exception,":", e
    f.close()
 
 
 
if __name__ == '__main__':
 
    postdata = {
        'Sel_Type': 'STU',
        'UserID': '2011070102',
        'PassWord': '070102',
        'cCode': ''
    }
 
    hds = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36'
    }
    cookies = {
    }
 
    post_url = 'http://jw.tsu.edu.cn/_data/home_login.aspx'
 
    s = rqs.Session()
    rsps = rqs.get(post_url) #不用session，发送get请求，得到响应对象
 
    parser = MyHtmlParser()
    parser.feed(rsps.text)
    parser.close()
    img_url = ORG_URL + parser.imgurl.strip('.') #从html代码中解析出验证码的url
    with open('cCode.jpg', 'wb') as f:
        f.write(s.get(img_url).content) #获取验证码图片
     
    cCode = raw_input("please input cCode:") #输入验证码
    postdata['cCode'] = cCode
 
    #print postdata
    rsps = s.post(post_url, data=postdata, headers=hds)#登陆
 
 
    print rsps.content # 显示登陆失败
     
    SaveToFile('content.html', rsps.content)
    print rsps.url
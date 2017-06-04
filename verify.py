#coding:utf-8


# #生成验证码
# from PIL import Image
# from PIL import ImageFilter
# from PIL import ImageFont  #设置字体
# from PIL import ImageDraw
# import random
#
# width = 80
# height = 40
# font = ImageFont.truetype('C:\\Windows\\Fonts\\AdobeFangsongStd-Regular.otf', 28)  #ImageFont.truetype()是选择字体
# image = Image.new("RGB",(width,height),(0,0,0))  #Image.new新建一张背景为白色的rgb图片
# draw = ImageDraw.Draw(image)
# for t in range(4):
#     draw.text((20*t,10),`random.randint(0,9)`,font=font,fill=(255,255,255))
# image.show()

import requests
url='https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=other&rand=sjrand&0.04580597826870303'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
req=requests.get(url=url,headers=headers,verify=False)
with open('code.jpg','wb')as f:
    f.write(req.content)

vurl='https://kyfw.12306.cn/otn/passcodeNew/checkRandCodeAnsyn'


data={
    'randCode':'BkbF',
    'rand':'sjrand'
}

req=requests.post(url=vurl,data=data,verify=False)

print req.content


#coding:utf-8
# from selenium import webdriver
#
# browser = webdriver.PhantomJS(executable_path="D:\HXprogram\python2.7\Scripts\phantomjs.exe")
# browser.maximize_window()
# browser.get("http://www.baidu.com")
#
# data=browser.find_element_by_id("s_top_wrap").text
#
# # browser.save_screenshot('screenshot.png')
# browser.get_screenshot_as_file('screenshot-%s.png')
# print browser.page_source
# # browser.find_element_by_id("su").click()
# print data
# browser.quit()


#
# import datetime
# import time
# print datetime.datetime.now()
# print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# print time.time()

# str1="j1Rqsf6cWukSCxcz1ox%2ByGwprmwk9iZ5zMy2Qioeo7Bk02xkmm6Jsdk8q1Sd58%2BKrTX9tKTB59GE%0A22CJwdB8m69jdau%2FRoP%2Fq7wxaRwYLMHTD1RBYc6tYXOJux70fB%2B%2FxUBckbwOV0i7AcY72Z%2FoTlPA%0AQfcCJa6vVoZcO9xkXkmo2u5BGHFeng7MRd%2BvMzcWKAjLqjCieBINLqhlc%2BgmmwveJq%2F0usbEXjyl%0AB%2Fs1Wsd1QCSE|预订|240000G1010C|G101|VNP|AOH|VNP|AOH|06:44|12:38|05:54|Y|PXohtXocHqmyhGNj3M%2FI%2Bs4YVSkSJ%2Ba1Q3qidCaNvf5MMb9w|20170601|3|P2|01|11|1|0|||||||||||有|有|有|O0M090|OM9"
# str2="ai8dN2gKqL5CLpIBiBQCmvq15xrSQlhDuMPjqgocR%2B96A9iV0xvWYRMEyKrweGDXIUKJI%2BHM0vaB%0AeS8mFcWC0roPrxJLLqZ0a30d4arZL7F79V9dy7wVMwhFaILvL8MuIf0IrMiYHJZ%2Fs5L%2FGs%2BSU4MS%0ALNmVeF5SS1gapRqi4Y%2F8UPq2N%2FuHY8qE%2B0PCEwoXqk2AlPX42M1GHkKcXt8hmAn88SZvoy7%2Fu1u%2B%0AiL%2Fgg9vxeQL8|预订|24000014611N|1461|BJP|SHH|BJP|SHH|11:54|07:19|19:25|Y|%2FSh5prCbhmJKuGb565ycCxJc0zQDh98of73nCQ71h0%2F9PiUDwe8ulS8QvSE%3D|20170601|3|P2|01|26|0|0||||1|||有||有|有||||10401030|1413"
# str1=str1.split('|')
# str2=str2.split('|')
# for i,j in enumerate(str1):
#     print i,j

# class Parent(object):
#     x = 1
#
# class Child1(Parent):
#     pass
#
# class Child2(Parent):
#     pass
#
# print Parent.x, Child1.x, Child2.x  #1,1,1
# Child1.x = 2
# print Parent.x, Child1.x, Child2.x  #1,2,1
# Parent.x = 3
# print Parent.x, Child1.x, Child2.x  #3,2,3

# from Tkinter import *
# import datetime
# import time
# root = Tk()
# root.title('与xxx聊天中')
# #发送按钮事件
# def sendmessage():
#   #在聊天内容上方加一行 显示发送人及发送时间
#   msgcontent = '我:' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + '\n '
#   text_msglist.insert(END, msgcontent, 'green')
#   text_msglist.insert(END, text_msg.get('0.0', END))
#   text_msg.delete('0.0', END)
#
# #创建几个frame作为容器
# frame_left_top   = Frame(width=380, height=270, bg='white')
# frame_left_center  = Frame(width=380, height=100, bg='white')
# frame_left_bottom  = Frame(width=380, height=20)
# frame_right     = Frame(width=170, height=400, bg='white')
# ##创建需要的几个元素
# text_msglist    = Text(frame_left_top)
# text_msg      = Text(frame_left_center);
# button_sendmsg   = Button(frame_left_bottom, text='发送', command=sendmessage)
# #创建一个绿色的tag
# text_msglist.tag_config('green', foreground='#008B00')
# #使用grid设置各个容器位置
# frame_left_top.grid(row=0, column=0, padx=2, pady=5)
# frame_left_center.grid(row=1, column=0, padx=2, pady=5)
# frame_left_bottom.grid(row=2, column=0)
# frame_right.grid(row=0, column=1, rowspan=3, padx=4, pady=5)
# frame_left_top.grid_propagate(0)
# frame_left_center.grid_propagate(0)
# frame_left_bottom.grid_propagate(0)
# #把元素填充进frame
# text_msglist.grid()
# text_msg.grid()
# button_sendmsg.grid(sticky=E)
# #主事件循环
# root.mainloop()
#!/usr/bin/python
# -*- coding: utf-8 -*-

# __author__ = 'xianhua.meng'
# # encoding: utf-8
# #!/usr/bin/python
#
# '''''Tkinter教程之Frame篇'''
# #Frame就是屏幕上的一块矩形区域，多是用来作为容器（container）来布局窗体。
# '''''1.创建Frame'''
# # -*- coding: cp936 -*-
# from Tkinter import *
# root = Tk()
# #以不同的颜色区别各个frame
# for fm in ['red','blue','yellow','green','white','black']:
#     #注意这个创建Frame的方法与其它创建控件的方法不同，第一个参数不是root
#     Frame(height = 20,width = 400,bg = fm).pack()
# root.mainloop()
# #添加不同颜色的Frame，大小均为20*400

# '''''3.Tk8.4以后Frame又添加了一类LabelFrame，添加了Title的支持'''
# from Tkinter import *
# root = Tk()
# for lf in ['red','blue','yellow']:
#     #可以使用text属性指定Frame的title
#     LabelFrame(height = 200,width = 300,text = lf, bg = lf).pack()
# root.mainloop()

'''''2.向Frame中添加Widget'''
# -*- coding: cp936 -*-
from Tkinter import *
root = Tk()
fm = []
#以不同的颜色区别各个frame
for color in ['red','blue']:
    #注意这个创建Frame的方法与其它创建控件的方法不同，第一个参数不是root
    fm.append(Frame(height = 200,width = 400,bg = color))
#向下面的Frame中添加一个Label
Label(fm[1],text = 'Hello label').pack()
fm[0].pack()
fm[1].pack()
root.mainloop()
#Label被添加到下面的Frame中了，而不是root默认的最上方。
#大部分的方法来自gm,留到后面gm时再介绍
#!/usr/bin/python
# -*- coding: UTF-8 -*-
#运行环境 python2.7
#author：hx

#简单
# import Tkinter
# top = Tkinter.Tk()
# # 进入消息循环
# top.mainloop()

#进阶
from Tkinter import *
import tkMessageBox

import random


name_list = ['李洪斌', '朱恒', '刘华利', '陈德兵', '何喜', '何子奇', '夏维炳', '王军', '秦闻', '冯国全']


#创建窗口
name = Tk()

# 设置窗口的标题
# name.title("点名程序")

#标签组件
labelname =Label(name, text = "python学员",height=2,width=40,fg='red',bg='orange')
labelname.pack()

#学员列表
listb = Listbox(name, fg='orange')
for item in name_list:
    listb.insert(0, item)
listb.pack()  # 将小部件放置到主窗口中

#按钮组件
global cc

cc = []
def btn1_clicked():
    while True:
        c_name = random.choice(name_list)
        if c_name not in cc:
            cc.append(c_name)
            tkMessageBox.showinfo(title="被选中的人", message=c_name)
            break

but1 = Button(name, text = "选择", width=5, command = btn1_clicked)
but1.pack(side=LEFT)

but2 = Button(name, text = "重置", width=5, command = btn1_clicked)
# but2.place(x=300,y=190)
but2.pack(side=LEFT)







name.mainloop()
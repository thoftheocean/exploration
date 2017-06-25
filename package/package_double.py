#!/usr/bin/python
# -*- coding: UTF-8 -*-
#运行环境 python2.7
#author：hx
from Tkinter import *
from PIL import ImageTk, Image


top = Tk()
top.geometry('260x260')
image2 = Image.open(r'img/maizi.png')
background_image = ImageTk.PhotoImage(image2)
# w = background_image.width()
# h = background_image.height()
# app.geometry('%dx%d+0+0' % (w,h))
background_label = Label(top, image=background_image, heigh=300, width=400)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# 进入消息循环
top.mainloop()

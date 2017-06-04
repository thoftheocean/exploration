#!/usr/bin/python
# -*- coding: utf-8 -*-

# from Tkinter import *
# from PIL import ImageTk
#
# root=Tk()
#
# canvas = Canvas(root,width = 300, height = 400)
# canvas.pack(expand = YES, fill = BOTH)
#
#
# image = ImageTk.PhotoImage(file = r"img3.jpg")
# canvas.create_image(10, 10, image = image, anchor = NW)
#
# but2 = Button(root, text = "重置", width=5).pack()
#
# root.mainloop()


from Tkinter import *
from PIL import ImageTk,Image

app = Tk()
app.title("Welcome")
image2 = Image.open(r'img3.jpg')
background_image = ImageTk.PhotoImage(image2)
# w = background_image.width()
# h = background_image.height()
# app.geometry('%dx%d+0+0' % (w,h))

background_label = Label(app, image=background_image,heigh=300,width=400)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#学员列表
name_list = ['李洪斌', '朱恒', '刘华利', '陈德兵', '何喜', '何子奇', '夏维炳', '王军', '秦闻', '冯国全']
listb = Listbox(app, fg='orange')
for item in name_list:
    listb.insert(0, item)
listb.pack()  # 将小部件放置到主窗口中

but2 = Button(app, text = "重置", width=5).pack()

# Frame(app,heigh=300,width=400)

but2 = Button(app, text = "重置", width=5).pack()

app.mainloop()
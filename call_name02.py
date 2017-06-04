#!/usr/bin/python
# -*- coding: UTF-8 -*-
#运行环境 python2.7
#author：hx

from Tkinter import *
import tkMessageBox
from PIL import ImageTk,Image

import random

#学员
name_list = ['李洪斌', '朱恒', '刘华利', '陈德兵', '何喜', '何子奇', '夏维炳', '王军', '秦闻', '冯国全']


#创建窗口
root = Tk()

# 设置窗口的标题
root.title("点名程序")


#修改自定义图标
# root.iconbitmap('img\maizi.ico')


#设置窗口大小
# root.geometry("300x300+0+0")   # 设置窗口大小 注意：是x 不是*

##设置窗口是否可以变化长/宽，
root.resizable(width=False, height=False) #False不可变，True可变，默认为True

name=Frame(root,bg='#c0d2e9')






#标签组件
labelname =Label(name, text = "这是一个点名小程序",height=2,width=35,font=("Arial", 10, "bold"),fg='blue',bg='orange')
labelname.pack(side=TOP)


#学员列表
listb = Listbox(name,selectmode = BROWSE,bg='yellow', height=12,width=15,font=('Arial',10))
for item in name_list:
    listb.insert(END, item)
listb.pack(side=LEFT)  # 将小部件放置到主窗口中

#添加滚动条
sl = Scrollbar(name)
sl.set(0, 0.5)
sl.pack(side=LEFT,fill=Y)
listb['yscrollcommand'] = sl.set
sl['command'] = listb.yview

#设置背景图片
# frame=Frame(name,width=100,height=100,bg='red').pack(side=RIGHT)
canvas=Canvas(name,width=155,height=200)
image2 = Image.open(r'maizi.png')
background_image = ImageTk.PhotoImage(image2)
canvas.create_image(80,80,image=background_image)
canvas.place(x=125, y=37)



#按钮组件
cc = []
def btn1_clicked():
    global cc
    while True:
        if len(cc) != 10:
            c_name = random.choice(name_list)
            # 选中操作
            index=name_list.index(c_name)
            listb.selection_set(index)

            if c_name not in cc:
                cc.append(c_name)
                tkMessageBox.showinfo(title="恭喜你被选中咯", message=c_name)
                break

        else:
            tkMessageBox.showinfo(title="恭喜你被选中咯", message='下一轮抽选开始')
            for i in cc:
                print i,
            print '\n'
            cc = []
            listb.selection_clear(0,9)

but1 = Button(name, text = "选择", width=5,command = btn1_clicked)
but1.pack(anchor=CENTER,side=BOTTOM,fill=BOTH)
# but1.pack(side=RIGHT,fill=X)



#绑定双击事件
def clicked(event):
    c_name=listb.get(listb.curselection())
    tkMessageBox.showinfo(title="恭喜你被选中咯", message=c_name)
listb.bind('<Double-Button-1>', clicked)


#必须设置这个，才能将其他控件装进frame框中
name.pack()

root.mainloop()
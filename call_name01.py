#!/usr/bin/python
# -*- coding: UTF-8 -*-
#运行环境 python2.7
#author：hx

from Tkinter import *
import tkMessageBox

import random

#学员
name_list = ['李洪斌', '朱恒', '刘华利', '陈德兵', '何喜', '何子奇', '夏维炳', '王军', '秦闻', '冯国全','z','w','l']


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

name=Frame(root,bg='orange')




#标签组件
labelname =Label(name, text = "这是一个小程序",height=2,width=35,bg='green')
labelname.pack(side=TOP)


#学员列表
listb = Listbox(name,selectmode = BROWSE,bg='yellow', height=11,width=15,font=('Arial',10))
for item in name_list:
    listb.insert(END, item)
listb.pack(side=LEFT)  # 将小部件放置到主窗口中

#添加滚动条
sl = Scrollbar(name)
sl.set(0,0.5)
sl.pack(side = LEFT,fill = Y)
listb['yscrollcommand'] = sl.set
sl['command'] = listb.yview



#按钮组件
cc = []
def btn1_clicked():

    global cc

    while True:
        if len(cc) != 10:
            c_name = random.choice(name_list)
            index=name_list.index(c_name)
            listb.selection_set(index)  # 选中操作
            if c_name not in cc:
                cc.append(c_name)
                tkMessageBox.showinfo(title="恭喜你被选中咯", message=c_name)
                break

        else:
            tkMessageBox.showinfo(title="恭喜你被选中咯", message='下一轮抽选开始')
            for i in cc:
                print i,
            print '\n'
            cc=[]
            listb.selection_clear(0,9)

but1 = Button(name, text = "选择", width=5,command = btn1_clicked)
but1.pack(anchor=CENTER,side=BOTTOM,fill=BOTH)



#绑定双击事件
def clicked(event):
    c_name=listb.get(listb.curselection())
    tkMessageBox.showinfo(title="恭喜你被选中咯", message=c_name)
listb.bind('<Double-Button-1>', clicked)


#必须设置这个，才能将其他控件装进frame框中
name.pack()

root.mainloop()
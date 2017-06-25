#!/usr/bin/python
# -*- coding: UTF-8 -*-
#运行环境 python3.5
#author：hx
from tkinter import *
from tkinter import messagebox


root = Tk()

root.geometry('300x200')

frame = Frame(root, bg='#08a62b')

def message():
    messagebox.showinfo(title='谁是卧底', message='游戏即将开始，请大家做好准备')

but = Button(frame, text="投票", width=10, command=message)
but.pack(anchor=CENTER)

frame.pack()
# 进入消息循环
root.mainloop()

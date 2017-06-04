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


def btnHelloClicked():
    new_lable=entryname.get()
    labelname.config(text=new_lable) #修改label中text文本


#创建窗口
name = Tk()

# 设置窗口的标题
name.title("点名程序")

#标签组件
labelname =Label(name, text = "python学员",height=2,width=50,fg='red',bg='blue')
labelname.pack()

#按钮组件
btnname = Button(name, text = "Hello", fg='red', bg='orange' ,command = btnHelloClicked)
btnname.pack(side = BOTTOM )

#输入框组件
entryname = Entry(name, text = "0",bg='yellow')
entryname.pack()

#单选框组件
    #控制标签的颜色，红色，蓝色，绿色
def colorChecked():
    labelname.config(fg=color.get())

color = StringVar()
Radiobutton(name, text = "Red", variable = color, value = "red", command = colorChecked).pack(side = RIGHT)
Radiobutton(name, text = "Blue", variable = color, value = "blue", command = colorChecked).pack(side = RIGHT)
Radiobutton(name, text = "Green", variable = color, value = "green", command = colorChecked).pack(side = RIGHT)

#复选框组件
    #控制标签的字体。粗体和斜体
def typeChecked():
    textType = typeBlod.get() + typeItalic.get()
    if textType == 1:
        labelname.config(font=("Arial", 12, "bold"))
    elif textType == 2:
        labelname.config(font=("Arial", 12, "italic"))
    elif textType == 3:
        labelname.config(font=("Arial", 12, "bold italic"))
    else:
        labelname.config(font=("Arial", 12))

typeBlod = IntVar()  #定义整型变量，value值送入变量中
typeItalic = IntVar()
Checkbutton(name, text = "Blod", variable = typeBlod, onvalue = 1, offvalue = 0, command = typeChecked).pack(side = RIGHT)
Checkbutton(name, text = "Italic", variable = typeItalic, onvalue = 2, offvalue = 0, command = typeChecked).pack(side = RIGHT)

#绘图组件
def drawCircle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)

cvs = Canvas(name, width = 600, height = 400)
cvs.pack()

cvs.create_line(50, 50, 50, 300)
cvs.create_line(100, 50, 200, 300, fill = "red", dash = (4, 4), arrow = LAST)

cvs.create_rectangle(200, 50, 400, 200, fill = "blue")

cvs.create_oval(450, 50, 550, 200, fill = "green" )
drawCircle(cvs, 450, 300, 50, fill = "red")

cvs.create_polygon(200, 250, 350, 250, 350, 350, 220, 300, fill="yellow")

#消息弹出窗口
import tkMessageBox
#3.4以后的版本 tkinter.messagebox

def btn1_clicked():
    tkMessageBox.showerror("Info", "Showinfo test.")

def btn2_clicked():
    tkMessageBox.showwarning("Warning", "Showwarning test.")


def btn3_clicked():
    tkMessageBox.showerror("Error", "Showerror test.")


def btn4_clicked():
    tkMessageBox.askquestion("Question", "Askquestion test.")


def btn5_clicked():
    tkMessageBox.askokcancel("OkCancel", "Askokcancel test.")


def btn6_clicked():
    tkMessageBox.askyesno("YesNo", "Askyesno test.")


def btn7_clicked():
    tkMessageBox.askretrycancel("Retry", "Askretrycancel test.")

btn1 = Button(name, text = "showinfo", command = btn1_clicked)
btn1.pack(fill = X)
btn2 = Button(name, text = "showwarning", command = btn2_clicked)
btn2.pack(fill = X)
btn3 = Button(name, text = "showerror", command = btn3_clicked)
btn3.pack(fill = X)
btn4 = Button(name, text = "askquestion", command = btn4_clicked)
btn4.pack(fill = X)
btn5 = Button(name, text = "askokcancel", command = btn5_clicked)
btn5.pack(fill = X)
btn6 = Button(name, text = "askyesno", command = btn6_clicked)
btn6.pack(fill = X)
btn7 = Button(name, text = "askretrycancel", command = btn7_clicked)
btn7.pack(fill = X)



#列表
li = ['李洪斌' ,  '朱恒' ,  '刘华利' ,  '陈德兵' ,  '何喜' ,  '何子奇' , '夏维炳' , '王军'  , '秦闻'  ,'冯国全']

listb = Listbox(name)
for item in li:
    listb.insert(0,item)
listb.pack(side=LEFT)  # 将小部件放置到主窗口中


name.mainloop()    # 进入消息循环
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:hx
# environment:python 2.7


#建立新表，写入数据。
import xlwt

# 创建一个Workbook对象，这就相当于创建了一个Excel文件,style_compression表示是否压缩
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
# 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
# 在电脑桌面右键新建一个Excel文件，其中就包含Sheet1，Sheet2，Sheet3三张表,而这里只创建了一张表
sheet = book.add_sheet('sheet1', cell_overwrite_ok=True)
# 向表aa中添加数据
sheet.write(0, 0, 'beijing')
sheet.write(0, 1, 'shanghai')

sheet.write(1, 0, u'北京烤鸭')
sheet.write(1, 1, u'上海外滩')

# 在路径前加r是禁止转译，\t,\n
# book.save(r'C:\Users\Administrator\Desktop\demo_hx.xls')
book.save(r'C:\Users\Mohammad He\Desktop\demo_hx.xls')



#读取数据
import xlrd
# xlsFile = r'C:\Users\Administrator\Desktop\demo_hx.xls'
xlsFile = r'C:\Users\Mohammad He\Desktop\demo_hx.xls'
book = xlrd.open_workbook(xlsFile)

# sheet1 = book.sheet_by_name('Sheet1')
sheet1 = book.sheet_by_index(0)    # 通过sheet索引获得sheet对象
sheetName = book.sheet_names()[0]  # 获得指定索引的sheet名字

# print type(sheetName)
# print sheetName

nrows = sheet1.nrows  # 总行数
ncols = sheet1.ncols  # 总列数
# print nrows
# print ncols

# 获得第一行的数据表
rowData1 = sheet1.row_values(0, 2, 4)
for i in rowData1:
    print i

# 获得第一列的数据表
colData1 = sheet1.col_values(0)
# for m in colData1:
#     print m

# 通过坐标读取表格中的数据
cellValue1x1 = sheet1.cell_value(0, 0)
#print cellValue1x1
cellValue3x2 = sheet1.cell_value(1, 1)
#print cellValue3x2

#修改数据
import xlutils.copy
import xlutils


# excel= xlrd.open_workbook(r'C:\Users\Administrator\Desktop\demo_hx.xls')
excel= xlrd.open_workbook(r'C:\Users\Mohammad He\Desktop\demo_hx.xls')
new_excel = xlutils.copy.copy(excel)

# 获取sheet对象，通过sheet_by_index()获取的sheet对象没有write()方法
ws = new_excel.get_sheet(0)

ws.write(0, 0, 'sicuan')
ws.write(1, 0, u'四川麻辣烫')
# 利用保存时同名覆盖达到修改excel文件的目的,注意未被修改的内容保持不变
# new_excel.save(r'C:\Users\Administrator\Desktop\demo_hx2.xls')
new_excel.save(r'C:\Users\Mohammad He\Desktop\demo_hx2.xls')
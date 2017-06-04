#coding:utf-8
from selenium import webdriver
driver = webdriver.PhantomJS(executable_path="D:\HXprogram\python2.7\Scripts\phantomjs.exe")
driver.set_page_load_timeout(5)
# obj.maximize_window()  #设置全屏
# obj.set_window_size('480','800') #设置浏览器宽480，高800
# try:
#     obj.get('http://www.baidu.com')  # 访问百度首页
#     obj.save_screenshot('1.png') #截屏保存为1.png
#     obj.get('http://www.sina.com.cn')  # 访问新浪首页
#     obj.save_screenshot('2.png')
#     obj.back()  # 回退到百度首页
#     obj.save_screenshot('3.png')
#     obj.forward()  # 前进到新浪首页
#     obj.save_screenshot('4.png')
# except Exception as e:
#     print e
driver.get('https://kyfw.12306.cn')
# text_data = driver.find_element_by_id("jd_comments").text #获取指定id的文本
# print text_data
source_data = driver.page_source  #获取网页源码
print source_data
# with open('maizi.html','w')as f:
#     f.write(source_data)
driver.quit()
#coding:utf-8
import unittest
from selenium import webdriver
from bs4 import BeautifulSoup


# class seleniumTest(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.PhantomJS(executable_path="D:\HXprogram\python2.7\Scripts\phantomjs.exe")
#
#     def testEle(self):
#         driver = self.driver
#         driver.get('http://www.douyu.com/directory/all')
#         soup = BeautifulSoup(driver.page_source, 'xml')
#         while True:
#             titles = soup.find_all('h3', {'class': 'ellipsis'})
#             nums = soup.find_all('span', {'class': 'dy-num fr'})
#             for title, num in zip(titles, nums):
#                 print title.get_text(), num.get_text()
#             if driver.page_source.find('shark-pager-disable-next') != -1:
#                 break
#             elem = driver.find_element_by_class_name('shark-pager-next')
#             elem.click()
#             soup = BeautifulSoup(driver.page_source, 'xml')
#
#     def tearDown(self):
#         print 'down'
#
# if __name__ == "__main__":
#     unittest.main()
#

class seleniumTEst(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.PhantomJS(executable_path="D:\HXprogram\python2.7\Scripts\phantomjs.exe")

    def testEle(self):
        driver = self.driver
        for str in range(1,40):
            url='https://book.douban.com/annual2016/?source=navigation#'+str
            driver.get()
            soup = BeautifulSoup(driver.page_source, 'xml')
            while True:
                titles = soup.find_all('h3', {'class': 'ellipsis'})
                nums = soup.find_all('span', {'class': 'dy-num fr'})
                for title, num in zip(titles, nums):
                    print title.get_text(), num.get_text()
                if driver.page_source.find('shark-pager-disable-next') != -1:
                    break
                elem = driver.find_element_by_class_name('shark-pager-next')
                elem.click()
                soup = BeautifulSoup(driver.page_source, 'xml')

    def tearDown(self):
            print 'down'

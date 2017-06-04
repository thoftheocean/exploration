#coding:utf-8
#python2.7环境
#描述

'''
题目1：打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。

题目2：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

题目3：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？（流程图课堂上已画）
'''

#题目1
def function1():
    for num in range(100, 999):
        bai = num // 100
        shi = (num // 10) % 10
        ge = num % 10
        if num == bai ** 3 + shi ** 3 + ge ** 3:
            print num,
        else:
            continue

def function11():
    for a in range(1, 10):
        for b in range(0, 10):
            for c in range(0, 10):
                x = a ** 3 + b ** 3 + c ** 3
                y = a * 100 + b * 10 + c
                if x == y:
                    print y,

#题目2
def function2():
    a = [1, 2, 3, 4]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if a[i] != a[j] and a[j] != a[k] and a[i] != a[k]:
                    num = a[i] * 100 + a[j] * 10 + a[k]
                    print num,
                else:
                    continue

#题目3
def function3():
    import math
    for num1 in range(1, 10000):
        num2 = math.sqrt(num1 + 100)
        num3 = math.sqrt(num1 + 268)
        if num3 == math.floor(num3) and num2 == math.floor(num2):
            print num1,

def function31():
    for a in range(10000):
        x = a ** 2 + 168
        y = x ** 0.5
        if y.is_integer():
            print (a ** 2 - 100),



if __name__=='__main__':
    function1()
    print '\n'+'----------'
    function11()
    print '\n' + '----------'
    function2()
    print '\n'+'----------'
    function3()
    print '\n' + '----------'
    function31()
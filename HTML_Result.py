#-*-coding:utf-8-*-
import os
import sys
import time
import unittest

from selenium import webdriver

import HTMLTestRunner


def Result(result,openNot,testunit):
    if result == 'Yes':
        print u'■■■■生成报告■■■■'
        #testunit=unittest.TestSuite()
        #定义报告存放路径
        now = time.strftime('%H-%M-%S',time.localtime(time.time()))
        day = time.strftime('%Y-%m-%d',time.localtime(time.time()))

        dirname = 'Results_Report'
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        dirname2 = dirname + '\\' + day + u'测试报告'
        if not os.path.exists(dirname2):
            os.mkdir(dirname2)

        filename = dirname2 + '\\' + now + 'result.html'
        #fp = file(filename, 'wb')
        with file(filename,'w') as fp:
            #定义测试报告
            runner =HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title=u'测试报告',
                description=u'用例执行情况')
            #运行用例
            print u'HTMLTestRunner运行...'
            runner.run(testunit)
        time.sleep(2)
        if openNot == 'Yes':
            #try:
                url = 'file:///' + os.path.abspath(filename)
                print 'url',url
                driver = webdriver.Firefox()
                driver.maximize_window()
                driver.implicitly_wait(30)
                driver.get(url)
                time.sleep(1)
                driver.refresh()
                sys.exit()
            #except:
                #print u'没有生成测试报告!'
    else:
        print u'■■■■没有报告■■■■'
        runner = unittest.TextTestRunner()
        runner.run(testunit)

#-*-coding:utf-8-*-
import unittest

from appium import webdriver
from selenium import webdriver


class AppTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        #测试系统，支持android，iOS，Firefox
        desired_caps['platformName'] = 'Android'
        #测试系统的版本
        desired_caps['platformVersion'] = '4.4.4'
        #设备名称
        desired_caps['deviceName'] = 'Samsung Galaxy S 4-4.4.4'
        #测试app的package
        desired_caps['appPackage'] = 'com.taobao.mobile.dipei'
        #被测app的activity
        desired_caps['appActivity'] = 'com.taobao.ecoupon.activity.PortalActivity'
        #使用Unicode输入法
        desired_caps['unicodeKeyboard'] = True
        # 在设定了UnicodeKeyboard关键字的Unicode测试结束后，重置输入法原有状态，默认False
        desired_caps['resetKeyboard'] = True
        #使用uiautomator2可以获取toast，需要appium1.6.3
        #desired_caps['automationName'] = 'Uiautomator2'
        #构造函数初始化驱动程序对象与URL地址
        self.driver = webdriver.Remote('http://127.0.0.1:4233/wd/hub',
                                       desired_caps)

    def tearDown(self):
        self.driver.quit()
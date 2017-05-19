#-*-coding:utf-8-*-
import os

class Init:
    def __init__(self):
        self.PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

    def init(self,platformName):
            desired_caps = {}
            #要测试的手机系统
            desired_caps['platformName'] = 'Android'
            #手机操作系统版本
            desired_caps['platformVersion'] = '5.1'
            #使用手机类型或模拟器类型
            desired_caps['deviceName'] = 'PD1501D'
            #使用Unicode输入法，默认False
            desired_caps['unicodeKeyboard'] = True
            #在设定了UnicodeKeyboard关键字的Unicode测试结束后，重置输入法原有状态，默认False
            desired_caps['resetKeyboard'] = True
            desired_caps['app'] = self.PATH('D:\\tool\\Android\\kbwm.apk')
            #要运行的Android应用包名
            desired_caps['app-package'] = 'com.taobao.mobile.dipei'
            #想要从应用包中启动的Android Activity名称
            desired_caps['app-Activity'] = 'com.eg.android.AlipayGphone.AlipayLogin'

            #desired_caps['automationName'] = 'Selendroid'
            return desired_caps

#-*-coding:utf-8-*-
import sys
import time
import unittest

reload(sys)
sys.setdefaultencoding('utf-8')
from config import keyWords
from page import BasePage
import HTML_Result
from test import test_support
from moudles import ReSuit
#testunit = unittest.TestSuite()
testunit = ReSuit.Suit()

class ExcutionEngin(unittest.TestCase):
    '''测试用例生成与执行'''

    @classmethod
    def setUpClass(cls):
        cls.filePath = 'dataEngin\\testData.xls'

    @classmethod
    def tearDownClass(cls):
        print 'End!'

    def action(self,tarApp,toastYN,*txt):
        '''
        测试demo
        :param txt: 参数,case data行数据
        :param tarApp: apk名
        :param toastYN: 是否获取toast
        :return: 无
        '''
        exeKeyword = keyWords.ActionKey()
        base = BasePage.AppAction()
        summary = txt[3]   #case data中的行数据，表示用例主题
        print '【' + summary + '】'
        k = 4
        stepsData = base.getSheetData(self.filePath,'Test Steps')
        for i in stepsData:  #遍历测试步骤
            if i[0] == txt[1]:
                if i[3] == 'openApp':
                    self.tarApps = tarApp
                    self.toastYN = toastYN
                    desired_caps = exeKeyword.getDesCap(self.tarApps)
                    #print 'desired_caps',desired_caps
                    print '+'*35
                    print u'测试平台：{}'.format(desired_caps[0])
                    print u'平台版本：{}'.format(desired_caps[1])
                    print u'设备：{}'.format(desired_caps[2])
                    print u'测试app：{}'.format(desired_caps[3].split('\\')[-1])
                    print '+'*35
                    print i[2]
                    try:
                        self.driver = exeKeyword.openApp(self.toastYN,*desired_caps)
                    except Exception,e:
                        print str(e)
                        try:
                            exeKeyword.appiumServer()
                            time.sleep(20)
                            self.driver = exeKeyword.openApp(*desired_caps)
                        except Exception, e:
                            print 'str(e)', str(e)
                            if str(e) and 'Could not find a connected Android device' in str(e):
                                print u'安卓设备未连接'
                                sys.exit()
                            elif str(e) and 'urlopen error' in str(e):
                                print u'appium server未启动'
                                sys.exit()
                            elif str(e) and 'Requested a new session but one was in progress' in str(e):
                                print u'session未覆盖'
                                sys.exit()

                elif i[3] == 'Click':
                    print i[2]
                    loc = exeKeyword.locate(i[4])
                    print u'点击元素：{}'.format(loc)
                    exeKeyword.click(loc)
                    #time.sleep(1)

                elif i[3] == 'Input':
                    print i[2]
                    loc = exeKeyword.locate(i[4])
                    exeKeyword.send_key(loc, txt[k])
                    k += 1  # 同一用例的所有输入数据都在case data表单页的同一行存储，每次遍历后都会往后移一位

                elif i[3] == 'Switch_Web':
                    print i[2]
                    exeKeyword.switch_to_webview()
                elif i[3] == 'Switch_app':
                    print i[2]
                    exeKeyword.switch_to_app()

                elif i[3] == 'Submit':
                    print i[2]
                    loc = exeKeyword.locate(i[4])
                    exeKeyword.submit(loc)
                elif i[3] == 'closeApp':
                    print i[2]
                    time.sleep(1)
                    #num += 1
                    #print 'num:%s'%num
                    exeKeyword.close()
                elif i[3] == 'Assert':
                    print i[2]
                    loc = base.locate(i[4])
                    actual = str(actual).split('.')[0].strip() if str(i[5]).endswith('.0') or str(i[5]).endswith('.00') else str(i[5]).strip()
                    print u'预期查找元素：%s'% loc
                    exeKeyword.assertData(loc,actual)
                elif i[3] == 'Sleep':
                    print i[2]
                    s = int(i[5])
                    time.sleep(s)
                elif i[3] == 'Login':
                    print i[2]
                    userinput = base.locate(i[4])
                    username = i[5]
                    pwdinput = base.locate(i[6])
                    password = i[7]
                    submit = base.locate(i[8])
                    exeKeyword.login(username,password,userinput,pwdinput,submit)
                    time.sleep(2)
                elif i[3] == 'DBsql':
                    print i[2]
                    host = base.getIniData('DataBase','host')
                    username = base.getIniData('DataBase','username')
                    pwd = base.getIniData('DataBase','pwd')
                    db = base.getIniData('DataBase','db')
                    sql = i[5]
                    actual = i[6]
                    expect = exeKeyword.sqlDB(host,username,pwd,db,sql)
                    exeKeyword.DBassert(actual,expect)
                elif i[3] == 'Swipe_Page':
                    print i[2]
                    direction = i[5]
                    duration = i[7]
                    n = i[6]   #滑动次数
                    if type(n) == int or type(n) == float or str(n).isdigit():
                        n = int(n)
                        print u'页面执行操作：{}滑动{}次'.format(i[5],n)
                        if type(duration)==int or type(duration)==float:
                            exeKeyword.swipe_page(direction,n,int(duration))
                        else:
                            exeKeyword.swipe_page(direction,n)
                    elif not n:
                        exeKeyword.swipe_page(direction)
                    else:
                        print u'滑动次数错误：{}'.format(n)
                elif i[3] == 'Swipe_Element':
                    print i[2]
                    loc = exeKeyword.locate(i[4])
                    direction = i[5]
                    duration = i[7]
                    n = i[6]
                    if type(n)==int or type(n)==float or str(n).isdigit():
                        n = int(n)
                        print u'执行元素{0}操作：{1}'.format(loc,direction)
                        if type(duration) and type(duration)==float or str(duration).isdigit():
                            exeKeyword.swipe_element(direction,loc,n,duration)
                        else:
                            exeKeyword.swipe_element(direction,loc,n)
                    elif direction and not n:
                        exeKeyword.swipe_element(direction,loc)
                elif i[3] == 'Tap':
                    print i[2]
                    position = i[5]
                    duration = i[6]
                    print u'点击屏幕{}'.format(position)
                    if str(duration) and str(duration).isdigit():
                        exeKeyword.tap_act(position,duration)
                    else:
                        exeKeyword.tap_act(position)

                elif i[3] == 'mulClick':
                    print i[2]
                    loc = exeKeyword.locate(i[4])
                    indexs = i[5]  # '[1,2,3,]'
                    print u'点击元素{0}：位置{1}'.format(loc,indexs)
                    exeKeyword.mulClick(loc,indexs)

                elif i[3] == 'Print':
                    print i[2]
                    loc = exeKeyword.locate(i[4])
                    exeKeyword.Prints(loc)

                elif i[3] == 'Drag_Drop':
                    print i[2]
                    loc1 = exeKeyword.locate(i[4])
                    loc2 = exeKeyword.locate(i[5])
                    print u'拖动元素{}到{}'.format(loc1,loc2)
                    exeKeyword.drag_drop(loc1,loc2)

                elif i[3] == 'Pinch_Zoom_Page':
                    print i[2]
                    how = i[5]
                    num = i[6]
                    if type(num)==int or type(num)==float or str(num).isdigit():
                        num = int(num)
                        exeKeyword.pinch_zoom_page(how,num)
                    else:
                        exeKeyword.pinch_zoom_page(how)

                elif i[3] == 'Pinch_Zoom_Element':
                    print i[2]
                    loc = exeKeyword.locate(i[4])
                    how = i[5]
                    num = i[6]
                    print u'{1}元素{0}'.format(loc,how)
                    if type(num)==int or type(num)==float or str(num).isdigit():
                        num = int(num)
                        exeKeyword.pinch_zoom_ele(loc,how,num)
                    else:
                        exeKeyword.pinch_zoom_ele(loc,how)

                elif i[3] == 'Shake':
                    print i[2]
                    exeKeyword.shake_window()

                elif i[3] == 'setNet':
                    print i[2]
                    types = str(i[5]).split('.')[0]
                    print u'设置网络为：{}'.format(types)
                    exeKeyword.set_net(int(types))

                elif i[3] == 'GPS':
                    print i[2]
                    exeKeyword.toggle()

                elif i[3] == 'screenShot':
                    print i[2]
                    name = i[5]
                    if name:
                        exeKeyword.save_img(name)
                    else:
                        exeKeyword.save_img('手动截图')
                elif i[3] == 'setTime':
                    print i[2]
                    loc = exeKeyword.locate(i[4])
                    loc2 = exeKeyword.locate(i[5])
                    time2 = i[6]
                    exeKeyword.setTime(loc,loc2,time2)
                elif i[3] == 'setTime2':
                    print i[2]
                    loc = exeKeyword.locate(i[4])
                    loc2 = exeKeyword.locate(i[5])
                    time2 = i[6]
                    exeKeyword.setTime2(loc, loc2, time2)

                elif i[3] == 'Install':
                    print i[2]
                    exeKeyword.install()

                elif i[3] == 'Uninstall':
                    print i[2]
                    exeKeyword.uninstall()

                elif i[3] == 'Back':
                    print i[2]
                    exeKeyword.Back()

                elif i[3] == 'Forward':
                    print i[2]
                    exeKeyword.Forward()
                else:
                    print u'未知关键字{}'.format(i[3])



    @staticmethod
    def getTestFunc(tarApp,toastYN,*txt):
        def func(self):
            self.action(tarApp,toastYN,*txt)
        return func

    #退出
    @classmethod
    def tearDown(self):
        print 'end'
'''
def getTestCase():
    page = BasePage.AppAction()
    casedata = page.getSheetData("dataEngine\\testData.xls", "Test Cases")
    for i in casedata:
        TestAction = i[1]
        if i[4] == 'Y':
            print '【Run】' + i[2] + ':'
            print '+ -'*8
            table = page.getSheetData("dataEngine\\testData.xls", "case data")
            for j in table:
                if j[2] == 'Y' and j[1] == TestAction:
                    print j
                    setattr(ExcutionEngin,'test_%s_%s'%(j[0],j[1]),ExcutionEngin.getTestFunc(j))
                    #添加测试用例到测试套件
                    testunit.addTest(ExcutionEngin,'test_%s_%s'%(j[0],j[1]))
                    #执行测试用例，生成测试报告
                    HTML_Result.Result(testunit)
'''
def generateTestCases(run,result='Yes',open='No'):
    login_page = BasePage.AppAction()
    casedata = login_page.getSheetData("dataEngin\\testData.xls", "Test Cases")
    for i in casedata:
        TCid = i[1]   #Login
        if i[4] == 'Y':
            tarApp = i[5]   #app名
            toastYN = i[6]
            table = login_page.getSheetData("dataEngin\\testData.xls", "case data")
            print TCid
            print "【Run】"+i[2]+"："
            print " + -"*12
            for txt in table:
                if (txt[2] == "Y") & (txt[1] == TCid):  #Login==Login
                    print txt
                    setattr(ExcutionEngin, 'test_%s_%s' % (txt[0], txt[1]), ExcutionEngin.getTestFunc(tarApp,toastYN,*txt))
                    #添加测试用例到测试套件
                    testunit.addTest(ExcutionEngin('test_%s_%s' % (txt[0], txt[1])))
    if run == 'Debug':
        print '■■■■Debug模式■■■■'
        test_support.run_unittest(ExcutionEngin)
    else:
        #调用测试生成报告
        HTML_Result.Result(result,open,testunit)

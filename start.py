#-*-coding:utf-8-*-
from threading import Thread

import executeMain
from config import keyWords
from page import BasePage

login_page = BasePage.AppAction()
#casedata = login_page.getTabledata("dataEngine\\testData.xls", "settings")

run = login_page.getCellData("dataEngin\\testData.xls","settings", 1, 1)
print u'运行模式:%s' %run
result = login_page.getCellData("dataEngin\\testData.xls","settings", 2, 1)
print u'是否生成测试报告:%s' %result
openNot = login_page.getCellData("dataEngin\\testData.xls","settings", 3, 1)
print u'测试完成后打开测试报告:%s' %openNot
if __name__ == '__main__':
    log = keyWords.ActionKey()
    t1 = Thread(target=log.log)
    t1.setDaemon(True)
    t1.start()
    #t2 = Thread(target=executeMain.generateTestCases,args=(run,result,openNot))
    executeMain.generateTestCases(run,result,openNot)

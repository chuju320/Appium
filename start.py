#-*-coding:utf-8-*-

import executeMain
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

    #t2 = Thread(target=executeMain.generateTestCases,args=(run,result,openNot))
    executeMain.generateTestCases(run,result,openNot)

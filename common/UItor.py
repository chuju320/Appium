#-*-coding:utf-8-*-
from uiautomator import device as d


def confirm():
    while 1:
        if d(text=u'继续安装',resourceId='com.android.packageinstaller:id/ok_button').exists:
            d(text=u'继续安装').click()

        if d(text=u'安全警告').exists and d(text=u'好').exists:
            d(text=u'好').click()

        if d(text=u'安装').exists and d(textContains=u'您要安装此应用吗').exists:
            d(text=u'安装').click()

        if d(text=u'确定').exists and d(text=u'替换应用').exists:
            d(text=u'确定').click()

        if d(text=u'安装完成').exists and d(text=u'完成').exists:
            d(text=u'完成').click()

confirm()
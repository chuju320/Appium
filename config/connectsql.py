#-*-coding:utf-8-*-
import pyodbc

class Mysql:
    '''链接mysql执行sql'''
    def __init__(self,host,username,pwd,db):
        self.host = host
        self.username = username
        self.pwd = pwd
        self.db = db

    def getConnect(self):
        if not self.db:
            raise (NameError,'没有数据库配置信息！')
        self.conn = pyodbc.connect('DRIVER={MySQL ODBC 5.3.7 Driver};'
                                   'server=self.host;'
                                   'user=self.user;'
                                   'password=self.pwd;'
                                   'database=self.db')
        cur = self.conn.cursor()
        if not cur:
            raise (NameError,'数据库连接失败！')
        else:
            return cur

    def executeSql(self,sql):
        cur = self.getConnect()     #获取游标
        cur.execute(sql)            #执行sql
        row = cur.fetchone()        #获取返回结果
        return row[0]               #返回字段值
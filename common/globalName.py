#-*-coding:utf-8-*-
listname = []
def getOrNot(name,pwd):
    if pwd == 1:
        print name
        listname.append(name)
    elif pwd == 2:
        realname = listname[0]
        return realname

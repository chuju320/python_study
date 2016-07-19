#-*-coding:utf-8-*-
'''修改当前目录下的内容含有NQM字样的的文本，删除每行中出现的--人名，并在完成后弹窗提示修改的文本记录'''

from Tkinter import tkinter as tk
import os,time,sys,xlrd
reload(sys)
sys.setdefaultencoding( "utf-8" )


global Dict
Dict = {}
def find():
    '''查找当前目录下的所有文件'''
    pass

def files(fileName='1NQM.xls'):
    '''打开指定文件，读取内容并返回指定内容'''
    try:
        cotent = xlrd.open_workbook(fileName)
        tables = cotent.sheet_by_index(0)
        return  tables
    except:
        print '请将“NQM.XLS”文件放在本软件统一目录或者将其更名为NQM.xls，然后执行！'
        time.sleep(3)
        sys.exit()


def getTableData():
    '''获取行内容'''
    table = files()
    for i in range(1,table.nrows):
        yield table.row_values(i)

def indexs(name):
    '''取指定的内容字段的列'''
    table = files()
    rowValues = table.row_values(0)
    try:
        clo1 = rowValues.index(name)
        return clo1
    except:
        print '"%s"未找到！'%name

def hos():
    '''获取所有现场目录'''
    hoslist = []  #所有现场名
    table = files()
    hosName = indexs(u'移动医疗实施项目')
    lines = getTableData()
    for i in lines:
        #i[hosName]=医院名
        hoslist.append(i[hosName])
    hoslist = list(set(hoslist))
    return hoslist


def filew(content):
    '''写文件'''
    with open('123.txt','w') as f:
        f.write(content)

def sqls(row,clo):
    '''检索sql'''
    table = files()
    content = table.cell_value(row,clo)
    list2 = repr(content).split(r"\n")
    sql = ''
    for i in list2:
        i = i.strip()
        if '.SQL' in i.upper():
            num = i.upper().index('.SQL')
            sql = i[0:num+4] + ',\n'
            num2 = sql.index('201')
            if 'view'.upper() not in sql.upper():
                #print '不在'
                sql = sql.replace(sql[0:num2],'sql\\0TABLEDATA\\')
            else:
                sql = sql.replace(sql[0:num2],'sql\\1VIEW_FUNC\\')

    return  sql.strip()

def start():
    names = hos()
    #print 'names:',names
    table = files()
    hosNum = indexs(u'移动医疗实施项目')
    clo1 = indexs(u'标识')
    clo2 = indexs(u'主题')
    clo3 = indexs(u'报告人')
    clo4 = indexs(u'上传源代码文件列表')


    hossql = {}  #任务脚本
    nohos = {}   #非现场任务

    f = open('123.txt','w')
    for j in range(1,table.nrows):
        hosdic = {}  #现场医院名
        clo1s = table.cell_value(j,clo1) #标识
        clo2s = table.cell_value(j,clo2) #主题
        clo3s = table.cell_value(j,clo3) #报告人
        clo4s = table.cell_value(j,clo4) #上传源代码文件列表
        sql = sqls(j,clo4)
        hossql[clo1s] = sql
        hosName = table.cell_value(j,hosNum)
        hosName = hosName.strip()
        list2 = []
        hoss = {}  #现场任务
        if clo3s.strip()!='张倩' and clo3s.strip()!='李甲林':
            if hosName == '':
                nohos[clo1s] = clo2s
            else:
                #print 'hosName:',hosName
                hosdic[clo1s] = clo2s  #吧 标识、主题  写进字典
                #print 'hosdic:',hosdic
                #list2.append(hosdic)
                #hoss[hosName] = list2
                if Dict.has_key(hosName):
                    Dict[hosName].update(hosdic) #把现场创建的任务放进Dict总字典
                else:
                    #print '第一次出现'
                    #print Dict
                    Dict[hosName] = hosdic
                    #print Dict
                #hoslist.append(hoss)
#没有根据医院区分出  具体信息
    f.write('本地创建任务：\n\n')
    for i in nohos.keys():
        line1 = '%s %s'%(i,nohos[i])
        #f.write('\n')
        f.write(line1)
        f.write('\n')
        sqll = hossql[i]
        #print sqll
        if sqll:
            f.write(sqll)
            f.write('\n')
    #把现场任务写进txt
    keys = Dict.keys()
    #print 'keys:',keys
    for i in keys:
        f.write('\n')
        ii = '*' +i.strip()+'*'
        f.write(ii)
        f.write('\n\n')
        for j in Dict[i].keys():
            line = '%s %s'%(j,Dict[i][j])
            #f.write('\n')
            f.write(line)
            f.write('\n')
            sqll = hossql[j]
            if sqll:
                f.write(sqll)
                f.write('\n')

    f.close()
    print 'Done!'

start()
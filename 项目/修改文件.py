#-*-coding:utf-8-*-
'''
修改当前目录下的内容含有NQM字样的的文本，删除每行中出现的--人名，并在完成后弹窗提示修改的文本记录
'''

from Tkinter import tkinter as tk
import os,time,sys,xlrd,re
reload(sys)
sys.setdefaultencoding( "utf-8" )
type = sys.getfilesystemencoding()

global Dict,Dict2
global numFile

Dict = {}
Dict2 = {}
def find():
    '''查找当前目录下的所有文件'''
    pass

def files():
    '''打开指定文件，读取内容并返回指定内容'''
    fileName = 'NQM.xls'
    fileName2 = 'NQM.xlsx'
    if os.path.exists(fileName):
        try:
            cotent = xlrd.open_workbook(fileName)
            tables = cotent.sheet_by_index(0)
            return  tables
        except:
            print '请检查excel文档格式，文档不能有附件及链接等'
            time.sleep(3)
            sys.exit()
    elif os.path.exists(fileName2):
        try:
            cotent = xlrd.open_workbook(fileName2)
            tables = cotent.sheet_by_index(0)
            return  tables
        except:
            print '请检查excel文档格式，文档不能有附件及链接等'
            time.sleep(3)
            sys.exit()
    else:
        print '请将“NQM.XLS(x)”文件放在当前目录下或者将其更名为NQM.xls或者NQM.xlsx，然后执行！'
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

def sqls(row,clo1,clo2):
    '''检索sql'''
    table = files()
    content = table.cell_value(row,clo1)
    content2 = table.cell_value(row,clo2)
    content3 = content + '\n'+ content2
    list2 = repr(content3).split(r"\n")
    sqlss = []
    for i in list2:
        i = i.strip()
        if '.SQL' in i.upper():
            num = i.upper().index('.SQL')
            sql = i[0:num+4] + ',\n'
            num2 = sql.index('201')
            if 'view'.upper()  in sql.upper():
                #print '在'
                print '含有view的sql：',sql
                sql = i.replace(sql[0:num2],'sql\\1VIEW_FUNC\\')
                sqlss.append(sql)
            else:
                sql = i.replace(sql[0:num2],'sql\\0TABLEDATA\\')
                sqlss.append(sql)

    return  sqlss

def start():
    print 'start...'
    numBug = 0
    names = hos()
    #print 'names:',names
    table = files()
    hosNum = indexs(u'移动医疗实施项目')
    clo1 = indexs(u'标识')
    clo2 = indexs(u'主题')
    clo3 = indexs(u'报告人')
    clo4 = indexs(u'上传源代码文件列表')
    clo5 = indexs(u'包含脚本列表')


    hossql = {}  #任务脚本
    nohos = {}   #非现场任务
    hosql2 = {}
    nohos2 = {}  #bug

    f = open('123.txt','w')
    for j in range(1,table.nrows):
        hosdic = {}  #现场医院名
        hosdic2 = {}  #bug医院名
        clo1s = table.cell_value(j,clo1) #标识
        clo2s = table.cell_value(j,clo2) #主题
        clo3s = table.cell_value(j,clo3) #报告人
        clo4s = table.cell_value(j,clo4) #上传源代码文件列表
        sql = sqls(j,clo4,clo5)
        '''
        if hosql2.has_key(clo2s):
            hosql2[clo2s].append(sql)
        else:
            hosql2[clo2s] = sql
        '''
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
        elif clo3s.strip()=='张倩' or clo3s.strip()=='李甲林':
            numBug += 1
            #print 'hosName:',hosName
            hosdic2[clo1s] = clo2s  #吧 标识、主题  写进字典
            #print 'hosdic:',hosdic
            #list2.append(hosdic)
            #hoss[hosName] = list2
            if Dict2.has_key(hosName):
                Dict2[hosName].update(hosdic2) #把现场创建的任务放进Dict总字典
            else:
                #print '第一次出现'
                #print Dict
                Dict2[hosName] = hosdic2
                #print Dict
            #hoslist.append(hoss)

#没有根据医院区分出  具体信息
    if nohos:
        f.write('本地创建任务：\n\n')
        for iq in nohos.keys():
            line1 = '%s %s'%(iq,nohos[iq])
            #f.write('\n')
            f.write(line1)
            f.write('\n')
            sqll = hossql[iq]
            #print sqll
            if sqll:
                for ij in sqll:
                    f.write(ij)
                    f.write('\n')
            f.write('本地创建任务：\n\n')

    #把现场任务写进txt
    keys = Dict.keys()

    #print 'keys:',keys
    for ia in keys:
        list2 = []
        f.write('\n')
        ii = '*' +ia.strip()+'*'
        f.write(ii)
        f.write('\n\n')
        for j in Dict[ia].keys():
            line = '%s %s'%(j,Dict[ia][j])
            #f.write('\n')
            f.write(line)
            f.write('\n')
            sqll = hossql[j]
            if sqll:
                for ix in sqll:
                    list2.append(ix)

                    #f.write(ix)
                    #f.write('\n')
        if Dict2.has_key(ia):
            for bugsql in Dict2[ia].keys():
                sqll2 = hossql[bugsql]
                if sqll2:
                    for bug in sqll2:
                        list2.append(bug)
        list2 = list(set(list2))
        list2.sort()
        for aa in list2:
            f.write(aa)
            f.write('\n')

    f.close()
    print 'Done!'
    ff = open('123.txt')
    con = ff.read()
    p = re.compile('NQM')
    num = p.findall(con)
    print '共统计现场任务数:'.decode('utf-8').encode(type),len(num)
    print '共统计Bug数:'.decode('utf-8').encode(type),numBug
    time.sleep(5)
start()
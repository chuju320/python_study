#-*-coding:utf-8-*-

list = ['SQL\4ADVERSEEVENTS\1DATA\201608101159_Rp_NameRecord_Insert.sql']

sqlss = []
for i in list:
        i = i.strip()
        if '.SQL' in i.upper():
            num = i.upper().index('.SQL')
            sql = i[0:num+4] + ',\n'
            num2 = sql.index('\201')
            if 'view'.upper()  in sql.upper():
                #print '在'
                sql = i.replace(sql[0:num2],'sql\\1VIEW_FUNC\\')
                print r"%s"%sql
            else:
                sql = i.replace(sql[0:num2],'sql\\0TABLEDATA\\')
                print r'%s'%sql
#-*-coding:utf-8-*-


a = 'SQL\\1SYSTEMMANAGEMENT\\0DDL\\2VIEW_FUNC201607121648_SYS_OPERATION_INSERT.SQL'

num = a.upper().index('201')
b = a[0:num]
c = a.replace(b,'sql\\0TABLEDATA\\')
print b
print c
print 'view'.upper() in a.upper()
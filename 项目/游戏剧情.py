#-*-coding:utf-8-*-
'''
故事主角：A、B、C
主线：A和B是男女朋友，C插足，B努力争取，多年后（分支条件）
    1.A、B在一起
    2.A、C在一起
    3.A、B、C都没有在一起
    ...（结局不限）
故事主线依靠对话控制并支线发展
'''

class Person(object):
    '''角色类'''
    def __init__(self,name,sex,age,money,makings):
        self.name = name
        self.sex = sex
        self.age = age
        self.money = money
        self.makings = makings

    def say(self,content):
        '''人物谈话'''
        return content

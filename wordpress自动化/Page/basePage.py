#-*-coding:utf-8-*-
from appium import webdriver
from selenium import webdriver
import time
from threading import Thread
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.common.by import By
from model.Model import Config

class Factory(object):
    def __init__(self,driver):
        self.driver = driver

    #工厂方法
    def createWebDriver(self,webDriver):
        if webDriver == 'web':
            return WebUI(self.driver)
        elif webDriver == 'app':
            return AppUI(self.driver)

class WebDriver(object):
    def __init__(self,driver):
        self.driver = driver
    def __str__(self):
        return 'WebDriver'

    def findElement(self,loc):
        try:
            return self.driver.find_element(*loc)
        except NoSuchElementException,e:
            print 'Error details:%s'%(e.args[0])

    def findElements(self,loc):
        try:
            return self.driver.find_elements(*loc)
        except NoSuchElementException,e:
            print 'Error details:%s'%(e.args[0])

    def getScreenshot(self,name,form='png'):
        time.sleep(2)
        config = Config()
        self.driver.get_screenshot_as_file(config.data_dirs('img') + '/' +name +'.' +form)

    @property
    def wait(self):
        time.sleep(2)

class WebUI(WebDriver):
    def __str__(self):
        return 'WEB UI'


class AppUI(WebDriver):
    def __str__(self):
        return 'AppUI'
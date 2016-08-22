#-*-coding:utf-8-*-
import unittest
from appium import webdriver
from selenium import webdriver
import os

PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

class WebTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://localhost/wordpress/wp-login.php')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()


class AppTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platforVersion'] = '4.4.4'
        desired_caps['deviceName'] = 'm2'
        #desired_caps['deviceName'] = 'Samsung Galaxy S5-4.4.4'
        #desired_caps['appPackage'] = 'com.qihoo.appstore'
        #desired_caps['appActivity'] = 'com.qihoo.appstore.home.MainActivity'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['app'] = PATH('c:\\ddandroid_206200.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def tearDown(self):
        self.driver.quit()
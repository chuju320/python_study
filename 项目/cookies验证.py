#-*-coding:utf-8-*-
from  selenium import webdriver
import time


driver = webdriver.Firefox()
driver.get('http://172.16.0.32:5055/login.html')
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element_by_id('os_username').clear()
driver.find_element_by_id('os_username').send_keys('001')
time.sleep(1)
driver.find_element_by_id('os_password').clear()
driver.find_element_by_id('os_password').send_keys('0')
time.sleep(1)
driver.find_element_by_id('loginButton').click()
time.sleep(2)
driver.find_element_by_xpath(".//img[@title='上报事件管理']").click()
time.sleep(1)

cookie = driver.get_cookies()
print 'cookie:',cookie
url = driver.current_url
print 'url:',url

driver.delete_all_cookies()
driver.quit()
print 'close'
driver = webdriver.Firefox()
time.sleep(1)
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(30)

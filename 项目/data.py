#-*-coding:utf-8-*-
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://www.hqms.org.cn/usp/roster/index.jsp")
driver.implicitly_wait(30)
driver.maximize_window()
time.sleep(1)


all = Select(driver.find_element_by_name('organid'))
all2 = Select(driver.find_element_by_name('hgrade'))
for i in range(1,32):
    all.select_by_index(i)
    all2.select_by_index(1)

    driver.find_element_by_id('btn_search').click()
    time.sleep(1)
    elements = driver.find_elements_by_xpath(".//div[@class='brief_right']//form//div[5]/span")
    for i in range(len(elements)):
        print elements[i].text
driver.quit()
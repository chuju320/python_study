#-*-coding:utf-8-*-
'''
1、启动hub 
hub是中心点，将接收所有测试请求并将它们分发到节点，启动的命令为：
java -jar  selenium-server-standalone-2.49.0.jar  -role hub
2、启动nodes
节点注册到hub，命令为：
java -jar java -jar  selenium-server-standalone-2.49.0.jar -role 
node  -hub http://localhost:4444/grid/register 
3、启动selenium-server,然后启动浏览器，selenium-server会记录下执行的过程，当然selenium-server
启动的命令为：
         java -jar selenium-server-standalone-2.49.0.jar

'''
'''
对browserName进行参数化，可以实现一个功能，多个浏览器测试，比如百度搜索，
我们实现2个浏览器测试，分别是chrome,firefox，见修改后的代码：
'''
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from threading import Thread
#listBrowser = ['firefox','chrome']
def ipBrowser():
    list = {
        #'http://172.16.8.33:5556/wd/hub' : 'chrome',
        'http://172.16.8.34:5555/wd/hub' : 'firefox'
    }
    return list
class myThread(Thread):
    def run(self):
        Thread.run(self)

def testBaidu(host,browser):
    print 'ip:',host
    driver = webdriver.Remote(
        command_executor=host,
        desired_capabilities={
            'browserName':browser,
            'platform':'ANY',
            'version':'',
            'javascriptEnabled':True
        }
    )

    print '目前测试的浏览器是：',browser
    driver.get('http://www.baidu.com')
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.find_element_by_id('kw').send_keys('selenium grid2')
    time.sleep(1)
    driver.find_element_by_id('su').click()
    time.sleep(1)
    driver.quit()

threads = []
all = range(len(ipBrowser()))
for host,browser in ipBrowser().items():
    t1 = myThread(target=testBaidu,args=(host,browser))
    threads.append(t1)

if __name__ == '__main__':
    for i in all:
        threads[i].start()
    for i in all:
        threads[i].join()
    print 'Over'

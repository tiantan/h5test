# -*- coding:utf-8 -*-
from threading import Thread
from time import ctime,sleep
from selenium import webdriver

def test_baidu(browser,search):
    print('start:%s' % ctime())
    print('browser:%s' % browser)
    if browser=="ie":
        driver=webdriver.Ie()
    elif browser=="chrome":
        driver=webdriver.Chrome()
    elif browser=="ff":
        driver=webdriver.Firefox()
    else:
        print("browser 参数有误，只能为ie，ff，chrome")
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys(search)
    driver.find_element_by_id("su").click()
    sleep(2)
    driver.quit()

if __name__ == '__main__':
   lists={'ie':'ie','chrome':'chrome','ff':'ff'}
   thread=[]
   files=range(len(lists))
   for browser,search in lists.items():
       t=Thread(target=test_baidu,args=(browser,search))
       thread.append(t)
   for t in files:
       thread[t].start()
   for t in files:
       thread[t].join()
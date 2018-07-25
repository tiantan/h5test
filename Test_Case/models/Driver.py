# -*- coding:utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class Driver(object):

    def __init__(self, driver):
        self.driver = driver  # =webdriver.Chrome()

    '''   
   def start(self, driver_name):
       """
       启动浏览器
       :param url: 测试地址
       :param driver_name: 在启动时设置浏览器的类型
       :return:
       """
       if driver_name == "Firefox":
           self.driver = webdriver.Firefox()
       elif driver_name == "Ie":
           self.driver = webdriver.Ie()
       else:
           self.driver = webdriver.Chrome()
       return self.driver
   '''

    def element_wait(self, *loc):
        for i in range(20):
            try:
                # views = driver.find_element_by_class_name("views")
                views = self.driver.find_element(*loc)
                if views.is_displayed():
                    break
            except:
                pass
            time.sleep(1)
        else:
            print("time out")
        return views

    # 切换到组织编辑窗口
    def switch_frame(self, value):
        self.driver.switch_to_frame(value)

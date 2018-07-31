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

    def findElement(self, element):
        '''
        封装selenium中By库中的函数
        Find element
        element is a set with format (identifier type, value), e.g. ('id','username')
        Usage:
        self.findElement(element)
        '''
        try:
            type = element[0]
            value = element[1]
            if type == "id" or type == "ID" or type == "Id":
                elem = self.driver.find_element_by_id(value)

            elif type == "name" or type == "NAME" or type == "Name":
                elem = self.driver.find_element_by_name(value)

            elif type == "class" or type == "CLASS" or type == "Class":
                elem = self.driver.find_element_by_class_name(value)

            elif type == "link_text" or type == "LINK_TEXT" or type == "Link_text":
                elem = self.driver.find_element_by_link_text(value)

            elif type == "xpath" or type == "XPATH" or type == "Xpath":
                elem = self.driver.find_element_by_xpath(value)

            elif type == "css" or type == "CSS" or type == "Css":
                elem = self.driver.find_element_by_css_selector(value)
            else:
                raise NameError("Please correct the type in function parameter")
        except Exception:
            raise ValueError("No such element found" + str(element))
        return elem


    # 切换到组织编辑窗口
    def switch_frame(self, value):
        self.driver.switch_to_frame(value)

    #关闭
    def close(self):
        self.driver.close()



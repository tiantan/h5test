# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class login(object):

    def __init__(self, driver):
        self.driver=driver #=webdriver.Firefox()
        driver=self.driver
        #元素抽取
        self.username=driver.find_element(By.ID, "userName")
        self.password=driver.find_element(By.ID, "password")
        self.btnLogin=driver.find_element(By.ID, "btnLogin")
    #登录封装
    def login(self,username,password):
        driver = self.driver
        self.username.clear()
        self.username.send_keys(username)
        self.password.clear()
        self.password.send_keys(password)
        time.sleep(1)
        self.btnLogin.click()
        time.sleep(10)
        # 获取到当前窗口
        driver.switch_to_default_content()




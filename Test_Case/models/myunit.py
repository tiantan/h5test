# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver

'''用于初始化，然后测试类都继承这个类即可'''
class Mytest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

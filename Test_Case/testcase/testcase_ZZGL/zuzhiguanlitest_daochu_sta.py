# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Test_Case.page_obj.zuzhiguanliPage import zuzElement
from Test_Case.models import myunit
import HTMLTestRunner
import os


class MyTestCase(myunit.Mytest):
    # 启动只启动一次浏览器为全局，

    #wbb = webdriver.Chrome()
    '''
    def setUp(self):
        self.driver = driver= webdriver.Chrome()
        # self.wb = webdriver.Firefox()
        # self.wb.get("http://localhost:8082/web.hr")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    '''
    # 部门编辑
    def test_1_btnImportData(self):
        driver = self.driver
        ZuzElement = zuzElement(driver)

        #进入组织管理界面
        ZuzElement.gozuzhiguanli()
        #导出
        ZuzElement.Click_btnImportData()
        time.sleep(3)
        #导出Excel
        ZuzElement.Click_btnexport()
        time.sleep(3)
        #获取窗口标题
        window_title=driver.find_element_by_class_name("k-window-title")
        #print(test.text)
        self.assertEqual(window_title.text,u"部门导出")

        # 关闭窗口
        zuzElement(driver).tabCloseCurrent()
        time.sleep(10)
    def test_02_btnExportTemplate(self):
        driver = self.driver
        ZuzElement = zuzElement(driver)

        # 进入组织管理界面
        ZuzElement.gozuzhiguanli()
        # 导出
        ZuzElement.Click_btnImportData()
        time.sleep(3)
        #导出模板
        ZuzElement.Click_btnExportTemplate()
        time.sleep(3)
        btnImportData_loc=driver.find_element(By.ID,"btnImportData")
        self.assertEqual(btnImportData_loc.text,u"导入导出")
        # 关闭窗口
        zuzElement(driver).tabCloseCurrent()
        time.sleep(5)

    def test_03_btnExportTemplate(self):
        driver = self.driver
        ZuzElement = zuzElement(driver)

       # 进入组织管理界面
        ZuzElement.gozuzhiguanli()
        # 导出当前列表
        ZuzElement.Click_btnExportCurrentList()
        time.sleep(3)

        # 关闭窗口
        zuzElement(driver).tabCloseCurrent()
        time.sleep(5)
    '''
    def test_3_quit(self):
        self.driver.quit()
    '''
    '''
    def tearDown(self):
        self.driver.quit()
    '''
if __name__ == '__main__':
    unittest.main()
    '''
    print os.getcwd()
    testunit=unittest.TestSuite()
    testunit.addTest(MyTestCase("test_1_btnImportData"))
    #testunit.addTest(MyTestCase("test_02_btnExportTemplate"))
    #testunit.addTest(MyTestCase("test_03_btnExportTemplate"))
    testunit.addTest(MyTestCase("test_3_quit"))
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")  # 获取时间
    fp=open('G:/python/h5test/report/'+now_time+'_result.html','wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='test',description='qingkang')
    runner.run(testunit)
    fp.close()
    '''


# -*- coding:utf-8 -*-
import unittest
from Test_Case.page_obj.LoginPage import login
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from Test_Case.page_obj.DuozuzElementPage import DuozuzElement
from Test_Case.models import myunit
import random



class MyTestCase(myunit.Mytest):
    # 启动只启动一次浏览器为全局，

    #wbb = webdriver.Chrome()
    '''
    def setUp(self):
        self.wb = wb=webdriver.Chrome()
        # self.wb = webdriver.Firefox()
        # self.wb.get("http://localhost:8082/web.hr")
        self.wb.maximize_window()
        self.wb.implicitly_wait(30)
    '''
    def test_2_btnEdit(self):
        #        duozuzElement=DuozuzElement(self.wb)
        self.driver.get("http://localhost:8082/web.hr")
        try:
            login(self.driver).login("hr2", "longshine")
        except Exception:
            print('time out')
        self.driver.switch_to_default_content()
        time.sleep(3)
        # 规划
        DuozuzElement(self.driver).menuClick()
        time.sleep(3)
        # 多组织关系管理
        DuozuzElement(self.driver).menuItemDuoGXClick()
        time.sleep(3)
        # 切换iframe
        DuozuzElement(self.driver).switch_to_frame()
        time.sleep(10)
        DuozuzElement(self.driver).getVIRTUALDEPTLIST_VDEPTNAME()
        time.sleep(2)
        # 点击编辑按钮
        DuozuzElement(self.driver).Click_btnEdit()
        time.sleep(3)
        # 清除并输入信息
        #random.randint(0,9)
        MEMOText = u'团组织测试'#+ str(random.randint(0.9))
        DuozuzElement(self.driver).Send_VirtualdeptListMEMO(MEMOText)
        DuozuzElement(self.driver).Click_save_data()
        #time.sleep(3)
        self.driver.switch_to_default_content()
        # 显式等待 元素等待
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'kendoNotifyDiv')))
        # 从标签中获取文本内容
        print self.driver.find_element_by_id('kendoNotifyDiv').get_attribute('textContent')

        # 验证是否保存成功
        '''
        listsmemo = self.driver.find_elements_by_id("td_VIRTUALDEPTLIST_MEMO")
        print(listsmemo[len(listsmemo) - 1].text)
        getMEMOText = listsmemo[len(listsmemo) - 1].text
        self.assertEqual(MEMOText, getMEMOText)
        time.sleep(10)
        '''
        # 关闭窗口
        DuozuzElement(self.driver).tabCloseCurrent()
        time.sleep(20)

    def ttest_1_btnAdd(self):
        self.driver.get("http://localhost:8082/web.hr")
        login(self.driver).login("hr2", "longshine")
        # 规划
        DuozuzElement(self.driver).menuClick()
        time.sleep(3)
        # 多组织关系管理
        DuozuzElement(self.driver).menuItemDuoGXClick()
        time.sleep(3)
        # 切换iframe
        DuozuzElement(self.driver).switch_to_frame()
        # 点击新增
        time.sleep(10)
        DuozuzElement(self.driver).Click_btnAdd()
        time.sleep(10)
        # 关闭窗口
        DuozuzElement(self.driver).tabCloseCurrent()
        time.sleep(10)



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

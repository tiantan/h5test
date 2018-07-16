# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from Test_Case.page_obj.zuzhiguanliPage import zuzElement
from Test_Case.models import myunit
import random


class MyTestCase(myunit.Mytest):
    # 启动只启动一次浏览器为全局，

    #wbb = webdriver.Chrome()
    '''
    def setUp(self, ):
        self.driver = driver= webdriver.Chrome()
        # self.wb = webdriver.Firefox()
        # self.wb.get("http://localhost:8082/web.hr")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    '''
    # 部门编辑
    def ttest_1_btnEdit(self):
        driver = self.driver
        ZuzElement = zuzElement(driver)

        #进入组织管理界面
        ZuzElement.gozuzhiguanli()
        # 编辑
        zuzElement(driver).Click_btnNodeModify()
        time.sleep(5)
        # 备注输入
        B01_MARK_text = u'部门编辑'+str(random.randint(0,9))
        ZuzElement.Send_B01_MARK(B01_MARK_text)

        # 下一步
        ZuzElement.Click_btn_nextvrorgwin()
        time.sleep(5)
        # 保存
        ZuzElement.Click_btn_finishvrorgwin()
        time.sleep(5)
        # 点击部门树第二个节点
        zuzElement(driver).Click_bmTree()
        time.sleep(5)
        gridcell_Beizhu = driver.find_element_by_xpath('//*[@id="TreeListData"]/div[2]/table/tbody/tr[1]/td[8]')
        print(gridcell_Beizhu.text)
        self.assertEqual(B01_MARK_text, gridcell_Beizhu.text)

        # 关闭窗口
        zuzElement(driver).tabCloseCurrent()
        time.sleep(10)
    def test_02_btnNodeOrderBy(self):
        driver = self.driver
        ZuzElement = zuzElement(driver)

        '''
        #        duozuzElement=DuozuzElement(self.driver)
        driver.get("http://localhost:8082/web.hr")
        try:
            login(self.driver).login("hr2", "longshine")
        except Exception:
            print('time out')
        driver.switch_to_default_content()
        time.sleep(3)
        # 规划
        DuozuzElement(driver).menuClick()
        time.sleep(3)
        # 组织管理
        zuzElement(driver).menuItemDuoGXClick()
        time.sleep(3)
        driver.switch_to_frame("iframe191101")
        time.sleep(5)
        # 点击部门树第二个节点
        zuzElement(driver).Click_bmTree()
        time.sleep(5)
        '''
        ZuzElement.gozuzhiguanli()
        ZuzElement.Click_btnNodeOrderBy()
        time.sleep(5)

        # 获取列所有数据
        lists = self.driver.find_elements_by_xpath('//div[@role="option"]')
        print len(lists)
        # 鼠标移动最后一条上
        ActionChains(self.driver).move_to_element(lists[len(lists)-1]).perform()
        #点击最后一条
        lists[len(lists) - 1].click()
        time.sleep(3)
        ZuzElement.Click_marginTop100()
        time.sleep(3)
        ZuzElement.Click_OKButton()
        time.sleep(10)

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

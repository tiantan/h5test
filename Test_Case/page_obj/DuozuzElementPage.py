# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Test_Case.models.Driver import Driver


class DuozuzElement(Driver):
    # 元素抽取
    # 模块菜单
    menu_loc = (By.ID, "19")
    # 多组关系管理菜单元素
    # menuItemDuoGX_loc = (By.XPATH, '//*[@id = "submenudiv"]/div[2]/ul/li[1]/ul/li/a')
    menuItemDuoGX_loc = ('LINK_TEXT', '多组织管理')
    # 保存按钮
    save_data_loc = (By.ID, "save_data")
    # 新增
    btnAdd_loc = (By.ID, "btnAdd")
    # 编辑
    btnEdit_loc = (By.ID, "btnEdit")

    # 规划模块
    def menuClick(self):
        driver = self.driver
        self.menu = self.element_wait(*self.menu_loc)
        # self.menu = driver.find_element()
        self.menu.click()

    # 多组关系管理菜单
    def menuItemDuoGXClick(self):
        self.menuItemDuoGX = self.findElement(self.menuItemDuoGX_loc)
        self.menuItemDuoGX.click()

    # 切换到组织编辑窗口
    def switch_to_frame(self):
        self.switch_frame("iframe190301")
        # self.driver.switch_to_frame("iframe190301")

    # 点击最后一条数据
    def getVIRTUALDEPTLIST_VDEPTNAME(self):
        # 获取列所有数据
        list = self.driver.find_elements_by_id("td_VIRTUALDEPTLIST_VDEPTNAME")
        print len(list)
        # 鼠标移动最后一条上
        ActionChains(self.driver).move_to_element(list[len(list) - 1]).perform()
        # 点击最后一条
        list[len(list) - 1].click()

    # 关闭窗口
    def tabCloseCurrent(self):
        self.driver.switch_to_default_content()
        lick = self.element_wait(By.XPATH, "/html/body/div[2]/div[3]/div[1]/div/button")
        ActionChains(self.driver).move_to_element(lick).perform()
        self.element_wait(By.CLASS_NAME, "tabCloseCurrent").click()

    # 组织管理备注输入
    def Send_VirtualdeptListMEMO(self, MEMOText):
        self.element_wait(By.ID, "ctl_VIRTUALDEPTLIST_MEMO").clear()
        self.element_wait(By.ID, "ctl_VIRTUALDEPTLIST_MEMO").send_keys(MEMOText)

    # 保存按钮
    def Click_save_data(self):
        self.element_wait(*self.save_data_loc).click()

    # 点击新增
    def Click_btnAdd(self):
        self.element_wait(*self.btnAdd_loc).click()

    # 点击编辑按钮
    def Click_btnEdit(self):
        self.element_wait(*self.btnEdit_loc).click()

    # 获取一列最后一个值
    def getMEMOText(self, emdoid):
        # 验证是否保存成功
        listsmemo = self.element_wait(emdoid)
        print(listsmemo[len(listsmemo) - 1].text)
        MEMOText = listsmemo[len(listsmemo) - 1].text
        return MEMOText

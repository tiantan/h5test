# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from Test_Case.models.Driver import Driver
from Test_Case.page_obj.LoginPage import login
from Test_Case.page_obj.DuozuzElementPage import DuozuzElement


class zuzElement(Driver):
    # 元素抽取
    # 模块菜单
    menu_loc = (By.ID, "19")
    # 多组关系管理菜单元素
                   # // *[ @ id = "submenudiv"] / div[2] / ul / li[2] / ul / li / a[1]
    menuItemDuoGX_loc = (By.LINK_TEXT, '//*[@id="submenudiv"]/div[2]/ul/li[2]/ul/li/a[1]')


    '''设立'''
    # 保存按钮
    btn_finishvrorgwin_loc = (By.ID, "btn_finishvrorgwin")
    # 新增
    btnNodeAdd_loc = (By.ID, "btnNodeAdd")
    # 编辑
    btnNodeModify_loc = (By.ID, "btnNodeModify")
    #输入备注字段信息
    B01_MARK_loc=(By.ID, "ctl_B01_MARK")

    # 点击部门树第二个
    bmTree_loc= (By.XPATH, '//*[@id="bmTree"]/ul/li/ul/li[2]/div/span[2]')
    #下一步
    btn_nextvrorgwin_loc=(By.ID,"btn_nextvrorgwin")

    '''排序'''
    btnNodeOrderBy_loc = (By.ID, "btnNodeOrderBy")
    #上移
    marginTop100_loc = (By.XPATH,'//button[@class="k-button marginTop100"]')
    #保存
    OKButton_loc = (By.ID, "OKButton")

    '''导出'''
    btnImportData_loc=(By.ID,"btnImportData")
    #导出excel
    btnexport_loc=(By.ID,"btnexport")
    #导出模板
    btnExportTemplate_loc=(By.ID,"btnExportTemplate")

    #导出当前列表
    btnExportCurrentList_loc=(By.ID,"btnExportCurrentList")

    # 规划模块
    def menuClick(self):
        driver = self.driver
        self.menu = self.element_wait(*self.menu_loc)
        # self.menu = driver.find_element()
        self.menu.click()

    # 多组关系管理菜单
    def menuItemDuoGXClick(self):
        self.menuItemDuoGX = self.element_wait(*self.menuItemDuoGX_loc)
        self.menuItemDuoGX.click()


    # 切换到组织编辑窗口
    def switch_to_frame(self):
        self.driver.switch_to_frame("iframe190301")

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
    def Click_btn_finishvrorgwin(self):
        self.element_wait(*self.btn_finishvrorgwin_loc).click()

    # 点击新增
    def Click_btnNodeAdd(self):
        self.element_wait(*self.btnNodeAdd_loc).click()

    #点击编辑按钮
    def Click_btnNodeModify(self):
        self.element_wait(*self.btnNodeModify_loc).click()

    def Send_B01_MARK(self,b01_mark_text):
        b01_mark=self.element_wait(*self.B01_MARK_loc)
        b01_mark.clear()
        b01_mark.send_keys(b01_mark_text)
    #获取一列最后一个值
    def getMEMOText(self,emdoid):
        # 验证是否保存成功
        listsmemo = self.element_wait(emdoid)
        print(listsmemo[len(listsmemo) - 1].text)
        MEMOText = listsmemo[len(listsmemo) - 1].text
        return MEMOText

    #点击第二个部门节点
    def Click_bmTree(self):
        self.element_wait(*self.bmTree_loc).click()

    # 点击下一步
    def Click_btn_nextvrorgwin(self):
        self.element_wait(*self.btn_nextvrorgwin_loc).click()

    '''排序'''
    def Click_btnNodeOrderBy(self):
        self.element_wait(*self.btnNodeOrderBy_loc).click()
    #上移
    def Click_marginTop100(self):
        self.element_wait(*self.marginTop100_loc).click()

    # 上移
    def Click_OKButton(self):
        self.element_wait(*self.OKButton_loc).click()

    #进入组织管理
    def gozuzhiguanli(self):
        driver=self.driver
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

    '''导出'''
    def Click_btnImportData(self):
        self.element_wait(*self.btnImportData_loc).click()

    #导出Excel
    def Click_btnexport(self):
        self.element_wait(*self.btnexport_loc).click()
        time.sleep(3)

    #导出模板
    def Click_btnExportTemplate(self):
        self.element_wait(*self.btnExportTemplate_loc).click()
        time.sleep(3)

    #导出当前列表
    def Click_btnExportCurrentList(self):
        self.element_wait(*self.btnExportCurrentList_loc).click()
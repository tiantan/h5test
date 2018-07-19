# -*- coding:utf-8 -*-
import unittest
import os
import time
import HTMLTestRunner

'''用于执行所有测试用例testcase目录用例'''
# 1、设置待执行用例的目录
#case_path = os.path.join(os.getcwd(),"testcase_ZZGL")
case_path = os.path.join(os.getcwd())
print(case_path)
def all_case():
# 2、自动搜索指定目录下的cas，构造测试集,执行顺序是命名顺序：先执行test_add，再执行test_sub
    discover = unittest.defaultTestLoader.discover(case_path,pattern="*_sta.py",top_level_dir=None)
    print(discover)
    return discover
if __name__ == '__main__':

        now_time = time.strftime("%Y_%m_%d_%H_%M_%S")  # 获取时间
        #获取到根目录路径
        genmulu=os.path.abspath(os.path.join(os.getcwd(), ".."))
        fp = open(genmulu+'/report/' + now_time + '_result.html', 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test', description='qingkang')
        # 实例化TextTestRunner类
        #runner = unittest.TextTestRunner()
        runner.run(all_case())



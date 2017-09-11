# coding=utf-8
import unittest
import testsuites
from testsuites.multi_baidu_search import BaiduSearch


suite = unittest.TestSuite(unittest.makeSuite(BaiduSearch))
# 使用makesuite将所有BaiduSearch类的测试用例装载到一个套件中

if __name__ == '__main__':
    # 执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)
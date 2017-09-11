# coding=utf-8
import unittest

suite = unittest.TestLoader().discover("testsuites")
# 将testsuites中所有测试用例装载到测试套件中，testsuites是可以包名，也可以是一个文件夹名称

print "suite is:",suite

if __name__ == '__main__':
    # 执行用例
    runner = unittest.TextTestRunner()
    #runner.run(suite)



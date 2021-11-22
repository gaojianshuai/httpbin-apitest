# coding=utf-8
"""
    作者：高建帅
    功能：
    新增功能：
    日期：2021/11/21 22:23
"""
import time
import unittest
from BeautifulReport import BeautifulReport


def testReports():
    """
    function: 生成测试报告方法
    description: 生成测试报告
    arg:
    return:
    """
    case_dir = '../testcase'
    discover = unittest.defaultTestLoader.discover(case_dir, 'test*.py')

    # 用时间命名测试报告   测试报告生成时间  +  后缀名   2021-11-20 14-49-30test_report.html
    report_dir = '../reports'
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    report_name = report_dir + '/' +now+ '_test_report.html'

    with open(report_name, 'wb') as f:
        # 执行用例
        # HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=2, title='unittest测试报告练习', description='练习HTMLTestRunner使用').run(discover)
        BeautifulReport(discover).report(description=u'每日构建测试报告', filename=report_name, report_dir='../reports')

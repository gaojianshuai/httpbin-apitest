# coding=utf-8
"""
    作者：高建帅
    功能：
    新增功能：
    日期：2021/11/22 16:42
"""
import unittest
import requests
from reports.testReports import testReports


class APITestRequestInspection(unittest.TestCase):
    """
    function:
    description:
    arg:
    return:
    """

    # 测试网站
    url = 'http://httpbin.org/'

    # 发送get请求
    def test_inspection_001(self):
        """
        功能：headers
        :return:
        """
        url = self.url + '/headers'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_inspection_002(self):
        """
        功能：headers
        :return:
        """
        url = self.url + '/ip'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_inspection_003(self):
        """
        功能：user-agent
        :return:
        """
        url = self.url + '/user-agent'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)
            raise Exception('状态码与预期不相符，请重试！')
# coding=utf-8
"""
    作者：高建帅
    功能：
    新增功能：
    日期：2021/11/22 16:38
"""
import unittest
import requests
from reports.testReports import testReports


class APITestStatus(unittest.TestCase):
    """
    function:
    description:
    arg:
    return:
    """

    # 测试网站
    url = 'http://httpbin.org/'

    # 发送get请求
    def test_status_002(self):
        """
        功能：200
        :return:
        """
        url = self.url + '/status' + '/200'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_status_003(self):
        """
        功能：300
        :return:
        """
        url = self.url + '/status' + '/300'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '300':
            print(res.text)
        else:
            print(res.status_code)

    def test_status_004(self):
        """
        功能：400
        :return:
        """
        url = self.url + '/status' + '/400'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '400':
            print(res.text)
        else:
            print(res.status_code)

    def test_status_005(self):
        """
        功能：500
        :return:
        """
        url = self.url + '/status' + '/500'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '500':
            print(res.text)
        else:
            print(res.status_code)

# coding=utf-8
"""
    作者：高建帅
    功能：
    新增功能：
    日期：2021/11/22 17:30
"""
import unittest
import requests
from reports.testReports import testReports


class APITestCookies(unittest.TestCase):
    """
    function:
    description:
    arg:
    return:
    """

    # 测试网站
    url = 'http://httpbin.org/'

    # 发送get请求
    def test_cookies_001(self):
        """
        功能：cookies
        :return:
        """
        url = self.url + '/cookies'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_cookies_002(self):
        """
        功能：cookies/delete
        :return:
        """
        url = self.url + '/cookies/delete'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_cookies_003(self):
        """
        功能：cookies/set
        :return:
        """
        url = self.url + '/cookies/set'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_cookies_004(self):
        """
        功能：/cookies/set/{name}/{value}
        :return:
        """
        url = self.url + '/cookies/set' + '/gaojianshuai/gjs199074'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)


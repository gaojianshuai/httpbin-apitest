# coding=utf-8
"""
    作者：高建帅
    功能：
    新增功能：
    日期：2021/11/22 15:38
"""
import unittest
import requests
from reports.testReports import testReports


class APITestAuth(unittest.TestCase):
    """
    function:
    description:
    arg:
    return:
    """
    # 测试网站
    url = 'http://httpbin.org/'

    def test_auth_001(self):
        """
        功能：auth
        :return:
        """
        params = {"user": "gaojianshuai", "passwd": "gjs199074"}
        url = self.url + '/basic-auth/gaojianshuai/gjs199074'
        res = requests.get(url, auth=(params.get('user'), params.get('passwd')))
        # 获取响应码
        print(res.status_code)
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)
            raise Exception('状态码与预期不相符')

    @unittest.skip("强制性跳过！")
    def test_auth_002(self):
        """
        功能：bearer
        :return:
        """
        params = {"user": "gaojianshuai", "passwd": "gjs199074"}
        url = self.url + '/bearer'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)

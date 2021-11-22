# coding=utf-8
"""
    作者：高建帅
    功能：
    新增功能：
    日期：2021/11/22 17:39
"""
import unittest
import requests
from reports.testReports import testReports


class APITestRedirects(unittest.TestCase):
    """
    function:
    description:
    arg:
    return:
    """

    # 测试网站
    url = 'http://httpbin.org/'

    # 发送get请求
    def test_redirects_001(self):
        """
        功能：/absolute-redirect/{n}
        :return:
        """
        url = self.url + '/absolute-redirect' + '/5'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '302':
            print(res.text)
        else:
            print(res.status_code)
            raise Exception('状态码与预期不相符，请重试！')

    def test_redirects_002(self):
        """
        功能：/redirect-to
        :return:
        """
        url = self.url + '/redirect-to'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '302':
            print(res.text)
        else:
            print(res.status_code)
            raise Exception('验证码与预期不相符，请重试！')

    def test_redirects_003(self):
        """
        功能：/absolute-redirect/{n}
        :return:
        """
        url = self.url + '/absolute-redirect' + '/5'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '302':
            print(res.text)
        else:
            print(res.status_code)
            raise Exception('验证码与预期不相符，请重试！')

    def test_redirects_004(self):
        """
        功能：/absolute-redirect/{n}
        :return:
        """
        url = self.url + '/absolute-redirect' + '/5'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '302':
            print(res.text)
        else:
            print(res.status_code)
            raise Exception('验证码与预期不相符，请重试！')


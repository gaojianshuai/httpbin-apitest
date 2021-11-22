# coding=utf-8
"""
    作者：高建帅
    功能：
    新增功能：
    日期：2021/11/22 17:33
"""
import unittest
import requests
from reports.testReports import testReports


class APITestImage(unittest.TestCase):
    """
    function:
    description:
    arg:
    return:
    """

    # 测试网站
    url = 'http://httpbin.org/'

    # 发送get请求
    def test_image_001(self):
        """
        功能：image
        :return:
        """
        url = self.url + '/image'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_image_002(self):
        """
        功能：image/jpeg
        :return:
        """
        url = self.url + '/image/jpeg'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_image_003(self):
        """
        功能：image/png
        :return:
        """
        url = self.url + '/image/png'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_image_004(self):
        """
        功能：image/svg
        :return:
        """
        url = self.url + '/image/svg'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_image_005(self):
        """
        功能：image/webp
        :return:
        """
        url = self.url + '/image/webp'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)


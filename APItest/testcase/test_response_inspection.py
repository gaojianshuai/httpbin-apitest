# coding=utf-8
"""
    作者：高建帅
    功能：
    新增功能：
    日期：2021/11/22 16:45
"""
import unittest
import requests


class APITestResponseInspection(unittest.TestCase):
    """
    function:
    description:
    arg:
    return:
    """

    # 测试网站
    url = 'http://httpbin.org/'

    # 发送get请求
    def test_response_inspection_001(self):
        """
        功能：cache
        :return:
        """
        url = self.url + '/cache'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_response_inspection_002(self):
        """
        功能：cache/value
        :return:
        """
        url = self.url + '/cache' + '/500'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)
            raise Exception('状态码与预期不相符，请重试！')

    def test_response_inspection_003(self):
        """
        功能：etag/{etag}
        :return:
        """
        url = self.url + '/etag' + '/gaojianshuai'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_response_inspection_004(self):
        """
        功能：response-headers
        :return:
        """
        url = self.url + '/response-headers'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_response_inspection_005(self):
        """
        功能：etag/{etag}
        :return:
        """
        url = self.url + '/response-headers'
        res = requests.post(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)


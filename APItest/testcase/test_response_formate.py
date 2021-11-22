# coding=utf-8
"""
    作者：高建帅
    功能：
    新增功能：
    日期：2021/11/22 17:08
"""
import unittest
import requests
from reports.testReports import testReports


class APITestResponseFormate(unittest.TestCase):
    """
    function:
    description:
    arg:
    return:
    """

    # 测试网站
    url = 'http://httpbin.org/'

    # 发送get请求
    def test_response_formate_001(self):
        """
        功能：brotli
        :return:
        """
        url = self.url + '/brotli'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_response_formate_002(self):
        """
        功能：deflate
        :return:
        """
        url = self.url + '/deflate'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_response_formate_003(self):
        """
        功能：deny
        :return:
        """
        url = self.url + '/deny'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_response_formate_004(self):
        """
        功能：encoding/utf8
        :return:
        """
        url = self.url + '/encoding/utf8'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_response_formate_005(self):
        """
        功能：gzip
        :return:
        """
        url = self.url + '/gzip'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_response_formate_006(self):
        """
        功能：html
        :return:
        """
        url = self.url + '/html'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_response_formate_007(self):
        """
        功能：json
        :return:
        """
        url = self.url + '/json'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)
            raise Exception('状态码与预期不相符，请重试！')

    def test_response_formate_008(self):
        """
        功能：robot.txt
        :return:
        """
        url = self.url + '/robot.txt'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)
            raise Exception('状态码与预期不相符，请重试！')

    def test_response_formate_009(self):
        """
        功能：html
        :return:
        """
        url = self.url + '/xml'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)
            raise Exception('状态码与预期不相符，请重试！')
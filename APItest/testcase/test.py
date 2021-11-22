# coding=utf-8
"""
    作者：高建帅
    功能：
    新增功能：
    日期：2021/11/21 21:38
"""

import unittest
import requests
from reports.testReports import testReports


class APITest(unittest.TestCase):
    """
    function:
    description:
    arg:
    return:
    """

    # 测试网站
    url = 'http://httpbin.org/'

    # 发送get请求
    def test_001(self):
        """
        功能：get请求
        :return:
        """
        url = self.url + '/get'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        print(res.content.decode('utf8'))
        print(res.text)

    # 发送post请求
    def test_002(self):
        """
        功能：post请求
        :return:
        """
        url = self.url + '/get'
        res = requests.post(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        print(res.content.decode('utf8'))
        print(res.text)

    # 发送get请求
    def test_003(self):
        """
        功能：get请求
        :return:
        """
        url = self.url + '/get' + '?name=gaojianshuai&age=20'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        print(res.content.decode('utf8'))
        print(res.text)
    #
    # 发送get请求
    def test_004(self):
        """
        功能：请求参数    geturl
        # 键值对
        # name = gaojianshuai age = 20

        :return:
        """
        parames = {"name": "gaojianshuai", "age": 20}
        url = self.url + '/get'
        res = requests.get(url, params=parames)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        print(res.content.decode('utf8'))
        print(res.text)

    # 响应结果处理
    # 发送get请求
    def test_005(self):
        """
        功能：请求参数    geturl
        # 键值对
        # name = gaojianshuai age = 20

        :return:
        """
        parames = {"name": "gaojianshuai", "age": 20}
        url = self.url + '/get'
        res = requests.get(url, params=parames)
        # header  cookie  body
        print(res.headers['Content-Type'])
        print(res.cookies)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        print(res.content.decode('utf8'))
        print(res.text)
    #
    # 发送get请求
    def test_006(self):
        """
        功能：请求参数    geturl
        # 键值对
        # name = gaojianshuai age = 20

        :return:
        """
        parames = {"name": "gaojianshuai", "age": 20}
        url = self.url + '/get'
        res = requests.get(url, params=parames)

        # 获取响应码
        print(res.status_code)
        if res.status_code == '200':
            print(res.content.decode('utf8'))
            print(res.text)
        else:
            print(res.status_code)

    # 编码
    def test_007(self):
        """

        :return:
        """
        res = requests.get('http://www.baidu.com')
        if res.status_code == '200':
            print(res.text)
            print(res.content.decode('utf8'))
        else:
            print(res.status_code)

    # 编码apparent_encoding
    def test_008(self):
        """
        :return:
        """
        res = requests.get('http://www.baidu.com')
        # 解码方式， 根据header推断，
        print(res.apparent_encoding)
        # 解码方式， 根据header， 若没有则默认为ISO-8859-1
        print(res.encoding)
        if res.status_code == '200':
            print(res.text)
            print(res.content.decode('utf8'))
        else:
            print(res.status_code)

    def test_009(self):
        """
        put请求
        :return:
        """
        url = self.url + '/put'
        res = requests.get(url)
        if res.status_code == '200':
            print(res.text)
            print(res.content.decode('utf8'))
        else:
            print(res.status_code)

    def test_010(self):
        """
        delete请求
        :return:
        """
        url = self.url + '/delete'
        res = requests.get(url)
        if res.status_code == '200':
            print(res.text)
            print(res.content.decode('utf8'))
        else:
            print(res.status_code)

    def test_011(self):
        """
        delete请求
        :return:
        """
        url = self.url + '/patch'
        res = requests.get(url)
        if res.status_code == '200':
            print(res.text)
            print(res.content.decode('utf8'))
        else:
            print(res.status_code)


if __name__ == '__main__':
    testReports()

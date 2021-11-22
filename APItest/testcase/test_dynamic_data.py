# coding=utf-8
"""
    作者：高建帅
    功能：
    新增功能：
    日期：2021/11/22 17:14
"""
import unittest
import requests
from reports.testReports import testReports


class APITestDynamicData(unittest.TestCase):
    """
    function:
    description:
    arg:
    return:
    """

    # 测试网站
    url = 'http://httpbin.org/'

    # 发送get请求
    def test_dynamic_001(self):
        """
        功能：base64
        :return:
        """
        url = self.url + '/base64' + '/SFRUUEJJTiBpcyBhd2Vzb21l'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_dynamic_002(self):
        """
        功能：bytes/{n}
        :return:
        """
        url = self.url + '/bytes' + '/123'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_dynamic_003(self):
        """
        delete
        功能：delay/{delay}
        :return:
        """
        url = self.url + '/delay' + '/666'
        res = requests.delete(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_dynamic_004(self):
        """
        get
        功能：delay/{delay}
        :return:
        """
        url = self.url + '/delay' + '/666'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_dynamic_005(self):
        """
        patch
        功能：delay/{delay}
        :return:
        """
        url = self.url + '/delay' + '/666'
        res = requests.patch(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_dynamic_006(self):
        """
        post
        功能：delay/{delay}
        :return:
        """
        url = self.url + '/delay' + '/666'
        res = requests.post(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_dynamic_007(self):
        """
        put
        功能：delay/{delay}
        :return:
        """
        url = self.url + '/delay' + '/666'
        res = requests.put(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_dynamic_008(self):
        """
        delete
        功能：drip
        :return:
        """
        url = self.url + '/drip'
        res = requests.put(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_dynamic_009(self):
        """
        get
        功能：/links/{n}/{offset}
        :return:
        """
        url = self.url + '/links' + '/11' + '/520'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_dynamic_010(self):
        """
        get
        功能：/range/{numbytes}
        :return:
        """
        url = self.url + '/range' + '/11'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_dynamic_011(self):
        """
        get
        功能：/stream-bytes/{n}
        :return:
        """
        url = self.url + '/stream-bytes' + '/11'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_dynamic_012(self):
        """
        get
        功能：/stream/{n}
        :return:
        """
        url = self.url + '/stream' + '/11'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)

    def test_dynamic_013(self):
        """
        get
        功能：/uuid
        :return:
        """
        url = self.url + '/uuid'
        res = requests.get(url)
        # 获取响应码
        print(res.status_code)
        # 获取响应内容---body
        if res.status_code == '200':
            print(res.text)
        else:
            print(res.status_code)


import unittest
import requests
import json


class TestShopping(unittest.TestCase):
    '''加入购物车操作'''
    def setUp(self):
        self.url_add = r'http://192.168.10.131/TinyShop_v1.7/index.php?con=index&act=cart_add'
        self.url_change = r'http://192.168.10.131/TinyShop_v1.7/index.php?con=index&act=cart_num'
        self.url_Del = r'http://192.168.10.131/TinyShop_v1.7/index.php?con=index&act=cart_del'
        self.re = requests.Session()
        print("setup")

    def test_t1(self):
        ''' 增加  id和数据正确'''
        data = {
            'id': '80',
            'num': '1'
        }
        r = self.re.post(self.url_add, data)
        self.assertNotEqual('[]', r.text)


    def test_t2(self):
        '''id不符合要求'''
        data = {
            'id': '9999',
            'num': '1'
        }
        r = self.re.post(self.url_add, data)
        # print(r.text)
        self.assertEqual('[]', r.text)

    def test_t3(self):
        '''id和数量为空'''
        data = {
            'id': '',
            'num': ''
        }
        r = self.re.post(self.url_add, data)
        # print(r.text)
        self.assertEqual('[]', r.text)


    def test_t4(self):
        '''id为空'''
        data = {
            'id': '',
            'num': '1'
        }
        r = self.re.post(self.url_add, data)
        # print(r.text)
        self.assertEqual('[]', r.text)

    def test_t5(self):
        '''数量为空'''
        data = {
            'id': '80',
            'num': ''
        }
        r = self.re.post(self.url_add, data)
        # print(r.text)
        self.assertEqual('[]', r.text)

    def test_t6(self):
        '''id正确，数量为负数'''
        data = {
            'id': '84',
            'num': '-1'
        }
        r = self.re.post(self.url_add, data)
        # print(r.text)
        self.assertEqual('[]', r.text)

    def test_t7(self):
        '''修改购物车商品数量'''
        data = {
            'id': '84',
            'num': '2'
        }
        r = self.re.post(self.url_change, data)
        # print("%%%%%%"+r.text)
        self.assertEqual('[]', r.text)

    #
    def test_t8(self):
        '''修改购物车商品数量为负数'''
        data = {
            'id': '84',
            'num': '-1'
        }
        r = self.re.post(self.url_change, data)
        # print(r.text)
        self.assertEqual('[]', r.text)

    def test_t9(self):
        '''修改购物车商品数量为0'''
        data = {
            'id': '84',
            'num': '0'
        }
        r = self.re.post(self.url_change, data)
        # print(r.text)
        self.assertEqual('[]', r.text)

    def test_t10(self):
        '''修改购物车商品数量为极大值'''
        data = {
            'id': '84',
            'num': '9999'
        }
        r = self.re.post(self.url_change, data)
        # print(r.text)
        self.assertEqual('[]', r.text)

    def test_t11(self):
        '''修改购物车商品数量为字符串'''
        data = {
            'id': '84',
            'num': 'san'
        }
        r = self.re.post(self.url_change, data)
        # print(r.text)
        self.assertEqual('[]', r.text)

    def test_t12(self):
        '''修改购物车商品数量为中文'''
        data = {
            'id': '84',
            'num': '一'
        }
        r = self.re.post(self.url_change, data)
        # print(r.text)
        self.assertEqual('[]', r.text)

    def test_t13(self):
        '''删除购物车商品'''
        data = {
            'id': '84',
        }
        r = self.re.post(self.url_Del, data)
        print(r.text)
        self.assertEqual('{"status":"success"}', r.text)

    def tearDown(self):
        print("teardown")


if __name__ == '__main__':
    unittest.main()

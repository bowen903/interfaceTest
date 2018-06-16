import unittest
import requests


class TestLogin(unittest.TestCase):
    '''登录模块'''

    def setUp(self):
        self.url = r'http://192.168.10.131/TinyShop_v1.7/index.php?con=simple&act=login_act'
        self.re = requests.Session()
        print("setup")

    def test_t1(self):
        '''用户名为空'''
        data = {
            'email': '',
            'password': '123456'
        }
        r = self.re.post(self.url, data)
        self.assertFalse('安全退出' in r.text)

    def test_t2(self):
        '''密码为空'''
        data = {
            'email': '123@123.com',
            'password': ''
        }
        r = self.re.post(self.url, data)
        self.assertFalse('安全退出' in r.text)

    def test_t3(self):
        '''用户名错误'''
        data = {
            'email': '123@3.com',
            'password': '123456'
        }
        r = self.re.post(self.url, data)
        self.assertFalse('安全退出' in r.text)

    def test_t4(self):
        '''密码错误'''
        data = {
            'email': '123@123.com',
            'password': '1236'
        }
        r = self.re.post(self.url, data)
        self.assertFalse('安全退出' in r.text)

    def test_t5(self):
        '''密码错误'''
        data = {
            'email': '123@123.com',
            'password': '156'
        }
        r = self.re.post(self.url, data)
        self.assertFalse('安全退出' in r.text)

    def test_t6(self):
        '''用户名密码均正确'''
        data = {
            'email': '3@qq.com',
            'password': '123456'
        }
        r = self.re.post(self.url, data)
        self.assertTrue('安全退出' in r.text)

    def test_t7(self):
        '''用户名格式错误'''
        data = {
            'email': '3@qq.',
            'password': '123456'
        }
        r = self.re.post(self.url, data)
        self.assertFalse('安全退出' in r.text)

    def test_t8(self):
        '''密码为中文'''
        data = {
            'email': '3@qq.',
            'password': '一二三'
        }
        r = self.re.post(self.url, data)
        self.assertFalse('安全退出' in r.text)

    def tearDown(self):
        print("teardown")


if __name__ == '__main__':
    unittest.main()

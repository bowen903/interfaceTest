import unittest,requests,re

class TestTianjia(unittest.TestCase):
    '''提交订单'''
    def setUp(self):
        self.data = {'email': '3@qq.com', 'password': '123456'}
        self.te = requests.session()
        self.r = self.te.post('http://192.168.10.156/TinyShop_v1.7/index.php?con=simple&act=login_act', self.data)
        # if '安全退出' in r.text:
        #     print('登陆成功')

        # 进入购物页面
        self.te.get('http://192.168.10.156/TinyShop_v1.7/index.php?con=index&act=product&id=21')

        # 加入购物车
        self.data3 = {'con': 'index', 'act': 'cart_add', 'id': '117', 'num': '1'}
        self.te.post('http://192.168.10.156/TinyShop_v1.7/index.php', self.data3)

        # 确认订单信息

        self.te.get('http://192.168.10.156/TinyShop_v1.7/index.php?con=simple&act=cart')

        # #提交订单
        # data5={'con':'simple','act':'order'}
        self.r = self.te.get('http://192.168.10.156/TinyShop_v1.7/index.php?con=simple&act=order')
        self.html = self.r.text
        self.passent = re.compile(r"<input type='hidden' name='tiny_token_order' value='(.*)'/>")
        self.content = self.passent.findall(self.html)[0]
        # print(content)
    def test_t1(self):
        '''所有请求正确'''
        self.data6 = {'con': 'simple', 'act': 'order_act', 'address_id': '2', 'payment_id': '1', 'user_remark': '',
                 'invoice_type': '0', 'invoice_title': '', 'tiny_token_order': self.content}
        self.e = self.te.post('http://192.168.10.156/TinyShop_v1.7/index.php?con=simple&act=order_act', self.data6)
        self.r = self.e.text
        self.assertTrue('订单已成功提交！' in self.r)
    def test_t2(self):
        '''地址选择错误'''
        self.data6 = {'con': 'simple', 'act': 'order_act', 'address_id': 'aa', 'payment_id': '1', 'user_remark': '',
                 'invoice_type': '0', 'invoice_title': '', 'tiny_token_order': self.content}
        self.e = self.te.post('http://192.168.10.156/TinyShop_v1.7/index.php?con=simple&act=order_act', self.data6)
        self.r = self.e.text
        self.assertFalse('订单已成功提交！' in self.r)

    def test_t3(self):
        '''地址为空'''
        self.data6 = {'con': 'simple', 'act': 'order_act', 'address_id': '', 'payment_id': '1', 'user_remark': '',
                      'invoice_type': '0', 'invoice_title': '', 'tiny_token_order': self.content}
        self.e = self.te.post('http://192.168.10.156/TinyShop_v1.7/index.php?con=simple&act=order_act', self.data6)
        self.r = self.e.text
        self.assertFalse('订单已成功提交！' in self.r)
    def test_t4(self):
        '''payment_id为空'''
        self.data6 = {'con': 'simple', 'act': 'order_act', 'address_id': '2', 'payment_id': '', 'user_remark': '',
                      'invoice_type': '0', 'invoice_title': '', 'tiny_token_order': self.content}
        self.e = self.te.post('http://192.168.10.156/TinyShop_v1.7/index.php?con=simple&act=order_act', self.data6)
        self.r = self.e.text
        self.assertFalse('订单已成功提交！' in self.r)
    def test_t5(self):
        '''payment_id为空'''
        self.data6 = {'con': 'simple', 'act': 'order_act', 'address_id': '2', 'payment_id': '1', 'user_remark': '',
                      'invoice_type': '0', 'invoice_title': '', 'tiny_token_order': self.content}
        self.e = self.te.post('http://192.168.10.156/TinyShop_v1.7/index.php?con=simple&act=order_act', self.data6)
        self.r = self.e.text
        self.assertFalse('订单已成功提交！' in self.r)

    def test_t6(self):
        '''tiny_token_order错误'''
        self.data6 = {'con': 'simple', 'act': 'order_act', 'address_id': '2', 'payment_id': '1', 'user_remark': '',
                      'invoice_type': '0', 'invoice_title': '', 'tiny_token_order': ''}
        self.e = self.te.post('http://192.168.10.156/TinyShop_v1.7/index.php?con=simple&act=order_act', self.data6)
        self.r = self.e.text
        self.assertFalse('订单已成功提交！' in self.r)
    def test_t7(self):
        '''con项为空,其他正确'''
        self.data6 = {'con': '', 'act': 'order_act', 'address_id': '2', 'payment_id': '1', 'user_remark': '',
                      'invoice_type': '0', 'invoice_title': '', 'tiny_token_order':self.content}
        self.e = self.te.post('http://192.168.10.156/TinyShop_v1.7/index.php?con=simple&act=order_act', self.data6)
        self.r = self.e.text
        self.assertFalse('订单已成功提交！' in self.r)

    def test_t8(self):
        '''con项为空,其他正确'''
        self.data6 = {'con': 'simple', 'act': 'order_act', 'address_id': '2', 'payment_id': '1', 'user_remark': '',
                      'invoice_type': '0', 'invoice_title': '', 'tiny_token_order': self.content}
        self.e = self.te.post('http://192.168.10.156/TinyShop_v1.7/index.php?con=simple&act=order_act', self.data6)
        self.r = self.e.text
        self.assertFalse('订单已成功提交！' in self.r)

    def test_t9(self):
        '''act项为空,其他正确'''
        self.data6 = {'con': 'simple', 'act': '', 'address_id': '2', 'payment_id': '1', 'user_remark': '',
                      'invoice_type': '0', 'invoice_title': '', 'tiny_token_order': self.content}
        self.e = self.te.post('http://192.168.10.156/TinyShop_v1.7/index.php?con=simple&act=order_act', self.data6)
        self.r = self.e.text
        self.assertFalse('订单已成功提交！' in self.r)
    def test_t10(self):
        '''invoice_type项为空,其他正确'''
        self.data6 = {'con': 'simple', 'act': 'order_act', 'address_id': '2', 'payment_id': '1', 'user_remark': '',
                      'invoice_type': '0', 'invoice_title': '', 'tiny_token_order': self.content}
        self.e = self.te.post('http://192.168.10.156/TinyShop_v1.7/index.php?con=simple&act=order_act', self.data6)
        self.r = self.e.text
        self.assertFalse('订单已成功提交！' in self.r)



    def tearDown(self):
        print("teardown")


if __name__ == '__main__':
    unittest.main()
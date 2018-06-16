import unittest
from flow.register import Register


class TestRegist(unittest.TestCase):
    '''注册模块'''

    def setUp(self):
        print("setup")

    def test_t1(self):
        '''用户名密码均正确【前提未被注册】'''
        self.assertEqual(Register('yis12@123.com','123456','123456').submit(),'注册成功')
    def test_t2(self):
        '''用户名存在'''
        self.assertEqual(Register('yis1@123.com','123456','123456').submit(),'注册失败')
    def test_t3(self):
        '''用户名为空'''
        self.assertEqual(Register('','123456','123456').submit(),'注册失败')
    def test_t4(self):
        '''两次密码不一致'''
        self.assertEqual(Register('yis12@123.com','123456','123').submit(),'注册失败')
    def test_t5(self):
        '''密码为空'''
        self.assertEqual(Register('yis12@123.com',' ','123').submit(),'注册失败')
    def test_t6(self):
        '''邮箱格式错误1：@后面没有参数'''
        self.assertEqual(Register('yis12@','123','123').submit(),'注册失败')
    def test_t7(self):
        '''邮箱格式错误2：没有@'''
        self.assertEqual(Register('yis123.com','123','123').submit(),'注册失败')

    def test_t8(self):
        '''密码小于6位'''
        self.assertEqual(Register('yis123.com', '12345', '12345').submit(), '注册失败')
    def test_t9(self):
        '''密码大于20位'''
        self.assertEqual(Register('yis123.com', '1234567890asdfghjklqw', '1234567890asdfghjklqw').submit(), '注册失败')
    def test_t10(self):
        '''密码含中文'''
        self.assertEqual(Register('yis123.com', '12三四五', '12三四五').submit(), '注册失败')


def tearDown(self):
    print("teardown")


if __name__ == '__main__':
    unittest.main()

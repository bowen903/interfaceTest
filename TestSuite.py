import os
import unittest


from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    test_dir=os.getcwd()+r'\testcase' # 测试用例的路径
    test_report_dir=os.getcwd()+r'\report'
    print(test_dir)
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='Test_*.py') #查找上面路径里所有以Test_开头的文件作为测试集
    isExists=os.path.exists(test_report_dir)
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(test_report_dir)
    filename = test_report_dir+'\\'+'result.html'
    f = open(filename, 'wb')

    runner = HTMLTestRunner(
            stream=f,
            title='测试报告',
            description='tinyshop接口测试报告'
    )
    runner.run(discover)

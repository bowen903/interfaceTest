# interfaceTest

### 项目介绍
* 使用requests库+单元测试框架unittest搭建的接口测试

### 被测项目
* tinyshop

### 项目结构
```
 --flow 业务流程
 --report 报告
 --testcase 测试用例
 --HTMLTestRunner.py 美化报告的文件
 --TestSuite.py 直接运行的文件
  
```

### 使用
1. 测试用例写在testcase文件夹下，测试用例以Test_开头即可
2. 运行TestSuite.py文件即可

### 待优化
* 写一个配置文件，将url提取出来，作为参数传入
* 注册模块，在teardown做还原环境的处理，删除数据库中刚才新增加的那条数据



# interfaceTest

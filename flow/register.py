import requests
import re
class Register:
    def __init__(self,username,password,repassword,verifyCode='aaaa'):
        self.session = requests.session()
        self.username = username
        self.password = password
        self.repassword = repassword
        self.verifyCode = verifyCode
    def get_PHPSESSID(self):
        url = 'http://192.168.10.131/TinyShop_v1.7/index.php'
        self.session.get(url)
        self.PHPSESSID = 'PHPSESSID='+self.session.cookies['PHPSESSID']
    def get_tiny_token_reg(self):
        tokenurl = 'http://192.168.10.131/TinyShop_v1.7/index.php?con=simple&act=reg'
        tokenheaders = {
            'Cookie': self.PHPSESSID
        }
        tokenhtml = self.session.get(tokenurl,headers = tokenheaders).text
        passent = re.compile(r"<input type='hidden' name='tiny_token_reg' value='(.*)'/>")
        self.token = passent.findall(tokenhtml)[0]
    def sumbit_register(self):
        tokenurl = 'http://192.168.10.131/TinyShop_v1.7/index.php?con=simple&act=reg_act'
        tokendata = {
            'email':self.username,
            'password':self.password,
            'repassword':self.repassword,
            'tiny_token_reg':self.token
        }
        tokenheaders = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': self.PHPSESSID,
            'Referer': 'http://192.168.10.131/TinyShop_v1.7/index.php?con=simple&act=reg',
        }
        self.tokenhtml = self.session.post(tokenurl,headers =tokenheaders ,data = tokendata).text
        # print(self.tokenhtml)
    def isSuccess(self):
        # 判断注册的用户名是否在返回的页面中
        passent =re.compile(r'<input type="hidden" name="user_name" value="(.*)" /><input type="hidden"')
        content = passent.findall(self.tokenhtml)[0]
        if content ==self.username:
            return('注册成功')
        else:
            return('注册失败')
    def submit(self):
        try:
            self.get_PHPSESSID()
            self.get_tiny_token_reg()
            self.sumbit_register()
            return self.isSuccess()
        except Exception:
            return('注册失败')
if __name__ == "__main__":
    a=Register('yis14@123.com','123456','123456').submit()
    print(a)
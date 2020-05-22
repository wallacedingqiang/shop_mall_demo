import time


class Admin(object):
    admin='1'
    password='1'


    #管理员界面
    def AdminView(self):
        print("**********************************************")
        print("*                                            *")
        print("*                                            *")
        print("*               欢迎登录风暴银行              *")
        print("*                                            *")
        print("*                                            *")
        print("**********************************************")

    # 功能界面
    def FunctionView(self):
        print("**********************************************")
        print("*           开户（1）     查询（2）          *")
        print("*           取款（3）     存款（4）          *")
        print("*           转账（5）     改密码（6)         *")
        print("*           锁定（7）     解锁（8）          *")
        print("*           补卡（9）     销户（10）         *")
        print("*                   退出（0）                *")
        print("**********************************************")


    #管理员验证：
    def Check(self):
        inputadmin=input("请输入管理员帐号")
        if self.admin !=inputadmin:
            print("帐号输入错误")
            return -1
        inputpassword=input("请输入密码")
        if self.password !=inputpassword:
            print("密码输入错误")
            return -1
        print("输入正确")
        time.sleep(2)
        return 0


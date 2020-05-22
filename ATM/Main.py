import pickle
import time
from ATM.AtmMac import ATM
from ATM.Admin import *
import pysnooper

@pysnooper.snoop()
def main():
    # 界面对象
    admin = Admin()

    # 管理员开机
    admin.AdminView()
    if admin.Check():
        return -1

    # 提款机对象
    allusers = {}
    filepath = "userinfo.txt"
    try:
        with open(filepath, "rb") as file:
            allusers = pickle.load(file)
            if not isinstance(allusers, dict):
                allusers = {}
    except EOFError:
        return {}
    print(allusers)
    atm = ATM(allusers)



    while True:
        admin.FunctionView()
        # 等待用户操作
        option = input("请输入您的操作：")
        if option == '1':
            # 开户
            atm.CreatUser()
        elif option == '2':
            # 查询
            atm.searchUserInfo()
        elif option == '3':
            # 取款
            atm.getMoney()
        elif option == '4':
            # 存款
            atm.saveMoney()
        elif option == '5':
            # 转账
            atm.transferMoney()
        elif option == '6':
            # 改密码
            atm.changePasswd()
        elif option == '7':
            # 锁定
            atm.lockUser()
        elif option == '8':
            # 解锁
            atm.unlockUser()
        elif option == '9':
            # 补卡
            atm.newCard()
        elif option == '10':
            # 销户
            atm.killUser()
        elif option == '0':
            # 退出
            if not admin.Check():
                # 将当前系统中的用户信息保存到文件中
                f = open(filepath, "wb")
                pickle.dump(atm.allUsers, f)
                f.close()
                return -1

        time.sleep(2)


if __name__=="__main__":
    main()



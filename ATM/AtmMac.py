import random
from ATM.Card import *
from ATM.Person import *

class ATM(object):
    def __init__(self,allusers):
        self.allusers=allusers


    #创建用户
    def CreatUser(self):
        name=input("请输入姓名")
        idman=input("请输入身份证号")
        phone=input("请输入电话号码")
        premoney=int(input("请输入预存金额"))
        if premoney<0:
            print("输入预存金额有误，开户失败")
            return -1
        password=input("请输入密码")
        #验证密码
        if not self.checkPassword(password):
            print("密码设置错误，开户失败")
            return -1

        #生成卡号
        cardId=self.createCardId()


        card=Card(cardId,password,premoney)
        user=Person(name,idman,phone)

        self.allusers[cardId]=user

        print(user)

        print("开户成功，请牢记卡号(%s)"  %cardId)

    #查询余额
    def searchuserifo(self):
        cardnum=input("请输入卡号")
        #验证是否存在该卡号
        user=self.allusers.get(cardnum)
        if not user:
            print("该卡号不存在，查询失败")
            return -1
        #判断是否锁定
        if user.card.cardlock==True:       #user什么意思？
            print('该卡已经被锁定，请解锁完成后续操作')
            return -1

        #验证密码
        if not self.checkpassword(user.card.cardpassword):
            print("密码错误，该卡已经被锁定")
            user.card.cardlock==True
            return -1

        #查询成功，输出结果
        print("账户： %s    余额：  %d"   %(user.card.idcard,int(user.card.cardmoney)))

        # 存款
    def saveMoney(self):
            cardnum = input("请输入您的卡号：")
            # 验证是否存在该卡号
            user = self.allUsers.get(cardnum)
            if not user:
                print("该卡号不存在，查询失败......")
                return -1
            # 判断是否锁定
            if user.card.cardlock == True:
                print("该卡已经被锁定，请解锁后再使用其他操作......")
                return -1
            # 验证密码
            if not self.checkPasswd(user.card.cardpasswd):
                print("密码错误，该卡已经被锁定......")
                user.card.cardlock = True
                return -1
            savemoney = int(input("请输入您存款金额："))
            nowmoney = int(user.card.cardmoney)
            nowmoney += savemoney
            user.card.cardmoney = nowmoney
            print("取款成功，您目前余额为：%d" % user.card.cardmoney)

        # 转账
    def transferMoney(self):
            cardnum = input("请输入您的卡号：")
            # 验证是否存在该卡号
            user = self.allUsers.get(cardnum)
            if not user:
                print("该卡号不存在，查询失败......")
                return -1
            # 判断是否锁定
            if user.card.cardlock == True:
                print("该卡已经被锁定，请解锁后再使用其他操作......")
                return -1
            # 验证密码
            if not self.checkPasswd(user.card.cardpasswd):
                print("密码错误，该卡已经被锁定......")
                user.card.cardlock = True
                return -1
            # 查询成功，输出结果
            print("账户：%s     余额：%d" % (user.card.cardid, int(user.card.cardmoney)))
            tocardid = input("请输入您希望转账的账户：")
            # 验证是否存在该卡号
            usertoid = self.allUsers.get(tocardid)
            if not usertoid:
                print("该卡号不存在，查询失败......")
                return -1
            tomoney = int(input("请输入您希望转账的金额："))
            nowmoney = int(user.card.cardmoney)
            tonowmoney = int(usertoid.card.cardmoney)
            if tomoney > nowmoney:
                print("余额不足，转账失败......")
                return -1
            nowmoney -= tomoney
            tonowmoney += tomoney
            user.card.cardmoney = nowmoney
            usertoid.card.cardmoney = tonowmoney
            print("转账成功，您目前余额为：%d" % user.card.cardmoney)

            # 改密码
    def changePasswd(self):
                cardnum = input("请输入您的卡号：")
                # 验证是否存在该卡号
                user = self.allUsers.get(cardnum)
                if not user:
                    print("该卡号不存在，查询失败......")
                    return -1
                # 判断是否锁定
                if user.card.cardlock == True:
                    print("该卡已经被锁定，请解锁后再使用其他操作......")
                    return -1
                # 验证密码
                if not self.checkPasswd(user.card.cardpasswd):
                    print("密码错误，该卡已经被锁定......")
                    user.card.cardlock = True
                    return -1
                newpasswd = input("请输入新密码：")
                newpasswd2 = input("请确认新密码:")
                if newpasswd != newpasswd2:
                    print("两次密码输入不一致，密码修改失败")
                    return -1
                user.card.cardpasswd = newpasswd
                print("密码修改成功......")

                # 锁定

    def lockUser(self):
        cardnum = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardnum)
        if not user:
            print("该卡号不存在，查询失败......")
            return -1
        if user.card.cardlock:
            print("该卡已经被锁定，请结束后再使用其他功能")
            return -1
        # 验证密码
        if not self.checkPasswd(user.card.cardpasswd):
            print("密码错误......")
            return -1
        # 锁定
        user.card.cardlock = True
        print("锁定成功......")

        # 解锁
        def unlockUser(self):
            cardnum = input("请输入您的卡号：")
            # 验证是否存在该卡号
            user = self.allUsers.get(cardnum)
            if not user:
                print("该卡号不存在，解锁失败......")
                return -1
            if not user.card.cardlock:
                print("该卡没有锁定，无需解锁......")
                return -1
            # 验证密码
            if not self.checkPasswd(user.card.cardpasswd):
                print("密码错误,解锁失败......")
                return -1
            temid = input("请输入您的身份证号：")
            if temid != user.idCard:
                print("身份证号输入错误，解锁失败......")
                return -1
            # 解锁
            user.card.cardlock = False
            print("解锁成功......")

        # 补卡
        def newCard(self):
            cardnum = input("请输入您的卡号：")
            # 验证是否存在该卡号
            user = self.allUsers.get(cardnum)
            if not user:
                print("该卡号不存在，查询失败......")
                return -1
                # 验证密码
            if not self.checkPasswd(user.card.cardpasswd):
                print("密码错误......")
                return -1
            # 重新生成卡号
            newcard = self.creatCardId()
            user.card.cardid = newcard
            print("补卡办理成功，这是您的新卡号：%s" % user.card.cardid)

        # 销户
        def killUser(self):
            cardnum = input("请输入您的卡号：")
            # 验证是否存在该卡号
            user = self.allUsers.get(cardnum)
            if not user:
                print("该卡号不存在，查询失败......")
                return -1
                # 验证密码
            if not self.checkPasswd(user.card.cardpasswd):
                print("密码错误，销户失败......")
                return -1
            self.allUsers.pop(cardnum)
            print("该账户已经被销户......")

        # 验证密码,循环三次没有正确就输出错误
    def checkPassword(self, realPasswd):
            for i in range(3):
                temPasswd = input("请确认密码：")
                if temPasswd == realPasswd:
                    return True
            return False

        # 随机生成卡号
    def createCardId(self):
            # 验证密码是否重复
            while True:
                str = ""
                for i in range(6):
                    ch = chr(random.randrange(ord('0'), ord('9') + 1))
                    str += ch
                # 判断是否重复
                if not self.allUsers.get(str):
                    return str







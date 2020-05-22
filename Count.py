import sqlite3

class CountDataBase():
    '''定义了一个数据库操作类'''
    def __init__(self, id):
        self.id = id  # 当用户登录成功后 记录登录id

    '''查询账户余额'''
    def selectmoney_db(self,id):
        conn = sqlite3.connect('atm_data.db')  # 创建一个数据库链接
        cmdselect = "SELECT MONEY FROM USERS WHERE ID = {}".format(id)
        message = conn.execute(cmdselect)  # 查询该用户信息的SQL语句
        for i in message:
            print('你余额为:{}'.format(i))
            conn.commit()
            conn.close()
            return i
        else:
            return '没有此用户的信息...'


        '''购物车扣款'''
    def cart_withdraw(self,user_money,id):
            conn = sqlite3.connect('atm_data.db')  # 创建一个数据库链接
            before_money = self.selectmoney_db(id)  # 取钱之前的余额
            cmdpay="UPDATE USERS SET MONEY = \"{}\" WHERE ID = {}".format(before_money[0] - user_money,id) # 执行取钱的SQL操作
            conn.execute(cmdpay)
            print('购物共消费{}元,还剩{}元.'.format(user_money, before_money[0] - user_money))  # 打印出 取出的金额和余下的金额
            conn.commit()
            conn.close()




    def select_db(self):
        '''查询该账户的所有信息
        >>>"{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序
        'hello world'
        '''
        conn = sqlite3.connect('atm_data.db')  # 创建一个数据库链接
        cmdselect = "SELECT MONEY FROM USERS WHERE ID = {}".format(self.id)
        message = conn.execute(cmdselect)  # 查询该用户信息的SQL语句
        for i in message:
            print('你余额为:{}'.format(float(i[0])))
            conn.commit()
            conn.close()
            return i
        else:
            return '没有此用户的信息...'


    def select_other_db(self, other_ID):
        '''查询该账户的所有信息'''
        conn = sqlite3.connect('atm_data.db')  # 创建一个数据库链接
        message = conn.execute("SELECT MONEY FROM USERS WHERE ID = {}".format(other_ID))  # 查询指定id的余额信息.
        for i in message:
            print('转给他人余额为:{}'.format(i))
            conn.commit()
            conn.close()
            return i
        else:
            return '没有此用户的信息...'

    def withdraw(self, user_money):
        '''取钱'''
        conn = sqlite3.connect('atm_data.db')  # 创建一个数据库链接
        before_money = self.select_db()  # 取钱之前的余额
        conn.execute(
            "UPDATE USERS SET MONEY = \"{}\" WHERE ID = {}".format(before_money[0] - user_money, self.id))  # 执行取钱的SQL操作
        print('取出{}元,还剩{}元.'.format(user_money, before_money[0] - user_money))  # 打印出 取出的金额和余下的金额
        conn.commit()
        conn.close()


    def transfer_accounts(self, other_ID, turn_money,user_money):
        '''转账'''
        if self.id == other_ID:
            print('不能给自己转账')
            return None
        conn = sqlite3.connect('atm_data.db')  # 创建一个数据库链接
        #user_money = self.select_db()  # 己方转账之前的余额
        cmdtransfer1="UPDATE USERS SET MONEY = \"{}\" WHERE ID = {}".format(user_money[0] - turn_money, self.id)
        conn.execute(cmdtransfer1)  # 执行己方的转账操作
        other_money = self.select_other_db(other_ID)  # 对方转账之前的余额
        cmdtransfer2="UPDATE USERS SET MONEY = \"{}\" WHERE ID = {}".format(other_money[0] + turn_money, other_ID)
        conn.execute(cmdtransfer2)  # 执行对方的转账操作
        print('自己转出:{},还剩{}'.format(turn_money, user_money[0] - turn_money))  # 打印出己方的余额
        print('对方转入:{},还剩{}'.format(turn_money, other_money[0] + turn_money))  # 打印出对方的余额
        conn.commit()
        conn.close()

    def wallet(self, user_money):
        '''存钱'''
        conn = sqlite3.connect('atm_data.db')  # 创建一个数据库链接
        before_money = self.select_db()  # 存钱之前的余额
        cmdwallet="UPDATE USERS SET MONEY = {} WHERE ID = {}".format(before_money[0] + float(user_money), self.id)
        print("存钱SQL语句：")
        print(cmdwallet)
        conn.execute(cmdwallet)  # 执行存钱的操作
        print('存入{}元,现在{}元.'.format(user_money, before_money[0] + float(user_money)))  # 打印出存钱后的余额
        conn.commit()
        conn.close()

    def checking_money(self, turn_money):
        '''检查余额是否足够,足够返回True,否则返回False'''
        conn = sqlite3.connect('atm_data.db')  # 创建一个数据库链接
        before_money = self.select_db()  # 使用钱之前的钱
        if before_money[0] - turn_money >= 0:  # 余额不能为负数
            conn.commit()
            conn.close()
            return True
        else:
            conn.commit()
            conn.close()
            return False

    def checking_password(self, password):
        '''检查密码是否正确,正确返回True,否则返回False'''
        conn = sqlite3.connect('atm_data.db')  # 创建一个数据库链接
        before_password = conn.execute("SELECT PASSWORD FROM USERS WHERE ID = {}".format(self.id))  # SQL查询正确密码
        for i in before_password:  # 判断旧密码是否正确
            if i[0] == password:
                conn.commit()
                conn.close()
                return True
            else:
                conn.commit()
                conn.close()
                return False
        else:
            conn.commit()
            conn.close()
            return '没有找到此账户.'






class UserCountControl():
    def cun(self):
        '''获取存钱的输入'''
        while True:
            try:
                user_money = int(input('请输入您存入的金额:\n'))
            except:
                print('您的输入不符合规范,请重试.')
                continue
            listA = [user_money]  # 输入合规范后 将数据以列表的方式返回
            return listA



    def qu(self):
        '''获取取钱的输入'''
        while True:
            try:
                user_money = int(input('请输入您取出的金额:\n'))
            except:
                print('您的输入不符合规范,请重试.')
                continue
            listA = [user_money]  # 输入合规范后 将数据以列表的方式返回
            return listA



    def zhuan(self):
        '''获取转账的输入'''
        while True:
            try:
                other_ID = int(input('请输入对方账号:\n'))
                turn_money = float(input('请输入转账金额:\n'))
            except:
                print('您的输入不符合规范,请重试.')
                continue
            listA = [other_ID, turn_money]  # 输入合规范后 将数据以列表的方式返回
            return listA
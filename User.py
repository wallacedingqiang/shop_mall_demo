import sqlite3


class UserDataBase():
    '''定义了一个数据库操作类.'''
    def __init__(self, id):
        self.id = id  # 当用户登录成功后 记录登录id


    def insert_db(self,ID_user, PASSWORD_user, NAME_user, MONEY_user=0):
        '''将用户输入的用户信息写入到数据库'''
        conn = sqlite3.connect('atm_data.db')  # 创建一个数据库链接
        cmd = "INSERT INTO USERS (ID,PASSWORD,NAME,MONEY) VALUES ({},\"{}\",\"{}\",{})".format(ID_user, PASSWORD_user,
                                                                                               NAME_user,
                                                                                               MONEY_user)  # 将用户输入的信息写入数据库
        print(cmd)
        conn.execute(cmd)  # 写入数据到数据库
        conn.commit()  # 提交
        conn.close()  # 关闭数据库链接


    def del_db(self,user_ID):
        '''注销账户用,将账户的用户信息删除'''
        conn = sqlite3.connect('atm_data.db')  # 创建一个数据库链接
        cmd = "DELETE FROM USERS WHERE ID = {}".format(user_ID)  # 命令
        conn.execute(cmd)  # 删除该账号
        # 验证一下用户名 和 密码 确认删除 否则 return 请重新输入账号
        conn.commit()
        conn.close()

    def updata_db(self, user_password):
        '''更改密码'''
        conn = sqlite3.connect('atm_data.db')  # 创建一个数据库链接
        conn.execute("UPDATE USERS SET PASSWORD = \"{}\" WHERE ID = {}".format(user_password, self.id))  # 传入用户的新密码 进行更改
        print('更新信息完成.')
        conn.commit()
        conn.close()

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

class UserControl():
    def register_user(self):
        '''注册 / 注销 用户输入信息入口'''
        while True:
            try:
                user_ID = int(input('请输入您的账号:\n'))
                user_password = str(input('请输入您的密码:\n'))
                user_password2 = str(input('请再次输入您的密码:\n'))
                user_name = str(input('请输入开户人的姓名:\n'))
            except:
                print('输入信息不符合规范,请重试...')
                continue
            listA = [user_ID, user_password, user_password2, user_name]  # 将用户输入的信息以列表的方式返回.
            print("listA:")
            print(listA)
            return listA


    def login_user(self):
        '''登录信息录入'''
        while True:
            try:
                user_ID = int(input('请输入您需要登录的账号:\n'))
                user_password = str(input('请输入您的密码:\n'))
            except:
                print('登录信息有误,请重试.')
                continue
            listA = [user_ID, user_password]  # 将用户输入的信息以列表的方式返回.
            return listA

    def modify_information(self):
        '''用户修改密码的输入'''
        while True:
            try:
                user_password0 = str(input('请输入你的旧密码:\n'))
                user_password = str(input('请输入你的新密码:\n'))
                user_password2 = str(input('请再次输入你的新密码:\n'))
            except ValueError:
                print('您的输入不符合规范,请重新输入.')
                continue
            listA = [user_password0, user_password, user_password2]  # 输入合规范后 将数据以列表的方式返回
            return listA



class Verification():
    '''检查账户是否合规的类'''
    def validate_logon(self, user_ID, user_password):
        '''查询该账户的所有信息,核对密码是否正确'''
        conn = sqlite3.connect('atm_data.db')  # 创建一个数据库链接
        check = conn.execute("SELECT PASSWORD FROM USERS WHERE ID = {}".format(user_ID))  # 核对账户密码是否正确
        # check = conn.execute("SELECT PASSWORD FROM USERS WHERE ID = 999999")
        #print(user_ID)
        for i in check:
            print(i[0])
            if i[0] == str(user_password):
                conn.commit()
                conn.close()
                return True
            else:
                conn.commit()
                conn.close()
                return False

    def checking_ID(self, user_ID):
        '''检查该ID是否存在,如已存在返回False,否则返回True'''
        conn = sqlite3.connect('atm_data.db')  # 创建一个数据库链接
        check = conn.execute("SELECT ID FROM USERS WHERE ID = {}".format(user_ID))  # 查询数据库中的ID是否存在
        for i in check:
            if i[0] == user_ID:
                conn.commit()
                conn.close()
                return False
            else:
                conn.commit()
                conn.close()
                return True
        else:
            return True

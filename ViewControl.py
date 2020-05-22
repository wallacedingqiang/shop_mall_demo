from User import *
from admingoods import *
from shopcart import *
import pysnooper

class ViewControl():
    def __init__(self):
        self.database = GoodsDataBase('')
        self.admin = admincontrol()
        self.shopcart = Shopcart()

    @pysnooper.snoop()
    def login(self):
        """登录功能"""
        user = UserControl()
        verification = Verification()
        print("==========欢迎登录蔷蔷购物商场==========")
        listA = user.login_user()  # 获取用户账号 密码"""
        if verification.validate_logon(listA[0], listA[1]):  # 检查账户密码是否一致
            while True:
                  if listA[0] == 999999:
                       if listA[1] == "888888":
                         print("欢迎您，商品admin管理员")
                         self.adminwork()              #执行商品管理员功能
                       else:
                         print("管理员密码错误，登录失败！")
                  else:
                         print("欢迎您，%s用户" % (listA[0]))
                         self.usework(listA)           # 执行用户购买功能
        else:
           print("用户名密码错误")





    def adminwork(self):
        admin_menu = """
        ==========欢迎进入蔷蔷购物商场后台管理系统==========
            输入功能编号，您可以选择以下功能：
            输入“1”：显示所有商品的信息
            输入“2”：显示对应商品的信息
            输入“3”：添加商品的信息
            输入“4”：删除商品的信息
            输入“5”：修改商品的信息
            输入“6”：退出系统功能
        ==========================================
            """
        print(admin_menu)
        while True:
            try:
                code = input("请输入功能编号:>")
            except (IOError, ValueError):
                print('------------------------------')
                print('输入错误,请重新输入.')
                continue

            if code == "1":
                self.database.search_db()

            elif code == "2":
                '''查询商品方法输入信息入口'''
                while True:
                    selectID = input("请输入要查询的商品ID：")
                    self.database.select_db(selectID)
                    break
                else:
                    print('您没有输入正确账户信息,请重新选择您要操作的选项.')
                    break

            elif code == "3":
                while True:
                    print('您正在执行增加商品的操作：')
                    listA = self.admin.addGoods()  # 获取商品的ID、名称、价格
                    self.database.insert_db(
                        listA[0], listA[1], listA[2])  # 写入数据库
                    print('增加成功')
                    break
                else:
                    print('您没有输入正确账户信息,请重新选择您要操作的选项.')
                    break

            elif code == "4":
                while True:
                    delID = self.admin.delGoods()
                    self.database.del_db(delID)
                    print("删除成功")
                    break
                else:
                    print("没有找到对应的商品")
                    break

            elif code == "5":
                while True:
                    '''查询商品方法输入信息入口'''
                    selectID = self.admin.selectGoods()
                    self.database.select_db(selectID)
                    '''修改商品方法输入信息入口'''
                    listA = self.admin.updateGoods()
                    self.database.updata_db(selectID,listA[0], listA[1])
                    print("修改成功")
                    break
                else:
                    print("没有找到对应的商品")
                    break

            elif code == "6":
                print("感谢您的使用，正在退出系统！！")
                break

        else:
            print("输入编号有误，请重新输入！！")



    def usework(self, lists):
        user = UserControl()
        userdatabase = UserDataBase('')
        verification = Verification()  # 实例化一个检查类

        while True:
            index_User_Menu = '''
            ------------------------------------------------------------------------------
                                                用户管理

            ------------------------------------------------------------------------------
            【1】账户查询    【2】注册账号    【3】注销账号     【4】进入商城    【5】退出
            '''
            print(index_User_Menu)

            #print('1.账户查询\n2.注册账号\n3.注销账号\n4.购买\n5.退出')

            try:
                select = int(input('请输入您本次的操作序号:\n'))
            except (IOError, ValueError):
                print('------------------------------')
                print('输入错误,请重新输入.')
                continue



            if select == 1:
                self.after_logging(lists)  # 进入登录后的主程序

            elif select == 2:
                while True:
                    print('您正在执行注册账户的操作.')
                    listA = user.register_user()  # 获取用户注册信息 账户 密码 用户名
                    if verification.checking_ID(
                            listA[0]) and listA[1] == listA[2]:  # 检查注册ID是否重复 两次密码是否一致
                        userdatabase.insert_db(
                            listA[0], listA[1], listA[3])  # 将用户信息写入数据库
                        print('注册成功,您现在可以登录使用了.')
                        break
                    else:
                        print('您没有输入正确账户信息,请重新选择您要操作的选项.')
                        break

            elif select == 3:
                while True:
                    print('您正在执行注销账户的操作,没有取出的余额将不予退还.')
                    listA = user.register_user()  # 获取 账号 密码 密码 用户名
                    # 检查账户是否存在 账号密码是否一致 两次密码是否一致
                    if (not verification.checking_ID(listA[0])) and verification.validate_logon(
                            listA[0], listA[1]) and (listA[1] == listA[2]):
                        user.del_db(listA[0])  # 执行注销操作
                        print('注销成功,系统中已经不再有您的个人信息了.')
                        break
                    else:
                        print('您没有输入正确的账户信息,请重新选择您要操作的选项.')
                        break

            elif select == 4:
                self.usershopping(lists)

            elif select == 5:
                print('正在退出,请稍候.')
                return '本次交易已退出'
            else:
                print('------------------------------')
                print('输入错误,请重新输入.')
                continue
            print('------------------------------')


     # 登录之后的主函数
    def after_logging(self, listafter):
        user = UserControl()  # 实例化一个用户
        userCountControl = UserCountControl()  # 实例化一个账户
        verification = Verification()  # 实例化一个检查类
        countDataBase = CountDataBase(listafter[0])  # 实例化，传用户ID
        userdatabase = UserDataBase(listafter[0])

        while True:
            index_UserCard_Menu = '''
            ------------------------------------------------------------------------------
                                                ATM管理——信用卡管理

            ------------------------------------------------------------------------------
            【1】查询账户余额    【2】取款    【3】存款     【4】转账    【5】修改密码    【6】退出
            '''
            print(index_UserCard_Menu)

            try:
                select2 = int(input('请输入您本次的操作序号:\n'))
            except (IOError, ValueError):
                print('------------------------------')
                print('输入错误,请重新输入.')
                continue

            list_people = []   #创建用户操作卡对象

            if select2 == 1:  # 查询余额
               user_money=countDataBase.select_db()

            elif select2 == 2:  # 取款操作
                list_people = userCountControl.qu()  # 获取用户输入的 取款金额 存放在列表里
                if countDataBase.checking_money(list_people[0]):  # 检查用户余额是否足够
                    countDataBase.withdraw(list_people[0])  # 执行取钱操作
                    continue
                else:
                    print('余额不足,请重试.')
                    continue

            elif select2 == 3:  # 存款操作
                list_people = userCountControl.cun()  # 获取用户存款的金额
                if list_people[0] > 0:  # 判断存款金额是否正常
                    countDataBase.wallet(list_people[0])
                    continue
                else:
                    print('您存款的金额不对请重试.')
                    continue

            elif select2 == 4:  # 转账操作
                list_people = userCountControl.zhuan()  # 获取对方账号 获取转账金额
                if verification.checking_ID(
                    list_people[0]) or (
                    not countDataBase.checking_money(
                        list_people[1])):  # 检查对方ID存在为False 检查余额不足够就False
                    print('对方账户不存在或转出金额超出余额,请核对后再试...')
                    continue
                else:
                    countDataBase.transfer_accounts(
                        list_people[0], list_people[1],user_money)  # 执行转账操作
                    continue

            elif select2 == 5:  # 修改密码
                list_people = user.modify_information()  # 获取一个旧密码 两个新密码
                if list_people[1] == list_people[2] and userdatabase.checking_password(
                        list_people[0]):  # 两个新密码一致 并且 旧密码正确
                    userdatabase.updata_db(list_people[1])  # 满足上述条件  执行修改密码操作
                    continue
                else:
                    print('旧密码不正确,或两次新密码不一致.')
                    continue

            elif select2 == 6:  # 退出
                print('正在退出,请稍候.')
                return '本次交易已退出'
            else:
                print('------------------------------')
                print('输入错误,请重新输入.')
                continue
            print('------------------------------')



    def usershopping(self, lists):
        # 等待命令
        while True:
          index_UserShopping_Menu = '''
                    ------------------------------------------------------------------------------
                                                        商场管理

                    ------------------------------------------------------------------------------
                    【1】添加    【2】修改    【3】删除     【4】结算    【5】保存    【6】退出
                    '''
          print(index_UserShopping_Menu)

          try:
            cmd = int(input('请输入您本次的操作序号:\n'))
          except (IOError, ValueError):
            print('------------------------------')
            print('输入错误,请重新输入.')
            continue

          if cmd == 1:
                self.shopcart.add(lists[0])
                self.shopcart.shopcart_list()

          elif cmd == 2:
                self.shopcart.edit()
                self.shopcart.shopcart_list()

          elif cmd == 3:
                self.shopcart.delete()
                self.shopcart.shopcart_list()

          elif cmd == 4:
                self.shopcart.payment(lists[0])

          elif cmd == 5:
                self.shopcart.shoplist_insertdb()

          elif cmd == 6:
            print("感谢您的使用，返回上级界面！！")
            return '本次交易已退出'

        else:
            print("输入编号有误，请重新输入！！")

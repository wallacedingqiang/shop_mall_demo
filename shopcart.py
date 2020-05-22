import time
from Goods import *
from Count import *

# 定义购物清单对象
shop_list = []


class Shopcart():
    def __init__(self):
        self.database = GoodsDataBase('')
        self.countdatabase = CountDataBase('')


    def shopcart_list(self):
        print("=" * 100)
        # 如果清单不为空的时候，输出清单的内容
        if not shop_list:
            print("还未购买商品")
        else:
            title = "%-5s|%15s|%40s|%10s|%4s|%10s" % \
                    ("ID", "商品编号", "商品名称", "单价", "数量", "小计")
            print(title)
            # 记录总计的价钱
            sum = 0
            # 遍历代表购物清单的list列表
            for i, item in enumerate(shop_list):
                # 转换id为索引加1
                id = i + 1
                sum = sum + item[4]
                line = "%-5s|%17s|%40s|%12s|%6s|%12s" % \
                       (id, item[0], item[1], item[2], item[3], item[4])
                print(line)
            print("                                                                                        总计: ", sum)
        print("=" * 100)
        # 添加购买商品，就是向代表用户购物清单的list列表中添加一项。


    def add(self, username):
        # 显示商品库存，创建库存对象
        repository_goods = list(self.database.getallgoods_db())
        print("=" * 50 +"商品列表"+"="*50)
        title = "%-10s|%-10s|%40s|%15s" % ("商品序号","商品编号", "商品名称", "商品价格")
        print(title)
        for index, info in enumerate(repository_goods, start=1):
            line = "%-12s|%-12s|%42s|%17s" % (index,info[0], info[1], info[2])
            print(line)
        print("-" * 100)

        # 等待输入条码
        code = int(input("请输入购买商品的序号:\n"))
        # 没有找到对应的商品，序号错误
        if code > len(repository_goods):
            print("序号错误，请重新输入")
            return
        # 获取商品条码读取商品，再获取商品的名称
        name = repository_goods[code - 1][1]
        # 获取商品条码读取商品，再获取商品的单价
        price = repository_goods[code - 1][2]

        # 等待输入数量
        number = int(input("请输入购买数量:\n"))
        # 计算购买商品小计
        amount = price * number
        # 把商品和购买数量封装成list后加入购物清单
        shop_list.append([code, name, price, number, amount, username])
        # 修改购买商品的数量，就是修改代表用户购物清单的list列表的元素

    def edit(self):
        id = input("请输入要修改的购物明细项的ID:\n")
        # id减1得到购物明细项的索引
        index = int(id) - 1
        # 根据索引获取某个购物明细项
        item = shop_list[index]
        # 提示输入新的购买数量
        number = input("请输入新的购买数量:\n")
        # 修改item里面的number
        item[3] = int(number)
        #修改item里面的amount
        amount = item[2] * item[3]
        item[4]=float(amount)




    # 删除购买的商品明细项，就是删除代表用户购物清单的list列表的一个元素。
    def delete(self):
        id = input("请输入要删除的购物明细项的ID: ")
        index = int(id) - 1
        # 直接根据索引从清单里面删除掉购物明细项
        del shop_list[index]



    def payment(self, username):
        # 先打印清单
        self.shopcart_list()
        user_money_tuple = self.countdatabase.selectmoney_db(username)
        user_money = float(user_money_tuple[0])
        print("账户余额为：",user_money)
        car_money = 0
        for i in shop_list:
            car_money += i[4]
        if user_money >= float(car_money):
            self.countdatabase.cart_withdraw(float(car_money), username)
        else:
            print("余额不足！！")
        print('\n' * 3)
        print("欢迎下次光临")



    def shoplist_insertdb(self):
        '''将用户输入的用户信息写入到数据库'''
        # 生成订单编号
        order_num = self.get_order_code()
        conn = sqlite3.connect('atm_data.db')  # 创建一个数据库链接
        for item in shop_list:
            cmd = "INSERT INTO shoplist (idgoods,namegoods,pricegoods,numgoods,amount,ordernum,username) VALUES ({},\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")".format(
                item[0], item[1], item[2], item[3], item[4], order_num, item[5])   # 将用户输入的信息写入数据库
            conn.execute(cmd)  # 写入数据到数据库
        conn.commit()  # 提交
        conn.close()  # 关闭数据库链接

    # 生成订单号
    def get_order_code(self):
        order_no = str(time.strftime('%Y%m%d%H%M%S', time.localtime(
            time.time()))) + str(time.time()).replace('.', '')[-7:]
        return order_no

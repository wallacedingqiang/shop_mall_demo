import sqlite3


class GoodsDataBase():
    def __init__(self,ID):
        print(ID)
        self.ID=ID

    def search_db(self):
        '''查询所有商品'''
        conn=sqlite3.connect('atm_data.db')
        cmd="select ID,name,price from goods"
        message=conn.execute(cmd)
        print("=" * 100)
        title = "%-10s|%40s|%15s" % ("商品编号", "商品名称", "商品价格")
        print(title)
        for info in message:
            line = "%-12s|%42s|%17s" % (info[0], info[1] ,info[2])
            print(line)
        conn.commit()
        conn.close()
        print("=" * 100)

    def getallgoods_db(self):
            '''查询所有商品'''
            conn = sqlite3.connect('atm_data.db')
            cmd = "select ID,name,price from goods"
            message = conn.execute(cmd)
            good_list = list()
            for info in message:
                good_list.append(info)
            conn.commit()
            conn.close()
            return good_list



    def insert_db(self,ID_goods,name_goods,price_goods):
        '''将用户输入的用户信息写入到数据库'''
        conn = sqlite3.connect('atm_data.db')  # 创建一个数据库链接
        cmd = "INSERT INTO goods (ID,name,price) VALUES ({},\"{}\",\"{}\")".format(ID_goods, name_goods,price_goods)  # 将用户输入的信息写入数据库
        conn.execute(cmd)  # 写入数据到数据库
        conn.commit()  # 提交
        conn.close()  # 关闭数据库链接


    def del_db(self,ID_goods):
        '''删除对应的商品信息'''
        conn=sqlite3.connect('atm_data.db')
        cmd="Delete from goods where ID={}".format(ID_goods)
        conn.execute(cmd)
        conn.commit()
        conn.close()


    def select_db(self,ID_goods):
        '''查询显示对应的商品信息'''
        conn=sqlite3.connect('atm_data.db')
        selectdb="select ID,name,price from goods where ID= {}".format(ID_goods)
        message=conn.execute(selectdb)
        print("=" * 100)
        title = "%-10s|%40s|%15s" % ("商品编号", "商品名称", "商品价格")
        print(title)
        for info in message:
            line = "%-12s|%42s|%17s" % (info[0], info[1] ,info[2])
            print(line)
            print("=" * 100)
        conn.commit()
        conn.close()


    def qudb(self,ID_goods):
        '''查询对应的商品信息'''
        conn=sqlite3.connect('atm_data.db')
        selectdb="select ID,name,price from goods where ID= {}".format(ID_goods)
        message=conn.execute(selectdb)
        for info in message:
            return info
        conn.commit()
        conn.close()


    def updata_db(self,ID_goods,name_goods,price_goods):
        '''修改对应的商品信息'''
        conn=sqlite3.connect('atm_data.db')
        cmd="UPDATE goods SET name = \"{}\",price = \"{}\" WHERE ID = {}".format(name_goods,price_goods,ID_goods)
        conn.execute(cmd)
        conn.commit()
        conn.close()
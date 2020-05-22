class admincontrol():
    def addGoods(self):
            '''添加商品方法输入信息入口'''
            while True:
                try:
                    ID_goods = int(input('请输入商品ID:\n'))
                    name_goods = str(input('请输入商品名称:\n'))
                    price_goods = str(input('请输入商品价格:\n'))
                except:
                    print('输入信息不符合规范,请重试...')
                    continue
                listA = [ID_goods, name_goods, price_goods]  # 将用户输入的信息以列表的方式返回.
                return listA

    def delGoods(self):
        '''删除商品方法输入信息入口'''
        while True:
            try:
                ID_goods=input("请输入要删除的商品ID:")
            except:
                print('输入信息不符合规范,请重试...')
                continue
            delID=ID_goods
            return delID



    def selectGoods(self):
        '''查询商品方法输入信息入口'''
        while True:
            try:
                ID_goods=input("请输入要查询的商品ID：")
            except:
                print('输入信息不符合规范,请重试...')
                continue
            return ID_goods

    def updateGoods(self):
        '''修改商品方法输入信息入口'''
        while True:
            try:
                #ID_goods=input("请输入要修改的商品ID：")
                name_goods=input("请输入要修改的商品名称：")
                price_good=input("请输入修改的价格:")
            except:
                print('输入信息不符合规范,请重试...')
                continue
            listA=[name_goods,price_good]
            return listA
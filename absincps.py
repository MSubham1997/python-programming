class Product:
    def __init__(self):
        self.__Productid= ""
        self.__ProductName= ""
        self.__Price=""


    def setProduct(self, pid,pname,price):
        self.__Productid=pid
        self.__ProductName=pname
        self.__Price=price

    def showProduct(self):
        print("Product Id :{} \n Product Name: {}\n Product Price: {} ".format(self.__Productid,self.__ProductName,self.__Price))

tv=Product()
tv.setProduct("tv102020","Sony Bravia",22000)
tv.showProduct()
tv.__ProductName="Pixel"
tv.showProduct()

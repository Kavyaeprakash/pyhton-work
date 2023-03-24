class Product:
    count =0
    def __init__(self,name,category,price):
        self.name=name
        self.category=category
        self.__price=price
        Product.count=Product.count+1

    def display_products(self):
        print("name:",self.name)
        print("category:",self.category)
    
    def product_count(self):
        print("Total number of products: %d" %Product.count)
    @property
    def price(self):
        print('geting value')
        return self.__price
    @price.setter
    def price(self,price):
        print('setting value')
        if price>25:
            raise ValueError('price should not exceed 25')
        self.__price=price

    


product1=Product('pen','stationary','20')
product2=Product('orange','food','45')
# print(product1.__price)
# print(product2.category)
# product1.display_products()
# product1.product_count()
# product2.product_count()
# product1.name='book'
# print(product1.name)
# print(product1.getprice())
# product1.setprice(12)
# print(product1.getprice())
print(product1.price)
product1.price=20
print(product1.price)

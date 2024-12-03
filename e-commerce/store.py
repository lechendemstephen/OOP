
class Product: 
    products = {
        
    }
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name 
        self.price = price 

    # add products 
    def add_products(self): 
        Product.products[self.product_id] = {
            'name': self.name,
            'price': self.price
        }
        print('product added')
    
    #show all products 
    def all_products(self): 
        for product, details in Product.products.items(): 
            print(product)
            print(details)
            print('\n')
class Order(Product): 
    products = Product.products 
    orders = {}

    def __init__(self):
        pass
      

  
    # make an order 
    def make_order(self, product_id): 
        for id, details in Order.products.items():
            if product_id == id: 
                Order.orders[product_id] = {
                    'name': details['name'], 
                    'price': details['price']
                }
                

    # show all orders 
    def show_orders(self): 
       costs = []
       total_cost = 0

       for id, order in Order.orders.items():
           costs.append(order['price']) 
          
           for cost in costs:
               total_cost += cost     

                # print('your order: \n ')
                # print(f"Products: {order['name']},")
                # print(f'total cost: {total_cost}')
       print(total_cost)
       print(cost)





product1 = Product(1, 'Shoe', 203)
product2 = Product(2, 'Cap', 260)


product1.add_products()
product2.add_products()

product1.all_products()

order1 = Order() 
order1.make_order(1)
order1.make_order(2)
order1.show_orders()



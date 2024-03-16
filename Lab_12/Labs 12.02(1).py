'''Lab_12'''
class Item:
    '''Item'''
    def __init__(self, name, price, weight):
        '''Self'''
        self.name = name
        self.price = price
        self.weight = weight

    def get_name(self):
        '''Get_Name'''
        return self.name

    def get_price(self):
        '''Get_Price'''
        return self.price

    def get_weight(self):
        '''Get_Weight'''
        return self.weight

    def get_cost(self):
        '''Get_Cost'''
        return self.price / self.weight

def main():
    '''Main'''
    import json
    item_in = json.loads(input())
    item = Item(item_in["name"], item_in["price"], item_in["weight"])
    print(item.get_name(), item.get_price(), item.get_weight(), sep='\n')

main()

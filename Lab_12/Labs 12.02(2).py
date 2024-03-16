"""lab12.02-2 KnapSack"""
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

def knapsack(amount, item_list):
    '''Knapsack'''
    cur_weight = 0
    cur_price = 0
    s_item_list = sorted(item_list, key=lambda x: x.get_cost(), reverse=True)
    print("Knapsack Size: %.1f kg"  % (amount))
    print("===============================")
    for i in s_item_list:
        if cur_weight + i.get_weight() <= amount:
            cur_weight += i.get_weight()
            cur_price += i.get_price()
            print(i.get_name() + " -> " + str(i.get_weight()) + " kg -> " + \
                   str(i.get_price()) + " THB")
        else:
            break
    print("Total: %d THB" % int(cur_price))

def main():
    '''Main'''
    import json
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(
            Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(knapsack_capacity, items)

main()

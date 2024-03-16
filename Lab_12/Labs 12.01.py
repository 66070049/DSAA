'''Lab_12'''
import json
def convert_key(data):
    """JSON"""
    return {int(k): v for k, v in data.items()}
def coin_exchange(amount, coin):
    '''Coin_Exchange'''
    change = {10:0, 5:0, 2:0, 1:0}
    total = sum(coin.values())
    check = False
    for i in coin:
        if amount < 0:
            break
        elif total < 0:
            check = True
            break
        else:
            while i <= amount and coin.get(i) > 0:
                amount -= i
                coin[i] -= 1
                change[i] += 1
                total -= 1
                if total <= 0 and amount > 0:
                    check = True
                    break
    if check is False:
        return change
    else:
        change = 1
        return change

def main(amount, inp):
    '''Main'''
    coin = convert_key(json.loads(inp))
    change = coin_exchange(amount, coin)
    if change != 1:
        total = sum(change.values())
        print("Amount: {}\nCoin exchange result: \
            \n  10 baht = {} coins\n  5 baht = {} coins \
            \n  2 baht = {} coins\n  1 baht = {} coins \
            \nNumber of coins: {}" .format(amount, change.pop(10), change.pop(5), \
            change.pop(2), change.pop(1), total))
    else:
        print("Amount: %d\nCoins are not enough."%amount)
main(int(input()), input())
    
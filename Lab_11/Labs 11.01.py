'''Lab_11'''
import json
def insertionsort(inp, last): #เทียบซ้ายไปขวา
    '''Insertion_Sort'''
    count = 0
    check = 0
    for i in range(1, last+1):
        key = inp[i]
        check = i - 1
        while check >= 0 and key < inp[check]:
            inp[check + 1] = inp[check]
            check -= 1
            count += 1
        if check >= 0 and key > inp[check]:
            count += 1
        inp[check + 1] = key
        print(inp)
    print("Comparison times:", count)
def main():
    '''Main'''
    inp = json.loads(input())
    num = int(input())
    insertionsort(inp, num)

main()

'''Lab_11'''
import json
def insertionsort(inp, last): #เทียบซ้ายไปขวา
    '''Insertion_Sort'''
    count = 0
    check = 0
    for i in range(1, last+1):
        key = inp[i]
        check = i - 1
        while check >= 0 and compare(key, inp[check], '<'):
            inp[check + 1] = inp[check]
            check -= 1
            count += 1
        if check >= 0 and compare(key, inp[check], '>'):
            count += 1
        inp[check + 1] = key
        print(inp)
    print("Comparison times:", count)
def main():
    '''Main'''
    inp = json.loads(input())
    num = int(input())
    insertionsort(inp, num)

def compare(val1, val2, condi):
    val1 = split_value(val1)
    val2 = split_value(val2)

    if condi == "<":
        return val1[0] < val2[0] and val1[1] < val2[1]
    elif condi == ">":
        return val1[0] > val2[0] and val1[1] > val2[1]

def split_value(val):
    return val[0], int(val[1:])

main()
# print(compare("A94", "A740"))
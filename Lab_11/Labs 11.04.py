'''Lab_11'''
import json
def insertionsort(inp, last): #เทียบซ้ายไปขวา
    '''Insertion_Sort'''
    count = 0
    check = 0

    for i in range(1, last+1):
        key = inp[i][0], int(inp[i][1:])
        # print(inp[check][0], inp[check][1:])
        sorter2 = inp[check][0], int(inp[check][1:])
        check = i - 1
        while (check >= 0 and (key[0] < sorter2[0] or (key[0] == sorter2[0] and key[1] < sorter2[1]))):
            inp[check + 1] = inp[check]
            check -= 1
            count += 1
        if check >= 0 and (key[0] < sorter2[0] or (key[0] == sorter2[0] and key[1] < sorter2[1])):
            count += 1
        inp[check + 1] = key[0] + str(key[1])
        print(count)
        print(inp)
    print("Comparison times:", count)
def main():
    '''Main'''
    inp = json.loads(input())
    num = int(input())
    insertionsort(inp, num)

main()

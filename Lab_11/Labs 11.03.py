'''Lab_11'''
import json
def bubblesort(inp, last):
    '''BubbleSort'''
    count = 0
    sort = False
    for i in range(last+1):
        if sort is False:
            sort = True
            for j in range(last, i, -1):
                if inp[j] < inp[j-1]:
                    inp[j], inp[j-1] = inp[j-1], inp[j]
                    count += 1
                    sort = False
                else:
                    count += 1
        if sort is True:
            print(inp)
            break
        print(inp)
    print("Comparison times: %d"%count)
 
def main():
    '''Main'''
    inp = json.loads(input())
    num = int(input())
    bubblesort(inp, num)
main()

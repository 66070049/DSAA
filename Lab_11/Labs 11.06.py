'''Lab_11'''
import json
def bubblesort(inp, last): #เทียบ1ตัวขวาไปซ้ายละวนลูปจนsort
    '''BubbleSort'''
    count = 0
    sort = False
    for i in range(last+1):
        if sort is False:
            sort = True
            for j in range(last, i, -1):
                if inp[j][0] == inp[j-1][0]: #ตัวอักษรเหมือนกัน
                    count += 1
                    if int(inp[j][1:]) < int(inp[j-1][1:]): 
                        inp[j], inp[j-1] = inp[j-1], inp[j]
                        sort = False
                elif ord(inp[j][0]) < ord(inp[j-1][0]): #ตัวอักษรต่างกัน
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

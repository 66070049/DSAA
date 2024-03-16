'''Lab_11'''
import json
def selectionsort(inp, last): #หาค่าที่น้อยที่สุดแล้วเทียบจนหาค่าน้อยที่สุดแล้วสลับ
    '''SelectionSort'''
    count = 0
    for i in range(last):
        min_n = inp[i]
        for j in range(i + 1, last + 1):
            if inp[j][0] == min_n[0]: #ตัวอักษรเหมือนกัน
                count += 1
                if int(inp[j][1:]) < int(min_n[1:]):
                    min_n = inp[j]
            elif ord(inp[j][0]) < ord(min_n[0]): #ตัวอักษรต่างกัน
                min_n = inp[j]
                count += 1
            else:
                count += 1
        inp[inp.index(min_n)], inp[i] = inp[i], inp[inp.index(min_n)]
        print(inp)
    print("Comparison times: %d" % count)


def main():
    '''Main'''
    inp = json.loads(input())
    num = int(input())
    selectionsort(inp, num)
main()

'''Lab_09'''
import time
def summation_1(num):
    '''Summation (Type 1)'''
    total = 0
    for i in range(1, num+1):
        total += i
    print(total)
summation_1(int(input()))

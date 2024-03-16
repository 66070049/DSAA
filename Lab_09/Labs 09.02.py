'''Lab_09'''
import json
def isintersect():
    '''Is_intersect'''
    l_a = list(json.loads(input()))
    l_b = list(json.loads(input()))
    l_c = list(json.loads(input()))
    check = 0
    for i in l_a:
        if i in l_b and i in l_c:
            check += 1
    if check == 0:
        return False
    else:
       return True
    
print(isintersect())

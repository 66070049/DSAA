'''Lab_12'''
import json
def Radio(_, num):
    choice_city = []
    res_dict = []
    checker_val = []
    checker_dict = []
    for i in range(num):
        val_ue = json.loads(input())
        choice_city.append(val_ue)

    sorted_choice_city = sorted(choice_city, key=lambda x: len(x["Cities"]), reverse=True)
    for i in sorted_choice_city:
        counter = 0
        new_check = []
        if res_dict == []:
            res_dict.append(i["Name"])
            checker_val.extend(i["Cities"])
        else:
            for j in i["Cities"]:
                if j not in checker_val:
                    counter += 1
                    new_check.append(j)
            checker_dict.append([i["Name"], new_check, int(counter)])

    for i in sorted(checker_dict, key=lambda x: x[2], reverse=True):
        if i[2] != 0 and all(city not in checker_val for city in i[1]):
            res_dict.append(i[0])
            checker_val.extend(i[1])
    print(checker_dict)
    print(sorted(res_dict))
Radio(json.loads(input()), int(input()))
#!/usr/bin/python3
def common_elements(set_1, set_2):
    list_1 = list(set_1)
    list_2 = list(set_2)
    res = []
    for ele1 in list_1:
        for ele2 in list_2:
            if ele1 == ele2:
                res.append(ele1)
    return (res)

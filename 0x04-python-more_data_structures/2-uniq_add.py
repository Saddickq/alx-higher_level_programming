#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    if my_list:
        set_list = set(my_list)
        for num in set_list:
            sum += num
        return (sum)
    else:
        return (sum)

#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        sum = 0
        set_list = set(my_list)
        for num in set_list:
            sum += num
        return (sum)

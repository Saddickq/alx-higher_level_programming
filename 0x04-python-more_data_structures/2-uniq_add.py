#!/usr/bin/bash
def uniq_add(my_list=[]):
    if my_list:
        sum = 0
        for num in set(my_list):
            sum += num
        return (sum)

#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        new_list = []
        for num in my_list:
            if (num % 2) == 0:
                new_list.append(1)
            else:
                new_list.append(0)
        return (new_list)

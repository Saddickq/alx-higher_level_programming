#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    if (idx < 0 or idx >= len(copy)):
        return (copy)
    for i in range(len(copy)):
        if (i == idx):
            copy.remove(copy[i])
            copy.insert(i, element)
            return (copy)

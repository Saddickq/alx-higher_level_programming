#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l_t1 = list(tuple_a)
    l_t2 = list(tuple_b)
    res = []
    for i in range(2):
        l_t1.append(0)
        l_t2.append(0)
    res = [l_t1[0] + l_t2[0], l_t1[1] + l_t2[1]]
    return (tuple(res))

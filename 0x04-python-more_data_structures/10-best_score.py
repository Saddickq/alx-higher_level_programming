#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    maxv = float('-inf')
    maxk = None
    for k, v in a_dictionary.items():
        if v > maxv:
            maxk = k
            maxv = v
    return maxk


a_dictionary = { "a": 1, "b": 2, "c": 3, "d": 4, "e": 5 }
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))

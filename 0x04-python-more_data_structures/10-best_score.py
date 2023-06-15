#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best = a_dictionary[0]
        print(a_dictionary[0])
        for key in a_dictionary:
            if (a_dictionary[key] > best):
                best = a_dictionary[key]
                print(best)
            return(key)
    else:
        return


a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))

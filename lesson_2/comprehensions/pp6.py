# Given the following data structure, return a new list identical in structure
# to the original but, with each number incremented by 1. Do not modify the
# original data structure. Use a comprehension

def inc_value(dict1):
    return {key: value + 1 for key, value in dict1.items()}


lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]


newlist = [inc_value(item) for item in lst]

print(newlist)

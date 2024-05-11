lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

# Given the following data structure, write some code to return a list
# that contains only the dictionaries where all the integers are even.

# Loop over every dictionary in original list,
# Check if all lists within said dictionary are even
#   - for each list in the dictionary, check if all the values are even
#   - if they are, continue to next list, otherwise, return False
# If so, append to new list


def all_lists_even(dictionary):
    for key, value in dictionary.items():
        for item in value:
            if item % 2:
                return False
    return True


new_list = []

for dictionary in lst:
    if all_lists_even(dictionary):
        new_list.append(dictionary)

print(new_list)

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

# Given the following data structure, write some code to return a list
# that contains the colors of the fruits and the sizes of the vegetables.
# The sizes should be uppercase, and the colors should be capitalized.

list1 = []
for entry in dict1:
    if dict1[entry]['type'] == 'fruit':
        list1.append([color.capitalize()
                      for color in dict1[entry]['colors']])
    else:
        list1.append(dict1[entry]['size'].upper())

print(list1)

produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}


def select_fruit(dict1):
    selected = {}
    for item, category in dict1.items():
        print(item, category)
        if category == 'Fruit':
            selected[item] = category 
    return selected


print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

lst2 = [sorted(item, key=str) for item in lst]
print(lst2)

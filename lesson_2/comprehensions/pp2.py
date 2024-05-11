lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

lst2 = [sorted(item) for item in lst]
print(lst2)

lst3 = lst[::]
for item in lst3:
    item.sort()
print(lst3)

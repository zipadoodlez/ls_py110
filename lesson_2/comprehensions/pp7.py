lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

newlist = [[item for item in sublist if item % 3 == 0]
           for sublist in lst]

print(newlist)

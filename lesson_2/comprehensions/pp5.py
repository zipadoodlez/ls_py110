# Given the following data structure, sort the list so that the sub-lists are
# ordered based on the sum of the odd numbers that they contain. You shouldn't
# mutate the original list.
lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]


def odd_sum(list1):
    return sum([num for num in list1 if num % 2])


lst2 = sorted(lst, key=odd_sum)
print(lst2)

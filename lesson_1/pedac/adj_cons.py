CONSONANTS = set('bcdfghjklmnpqrstvwxyz')

example = ['hello world', 'ajkhfa', 'yesyes']


def adj_cons(list1):
    list2 = [[string, 0] for string in list1]
    for i in range(len(list2)):
        cc = 0
        for char in list2[i][0].replace(' ', ''):
            if char in CONSONANTS:
                cc += 1
            else:
                if cc > 1:
                    list2[i][1] += cc
                cc = 0
        if cc > 1:
            list2[i][1] += cc
    list2.sort(key=lambda tup: tup[1], reverse=True)
    for i in range(len(list2)):
        list2[i] = list2[i][0]
    return list2


my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(adj_cons(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(adj_cons(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(adj_cons(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(adj_cons(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(adj_cons(my_list))
# ['xxxx', 'xxxb', 'xxxa']
print(adj_cons(example))

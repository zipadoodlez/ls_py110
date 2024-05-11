VOWELS = 'aeiou'

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

list_of_vowels = []

# for key, lst in dict1.items():
#    for word in lst:
#        for char in word:
#            if char in VOWELS:
#                list_of_vowels.append(char)

list2 = [char for key in dict1
         for word in dict1[key]
         for char in word if char in VOWELS]


print(list2)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']

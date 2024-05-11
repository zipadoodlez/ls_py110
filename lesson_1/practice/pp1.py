fruits = ("apple", "banana", "cherry", "date", "banana")

# How would you count the number of occurrences of "banana" in the tuple?

counter = 0
for fruit in fruits:
    if fruit == 'banana':
        counter += 1

# or

count = fruits.count('banana')

# Given the following string, create a dictionary that represents the frequency
# with which each letter occurs. The frequency count should be case-sensitive:

statement = "The Flintstones Rock"

counter = {}
statement = statement.replace(' ', '')
for char in statement:
    if not counter.get(char):
        counter[char] = 1
    else:
        counter[char] += 1

print(counter)

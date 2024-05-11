ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

# Calculate the total age given the following dictionary:

counter = 0
for age in ages.values():
    counter += age

min_age = min(ages.values())
print(min_age)

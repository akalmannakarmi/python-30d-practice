# The following is a list of 10 students ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print(ages[0])
print(ages[-1])

# Add the min age and the max age again to the list
ages.append(ages[0])
ages.append(ages[-1])

# Find the median age (one middle item or two middle items divided by two)
ages.sort()
print(ages[int(len(ages)/2)])

# Find the average age (sum of all items divided by their number )
a =sum(ages)/len(ages)
print(a)

# Find the range of the ages (max minus min)
print(ages[-1]-ages[0])

# Compare the value of (min - average) and (max - average), use abs() method
print(abs(ages[0]-a) > abs(ages[1]-a))

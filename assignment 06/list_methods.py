# extend
# adds the specified list elements to the end of the current list
fruits = ['apple', 'banana', 'cherry']
other_fruits = ['peach', 'watermelone', 'pineapple']
fruits.extend(other_fruits)
print(fruits)

# index
# returns the position at the first occurrence of the specified value
fruits = ['apple', 'banana', 'cherry']
print(fruits.index("cherry"))

# insert
# inserts the specified value at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

# copy
# returns a copy of the specified list
fruits = ["apple", "banana", "cherry"]
print(fruits.copy())

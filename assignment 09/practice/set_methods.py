# add
## The add() method adds an element to the set.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# remove
## The remove() method removes the specified element from the set.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# copy
## The copy() method copies the set.
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)

# clear
## The clear() method removes all elements in a set.
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# discard
## The discard() method removes the specified item from the set.
### This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# update
## The update() method updates the current set, by adding items from another set (or any other iterable).
## If an item is present in both sets, only one appearance of this item will be present in the updated set.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
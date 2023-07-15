# copy
## The copy() method returns a copy of the specified dictionary.
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.copy()
print(x)

# clear
## The clear() method removes all the elements from a dictionary.
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.clear()
print(car)

# pop
## The pop() method removes the specified item from the dictionary.
### The value of the removed item is the return value of the pop() method, see example below.
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.pop("model")
print(car)

# update
## The update() method inserts the specified items to the dictionary.
### The specified items can be a dictionary, or an iterable object with key value pairs.
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.update({"color": "White"})
print(car)

# keys
## The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
### The view object will reflect any changes done to the dictionary, see example below.
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.keys()
print(x)

# values
## The values() method returns a view object. The view object contains the values of the dictionary, as a list.
### The view object will reflect any changes done to the dictionary, see example below.
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.values()
print(x)

# items
## The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
### The view object will reflect any changes done to the dictionary, see example below.
car = {"brand": "Ford","model": "Mustang","year": 1964}
x = car.items()
print(x)

# get
## The get() method returns the value of the item with the specified key.
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.get("model")
print(x)
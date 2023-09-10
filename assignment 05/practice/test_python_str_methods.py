# title
# Make the first letter in each word upper case
text = "Welcome to my world"
print(text.title())

# is title
# Check if each word start with an upper case letter
text = "Hello, And Welcome To My World!"
print(text.istitle())

# find
# method finds the first occurrence of the specified value
text = "Hello, welcome to my world."
print(text.find("welcome"))

# replace
# method replaces a specified phrase with another specified phrase
text = "I like bananas"
print(text.replace("bananas", "apples"))

# rstrip
# Remove any white spaces at the end of the string
text = "     banana     "
print("of all fruits", text.rstrip(), "is my favorite")

# lstrip
# Remove spaces to the left of the string
text = "     banana     " 
print("of all fruits", text.lstrip(), "is my favorite")

# rjust
# right align the string, using a specified character (space is default) as the fill character
text = "banana"
print(text.rjust(20), "is my favorite fruit.")

# ljust
# left align the string, using a specified character (space is default) as the fill character
text = "banana"
print(text.ljust(20), "is my favorite fruit.")

# zfill
# Fill the string with zeros until it is 10 characters long
text = "50"
print(text.zfill(10))

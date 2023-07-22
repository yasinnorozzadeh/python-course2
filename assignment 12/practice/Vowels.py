def vowels(string):
    for s in string:
        if   ord(s) ==  97 or ord(s) == 65: # a
            string = string.replace(s, "!")
        elif ord(s) == 101 or ord(s) == 69: # e
            string = string.replace(s, "!")
        elif ord(s) == 105 or ord(s) == 73: # i
            string = string.replace(s, "!")
        elif ord(s) == 111 or ord(s) == 79: # o
            string = string.replace(s, "!")
        elif ord(s) == 117 or ord(s) == 85: # u
            string = string.replace(s, "!")
    return string

string = input("enter youre string: \n")
print(vowels(string))
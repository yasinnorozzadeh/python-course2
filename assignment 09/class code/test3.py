text = input("text: ")
text_dict = {}
for char in text:
    if char in text_dict:
        text_dict[char] += 1
    else:
        text_dict[char] = 1

print(text_dict)
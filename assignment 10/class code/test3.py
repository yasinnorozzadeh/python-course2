import random

Animals = ["cat", "dog"]
#  Animals = ["cat", "bat", "turtle", "spider", "dog", "ant", "elephant", "goat", "giraffe", "kitten", "scorpian", "monkey", "lion", "deer"]
word = random.choice(Animals)
hearts = (len(word) * 1.5) // 1
show_word = []
for i in range(len(word)):
    show_word.append("_")
# print("_"* len(word))
while True:
    # print word hearts
    print(" ".join(show_word))
    print("*" * int(hearts))
    if hearts == 0:
        print("Game over")
        break
    user_char = input("enter character : ")
    # check_end_game
    if not("_" in show_word):
        print("Hip Hip Hoorey!")
        break
    # new_char
    if user_char in word:
        idx = word.index(user_char)
        show_word[idx] = user_char
    else:
        print("this is not exist")
        hearts -= 1

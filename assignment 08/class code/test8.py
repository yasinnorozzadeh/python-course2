import random
clothes = ['green', "blue", "red", "yellow", "gray", "gold", "white", "pink", "purple", "black"]
party_name = input("youre party name:\n")
cloth = random.choice(clothes)
print(f"youre clothes in{party_name} is {cloth}")
length = int(input("ernter length of diamond range(odd numbers): "))
print("💙 🧡 💛 💜 💚 🤎 🤍 💘 💖 💝 💗 💓")
char = input("enter youre character from imoji lists\n")
for i in range(length):
    print((length - i) * "  ", end='')
    print((i * 2 - 1) * char)

for i in range(length, 0, -1):
    print((length - i) * "  ", end='')
    print((i * 2 - 1) * char)

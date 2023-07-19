import random
def player1_2_player2():
    number = int(input("player1: enter youre number:(range = 0 to 100)\t"))
    while True:
        input_number = int(input("player2: enter youre number:(range = 0 to 100)\t"))
        if input_number == number :
            print("you win!")
            break
        elif input_number > number:
            print("player2 go down!")
        else:
            print("player2 go up!")

def player2_2_player1():
    number = int(input("player2: enter youre number:(range = 0 to 100)\t"))
    while True:
        input_number = int(input("player1: enter youre number:(range = 0 to 100)\t"))
        if input_number == number :
            print("you win!")
            break
        elif input_number > number:
            print("player1 go down!")
        else:
            print("player1 go up!")
   
def player_2_computer():
    number = int(input("player1: enter youre number:(range = 0 to 100)\t"))
    upperـbound = 100
    lowerـbound = 0
    input_number = random.randint(lowerـbound, upperـbound)
    while True:
        if input_number == number :
            print(f"computer number is:{input_number}", "computer win!")
            break
        elif input_number > number:
            print(f"computer number is:{input_number}", "go down!")
            upperـbound = input_number
            input_number = random.randint(lowerـbound, upperـbound-1)
        else:
            print(f"computer number is:{input_number}", "go up!")
            lowerـbound = input_number
            input_number = random.randint(lowerـbound + 1, upperـbound)

def computer_2_player():
    number = random.randint(0, 100)
    while True:
        input_number = int(input("enter youre number:\t"))
        if input_number == number :
            print("you win!")
            break
        elif input_number > number:
            print("go down!")
        else:
            print("go up!")

def check(start_game):
    if start_game == 1:
        player1_2_player2()
        
    elif start_game == 2:
        player2_2_player1()

    elif start_game == 3:
        player_2_computer()

    elif start_game == 4:
        computer_2_player()
    else:
        print("youre number doesnt find")

while True:
    start_game = int(input("1_player1 vs player2\n2_player2 vs player1\n3_player vs computer\n4_computer vs player\n\tenter youre number: "))
    check(start_game)
    try_again = input("do you want to try again?(y, n):\t") # try again
    if try_again == "n":
        break
import random
import fontstyle
import pyfiglet
from termcolor import colored

def choose_user(number):
    if number == 1:
        number = rps[0]
    elif number == 2:
        number = rps[1]
    elif number == 3:
        number = rps[2]
    else:
        number = "youre number is out of range(1 to 3)\npelease try again!"
    return number
def check_game(user, user2, number):
    if (user == "rock" and user2 == "scissors") or (user == "scissors" and user2 == "paper" ) or (user == "paper" and user2 == "rock"):
        if number == 1:
            win = "player"
        else:
            win = "player1"
    elif (user2 == "rock" and user == "scissors") or (user2 == "scissors" and user == "paper") or (user2 == "paper" and user == "rock"):
        if number == 1:
            win = "computer"
        else:
            win = "player2"
    elif user == user2:
        win = 0
    return win
def check_winer(user_score, heighest_score, user_name):
    if user_score == heighest_score:
        winer = user_name
    else:
        winer = ""
    return winer
rps = ["rock", "paper", "scissors"]
result1 = colored(pyfiglet.figlet_format(('Welcome to rock paper scissors Game '), font = "digital"), "green")
print(result1)
while True:
    user = int(input("1_player vs computer\n2_player vs player\nenter number of your choice: "))
    heighest_score = int(input("enter the highest score from (1, 3, 5): "))
    if user == 1:
        player = 0
        computer = 0
        while True:
            user_choice = int(input("1_rock\n2_paper\n3_scissors\nenter number of your choice: "))
            computer_choice = random.choice(rps)
            user = choose_user(user_choice)
            if not(user == "youre number is out of range(1 to 3)\npelease try again!"):
                print("palyer:", user, "computer:", computer_choice)
                winer_r = check_game(user, computer_choice, 1)
                if winer_r == 0:
                    text = fontstyle.apply("equal", 'bold/Italic/red/GREEN_BG')
                    print(text)
                else:
                    locals()[winer_r] += 1
                    winer_all = check_winer(locals()[winer_r], heighest_score, winer_r)
                    text = fontstyle.apply(f"{winer_r} is win for this round", 'bold/Italic/red/GREEN_BG')
                    print(text)
                    if not(winer_all == ""):
                        text = fontstyle.apply(f"{winer_all} is winer", 'bold/Italic/red/GREEN_BG')
                        print(text)
                        break
    elif user == 2:
        player1 = 0
        player2 = 0
        while  True:
            user1_choice = int(input("player1\n1_rock\n2_paper\n3_scissors\nenter number of your choice: "))
            user2_choice = int(input("player2\n1_rock\n2_paper\n3_scissors\nenter number of your choice: "))
            user1 = choose_user(user1_choice)
            user2 = choose_user(user2_choice)
            if not(user == "youre number is out of range(1 to 3)\npelease try again!"):
                print("palyer1:", user1, "palyer2:", user2)
                winer_r = check_game(user1, user2, 2)
                if winer_r == 0:
                    text = fontstyle.apply("equal", 'bold/Italic/red/GREEN_BG')
                    print(text)
                else:
                    locals()[winer_r] += 1
                    winer_all = check_winer(locals()[winer_r], heighest_score, winer_r)
                    text = fontstyle.apply(f"{winer_r} is win for this round", 'bold/Italic/red/GREEN_BG')
                    print(text)
                    if not(winer_all == ""):
                        text = fontstyle.apply(f"{winer_all} is winer", 'bold/Italic/red/GREEN_BG')
                        print(text)
                        break
    else:
        print("your number is out off range!")
    try_again = input("do you want to try again??(y, n)")
    if not(try_again == "y"):
        break
result = colored(pyfiglet.figlet_format('Good Bye! '), 'green')
print(result)

import random
import pyfiglet
from termcolor import colored
import fontstyle


rps = ["rock", "paper", "scissors"]
trry = True
check = False
score_user = 0
score_computer = 0
score_user1 = 0
score_user2 = 0
winer = None
# 
result1 = colored(pyfiglet.figlet_format(('Welcome to rock paper scissors Game '), font = "digital"), "green")
print(result1)
while trry:
    user = int(input("1_player vs computer\n2_player vs player\nenter number of your choice: "))
    if user == 1 or user == 2:
        heighest_score = int(input("enter the highest score from range (1, 3, 5): "))
        while user == 1 and (heighest_score == 1 or heighest_score == 3 or heighest_score == 5):
            user_choice = int(input("1_rock\n2_paper\n3_scissors\nenter number of your choice: "))
            computer_choice = random.choice(rps)
            if 1 <= user_choice <= 3:
                if user_choice == 1:
                    user_choice = rps[0]
                elif user_choice == 2:
                    user_choice = rps[1]
                else:
                    user_choice = rps[2]
                check = True
            else:
                print("youre number is out of range(1 to 3)\npelease try again!")
                check = False
            if check == True:
                if user_choice == "rock" and computer_choice == "scissors" or user_choice == "scissors" and computer_choice == "paper"  or user_choice == "paper" and computer_choice == "rock":
                    score_user += 1
                    text = fontstyle.apply("user is win for this round", 'bold/Italic/red/GREEN_BG')
                    print(text)
                elif computer_choice == "rock" and user_choice == "scissors" or computer_choice == "scissors" and user_choice == "paper" or computer_choice == "paper" and user_choice == "rock":
                    score_computer += 1
                    text = fontstyle.apply("computer is win for this round", 'bold/Italic/red/GREEN_BG')
                    print(text)
                else:
                    text = fontstyle.apply("equal", 'bold/Italic/red/GREEN_BG')
                    print(text)
                if score_user == heighest_score:
                    winer = "user"
                    break
                elif score_computer == heighest_score:   
                    winer = "computer"
                    break 

        while user == 2 and (heighest_score == 1 or heighest_score == 3 or heighest_score == 5):
            user1_choice = int(input("player1\n1_rock\n2_paper\n3_scissors\nenter number of your choice: "))
            user2_choice = int(input("player2\n1_rock\n2_paper\n3_scissors\nenter number of your choice: "))
            if 1 <= user1_choice <= 3 and 1 <= user2_choice <= 3:
                if user1_choice == 1:
                    user1_choice = rps[0]
                elif user1_choice == 2:
                    user1_choice = rps[1]
                elif user1_choice == 3:
                    user1_choice = rps[2]

                if user2_choice == 1:
                    user2_choice = rps[0]
                elif user2_choice == 2:
                    user2_choice = rps[1]
                elif user2_choice == 3:
                    user2_choice = rps[2]
                check = True
            else:
                print("youre number is out of range(1 to 3)\npelease try again!")
                check = False

            if check == True:
                if (user1_choice == "rock" and user2_choice == "scissors") or (user1_choice == "scissors" and user2_choice == "paper")  or (user1_choice == "paper" and user2_choice == "rock"):
                    score_user1 += 1
                    text = fontstyle.apply("player1 is win for this round", 'bold/Italic/red/GREEN_BG')
                    print(text)
                elif (user2_choice == "rock" and user1_choice == "scissors") or (user2_choice == "scissors" and user1_choice == "paper") or (user2_choice == "paper" and user1_choice == "rock"):
                    score_user2 += 2
                    text = fontstyle.apply("player2 is win for this round", 'bold/Italic/red/GREEN_BG')
                    print(text)
                elif user2_choice == "rock" and user1_choice == "rock" or user2_choice == "scissors" and user1_choice == "scissors" or user2_choice == "paper" and user1_choice == "paper":
                    text = fontstyle.apply("equal", 'bold/Italic/red/GREEN_BG')
                    print(text)
            if score_user1 == heighest_score:
                winer = "player 1"
                break
            elif score_user2 == heighest_score:
                winer = "player 2"
                break
        text = fontstyle.apply(f"winer is {winer}", 'bold/Italic/red/GREEN_BG')
        print(text)
    else:
        print("your chosen number is not found")
    try_again = input("do you want to play again?(y, n)")
    if try_again == "y":
        trry = True
    else: 
        trry = False

result = colored(pyfiglet.figlet_format('Good Bye! '), 'green')
print(result)
# text = fontstyle.apply('GEEKSFORGEEKS', 'bold/Italic/red/GREEN_BG')
# print(text)

# text = 'This is so fancy'
# print(fancy.light(text))
# print(fancy.bold(text))
# print(fancy.box(text))

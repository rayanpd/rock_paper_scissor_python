import random

rounds = int(input("how meny rounds do you want to play : "))
list_bot = ['rock','paper','scisser']
nameListBot = ['ali','sina','hana']


name_player_1 = input("enter your name player_1 : ")
name_bot = random.choice(nameListBot)
print(f"name bot is {name_bot}")

score_player_1 = 0
score_bot = 0

for round in range(rounds):
    choose_player_1 = input(f"{name_player_1} entekhap kon az bein (rock,paper,scisser) : ")
    choose_bot = random.choice(list_bot)
    print(f"{name_bot} choose {choose_bot}")
    if choose_player_1 == choose_bot:
        print("draw")

    elif choose_player_1 == "rock" and choose_bot == "paper":
        print(f"{name_bot} is winner")
        score_bot += 1
        print(f"resualt is : {score_player_1} - {score_bot}")

    elif choose_player_1 == "rock" and choose_bot == "scisser":
        print(f"{name_player_1} is winner")
        score_player_1 += 1
        print(f"resualt is : {score_player_1} - {score_bot}")

    elif choose_player_1 == "paper" and choose_bot == "scisser":
        print(f"{name_bot} is winner")
        score_bot += 1
        print(f"resualt is : {score_player_1} - {score_bot}")

    elif choose_player_1 == "paper" and choose_bot == "rock":
        print(f"{name_player_1} is winner")
        score_player_1 += 1
        print(f"resualt is : {score_player_1} - {score_bot}")

    elif choose_player_1 == "scisser" and choose_bot == "rock":
        print(f"{name_bot} is winner")
        score_bot += 1
        print(f"resualt is : {score_player_1} - {score_bot}")

    elif choose_player_1 == "scisser" and choose_bot == "paper":
        print(f"{name_player_1} is winner")
        score_player_1 += 1
        print(f"resualt is : {score_player_1} - {score_bot}")
    else:
        print("this is a eshtebah!!")
    
    print("--------------------------------------------")

if score_player_1 > score_bot :
    print(f"{name_player_1} is winner")
elif score_player_1 < score_bot :
    print(f"{name_bot} is winner")
else:
    print("draw")

print(f"resualt is : {score_player_1} - {score_bot}")
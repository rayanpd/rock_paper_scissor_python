import random

rounds = int(input("how meny rounds do you want to play : "))
list_bot = ['rock','paper','scisser']
nameListBot_1 = ['ali','sina','hana']
nameListBot_2 = ['hossin','ilon','mark']


name_bot_1 = random.choice(nameListBot_1)
name_bot_2 = random.choice(nameListBot_2)
print(f"name bot_1 is {name_bot_1}")
print(f"name bot_2 is {name_bot_2}")

score_bot_1 = 0
score_bot_2 = 0

for round in range(rounds):
    choose_bot_1 = random.choice(list_bot)
    choose_bot_2 = random.choice(list_bot)
    print(f"{name_bot_1} choose {choose_bot_1}")
    print(f"{name_bot_2} choose {choose_bot_2}")
    if choose_bot_1 == choose_bot_2:
        print("draw")

    elif choose_bot_1 == "rock" and choose_bot_2 == "paper":
        print(f"{name_bot_2} is winner")
        score_bot_2 += 1
        print(f"resualt is : {score_bot_1} - {score_bot_2}")

    elif choose_bot_1 == "rock" and choose_bot_2 == "scisser":
        print(f"{name_player_1} is winner")
        score_bot_1 += 1
        print(f"resualt is : {score_bot_1} - {score_bot_2}")

    elif choose_bot_1 == "paper" and choose_bot_2 == "scisser":
        print(f"{name_bot_2} is winner")
        score_bot_2 += 1
        print(f"resualt is : {score_bot_1} - {score_bot_2}")

    elif choose_bot_1 == "paper" and choose_bot_2 == "rock":
        print(f"{name_bot_1} is winner")
        score_player_1 += 1
        print(f"resualt is : {score_bot_1} - {score_bot_2}")

    elif choose_bot_1 == "scisser" and choose_bot_2 == "rock":
        print(f"{name_bot_2} is winner")
        score_bot_2 += 1
        print(f"resualt is : {score_bot_1} - {score_bot_2}")

    elif choose_bot_1 == "scisser" and choose_bot_2 == "paper":
        print(f"{name_bot_1} is winner")
        score_player_1 += 1
        print(f"resualt is : {score_bot_1} - {score_bot_2}")
    else:
        print("this is a eshtebah!!")
    
    print("--------------------------------------------")

if score_bot_1 > score_bot_2 :
    print(f"{name_bot_1} is winner")
elif score_bot_1 < score_bot_2 :
    print(f"{name_bot_2} is winner")
else:
    print("draw")

print(f"resualt is : {score_bot_1} - {score_bot_2}")
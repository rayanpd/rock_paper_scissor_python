rounds = int(input("how meny rounds do you want to play : "))

name_player_1 = input("enter your name player_1 : ")
name_player_2 = input("enter your name player_2 : ")

score_player_1 = 0
score_player_2 = 0

for round in range(rounds):
    choose_player_1 = input(f"{name_player_1} entekhap kon az bein (rock,paper,scisser) : ")
    choose_player_2 = input(f"{name_player_2} entekhap kon az bein (rock,paper,scisser) : ")

    if choose_player_1 == choose_player_2:
        print("draw")

    elif choose_player_1 == "rock" and choose_player_2 == "paper":
        print(f"{name_player_2} is winner")
        score_player_2 += 1
        print(f"resualt is : {score_player_1} - {score_player_2}")

    elif choose_player_1 == "rock" and choose_player_2 == "scisser":
        print(f"{name_player_1} is winner")
        score_player_1 += 1
        print(f"resualt is : {score_player_1} - {score_player_2}")

    elif choose_player_1 == "paper" and choose_player_2 == "scisser":
        print(f"{name_player_2} is winner")
        score_player_2 += 1
        print(f"resualt is : {score_player_1} - {score_player_2}")

    elif choose_player_1 == "paper" and choose_player_2 == "rock":
        print(f"{name_player_1} is winner")
        score_player_1 += 1
        print(f"resualt is : {score_player_1} - {score_player_2}")

    elif choose_player_1 == "scisser" and choose_player_2 == "rock":
        print(f"{name_player_2} is winner")
        score_player_2 += 1
        print(f"resualt is : {score_player_1} - {score_player_2}")

    elif choose_player_1 == "scisser" and choose_player_2 == "paper":
        print(f"{name_player_1} is winner")
        score_player_1 += 1
        print(f"resualt is : {score_player_1} - {score_player_2}")
    else:
        print("this is a eshtebah!!")

    print("--------------------------------------------")

if score_player_1 > score_player_2 :
    print(f"{name_player_1} is winner")
elif score_player_1 < score_player_2 :
    print(f"{name_player_2} is winner")
else:
    print("draw")

print(f"resualt is : {score_player_1} - {score_player_2}")
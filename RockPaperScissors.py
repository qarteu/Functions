import random
choices = ["rock", "paper", "scissors"]
rand = random.choice(choices)
player = input("r,p,s")

print("computer: ", rand)
print("player: " , player)

if player == "rock":
    print("computer: " , rand)
    print("player: " , player)
    print("Tie!")
elif player == "rock":
    if rand == "paper":
        print("computer: " , rand)
        print("player:")






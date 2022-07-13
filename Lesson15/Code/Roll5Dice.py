import random

keep_going = True
while keep_going:
    # 1. do some coding
    dice = [1, 1, 1, 1, 1]

    for n in range(5):
        dice[n] = random.randint(1, 6)

    print(f"You rolled {dice}.")
    dice.sort()
    if dice[0] == dice[4]:
        print("Yahtzee!")
    elif dice[0] == dice[3] or dice[1] == dice[4]:
        print("Four of a kind!")
    elif dice[0] == dice[2] or dice[1] == dice[3] or dice[2] == dice[4]:
        print("Three of a kind!")
    else:
        print("You lose!")

    # 2. keep it going or not?
    answer = input("Hit [Enter] to keep going, any key to exit: ")
    keep_going = (answer == "")

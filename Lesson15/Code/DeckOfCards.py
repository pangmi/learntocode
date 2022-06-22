import random

suits = ['clubs', 'diamonds', 'hearts', 'spades']
faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

#for s in suits:
#    for f in faces:
#        print(s, '-', f, '')

keep_going = True
while keep_going:
    # Compare card
    # my_suit = input("Please pick your suit: ")
    # my_face = input("Please pick your face: ")
    my_suit = random.choice(suits)
    my_face = random.choice(faces)
    print("My card is", my_suit, '-', my_face)

    pc_suit = random.choice(suits)
    pc_face = random.choice(faces)
    print("Computer card is", pc_suit, '-', pc_face)

    if faces.index(my_face) > faces.index(pc_face):
        print("You won!")
    elif faces.index(my_face) < faces.index(pc_face):
        print("You lost.")
    else:
        if suits.index(my_suit) > suits.index(pc_suit):
            print("You won!")
        elif suits.index(my_suit) < suits.index(pc_suit):
            print("You lost.")
        else:
            print("It's a tie.")

    print()

    # keep going loop
    answer = input("Do you want to keep going (y/n)? ")
    keep_going = (answer == 'y')
        

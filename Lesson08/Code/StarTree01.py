star = '*'
space = ' '
num_of_stars = 1
num_of_spaces = 9
for x in range(1, 11):
    for i in range(num_of_spaces):
        print(space, end='')
    for i in range(num_of_stars):
        print(star, end='')
    print()

    num_of_stars += 2
    num_of_spaces -= 1

for x in range(5):
    for i in range(9):
        print(space, end='')
    print(star)

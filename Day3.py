print("Welcome to the treasure island, your mission is to find the treasure")
first = input("left or right?")
if first == 'left':
    second = input("swim or wait?")
    if second == 'wait':
        third = input("Which door? Red, Blue or Yellow")
        if third == "Yellow?":
            print("You win!")
        else:
            if third == "Red":
                print("Burned, game over")
            elif third == "Blue":
                print('eaten, game over')
            else:
                print("Game over.")

    else:
        print("attacked by trout, game over")
else:
    print('fall into a hole, game over')

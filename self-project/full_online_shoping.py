# remember to check first if they money to buy and then ask to buy.

import os


def clear():
    os.system('cls')


wallet = 20

bag = []

fruits = {}

with open("text_files/fruits.txt") as f:

    for line in f:

        (key, val) = line.split('=')

        fruits[key] = float(val)

veg = {}

with open("text_files/veg.txt") as f:

    for line in f:

        (key, val) = line.split('=')

        veg[key] = float(val)

meat = {}

with open("text_files/meat.txt") as f:

    for line in f:

        (key, val) = line.split('=')

        meat[key] = float(val)

dairy = {}

with open("text_files/dairy.txt") as f:

    for line in f:

        (key, val) = line.split('=')

        dairy[key] = float(val)

print("Here is your start amount of money: $" + str(wallet) + ". Use it wisely!")

while wallet >= 5:

    choice = input("Do you want to buy fruits/veg/dairy/meat? Or enter q to quit ").lower().strip()

    if choice == 'q' or choice == 'quit':
        break

    elif choice == 'fruits' or choice == 'fruit':

        print(fruits)

        COF = input("Which fruit do you want to buy? ")

        if COF in fruits:

            cost = veg.get(COF)

            buy = input("Do you want to buy " + COF + "? "
                        "It costs $" + str(cost) + ". "
                        "You have: $" + str(wallet) + ". ").lower().strip()

            if buy == 'y' or buy == 'yes':

                wallet -= cost

                clear()

                print("You have: $" + str(wallet) + " left.")

                bag.append(COF)

            else:

                clear()

                pass

        else:

            clear()

            print("You have mistyped or chose an option not in the list. Pls try again.")

            pass

    elif choice == 'veg' or choice == 'vegetable':

        print(veg)

        COV = input("Which veg do you want to buy? ")

        if COV in veg:

            cost = veg.get(COV)

            buy = input("Do you want to buy " + COV + "? "
                        "It costs $" + str(cost) + ". "
                        "You have: $" + str(wallet) + ". ").lower().strip()

            if buy == 'y' or buy == 'yes':

                wallet -= cost

                clear()

                print("You have: $" + str(wallet) + " left.")

                bag.append(COV)

            else:

                clear()

                pass

        else:

            clear()

            print("You have mistyped or chose an option not in the list. Pls try again.")

            pass

    elif choice == 'dairy':

        print(dairy)

        COD = input("Which dairy product do you want to buy? ")

        if COD in dairy:

            cost = dairy.get(COD)

            buy = input("Do you want to buy " + COD + "? "
                        "It costs $" + str(cost) + ". "
                        "You have: $" + str(wallet) + ". ").lower().strip()

            if buy == 'y' or buy == 'yes':

                wallet -= cost

                clear()

                print("You have: $" + str(wallet) + " left.")

                bag.append(COD)

            else:

                clear()

                pass

        else:

            clear()

            print("You have mistyped or chose an option not in the list. Pls try again.")

            pass

    else:
        print(meat)

        COM = input("Which meat product do you want to buy? ")

        if COM in meat:

            cost = meat.get(COM)

            buy = input("Do you want to buy " + COM + "? "
                        "It costs $" + str(cost) + ". "
                        "You have: $" + str(wallet) + ". ").lower().strip()

            if buy == 'y' or buy == 'yes':

                wallet -= cost

                clear()

                print("You have: $" + str(wallet) + " left.")

                bag.append(COM)

            else:

                clear()

                pass

        else:

            clear()

            print("You have mistyped or chose an option not in the list. Pls try again.")

            pass
if wallet <5:

    print("You cannot buy any other item")

else:
    pass

print("Here is the amount of money you have left and your bag.")

print("$" + str(wallet))

print(bag)

print("Come back next time.")

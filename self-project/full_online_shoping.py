# remember to check first if they money to buy and then ask to buy.
# there is definetely a shorter version of this code. Working on it right now!
# maybe use def functions

import os
import time


def clear():
    os.system('cls')


wallet = 20

fruit_bag = []

veg_bag = []

meat_bag = []

dairy_bag = []

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

    time.sleep(2)

    clear()

    choice = input("Do you want to buy fruits/veg/dairy/meat? Or enter q to quit ").lower().strip()

    if choice == 'q' or choice == 'quit':
        break

    elif choice == 'fruits' or choice == 'fruit':

        print(fruits)

        COF = input("Which fruit do you want to buy? ")

        if COF in fruits:

            cost = fruits.get(COF)

            qt = int(input("How many do you want to buy? "))

            print("Adding to cart...")

            total = qt * cost

            wallet -= total

            fruit_bag.append(["Product: " + COF, "Each cost: " + str(cost),
                              "Quantity: " + str(qt), "Total for item: " + str(total)])

        else:

            clear()

            print("You have mistyped or chose an option not in the list. Pls try again.")

            pass

    elif choice == 'veg' or choice == 'vegetable':

        clear()

        print(veg)

        COV = input("Which veg do you want to buy? ")

        if COV in veg:

            cost = veg.get(COV)

            qt = int(input("How many do you want to buy? "))

            print("Adding to cart...")

            total = qt * cost

            wallet -= total

            veg_bag.append(
                ["Product: " + COV, "Each cost: " + str(cost),
                 "Quantity: " + str(qt), "Total for item: " + str(total)])

        else:

            clear()

            print("You have mistyped or chose an option not in the list. Pls try again.")

            pass

    elif choice == 'dairy':

        print(dairy)

        COD = input("Which dairy product do you want to buy? ")

        if COD in dairy:

            cost = dairy.get(COD)

            qt = int(input("How many do you want to buy? "))

            print("Adding to cart...")

            total = qt * cost

            wallet -= total

            dairy_bag.append(["Product: " + COD, "Each cost: " + str(cost),
                              "Quantity: " + str(qt), "Total for item: " + str(total)])

        else:

            clear()

            print("You have mistyped or chose an option not in the list. Pls try again.")

            pass

    else:
        print(meat)

        COM = input("Which meat product do you want to buy? ")

        if COM in meat:

            cost = meat.get(COM)

            qt = int(input("How many do you want to buy? "))

            print("Adding to cart...")

            total = qt * cost

            wallet -= total

            meat_bag.append(
                ["Product: " + COM, "Each cost: " + str(cost),
                 "Quantity: " + str(qt), "Total for item: " + str(total)])

        else:

            clear()

            print("You have mistyped or chose an option not in the list. Pls try again.")

            pass
if wallet < 5:

    print("You cannot buy any other item")

else:
    pass

clear()

print("Here is the amount of money you have left and your bag.")

for x in fruit_bag:
    if len(x) > 0:

        print(fruit_bag)

    else:
        pass

print()

for x in veg_bag:
    if len(x) > 0:

        print(veg_bag)

    else:
        pass

print()

for x in dairy_bag:
    if len(x) > 0:

        print(dairy_bag)

    else:
        pass

print()

for x in meat_bag:
    if len(x) > 0:

        print(meat_bag)

    else:
        pass

print("Money left: $" + str(wallet))

print("Come back next time.")

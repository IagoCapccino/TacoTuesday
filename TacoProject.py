
foods = ["Mini Tacos", "Nacho Fiesta", "Waffle Taco", "Cheesadilla"]
price = [3.99, 7.45, 9.99, 6.85]
order= []
totalPrice= []
print("Welcome to Taco Time!  Please view the menu below and make a selection")
print("Taco Time Menu")
print()

menu = True
while menu:
    print("1. Mini Tacos")
    print("2. Nacho Fiesta")
    print("3. Waffle Taco")
    print("4. Cheesadilla")
    print("5. Quit")
    userInput = int(input("Enter the number of the food or 5 to quit: "))
    print()
    if userInput == 5:
        print("You ordered ", end="")
        for i in range(len(order)):
            if i == len(order)-1:
                print(f"{order[i]}. Your total is ${sum(totalPrice):.2f}")
            else:
                print(order[i], end=", ")
        menu = False
    else:
        print(f"You selected {foods[userInput - 1]}")
        order.append(foods[userInput - 1])
        totalPrice.append(price[userInput-1])
        print()
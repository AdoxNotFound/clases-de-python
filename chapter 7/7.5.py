while True:
    print("ticket prices are depending on your age.")
    ticket = int(input("how old are you?: "))

    if ticket < 3:
        print("you are a baby, your ticket is free.")
    elif ticket >= 3 and ticket < 12:
        print("your ticket price is 10$.")
    else:
        print("your ticket price is 15$.")


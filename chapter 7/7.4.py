prompt = "\nEnter the topping you want on your pizza: "
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"\nYou'll add {topping} to your pizza.")
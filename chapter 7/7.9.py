finished_sandwiches = []
sandwich_orders = ['tuna','pastrami', 'hawai', 'barbecue','pastrami', 'cheese', 'vegetarian', 'pastrami']

print("Deli run's out of 'pastrami'")
print(sandwich_orders)
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

while sandwich_orders:
    order = sandwich_orders.pop()

    print(f"Your order of {order.title()} is ready.")
    finished_sandwiches.append(order)

print("\nThe sandwich orders are:")
for finished_sandwich in finished_sandwiches:
    print (finished_sandwich.title())
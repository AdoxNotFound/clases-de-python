finished_sandwiches = []
sandwich_orders = ['tuna', 'hawai', 'cheese', 'vegetarian']

while sandwich_orders:
    order = sandwich_orders.pop()

    print(f"Your order of {order.title()} is ready.")
    finished_sandwiches.append(order)

print("\nThe sandwich orders are:")
for finished_sandwich in finished_sandwiches:
    print (finished_sandwich.title())
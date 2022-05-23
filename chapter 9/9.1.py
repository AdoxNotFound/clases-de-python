class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restarurant name is: {self.restaurant_name.title()}.")
        print(f"The cuisine type is: {self.cuisine_type.title()}.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!")


my_restaurant = Restaurant('cozzolizi', 'pizza')

print(f"The best {my_restaurant.cuisine_type} restaurant in town is {my_restaurant.restaurant_name.title()}.")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
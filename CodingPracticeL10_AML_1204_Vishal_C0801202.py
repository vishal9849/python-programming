# 9.1 Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is famous for {self.cuisine_type}")

    def open_restaurant(self):
        print(self.restaurant_name, "is open right now.")

    # 9.4
    def set_number_served(self, number_of_customers):
        self.number_served = number_of_customers

    def increment_number_served(self, increment):
        self.number_served += increment
        print(f"Customer served: {self.number_served}")


vishal_restaurant_obj = Restaurant("Vishal's_restaurant", "Biryani")
print("Name of the restaurant", vishal_restaurant_obj.restaurant_name)
print("Famous cuisine", vishal_restaurant_obj.cuisine_type)
vishal_restaurant_obj.describe_restaurant()
vishal_restaurant_obj.open_restaurant()
print('-------------------------------------------')

# 9.2 Three Restaurants
ram_obj = Restaurant("ram's_restaurant", "Burger")
ram_obj.describe_restaurant()
ani_obj = Restaurant("Anil's_restaurant", "Fried-rice")
ani_obj.describe_restaurant()
avi_obj = Restaurant("Avi's_restaurant", "Butter Chicken")
avi_obj.describe_restaurant()
print('-------------------------------------------------')


# 9.3 Users
class Users:
    def __init__(self, first_name, last_name, user_id, mail_id):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.mail_id = mail_id
        #   9.5
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.last_name}'s Summary: First name: {self.first_name}, "
              f"Last Name: {self.last_name}, \n"
              f"User ID: {self.user_id}, "
              f"Mail ID: {self.mail_id}, \n")

    def greet_user(self):
        print(f"Welcome {self.first_name + ' ' + self.last_name}")

    # 9.5
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


vishal_user = Users('Vishal', 'Sab', '001', 'vish@112.gmail.com')
avi_user = Users("Avi", 'Ravi', '002', 'avi342@gmail.com')
ani_user = Users('Ani', 'Rude', '003', 'ani78@gmail.com')
vishal_user.greet_user()
avi_user.greet_user()
ani_user.greet_user()
vishal_user.describe_user()
avi_user.describe_user()
ani_user.describe_user()
print('-------------------------------------------------')

# 9.4 Number served
print(f"Number of customer's {vishal_restaurant_obj.restaurant_name} served "
      f"yesterday: {vishal_restaurant_obj.number_served}")

vishal_restaurant_obj.set_number_served(53)

print(f"Number of customer's {vishal_restaurant_obj.restaurant_name} served "
      f"today: {vishal_restaurant_obj.number_served}")

vishal_restaurant_obj.increment_number_served(3)
print('-------------------------------------------')

# 9.5 Login Attempts
vishal_user.increment_login_attempts()
vishal_user.increment_login_attempts()
vishal_user.increment_login_attempts()
vishal_user.increment_login_attempts()
vishal_user.increment_login_attempts()
print("Login attempts after incrementing", vishal_user.login_attempts)
vishal_user.reset_login_attempts()
print("Login attempts after resetting", vishal_user.login_attempts)
print('-------------------------------------------')


#  9.6 Updating the code
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.increment_odometer(miles=50)
my_new_car.read_odometer()
print('-------------------------------------------')

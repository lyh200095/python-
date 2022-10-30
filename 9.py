#9-1
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name+' have '+self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name+' is open')

res1=Restaurant('a','b')
print(res1.restaurant_name)
print(res1.cuisine_type)
res1.open_restaurant()
res1.describe_restaurant()

#9-2
res2=Restaurant('c','d')
res3=Restaurant('e','f')
res2.describe_restaurant()
res3.describe_restaurant()

#9-3
class User():
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

    def describe_user(self):
        print('user: '+self.first_name+' '+self.last_name+' '+self.age)

    def greet_user(self):
        print('hello '+self.first_name+' '+self.last_name)

u1=User('li','hua','17')
u2=User('jay','chou','18')
u1.describe_user()
u1.greet_user()
u2.describe_user()
u2.greet_user()

#9-4
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print(self.restaurant_name+' have '+self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name+' is open')

    def set_number_served(self,number_served):
        self.number_served=number_served
        print('the number of diners is '+str(self.number_served))

    def increment_number_served(self,number):
        self.number_served+=number
        print('the number of dinner is '+str(self.number_served))

res1=Restaurant('a','b')
res1.set_number_served(3)
res1.increment_number_served(2)

#9-5
class User():
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.login_attemps=0

    def describe_user(self):
        print('user: '+self.first_name+' '+self.last_name+' '+self.age)

    def greet_user(self):
        print('hello '+self.first_name+' '+self.last_name)

    def increment_login_attemps(self):
        self.login_attemps+=1
        print(str(self.login_attemps))

    def reset_login_attemps(self):
        self.login_attemps=0
        print(str(self.login_attemps))

u1=User('a','b','10')
print(u1.login_attemps)
u1.increment_login_attemps()
u1.increment_login_attemps()
u1.increment_login_attemps()
u1.reset_login_attemps()

#9-6
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print(self.restaurant_name+' have '+self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name+' is open')

    def set_number_served(self,number_served):
        self.number_served=number_served
        print('the number of diners is '+str(self.number_served))

    def increment_number_served(self,number):
        self.number_served+=number
        print('the number of dinner is '+str(self.number_served))

class IceCreamstand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavours=['f1','f2','f3']
    def show(self):
        for n in self.flavours:
            print(n)
i1=IceCreamstand('r1','c1')
i1.show()

#9-7
class User():
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.login_attemps=0

    def describe_user(self):
        print('user: '+self.first_name+' '+self.last_name+' '+self.age)

    def greet_user(self):
        print('hello '+self.first_name+' '+self.last_name)

    def increment_login_attemps(self):
        self.login_attemps+=1
        print(str(self.login_attemps))

    def reset_login_attemps(self):
        self.login_attemps=0
        print(str(self.login_attemps))
class Admin(User):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges=["can add post","can delete post","can ban user"]

    def show_privileges(self):
        for n in self.privileges:
            print(n)

a1=Admin('liu','han','18')
a1.show_privileges()

#9-8
class Privileges():
    def __init__(self,privileges=["can add post","can delete post","can ban user"]):
        self.privileges=privileges
    def show_privileges(self):
        for n in self.privileges:
            print(n)

class User():
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.login_attemps=0

    def describe_user(self):
        print('user: '+self.first_name+' '+self.last_name+' '+self.age)

    def greet_user(self):
        print('hello '+self.first_name+' '+self.last_name)

    def increment_login_attemps(self):
        self.login_attemps+=1
        print(str(self.login_attemps))

    def reset_login_attemps(self):
        self.login_attemps=0
        print(str(self.login_attemps))
class Admin(User):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges=Privileges()

a2=Admin('l','k','20')
a2.privileges.show_privileges()

#9-9
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + str(self.make) + " " + str(self.model)
        return long_name.title()

    def read_odometer(self):
        print("the car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + " kMh battery")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge"
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar("tesla","model s'",2016)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

#9-14
from random import randint
class Die():
    def __init__(self,sides=6):
        self.sides=sides
    def roll_die(self):
        n=randint(1,self.sides)
        return n
d1=Die()
print('throw the dice 10 times')
for i in range(1,11):

    print(d1.roll_die())






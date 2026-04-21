from datetime import datetime

class Person:
    def __init__(self,name,age,email,address,dob):
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.dob = dob

    def talk(self):
        # print("Person talks")
        print(f"{self.name} talks")

    def code(self):
        print(f"{self.name} codes in Python")

    def sleep(self):
        print(f"{self.name} sleeps")

    def earn_salary(self):
        print(f"{self.name} earn_salary")

    def work(self):
        print(f"{self.name} works")


person1 = Person("Jake",25,'jake@gmail.com','Buruburu Phase 1','2001-8-19')
print(type(person1))
print(person1.address)

person1.talk()
person1.work()

person2 = Person("Kate",24,'kate@gmail.com','Karen','2002-3-20')
print(type(person2))
print(person2.address)
person2.talk()


class BankAccount:
    def __init__(self,account_number,balance,owner_name,date_opened):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened

    def deposit(self):
        print(f"{self.account_number} deposits")

    def withdraw(self):
        print(f"{self.account_number} withdraws")

    def display_info(self):
        print(f"{self.account_number} displays_info")


bank1 = BankAccount(54321,10000,"Hussna Mwinyi",'2005-07-23')

bank1.deposit()
bank1.withdraw()
bank1.display_info()

bank2 = BankAccount(98234,25000,"Juma Said",'2005-06-15')

bank2.deposit()
bank2.withdraw()
bank2.display_info()

today = datetime.now()
#print(today)
class BankAccount:
    def __init__(self,account_number,balance,owner_name,date_opened=today):
        
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened

    def display_info(self):
        print(f"Account details: {self.account_number},- {self.balance},- {self.owner_name},- {self.date_opened}")

bankacc1 = BankAccount('ACC001234',0,"Jane Doe")
bankacc1.display_info()



class Car:
    def __init__(self,brand,model,year,fuel_capacity,fuel_level,is_running):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_level
        self.is_running = is_running

    def start(self):
        print(f"{self.brand} starts")

    def stop(self):
        print(f"{self.brand} stops")

    def refuel(self):
        print(f"{self.brand} refuels")

    def drive(self):
        print(f"{self.brand} drives")

    def display_car_info(self):
        print(f"Car details: {self.brand},- {self.model},- {self.year},- {self.fuel_capacity},- {self.fuel_level},- {self.is_running}")

car1 = Car("Audi","Q5",2025,"65L","50L","True")
car1.start()
car1.display_car_info()






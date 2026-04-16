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






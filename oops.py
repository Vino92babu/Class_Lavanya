"class and object"
class Test: # crearting the class
    def myfun(self):
        print("this is oops concept")
    def myfun1(self):
        print("Press the valid Button")

Test_obj = Test() # Creating the Object
# Test_obj.myfun1()
# Test_obj.myfun()

# Accessing a class level variable:

# class demo:
#     A = 38
#     def myfun(self):
#         print("this is oops concept")
# o = demo()
# print(o.A)

class demo:
    def myfun1(self,name,age):
        self.name = name
        self.age = age
    def myfun2(self):
        print("Name: ",self.name)
        print("Name: ",self.age)
# obj = demo()
# obj.myfun1("Vinoth",13)
# obj.myfun2()


# ..........................................
# inheritance

# class vehicle:
#     def __init__(self,brand):
#         self.brand = brand
#     def general_info(self):
#         print("Brand:",self.brand)
# class car(vehicle):
#     def __int__(self,brand):
#         print(brand)

     
# a = vehicle()


class animal:
    def sound(self):
        print("Animal sounds")
class dog(animal):
    def sound(self):
        print("dogs barks")
# DOG = dog()
# DOG.sound()


class employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name",self.name)
        print("age",self.age)
 


# A = employee("Vinoth",20)
# A.display()

class bankaccount:
    def __init__(self,balance):
        self._balance = balance # private variable
    def deposit(self,amount):
        if amount >0:
            self._balance+=amount
    def get_balance (self):
        return self._balance

# acc = bankaccount(1000)
# acc.deposit(500)
# print(acc.get_balance())

class Dog:
    def sound(self):
        print("braks")
class Cat:
     def sound(self):
         print("Meow")
for animal in (Dog(), Cat()):
    animal.sound()


class BankAccount:
    def __init__(self,balance):
        self.__balance = balance     #private variable
    def deposit(self, amount):
        if amount>0:
            self.__balance += amount
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance-= amount
        else:
            print("insufficient balance")
    def get_balance(self):           # controlled access
        return self.__balance
acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())


'''
Encapasulation is the concept of bundling data and methods inside the data and restricting direct acc to the internal data. 
in Python, this can be used by namining conventiobns  like _varible and namining conventiobns  like __varible

'''

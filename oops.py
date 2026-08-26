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
obj = demo()
obj.myfun1("Vinoth",13)
obj.myfun2()
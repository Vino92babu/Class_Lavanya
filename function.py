# A = 18
# B = 48 
# C= A+B 
# print(C)
def add(a,b):
    c = a+b
    print(c)

# def add():
#     A = 3
#     B = 4
#     c = A+B
#     print(c)

# add()

'''
No return, without arguments
No Return, with arguments
Return, without arguments
Return, with arguments
'''

# No return, without arguments
def Add():
    a = 3
    b = 6
    c = a+b
    print(c)

# add()

def url():
    base_url = "www.google.com"
    print(base_url)
    return(base_url)


# No Return, with arguments

# Add(74,96)

# Return, without arguments

def sub():
    a = 85
    b = 41
    return a - b
# result = sub()
# print(result)


# Return, with arguments

def div(a,b):
    return a/b
# div()


choice = int(input("Enter the button: "))
def firstfloor():
    print("First_Floor")
def secondfloor():
    print("Second_Floor")
def Thirdfloor():
    print("Third_Floor")
if choice == 1:
    firstfloor()
if choice == 2:
    secondfloor()
if choice == 3:
    Thirdfloor()
# if choice>3:
#     print("Press the valid Button")
else:
    print("Press the valid Button")



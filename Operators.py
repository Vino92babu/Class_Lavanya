'''
Operators: 
Operators are symbols that tell python to "do somthing" with values - like add them, compare them, or combine conditions.

# Arithmetic Operators: 

"+" --> add two num ( 3+5=8)
"-" --> sub (5-3=2)
"*" --> Mul (5*3=15)
"/" --> division (10/2= 5.0) --> Divides, and alwalys gives back a decimal answer, even if it divides evenly 
"%" --> Moduls --> Gives you the remainder after division. This super useful for checking oddd/even num , since  any of num %2 will be 0 (even) or 1 (odd)
"**" --> power/exponent --> 2**3 means 2 raised to the power of 3, which is 8  
"//" --> floor division --> dived but throws awy anything after the decimal point, keeping only the "whole number part" (7 // 2 = 3.)


# print(7/2)
# print(7//2)

Comparison operator --> (For compairing two values --> result always will be True or False)
"==" --> "is equal to" 
"!=" --> "is not equal to
">" --> "Greater than
"<" --> "Less than
">=" --> greater than or equal to
"<=" --> lesser than or equal to

a,b = 10,20

print(a==b) # False
print(a!=b) #True
print(a>b) #False
print(a<b) #True
print(a>=b) #False
print(a<=b) #True


Logical Operators --> for combining multiple True/False conditions: 

add --> the overall result is True ONLY if both sides are True. If even one side is false also the whole things becomes false. 
or --> the averall result is True if at least one side is true
not --> flips a value : not True becomes False, and not False become True. 





A = True
B = False

print (A and B)
print(A or B)
print(not A)

Identity Operators: is /is not




a = [1,2]
b = [3,4]
c=a 
print(c)

print(a==b)  # True (Same Values)
print(a is b) # False (different objects in memory)

print(a is c) # True
print(a is not b) # True

Membership Operators (in / not in): To check wheather a value exists a collection like a list, string, or set. 

'''
A = "apple"

print('appe' in A)
print('appe' not in A)

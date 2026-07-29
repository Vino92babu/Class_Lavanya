'''
Number
String
List
Tuple
Dictionary
Set

Mutable datatypes

Immutable datatypes
'''
# Number / numeric

# A = 10

# python supports 4 different numerical types
'''
int [integers] --> A = 2
long[long int, they can also be represtented in hexadecimal] B = 101000101
Float[floating point real values] c= 5.4
Complex[]  --> D = 10+5j
'''
# A = 2
# print(A)
# print(type(A))
# B = 101000101
# print(type(B))

# Name = input()
# print(type(Name))

# age = 5
# print(type(age))
# age_add = age+3
# print(type(age_add))

# age = input()
# print(type(age))
# age_add = age+3
# print(type(age_add))

# String
# Strings in python are identified as a contiguous set of characters represented in the quotation mark.
# python allows for either pair of single or double quotes.

# String concatenatio : Using "+" operator
FN = "Vinoth"
LN = "Babu"
# FullName = FN + LN
# print(FullName)

# FullName = FN+" "+LN
# print(FullName)

# using ('-')

# FullName = FN - LN
# print(FullName)

# FullName = FN - 5
# print(FullName)

# FullName = FN * LN
# print(FullName)


# FullName = FN * 5
# print(FullName)

# FullName = FN / LN
# print(FullName)

# printing the string Statement:

A = "Wellcome to"
B = "Python class"

# Method1
# print("you are"+A+"famous"+B)
# # Method2
# print("you are{A} famous{B}".format(A=A,B=B))
# # Method3
# print("you are {} famous{}".format(A,B))
# Method4
# print(f"you are {A} fomous {B}") --> this

# String Indexing:
'''
Positive indexing


v	i	n	o	t	h
					
0	1	2	3	4	5


negative indexing 

v	i	n	o	t	h
-6	-5	-4	-3	-2	-1

'''

# A = "Vinoth"
# b =  "lavanya"
# o = "Python"

# print(b[0])

# print(b[-2])

# string Slicing:
'''Used to print onr range of index to another range of index
syntax-->  object[Start :End-1]
'''
# positive slice
# A = "Vinoth"
# print(A[4]) --> indexing

# print(A[0:5])

# Negative slice

# print(A[-5:-1])

# print(A[1:])

# step Arguments --> skiping the index value
# Syntax:  [Start : End : Skip]

# vnt

# print(A[0:5:2])

# String Methods:
# capitalize(): --> will chnage our 1st string into capital letter.

# A = 'apple phone'
# print(A.capitalize())

# B = '4 is my age'
# print(B.capitalize())

# count()-->  to find how many times the word/char present in that particular variable.

# a = "is is is vinoth vinoth babu"

# print(a.count("vinoth babu"))
# lower()--> to change the string into lower case.
A = "ViNoTh BaBu"
# print(A.lower())
# upper()-->to change the string into upper case.
# islower():
print(A.islower())
print(A.isupper())
# swapcase--> it is used to interchange in string
print(A)
print(A.swapcase())
# tittle ()--> it is used to change each word 1st letter in string in captical letter.

B  = " i am an supper hero"
print(B.title())
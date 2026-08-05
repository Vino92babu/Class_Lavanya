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
# print(A.islower())
# print(A.isupper())
# swapcase--> it is used to interchange in string
# print(A)
# print(A.swapcase())
# tittle ()--> it is used to change each word 1st letter in string in captical letter.

B  = " i am an supper hero"
# print(B.title())
# print(B.istitle())
# startswith--> will check the given "startswith" input is gets satisfy or not.

# C = "how are you"
# print(C.startswith("How"))

# D = ["Vinoth"]
# endswith
# print(C.endswith("you"))

# print(C.isnumeric())
# print(C.isalpha())
# print(C.isalnum())

# find()--> it is used to find the given "str" in variable $ o/p will be in index value.
# E = "To me you"
# print(E.find("2"))

'''
T -> 0  
O ->1
    ->2
m 3
E
'''
# replace() --> to replace the words in str

# aa = "i hate you"
# print(aa.replace("hate","like"))

# strip()--> used to remove the given letters or specfic char in str
# bb = "@#+python+*#@"
# print(bb.strip("@"))

# Lstrip --> To remove the char only in left side

# cc = "#+@python+*#+"
# print(cc.lstrip("#+"))

# rstrip --> To remove the char only in right side 

# print(cc.rstrip("#+"))

# Ljust--> To add any symbol in right side of string --> Total string index should be [10]
# cc = "python"
# print(cc.ljust(10,'@'))
# print(cc.rjust(1,"a"))

# center()--> to add any symbol equally before and after the string
# print(cc.center(11,"@"))



"_______________________________________________________________________________________________________________________________________"

# List
#  Collection of elements
'''
A list containg items seperated by commas and enclosed with sq brackets ([])'''

# fruits = "apple" --> String

# Subject = "Python"

# Student_names = ["Vinoth","lavanya","babu","ramu"]

# print(Subject)
# print(Student_names)

# note: Similar to string indexs, list index also starts with Zero(0),and can sliced, concatenated and so on.

# a_list = [1,2,5,"Vino"]
# b_list = [3,4]

# A = [4]
# B = [3]
# print(a_list) --> complete list
# print(a_list[0])
# print(a_list[1:3])
# print(a_list[1:])

# print(a_list*2)
# print(a_list+b_list)

# print(A+B)

# updating  list

# Num = [10,20,30,40,50,60]
# Num[2] = 90 --> [10,20,90,40,50,60]
# Num[0:4] = [1,2,3,4]

# print(Num)

# [1,2,3,90,50,60]

# [1,2,90,3,4,60]


# Delete list elements
# Num = [10,20,30,40,50,60]
# del Num[3]
# del Num[3:5]
# A = [10,"Vino",8.5,"ECE"]


# del A[1:3+1]


# print(A)



# Basic list operations: 
# A = [1,2,3,90,50,60]
# l_list = len(A)
# print(l_list)
# print(len(A))

# Concatenation ("+" --> for list)

# A = [10,30]
# B = [20,40]
# print(A+B)

# repetition ("*")

# A =[10,20,30]


# print(A*2)

# Membership Operator --> ("in") --> true/false

# students = ["Vinoth","Babu","Raju","Lavanya"]
# print("Lavanya" in students)

# Build- in functions /Methods: 
'''
len() --> this method returns the number of elements in list --> len(list)
max() --> this method returns the elements from the list with maximum value. --> max(list)
min() --> this method returns the elements from the list with minimum value. --> min(list)
list() --> this method takes sequence type and conver them to list. This is used to convert a given tuple to list. --> list(seq)
append() --> This method appends a passed object ito existing list
count() --> This method returns count of how many times,that obj occurs in list
extend() --> This method appends the contents of seq to list : Note: For numeric number extend will not be perform 
index() --> This method returns the lowest index in list that obj appers. 
insert() --> To add the elements in specific index.
pop() --> This methos removes and teturn last object the list / used to delete the elements in the last, if we doesn't give the index value.
remove() --> it is used to delete the elements when we does not able to find the index value. 
reverse() --> To used to print the element in list in reverse order. 
sort() --> it is used to keep elements in accending order (0-1). And for string it will be arrange in alphabetic order.
'''
# A = [1,2,3,90,50,60]

# print(max(A))
# print(min(A))

# list_ITEM = ["Green","Black","Yellow","Black"]
# list_ITEM.append("blue")
# print(list_ITEM)

# print(list_ITEM.count("Black"))

list_ITEM = ["Green","Black","Yellow","Black"]
# list_ITEM.extend("Red")
# list_ITEM.extend(2)
# print(list_ITEM)
B = list_ITEM.insert(2,"red")
print(B)

# without index 
# A = [1,2,3,4]
# A.pop()
# print(A)

# with index 
# A.pop(1)
# print(A)

# A = [1,2,3,4]
# A.remove(1)
# print(A)
# B = A.reverse()
# print(B)


# A = [50,60,1,8,0,25,41,65,56,28,16] 
# A.sort()
# print(max(A))
# print(A)

# tuple
'''
A tuple is a seq of immutable python obj. 
the main difference between the tupple and list is that the tuple cannot be changed unlike list. 
Tuple use parantheses"()" , where as list use square brackects "[]"

Note: Like string indices, tuple indices also start at 0 and they can be sliced , concatenated and so on. 

'''
# l = [1,2,3,4,5]
# l1 = []
# t1 = ()
# t = (1,2,3,4,5)
# print(type(l))
# print(type(t))
# print(type(l1))
# print(type(t1))
# Accessing value in tuples: 
# tuple1 = (10,"rise",2.5,"ece")
# print(tuple1[2])

# print("tuple [2 is :]" , tuple1[2])

# updating Tuples : Tuples are immutable, which means you cannot update or change the values of tuple elements. 
'''
Delete tuple elements: 
Removing individual tuple elements is not possible . 
But To explicitly we can revome the an entire tuple, Just using the "del" statement
'''

# abc = (1,2,34)
# bc = [1,2,34]

# del abc [1]

# print(abc)

# del bc [2]
# print(bc)

'''
# Basic tuple operations:

A = (10,"Vino",8.5)
len() 
Concatenation ("+")
Repetition("*")
Membership operator ("in")

Build in methods 
len()
max()
min()
tuple()

'''

# A = (10,"Vino",8.5)
# B = list(A)
# B.remove(8.5)
# A=tuple(B)
# print(A)

'''
# Dictionary --> Dict is an unordered set of "Keys:value" pairs with rquirements that the keys are unique[within one dict]
unlike sequences which are indexed by a range of number, dict are indexed by keys which can be any immutable type, String & numbrers can always be keys.

'''
A = {"rollno":5,"name":"Vinoth","dept":"ECE"}
# a = {}

# print(A["name"])
# print(A["rollno"])

# updating dict --> You can update a dict by adding a new entry or a key value pair

# print(A)
# A["dept"] = "CSE"
# A["rollno"] = 3
# print(A)

# delete dict element: we can remove individual dict element by using 'del' statement

# print(A)
# del A["rollno"]
# print(A)

# del A
# print(A)

# Build in dict functions & Methods

len()
str()
type()
clear()
copy()
get()
item()
keys()
Values()
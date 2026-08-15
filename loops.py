'''
Loops --> 
for loop --> saying "do this same thing for item in a list of things. 

Looping through a string. --> 


while loop --> repeat a block of code for as a condition until gets failed


'''
# Looping through a string..

# fruit = "apple"

# for i in fruit:
#     print(i)


# range() --> 1 -5


# for i in range(100):
#     print(i)

# for i in range(6,10):
#     print(i)

# strat = int(input("Enter the starting number: "))
# end = int(input("Enter the ending number: "))

# for i in range(strat,end):
#     print(i)

#  2 * 1 = 2
#  2 * 2 = 4


# for i in range(1,11):
#     print("2 *",i,"=",2*i)


# table = int(input("Enter the tables you want: "))

# for i in range(1,11):
#     print(table,"*",i,"=",table*i)

# for i in range (1,30):
#     if (i%2==0):
#         print(i)



# for i in range (1,30):
#     if (i%2==1
#         ):
#         print(i)

# count = 0
# for i in range (1,305):
#     if (i%2==0):
#         count = count+1
# print(count) 
# 
#       

# A = []
# for i in range(10):
#     Num = int(input("Enter_Num "+str(i+1)+":"))
#     A.append(Num)
# print(A)
        
# vowles = "aeiou"
# word = input("Enter a Word:")
# count = 0
# for ch in word:
#     if ch.lower() in vowles:
#         count = count+1
# print(count)

# while loop

# i = 0
# while i <=5:
#     i = i+1
#     print(i)

# i = 0
# while i <=5:
#     print(i)
#     i = i+1

# i = 10

# while i >=1:
#     print(i)
#     i = i-1

num =int(input("Enter the number"))
fact = 1
while num >0 :
    fact = fact*num
    num = num-1
print("Facrtorial:",fact)


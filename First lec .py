name="Parth"
age=18
print(name)
print(age)
print(type(name))
print(type(age))
# single line comment
"""this is 
a multi 
line comment"""
a,b=1,2.0
sum1=a+b
print(sum1)

#error 
"""c,d=1,"2" here "2" is a string.
sum2=c+d
print(sum2)"""

age=int(input("what's your age?"))#int stands for integer(non decimal numbers)
temperature=float(input("temperature?"))#float stands for decimal values
# Arthemetic operations
num1=float(input("first number"))
num2=float(input("second number"))
num3=num2+num1
print(num3)
# Comparision operator 
x=int(input("x="))
y=int(input("y="))
if (x<y) :
    print("x<y")
elif (x>y) :
    print("x>y")
elif (x==y):
    print("x=y")
else :
    print("Invalid input, Try again later.")    
# or we can do 
print("x>=y is",x>=y)   

# CONDITIONAL STATEMENTS

#TRAFFIC LIGHTS
light = input("Light is:")

if (light.lower()=="red"):
    print("Stop")
elif (light.lower()=="yellow"):
    print("Be ready")
elif (light.lower()=="green"):
    print("Go Go ")
else:    
    print("Light is broken.")

#STUDENTS GRADE
marks=float(input("Enter your marks:"))

if (marks >= 90):
    print("Your grade is A.")
elif (marks >= 75) and (marks < 90):
    print("Your grade is B.")
elif (marks >= 60) and (marks < 75):
    print("Your grade is C.")
else :
    print("Your grade is D.")    

#SINGLE LINE IF / TERNERY OPERATOR
food = input("food :")
eat = "Yes" if food.lower()=="cake" else "no"
print(eat)

food = input("food :")
print("i like it ") if food.lower()=="cake" or food.lower()=="cookie" else print("i don't like it.")

#CLEVER IF
age = int(input("Age:"))
vote = ("can not" , "can") [age>=18] #if condition gets tru then right result is printed.
print("you",vote ,"vote.")


sal = float(input("salary per annum:"))
if (sal<= 300000):
    tax1 = sal*0
    print("You have to pay " ,tax1)
elif (sal>300000 and sal<=600000):
    tax2 = sal*0.05
    print("You have to pay " ,tax2)
elif (sal>600000 and sal<=900000):
    tax3 = sal*0.1
    print("You have to pay " ,tax3)
elif (sal>900000 and sal<=1200000) :  
    tax4 = sal*0.15
    print("You have to pay ",tax4)
elif (sal>1200000 and sal<=1500000):
    tax5 = sal*0.2
    print("You have to pay ",tax5) 
elif (sal>1500000):
    tax6 = sal*0.3
    print("You have to pay " ,tax6)
else:
    print("Invalid input , try again later.")    

# FOR COMMENTING MULTIPLE LINES , SHORTCUT KEY IS CTRL+/
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")


# Type conversion 
a,b=int("2"),4
print(a+b) 

# Ques - WAP to input side of a square and print it's area ?
side = float(input("length of side of square: "))

area = side**2
print(area)

#Ques - WAP to input 2 floating point numbers & print their average ?
first = float(input("first:"))
second = float(input("second:"))

average = (first+second)/2
print (average)

#QUES- WAP to check if a number entered by the user is odd or even.
number =float(input("number:"))

if (number % 2 == 0):
    print("number is even")
elif (number % 2 != 0):
    print("number is odd")
else:
    print("Invalid input")

#Ques- WAP to find the greatest of 3 numbers entered by the user.
A = float(input("Enter a number A:"))
B = float(input("Enter a number B:"))
C = float(input("Enter a number C:"))

if (A>B) and (A>C):
    print("A is greatest.")
elif (B>C) and (B>A):
    print("B is greatest.")
elif (C>A) and (C>B):
    print("C is greatest.")
elif (A==B) or (B==C) or (A==C):
    print("equal inputs found.")
else:
    print("Invalid Input.")

name = input("enter your name:")
print("hello " , name)
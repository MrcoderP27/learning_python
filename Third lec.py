# making lists in python
name = ["parth" , "ayush" , "sahil" , "priyanshu"]
str = "parth"
marks = [95,73,78,92]
print("Marks of " ,name[0] , "is :",marks[0])
print("Marks of " , name[1] , " is :",marks[1])
print("Marks of " , name[2] , " is :",marks[2])   
print("Marks of " , name[3] , " is :",marks[3])
#print("Marks of student 5 is :",marks[4]) # this will give error as index 4 does not exist

"""string is immutable but list is mutable
 we can change and access the value of list
str[0] = "aman" """ # this will give error as string is immutable.
name[0] = "parth panjwani" # this will work as list is mutable.

#list slicing
print(marks[0:3])

# LIST METHODS 

subjects = ["English" , "Hindi" , "Maths" , "Physics" , "Chemistry"]

subjects.append("IT") # adds IT at the end of list
print(subjects)

subjects.sort() # sorts the list in ascending order
print(subjects)

subjects.sort(reverse=True) # sorts the list in descending order
print(subjects)

subjects.reverse() # reverses the list
print(subjects)

subjects.insert(5, "Biology") # inserts element at index 
print(subjects)

subjects.remove("IT") # removes the element from list 
print(subjects)

subjects.pop(4) # removes the element at index 4
print(subjects)

#TUPLES
# Tuples are immutable lists, they cannot be changed after creation.
# they are defined using parentheses () instead of square brackets []

tup = ("parth","ayush","sahil","priyanshu")
print(tup)
print(type(tup))
print(tup[3])
# tup[2] = 0  this will give error as tuples are immutable.
# in tuple , it is necesary to put a comma after single element to make it a tuple.
tup2 = ("parth",)  # this is a tuple with one element
print(type(tup2))
 
# Tuple methods
tup1 = (1,2,3,2,2,4)

print(tup1.index(4)) # returns the index of first occurrence of 4)
print(tup1.count(2)) # returns the count of 2 in the tuple 

# Ques- WPA to ask the user to enter the names of their 3 fav. movies & store them in a list.
movie1 = (input("Enter your 1st fav. movie:"))
movie2 = (input("Enter your 2nd fav. movie:"))
movie3 = (input("Enter your 3rd fav. movie:"))

fav_movies = [movie1 , movie2 , movie3]
print("Memory updated , your 3 fav. movies are :" ,fav_movies)

# Ques - WPA to check if a list contains a pallidrome of elements. (Hint: use copy()method.)

# [1,2,3,2,1] is a example of pallidrome. 
list1 = [1,2,3,2,1]

copylist1= list1.copy()
copylist1.reverse()

if(list1==copylist1):
    print("It is a pallidrome.")
else:
    print("It is not a pallidrome.")

# Ques - WPA to count the number of students with grade "A" in following tuple.
grades = ("C","D","A","A","B","B","A")

grades.count("A") # counts the number of A's in the tuple
print("Number of students with grade A is ", grades.count("A"))

# Store the above values in a list and then sort them from a to d . 
grades_list = list(grades) # converting tuple to list 

grades_list.sort()
print(grades_list)
      
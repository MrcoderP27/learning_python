str1 = "parth"
len1 = len(str1)
print(len1)

str2 = "panjwani"
print(len(str2))
ch=str2[5]
print(ch)

add = (str1 + " " + str2)
print (add)
print(len(add))

#slicing 
"""accessing slice instead of accessing Index
if we dont put any value in start or end of the sq. brackets 
then it will assume start and end of len(str).
"""
print(add[4:len(add)])
""" slicing negative index , going from right to left counts -ve."""
print(add[-5:-1])

str3 = "i m Parth , I m learning python from APNA_COLLEGE"

# STRING METHODS 

print(str3.endswith("EGE"))# returns true if string ends with substr
print(str3.capitalize())#capitalizes 1st character
print(str3.replace(" ","_"))#replaces all occurences of old and new 
print(str3.find("h"))#returns 1st index of 1st occurrer
print(str3.count("P"))#counts the occurence of substr
print(str3.upper())#converts all characters to upper case
print(str3.lower())#converts all characters to lower case

#Ques- WPA to input user's first name & print its length.
name = input("username:")
print("length of username :" , len(name))
print(name[0:3] , name[-3:len(name)])

#Ques- WPA to find the occurence of '$' in a string.
dollar = ("$ i$ $o expen$ive")
print(dollar.count("$"))

# Question practice

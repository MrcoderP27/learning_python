#Dictionary and sets 
info = {
    "name" : "parth",
    "age" : 18,
    "hobbies" : "cricket",
}
# Dictionaries are used to store data in key:value pairs 
# It can consist of multiple data types like int, str, list ,tuple,float etc.
# DIctionaries are unordered ,mutable(can be edited) and dont allow duplicate copies.
info["name"] = "Amit" #updating value of key "name"
info["surname"] = "Panjwani" #adding new key-value pair
print(type(info))
print(info)

null_dict = {}#empty dictionary
print(null_dict)

# NESTED DICTIONARIES
nested_dict = {
    "name1" : "parth",
    "subjects" : {
        "physics" : 75,
        "chemistry" : 79,
        "mathematics" : 93,
        "hindi" : 84,
        "english": 89,
    },
    "Result" : "Pass"
    }
print(nested_dict)
print(nested_dict["subjects"]) #we can also access particular key-value pair

print(list(nested_dict["subjects"]))#we can also convert the keys of a dictionary to a list or tuples

#DICTIONARY METHODS
print(list(nested_dict.keys())) #returns all the keys of a dictionary 
print(list(nested_dict.values())) #returns all the values of a dictionary
pairs = list(nested_dict.items()) #returns allthe key-value pairs as tuples
print(pairs[0])

print(nested_dict.get("name1")) #returns value of key "name1"
# Why not : print(nested_dict["name1"])?
# Because if the key doesn't exist, it will throw an error, while get() will return None.
print(nested_dict.get("name2")) #returns None if key doesn't exist

nested_dict.update({"Grade" : "A"}) #inserts the specified items to the dictionary
print(nested_dict)


# SETS
# Set is the collection of the unordered items .
# Each element in a set is unique and immutable .
collection = {1 , 2 , 3 ,"hello","world" , "world"}
print(collection) # it is unordered and ignore duplicate values .
print(type(collection))

Empty = {} # this is empty dictionary not set . 
Empty_set = set() # this is empty set . 
print(type(Empty))
print(type(Empty_set))

# Set methods

set = {2,4,6,8}

set.add(10) # adds the element to the set 
set.add(12)
set.add(14)
print(set)

set.remove(12) # removes the element from the set
set.remove(14)
print(set)

set.pop() # removes random element from the set 
print(set)

set.clear() #clears the set
print(set)

set1 = {"ram", "shyam ", "ghanshyam" }
set2 = {"ram" , "aman", "raman" ,"naman"}

print(set1.union(set2)) # union of two sets
print(set1.intersection(set2)) # intersecton of two 

#Ques - Store the following word meanings in a python dictionary:
word_meanings = {
    "cat" : "a small animal" , 
    "table" : ["a piece of furniture" , "list of facts and figures "]
}
print(word_meanings)

"""Ques - You are give a list of subjects for students. Assume one classroom 
is required for  1 subject . How many classrooms are needed by all students? 
"python", "java", "c++", "python", "javascript", "java", "python", "java" ,"c++", "c" """

classroom = {"python", "java", "c++", "python", "javascript", "java", "python", "java" ,"c++", "c"}
print(classroom)
print(len(classroom)) # length of set gives the number of unique 

"""Ques - WAP to enter marks of 3 subbjects from the user and store them in a dictionary. Start with an empty 
dictionary and add one by one . Use subject name as key and marks as value. """
mark = {}

mark.update({"phy" : int(input("Enter phy marks:"))})
mark.update({"chem" : int(input("Enter chem marks :"))})
mark.update({"maths": int(input("Enter maths marks :"))})

print(mark)


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

set1 = {2,4,6,8}

collection.add("10,12,14") # adds the element to the set 
print(set1)
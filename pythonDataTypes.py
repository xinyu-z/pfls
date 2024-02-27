# strings are defined by doubhle quotes 
# strings are arrays => can be accessed by indexing
# integers are round numbers
# floats are floating point numbers, e.g., 1.5
# changing a float to an integer rounds the float
# booleans also can be represented as 1 and 0
# NoneType: used to store "nothing", often used in functions when you don't want to return anything, or to represent missing data
# examples:

#you need this statement when running the file as a script:
if __name__ == "__main__":
    greeting = "Hellow, world!"
    #query data type:
    data_type = type(greeting)

    print(data_type)
    print(greeting[-1]) #prints the last character of the string

    for char in greeting:
        print(char)
    
    # if x is an input from the user
    x = input("type a number")
    #turn it into integer:
    x = int(x)

    #booleans
    x = 15
    y = 10
    print(x>y)

    true_num = int(True)
    print(true_num)

    # nonetype
    def say_hello(greeting):
        if len(greeting) > 2:
            return greeting
        else: 
            return None
    greeting = say_hello ("") #here length of greeting is zero
    print(greeting)

# data structures
# list / array: used to store a sequence of data and all elements need to be of the same data type
# lists are ordered, and allows duplicates
# e.g., fruit = ["apple", "banana", "cherry", "apple"]

# set: sotres a collection of data
    #not ordered
    #do not allow duplicates
    #e.g., fruit = {"apple", "banana", "cherry"}

fruit = ["apple", "banana", "cherry", "apple"]
data_type = type (fruit)

# the first frurit in the list
first_fruit = fruit[0]
# if asking for fruit[3], will return error message "list index out of range" because 3 is the 4th item and it does not exist in the list
fruit.append("pineapple") # adds pineapple to the list
# to add multiple items:
# not: fruit.append(["pineapple", "strawberry"]), which adds pineapple and strawberry as a list into the existing list
# instead, use: 
fruit += ["pineapple", "strawberry"]

fruit_set = set(fruit)
print(fruit_set)

# Tuple
    #used to store multple data items in a single variable
    #values donot need to be the same type

# dictionary
    #used to map data to each other in key:value pairs
    # values can be retrieved using the keys 
    # can include data of different types
    # ordered, changeable, and do not allow duplicates
    #e.g.,
favorite_fruit = {"Lois": "mango", "Lanmiao" : None, "Orhun" : None}
#retrieve Lois' favorite fruit
Lois_favorite = favorite_fruit["Lois"]
print(Lois_favorite)

#update dictionary
favorite_fruit["Lanmiao"] = "apple"
favorite_fruit["Orhun"] = "grapes"
Orhun_favorite = favorite_fruit["Orhun"]
print(Orhun_favorite)

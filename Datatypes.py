# integers are whole numbers whether negative or positive . decimals are called double , texts are called string
from collections.abc import async_generator

number = 45 #this is an integer
second = 34.98 # this is a float
greeting = "Good Morning" # this is a string
is_Python_Interesting = True #this is a Boolean

#data structures
fruits = ["apple", "banana", "cherry", "peach"] #this is a list
cars = ("jeep","tesla", "BMW") #this is a tuple
countries = {"Sudan", "Canada", "Iran"} #this is a set
student = {
"firstname" : "Kuyka",
"lastname" : "Kunji",
"age" : 20,
"nationality" : "Sudanese"
}




print(number)
print(is_Python_Interesting)
print(fruits)
print(cars)
print(countries)
print(student)
print(student["nationality"])


#typecasting is a method of converting one data type to another
print(float(number))
print(int(second))

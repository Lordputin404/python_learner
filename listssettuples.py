# collection = single variable used to store multiple values
# List = [] ordered and changeable duplicates ok
# Set = {} unordered and immutable but add/remove ok no duplicates
# Tuple = () ordered and unchangeable duplicates ok faster

#List
fruits = ["apple","mango","orange","banana"]
#print(dir(fruits))
#print(help(fruits))

print(fruits)
for fruit in fruits:
    print(fruit)

print(len(fruits))
print("apple" in fruits)

fruits[0] = "pineapple"
for fruit in fruits:
    print(fruit)

fruits.append("coconut")
print(fruits)
fruits.remove("orange")
print(fruits)
fruits.insert(4,"grapes")
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
print(fruits.index("mango"))
print(fruits.count("grapes"))
fruits.clear()
print(fruits)

#Set
fruits2 = {"apple","mango","orange","banana"}

fruits2.add("pineapple")
fruits2.remove("mango")
fruits2.pop()
fruits2.clear()
print(fruits2)

#Tuple
fruits3 = ("apple","mango","orange","banana","orange")
print(fruits3.index("mango"))
print(fruits3.count("orange"))
# dictionary = a collection of {key:value} pairs
 #              ordered and changeable no duplicates

capitals = {"USA" : "Washington DC",
            "India" : "New Delhi",
            "China" : "Beijing",
            "Russia" : "Moscow"}

input_value = input("Enter the Country : ")
print(f"The capital of {input_value} is {capitals.get(input_value)}")

capitals.update({"Germany":"Berlin"})
#capitals.pop("China")
#capitals.popitem(China) # Deletes last key:value
#capitals.clear()
print(capitals)
for key in capitals.keys():
    print(key)
for value in capitals.values():
    print(value)
for key, value in capitals.items():
    print(f"{key}:{value}")

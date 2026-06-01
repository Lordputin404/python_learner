fruits = ["mango", "grapes", "orange", "banana"]
veg =    ["cucumber", "cabbage", "potato"]
nonveg = ["fish", "chicken"]

groceries = [fruits, veg, nonveg]

for collection in groceries:
    for food in collection:
        print(food, end=(" "))
    print()


from car import Car

# object = a bundle of related attributes (variables)
#          and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure
#          and layout of an object

car1 = Car("Mustang",2024,"Yellow",False)
car2 = Car("Corvette",2025,"Green",True)
car3 = Car("Charger",2026,"Blue",False)

car1.drive()
car2.stop()
car3.describe()
#Inheritance = Allows you to inherit attributes and methods from another class
#              helps with code reusability and extendibility
#              class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
class Cat(Animal):
    pass
class Mouse(Animal):
    pass

cat = Cat("Tom")
mouse = Mouse("Jerry")

print(cat.name)
print(cat.is_alive)
print(mouse.name)
print(mouse.is_alive)
cat.eat()
mouse.sleep()
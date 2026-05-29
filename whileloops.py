# while loop = Execute the code until it's true

name = input("Enter your name:")

while name == "" :
    print("You have not entered your name")
    name = input("Enter your name")
print(f"Your name is {name}")

age = int(input("Enter your age:"))

while age < 0 :
    print("Age can't be negative number")
    age = int(input("Enter your age:"))
print(f"You are {age} years old")

sport = input("Enter your favourite sport(Press q to quit):")

while not sport == "q":
    print(f"Your favourite sport is {sport}")
print("You have exited the program")
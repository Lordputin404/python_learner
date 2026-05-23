operator = input("Enter an operator(+,-,*,/): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == "+" :
    result = float(num1 + num2)
    print(f"Addition of {num1} and {num2} is : {round(result ,2)}")
elif operator == "-" :
    result = float(num1 - num2)
    print(f"Subtraction of {num1} and {num2} is : {round(result ,2)}")

elif operator == "*" :
    result = float(num1 + num2)
    print(f"Multiplication of {num1} and {num2} is : {round(result ,2)}")

elif operator == "/" :
    result = float(num1 / num2)
    print(f"Division of {num1} and {num2} is : {round(result ,2)}")

else :
    print("You have an invalid input")


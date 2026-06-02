# return = It's used to end a function 
#          and send a result back to caller

def add(x,y):
    z = x + y
    return z

def subtract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(f"Addition is :{add(1,2)}")
print(f"Subtraction is :{subtract(1,2)}")
print(f"Multiplication is :{multiply(1,2)}")
print(f"Division is :{divide(1,2)}")
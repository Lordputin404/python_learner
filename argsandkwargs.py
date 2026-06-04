# *args = allows you to pass multiple non key arguments
# **kwargs = allows you to pass multiple keyword arguments
#  * = unpacking operator
#    1. positional 2. default 3. keyword 4. ARBITRARY

def add(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

print(add(1,2,3,4,5))

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake street",
              city="New York",
              state="New York",
              country="USA")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg,end =" ")
    print()
    for value in kwargs.values():
        print(value,end =" ")

shipping_label("Dr." ,"Spongebob", "Hudson",
               street="123 Fake street",
               city="New York",
               state="New York",
               country="USA")
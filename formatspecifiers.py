#format specifiers = {:flags}  format a value according to the flags inserted.

# .(number)f = round to many decimal places(fixed point)
# :(number) = allocate that many places
# :0(number) = allocate and zero pad that many spaces
# :>(number) = left justify
# :<(number) = right justify
# :^(number) = center align
# :+ use a + sign to indicate positive number
# := = place sign to left most position
# :(space)= insert a space before positive numbers
# :, = comma seperator

price1 = 3.14775
price2 = -466.67
price3 = 35.57

print(f"Price1 is ${price1: }")
print(f"Price2 is ${price2: }")
print(f"Price3 is ${price3: }")
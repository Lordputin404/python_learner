item = input("What would you like to buy?:")
price = float(input("What is the price of the item?:"))
quantity = int(input("How much you want to buy?:"))
total = price * quantity

print(f"You have bought {quantity} {item}/s")
print(f"Your total cost is ${total}")
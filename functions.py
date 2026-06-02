# function = a block of reusable code 
#            place () after the function name to invoke it

def wish(name,age):
    print(f"Happy birthday {name}")
    print(f"You are {age} years old")

def netflix_invoice(user,amount):
    print(f"User {user} has due amount of ${amount:.2f} of previous month")

wish("Amar",21)
wish("Amar",21)
netflix_invoice("Amar",21.76)
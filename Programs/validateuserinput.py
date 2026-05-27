#Validate user input program
#username can't be more than 12 characters
#username must not contain spaces
#username must not contain digits

username = input("Enter your username :")

if len(username) > 12:
    print(f"Your username {username} cannot contain more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username cannot contain spaces")
elif not username.isalpha():
    print("Your username cannot contain digits")
else:
    print(f"Welcome {username}")
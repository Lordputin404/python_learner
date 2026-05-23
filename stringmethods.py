#name =  input("Enter your full name: ")
phone_no = input("Enter your phone number: ")

#result = len(name) #returns length
#result = name.find(" ") #inds the first occurence given
#result = name.rfind("r") #finds the lastoccurence given
#name = name.capitalize() #Capitalizs the first letter of a string
#name = name.upper() #Converts all the chars to upper case
#name = name.lower() #Comverts all the chars to lower case
#result = name.isdigit() #Returns boolean value true if string comtains only digits
#result = name.isalpha() #Returns boolean value true if string contains only alphabets
result = phone_no.count("-") #finds the argument given 

print(result)
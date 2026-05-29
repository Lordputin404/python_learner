# for loops = Executes a block of code for a fixed number of time
# You can iterate over a range, string, sequence etc

for x in reversed(range(1,11)) :
    print(x)
print("Happy New Year")

#Using step count
for x in reversed(range(1,11,2)) :
        print(x)

credit_card = "1234-5678-4666-4777"

for x in credit_card :
    print(x)

#Skips an element in between
for x in range(1,20) :
        if x == 13 :
           continue
        else :
           print(x)
        
#Breaks from the loop
for x in range(1,20) :
        if x == 13 :
           break
        else :
           print(x)

numStart, numEnd = 0,0

numStart = int(input("Enter a starting number: ")) # strating number
numEnd = int(input("Enter an ending number: ")) # ending number
j = [] # array

for a in range(numStart, numEnd):
    num = int(input("Enter value numbers here: "))
    j.append(num)

for i in range(numStart, numEnd): # number positions in ordinal
    if(i == 1):
        print("The " + str(i) + "st ordinal number" + "\n")
    elif(i == 2):
        print("The " + str(i) + "nd ordinal number" + "\n")
    elif(i == 3):
        print("The " + str(i) + "rd ordinal number" + "\n")
    else:
        print("The " + str(i) + "th ordinal number" + "\n")
print("The inputted values respectively to its ordinal numbers are: "+ str(j)) # printing out the inputted numbers
    




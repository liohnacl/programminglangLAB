# print("Hello world \nHi Human \nGood afternoon\ta")
# print("""

# Gene

# """)

# print(str(1) +"a" + str(2) + "bd")

# a = "1"
# b = 2
# c = int(a) + b

# print(c)

# d = 2

# print(float(d))

# print("Hello Katty's friend")

# f = int(input("Enter a 1st value: "))
# g = int(input("Enter a 2nd value: "))
# h = f * g
# print(h)

# age = int(input("Enter age: "))

# if age >= 18 and age <=59:
#     print("Legal age")

# elif age >= 60:
#     print("Senior Citizen")

# else:
#     print("Your age is "+ str(age) + " not legal age.")

# age_Category = "legal age" if (age >= 18 and age <= 59)  else "Not legal Age"
# print(age_Category)

# arr1 = ["teddy bear","penguin","alcohol","mask"]
# print(arr1)
# print(arr1[0] + " " + arr1[1])

# arr1 = [["teddy bear","penguin","alcohol","mask"],["glass","toy","wallet"],["glass1","toy1","wallet1",["vaccine", "paper","towel"]]]
# print(arr1)
# print(arr1[0][3] + " or " + arr1[1][2] + " and " + arr1[2][0] +" and " + arr1[2][3][0])

# for a in range(10):
#     print(a)

# word = "String"
# for char in word:
#     print(char)
    
items = [
    ["teddy bear","penguin","alcohol","mask"], #0
    ["teddy bear1","penguin1","alcohol1","mask1"], #1
    ["teddy bear2","penguin2","alcohol2","mask2"] #2
    ]
# for item in items:
#     for inner_item in item:
#         for inner_item1 in inner_item:
#             print(inner_item1)
# print(len(items))

# for y in range (len(items)):
#     for x in range(len(items[y])):
#         print(items[y][x])

# len(items) = 3 #0
# len(items[y]) = 4

# len(items) = 3 #1
# len(items[y]) = 4

for y in range(1,10):
    print("OUTER" + str(y))
    for x in range(3):
        print("INNER")
        

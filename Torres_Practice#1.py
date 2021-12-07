# def multiply(*args):
#     return args[0] * args[1]


# a = int(input("Enter any number here: "))
# b = int(input("Enter any number here: "))

# product = multiply(a,b)
# print("The product of " + str(a) + " * " + str(b) + " is " + str(product))


# def add(**kwargs):
#     num1 = kwargs['num1']
#     num2 = kwargs['num2']
#     num3 = kwargs['num3']
#     return num1 + num2 + num3

# c = int(input("Enter any number here: "))
# d = int(input("Enter any number here: "))
# e = int(input("Enter any number here: "))

# sum = add(num1 = c,num2 = d,num3 = e)
# print("The sum of " + str(c) + " " + str(d) + " and " + str(e) + " is " + str(sum))

# nums = []
# ranges,values = 0,0

# ranges = int(input("Enter how many values you will enter: "))

# for h in range(0,ranges):
#     values = int(input(f"{h+1}: "))
#     nums.append(values)
# print(nums)

def valInput():
    try:
        temp = list(map(int,input("Enter numbers with the use of '+' to separate it: ").split("+")))
        return temp
    except Exception:
        print("INVALID INPUT.....")

def adding(val):
    try:
        add = 0
        for a in val:
            add += a
        return add
    except Exception:
        print("INVALID INPUT......")
        
if __name__ == "__main__":
    col = valInput()
    addition = adding(col)
    print(f"The sum of the inputted numbers is {addition}")


# valA=[]
# valB=[]
# sub =[]
# ranges1,ranges2 = 0,0

# def enteringListA():
#     ranges1 = int(input("Enter how many numebrs your will input in list A: "))
#     for a in range(0,ranges1):
#         numA = int(input(f"ListA number {a+1}: "))
#         valA.append(numA)
        
# def enteringListB():
#     ranges2 = int(input("Enter how many numbers your will input in list B: "))
#     for b in range(0,ranges2):
#         numB = int(input(f"ListB number {b+1}: "))
#         valB.append(numB)


# if __name__ == "__main__":
#     enteringListA()
#     enteringListB()
    
#     for c in range(len(valA)):
#         sub.append(valA[c]-valB[c])
#     print(sub)
    
    


    
 

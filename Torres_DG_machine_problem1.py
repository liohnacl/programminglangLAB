row = int(input("Input number of rows: "))
for y in range(1,row+3): #Outer loop
     for x in range(1,y-1): #Inner loop
         print(x)
     print("\n")

# Based from what I did, the outer loop is the sequence in which what numbers from 1 to 10 will be read by the machine.
# Then the inner loop will actually print it but it will decrease the value of y because of y-1.
# printing a normal 1 to 10 numbers has a structure of range(1,11) which makes my assumption that the additional 1 is 0
# 0 1 2 3 4 5 6 7 8 9 10 if we count all of this it is 11.
# But in this looping program makes my assumption that there are 13 numbers 
# 0 1 2 3 4 5 6 7 8 9 10 11 12 if we count it is 13.
# 1 2 3 4 5 6 7 8 9 10 11 12  if the range is (1,13)
# and if we decrease 12 by 1 because 12 is the value of y considering the 1 to 12 numbers.
# Now this will give 11 which means 0 to 10 are the numbers to be printed but since it indicates that the range is started at 1.
# 0 is excluded. Now the iteration of this program by the two loops depends on the logic of each iteration makes a increase sequeance
# of printed numbers. Like 1 then 1 2 then 1 2 3 etc.



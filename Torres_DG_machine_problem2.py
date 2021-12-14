for y in range (10+1,5,-1): # Outer loop
    for x in range (0, y-1): # Inner loop
        print("#", end = " ")
    print(" ")

# I used 10+1 for the sequence of decreasing the printed # hashtag signs.
# The inner for loop's y-1 decreases it as a demo of what I observed:
# y = 11 in the outer for loop but in the inner loop it will be 10 due to y-1
# This makes the value of 10 assigned to be the number of times it will print the hashtag symbol
# It will now go back to the first loop or outer loop after executing the inner loop the -1 in it decreases the value of 10 in 10+1 making it 9+1
# Same process as before but in this sequence it will print hastag symbols 9 times because of y-1 or 10 -1 which is 9
# The stoppage of the loop where the part of five times printing the hastag symbols.
# In the outer loop's values declared, on the middle value which is 5. This is a condition in which if the hashtag values
# are printed five times, the whole loop will be terminated.
# the end syntax is the same as \n or new line.
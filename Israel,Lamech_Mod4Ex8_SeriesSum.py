#############################################
# CS 1110A - Programming in Python          #
# Module 4 - Exercise 8 - Series Sum        #
# Author: Lamech Israel                     #
#                                           #
#############################################

def series_sum(n, d):
    # Initialize the variable that will hold each number and the total sum
    current_number = 0
    sum = 0
    
    # Iterate through the full value of n
    for i in range(n):
        # Add 'd' to the next highest 'tenth place' of the current number
        current_number += (d * 10**i)
        # Add the new number to the sum
        sum += current_number
        
    # Print the result
    print('\nn = {}   d = {}   series sum = {}'.format(n,d,sum))


print('Series Sums')

while True:
    # Obtain the first number from the user. Also, convert the input into a number.
    n = int(input('\nValue of n: '))
    
    # Exit program if 'n' is less than 1
    if n < 1:
        print('\nDone!')
        exit() 
    else:
        # Obtain the second number from the user. Also, convert the input into a number.
        d = int(input('Value of d: '))
        
        while d < 1 or d > 9:
            print('d must be between 1 and 9')
            d = int(input('Value of d: '))
        
        # Calculate the numbers in a series
        Running = series_sum(n, d)

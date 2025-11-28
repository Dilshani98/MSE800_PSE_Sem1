#Activity 3 - Part 2: Math functions using Math Lib


import math

#define function for calculate Fibonacci seq
def cal_fibonacci(length):

    #define initial values
    previousValue = 0
    currentValue = 1

    #handle special cases 
    if length <= 0:
        print("Invalid length")

    elif length == 1:
        print(0)

    else:
        print(previousValue) #0
        print(currentValue) #1

        for i in range(length - 2):
            #use math.fsum to do addition
            nextValue = int(math.fsum([previousValue,currentValue])) 
            print(nextValue)
            
            # update values
            previousValue = currentValue
            currentValue = nextValue




#define function for calculate Factorial
def cal_factorial(n):
   #use math.factorial to directly calculate the output
   factorial =  math.factorial(n)
   print(factorial)



#get user input for sequence length 
length = int(input("Enter length for the Fibonacci sequence: "))
cal_fibonacci(length)

#get user input for factorial
n = int(input("Enter a number to calculate the factorial: "))
cal_factorial(n)
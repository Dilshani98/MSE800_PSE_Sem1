#Update code in activity W1-A3 using recursive function

#factorial function using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
#fibonacci function using recursion
def fibonacci(n):
    if n <= 1:
        return n
    
    seq = fibonacci(n - 1) + fibonacci(n - 2)
    return seq
    

#get user input for sequence length 
length = int(input("Enter length for the Fibonacci sequence: "))
print(fibonacci(length))

#get user input for factorial
n = int(input("Enter a number to calculate the factorial: "))
factorial(n)
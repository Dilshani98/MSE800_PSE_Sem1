class mathFunctions:
    #factorial function using recursion
    def factorial(n):

        if n< 0:
            return "Invalid input"
        
        if n == 0 or n == 1:
            return 1
        
        return n * mathFunctions.factorial(n - 1)
        

    #fibonacci function using recursion
    def fibonacci(n):
        if n <= 1:
            return n      
        seq = mathFunctions.fibonacci(n - 1) + mathFunctions.fibonacci(n - 2)
        return seq
    


if __name__ == "__main__":
    length = int(input("Enter length for the Fibonacci sequence: "))

    n = int(input("Enter a number to calculate the factorial: "))

    print("\nFactorial result:", mathFunctions.factorial(length))
    print("\nFobonacci result:", mathFunctions.fibonacci(n))
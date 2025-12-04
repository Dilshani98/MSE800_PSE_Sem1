#Develop W2-A3 with using Class& Object

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
        if n<0:
            return "Invalid input"
        if n == 1:
            return n
        if n == 0:
            return n      
        seq = mathFunctions.fibonacci(n - 1) + mathFunctions.fibonacci(n - 2)
        return seq
    


if __name__ == "__main__":
    length = int(input("Enter length for the Fibonacci sequence: "))

    print("Fobonacci result:", mathFunctions.fibonacci(length))

    n = int(input("\nEnter a number to calculate the factorial: "))

    print("Factorial result:", mathFunctions.factorial(n))
    
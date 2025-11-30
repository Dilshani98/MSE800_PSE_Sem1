class MathSeries:

    def __init__(self,n):
        self.n = n

    # @staticmethod
    def factorial_recursive(n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n in (0, 1):
            return 1
        #print(MathSeries.factorial_recursive(n - 1))
        return n * MathSeries.factorial_recursive(n - 1)



    # @staticmethod
    def fibonacci_recursive(n):
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        if n == 0:
            return 0
        if n == 1:
            return 1      
        #print(n)
        return MathSeries.fibonacci_recursive(n - 1) + MathSeries.fibonacci_recursive(n - 2)

    def printFib(n):
        fibArray = []
        for i in range(n+1):
            nextValue = MathSeries.fibonacci_recursive(i) 
            fibArray.append(nextValue)
        return fibArray



if __name__ == "__main__":
    n = 5

    #create an object
    obj = MathSeries(n)

    print("Factorial (recursive):", factorial_recursive(obj))
    print("Fibonacci (recursive):", fibonacci_recursive())
    print("Fibonacci (recursive):", obj.printFib())

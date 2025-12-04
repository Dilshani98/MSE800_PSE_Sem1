#print Fib series
class MathSeries:

    def __init__(self,n): #define _init_ method with self param
        self.n = n

    def factorial_recursive(self):
        if (self.n) < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if (self.n) in (0, 1):
            return 1
        return self.n * MathSeries(self.n-1).factorial_recursive()

    # @staticmethod --> no need this here bc we are using self param
    def fibonacci_recursive(self):
        if self.n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        if self.n == 0:
            return 0
        if self.n == 1:
            return 1      
        return MathSeries(self.n-1).fibonacci_recursive() + MathSeries(self.n-2).fibonacci_recursive()

    def printFib(self):
        fibArray = []
        for i in range(self.n+1):
            nextValue = MathSeries(i).fibonacci_recursive() 
            fibArray.append(nextValue)
        return fibArray



if __name__ == "__main__":
    n = 5

    #create an object
    obj = MathSeries(n) # once we create an object it should define the _init_ method with self param

    #otherwise python will automatically pass the object reference as the first param to the methods

    print("Factorial value(recursive):", obj.factorial_recursive())
    print("Fibonacci value(recursive):", obj.fibonacci_recursive())
    print("Fibonacci series(recursive):", obj.printFib())

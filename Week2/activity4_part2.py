#print Fib series
class MathSeries:

    def factorial_recursive(n):
        if (n) < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if (n) in (0, 1):
            return 1
        return n * MathSeries.factorial_recursive(n-1)

    def fibonacci_recursive(n):
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        if n == 0:
            return 0
        if n == 1:
            return 1      
        return MathSeries.fibonacci_recursive(n-1) + MathSeries.fibonacci_recursive(n-2)

    def printFib(n):
        fibArray = []
        for i in range(n+1):
            nextValue = MathSeries.fibonacci_recursive(i) 
            fibArray.append(nextValue)
        return fibArray



if __name__ == "__main__":
    n = 5

    print("Factorial value(recursive):", MathSeries.factorial_recursive(n))
    print("Fibonacci value(recursive):", MathSeries.fibonacci_recursive(n))
    print("Fibonacci series(recursive):", MathSeries.printFib(n))

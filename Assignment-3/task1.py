def factorial(n):
    """Function to calculate factorial of a number"""
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

num = 5
print(f"The factorial of {num} is: {factorial(num)}")

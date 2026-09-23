# functions.py

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the division of a by b, with zero check."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def factorial(n):
    """Return the factorial of n using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 0:
        return "Error: Input must be positive"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
if __name__ == "__main__":
    print("Add:", add(5, 3))
    print("Subtract:", subtract(5, 3))
    print("Multiply:", multiply(5, 3))
    print("Divide:", divide(5, 3))
    print("Factorial:", factorial(5))
    print("Fibonacci:", fibonacci(7))

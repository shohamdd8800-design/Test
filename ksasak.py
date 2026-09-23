# utilities.py

import math

# --- Math Functions ---
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def factorial(n):
    return math.factorial(n)

def fibonacci(n):
    if n < 0:
        return "Error: Input must be non-negative"
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# --- String Functions ---
def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# --- Utility Functions ---
def max_in_list(lst):
    return max(lst) if lst else None

def min_in_list(lst):
    return min(lst) if lst else None

def average(lst):
    return sum(lst) / len(lst) if lst else None

# Example usage
if __name__ == "__main__":
    print("Add:", add(10, 5))
    print("Fibonacci:", fibonacci(10))
    print("Is Prime:", is_prime(29))
    print("Reverse:", reverse_string("Shoham"))
    print("Palindrome:", is_palindrome("madam"))
    print("Vowels:", count_vowels("Black Clover"))
    print("Max:", max_in_list([1, 5, 9, 3]))
    print("Average:", average([10, 20, 30]))

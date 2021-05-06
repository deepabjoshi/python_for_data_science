"""
Examples for input and output.
Input: user input
Output: print to stderr
"""
import sys

try:
    name = input("Enter your name: ")
    print(name)
    # num = input("Enter a number: ") # Raises a TypeError
    num = int(input("Enter a number: "))
    num += 1
    print(num)
except EOFError as e:
    print("No input found: ", e, file=sys.stderr)
except TypeError as e:
    print("Have you converted to required type? ", e, file=sys.stderr)
except ValueError as e:
    print("Bad value: ", e, file=sys.stderr)
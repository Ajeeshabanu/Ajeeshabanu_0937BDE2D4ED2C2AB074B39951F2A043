# Python 3 program to find
# factorial of given number
def factorial(n):

  # single line to find factorial
  return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


# Driver Code
num = int(input("enter a value:"))
print("Factorial of", num, "is", factorial(num))

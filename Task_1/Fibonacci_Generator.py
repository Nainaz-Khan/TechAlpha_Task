# Fibonacci_Generator - Fibonacci series by Generator

def fibonacci():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b
f=fibonacci()
number=int(input("Enter the term number:"))
if number<=0:
    print("Invalid number!! Please Enter number greater than 0 ")
else:
    for i in range(number):
        print(next(f), end=' ')
# Fibonnaci_Generator - Fibonacci Series by recursion

def fib(n):
    if n<=1:
        return n
    else:
        return fib (n-1)+ fib (n-2)
n=int(input("Enter a number here:"))
if n<=0:
    print("Enter positive number:")
else:
    for i in range(n):
        print(fib(i), end=' ')
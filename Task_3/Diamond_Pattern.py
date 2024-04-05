# program to print Diamond shape with 2n rows

def print_diamond(rows):
    # Upper half of the diamond
    for i in range(1, rows//2 + 2):
        print(" " * ((rows//2 + 1 - i)) + "*" * (2 * i - 1))
    
    # Lower half of the diamond
    for i in range(rows//2, 0, -1):
        print(" " * ((rows//2 + 1 - i)) + "*" * (2 * i - 1))

n=int(input("Enter any number:"))
print_diamond(n)





"""
Diamond pattern for only odd numbers,
Same given as in assignment

"""

def print_star_pattern(rows):
    # Upper half of the pattern
    for i in range(1, rows + 1, 2):
        print(" " * ((rows - i) // 2) + "*" * i)

    # Middle line
    print("*" * rows)

    # Lower half of the pattern
    for i in range(rows - 2, 0, -2):
        print(" " * ((rows - i) // 2) + "*" * i)


n = int(input("Enter odd number:"))
if n%2 != 0:
    print_star_pattern(n)
else:
    print("Please enter odd number!!")

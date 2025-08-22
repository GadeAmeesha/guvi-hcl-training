n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))



for i in range(0, 5):
    for j in range(0, 5):
        print("*", end="")
    print()


n = 5
for i in range(1, n + 1):
    
    for sp in range(n, i, -1):
        print(" ", end="")
    
    for j in range(1, i + 1):
        print(j, end=" ")
    
    print()


    rows = 5
for i in range(rows):
    # Print spaces
    for j in range(rows - i - 1):
        print(" ", end="")
    # Print stars
    for k in range(2 * i + 1):
        print("*", end="")
    print()


    # Right-angled triangle
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()


    # Isosceles triangle
rows = 5
for i in range(rows):
    # Print spaces
    for j in range(rows - i - 1):
        print(" ", end="")
    # Print stars
    for k in range(2 * i + 1):
        print("*", end="")
    print()

    # Rectangle
height = 4
width = 8
for i in range(height):
    for j in range(width):
        print("*", end="")
    print()
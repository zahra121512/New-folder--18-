print("Inverted half pyramid pattern of stars (*): ")
n = int(input("Enter the number of rows: "))

for i in range(n, 0, -1):
    for j in range(0, i):
        print("*", end="")
    print()
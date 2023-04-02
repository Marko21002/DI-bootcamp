rows = 9  # number of rows in the pattern

for i in range(rows):
    if i <= rows//2:
        for j in range(i+1):
            print("*", end="")
    else:
        for j in range(rows-i):
            print("*", end="")
    print()

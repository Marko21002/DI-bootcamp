password = 1234
password1 = 4123

while True:
    try:
        x = int(input("Please enter a number: "))
        if x == password:
            break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

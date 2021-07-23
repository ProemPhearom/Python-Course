
try: #block lets you test a block of code for errors.
    number = int(input("Enter any number: "))
    print(number)
except:#block lets you handle the error.
    print("Invalid input , input must be an integer")
finally:#The finally block lets you execute code, regardless of the result of the try- and except blocks
    print("Please rerun the program again")
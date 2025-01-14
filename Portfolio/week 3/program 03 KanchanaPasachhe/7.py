"""Modify your "Times Table" program so that the user enters the number of the table
 they require. This number should be between 0 and 12 inclusive."""

number=int(input("Enter a number between 0 to 12:"))

if number<0 or number>12:
    print("Invalid")
else:
    for i in range (13):
        result=i*number
        print(f"{i}*{number}={result}")
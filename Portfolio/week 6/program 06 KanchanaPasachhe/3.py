"""Write and test a function that determines if a given integer is a prime 
number. A prime number is an integer greater than 1 that cannot be produced 
by multiplying two other integers."""

def prime(number):
    count=0
    for i in range (1,number+1):
        if number%i==0:
            count=count+1
    if (count==2):
        print(f"The given number {number} is prime number.")
    else:
        print(f"The given number {number} is not a prime number.")

number=int(input("Enter the number you want to check:"))
prime(number)

"""Functions are often used to validate input. Write a function 
that accepts a single integer as a parameter and returns True 
if the integer is in the range 0 to 100 (inclusive), or False 
otherwise. Write a short program to test the function. """

def input(num):
    return num in range(0,100)

def input_test():
    values=[-1,-2,10,99,-50,40,4,-9]
    for value in values:
        result=input(value)
        print(f"Input value: {value}, validation: {result}")
input_test()
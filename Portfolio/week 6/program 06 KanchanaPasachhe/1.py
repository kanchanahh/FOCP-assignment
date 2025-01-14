""" Write a function that accepts a positive integer as a parameter 
and then returns a representation of that number in binary (base 2).
 Hint: This is in many ways a trick question. Think!"""

def to_binary(n):
    
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    return bin(n)[2:]  

number = int(input("Enter a number:"))
binary_representation = to_binary(number)
print(f"The binary representation of {number} is {binary_representation}")

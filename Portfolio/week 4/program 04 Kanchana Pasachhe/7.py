"""Write a program that reads 6 temperatures (in the same 
format as before), and displays the maximum, minimum, and 
mean of the values. Hint: You should know there are built-in 
functions for max and min. If you hunt, you might also find 
one for the mean. """

temperature=[]

for i in range(6):
    input_temp=float(input(f"Enter the temperature in celsius {i+1}:"))
    temperature.append(input_temp)

max_temp=max(temperature)
min_temp=min(temperature)
sum_temp=max_temp + min_temp
mean_temp = sum_temp / len(temperature)

print(f"Maximum temperature:{max_temp}")
print(f"Minimum temperature:{min_temp}")
print(f"Sum of temperatures:{sum_temp}")
print(f"Mean temperature:{mean_temp}")
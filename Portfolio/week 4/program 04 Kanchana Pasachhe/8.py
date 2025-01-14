"""Modify the previous program so that it can process any 
number of values. The input terminates when the user just 
pressed "Enter" at the prompt rather than entering a value."""

temperature=[]

while True:
    input_temp=input("Enter the temperature in celsius")
    if input_temp=="":
        break
    temperatures=float(input_temp)
    temperature.append(temperatures)

    if temperature:
        max_temp=max(temperature)
        min_temp=min(temperature)
        sum_temp=max_temp + min_temp
        mean_temp = sum_temp / len(temperature)

        print(f"Maximum temperature:{max_temp}")
        print(f"Minimum temperature:{min_temp}")
        print(f"Sum of temperatures:{sum_temp}")
        print(f"Mean temperature:{mean_temp}")
    
    else:
        print("Temperature not entered")
"""Last week you wrote a program that processed a collection 
of temperature readings entered by the user and displayed the
maximum, minimum, and mean. Create a version of that program 
that takes the values from the command-line instead. Be sure 
to handle the case where no arguments are provided!"""

from sys import argv
from statistics import mean
try:
    list=argv[1:]
    new_list=[(int(i)) for i in list]
    max_value=max(new_list)
    min_value=min(new_list)
    mean_value=mean(new_list)
except IndexError as i:
    print("No string provided and ",i)
except ValueError as v:
    print("No argument provided",v)
except NameError as n:
    print("No argument provided",n)
else:
    print("The max value is",max_value)
    print("The min value is",min_value)
    print("The mean value is",mean_value)
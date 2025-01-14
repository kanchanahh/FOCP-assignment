"""Write a program that, when run from the command line, 
reports how many arguments were provided. (Remember that the 
program name itself isnotan argument)."""

from sys import argv
print(len(argv)-1)
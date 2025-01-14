"""Write a program that takes the name of a file as a command-line 
argument, and creates a backup copy of that file. The backup should 
contain an exact copy of the contents of the original and should, 
obviously, have a different name. Hint: By now, you should be 
getting the idea that there is a built-in way to do the heavy 
li ing here! Take a look at the "Brief Tour of the Standard 
Library" in the docs."""

from shutil import copyfile
from sys import argv
origin_filename=None
try:
    origin_filename=argv[1]
    filename, extension=origin_filename.split('.')
    target_filename=(f"{filename}_backup.{extension}")
    copyfile(origin_filename, target_filename)
    print("File copied")
except IndexError as i:
    print("File name is not given",i)
except ValueError as v:
    print("Cannot find file extension",v)
except FileNotFoundError as f:
    filename=origin_filename
    print(f"Cannot open {filename}.",f)
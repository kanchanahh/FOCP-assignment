"""Modify your "greetings" program so that the first 
letter of the name entered is always in uppercase with 
the rest in lowercase. This should happen even if the 
user entered their name dierently. So if the user entered 
arthur, ARTHUR, or even arTHur the name should be displayed 
as Arthur."""

def name_correction():
    name=input("Enter your name: ")
    format_name=name.capitalize()
    print(f"{format_name}")
name_correction()
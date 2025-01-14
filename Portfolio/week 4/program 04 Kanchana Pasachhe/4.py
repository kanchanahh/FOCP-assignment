"""When processing data it is often useful to remove the 
last character from some input (it is often a newline). 
Write and test a function that takes a string parameter 
and returns it with the last character removed. 
(If the string contains one or fewer characters, return 
it unchanged.) """

def last_char(string):
    if len(string)>1:
        return string[:-1]
    return string

print(last_char("Kanchana"))
print(last_char("K"))
print(last_char(""))
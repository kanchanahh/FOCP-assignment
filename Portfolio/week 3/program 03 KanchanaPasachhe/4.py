""" Modify your program again so that the chosen password cannot be one of a list of
 common passwords, defined thus:
 BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']"""

def set_password():
    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
    while True:
        password=input("Enter new password:")
        if len(password)<8 or len(password)>12:
            print("Password doesnot meet the requirement.Please try again.")
            continue
            
        if password.lower() in BAD_PASSWORDS:
            print("Password too common. Try another one.")
            continue
        
        password1=input("Re-enter your password again:")
        if password == password1:
            print("Password set")
        else:
            print("Error: Passwords do not match. Try again.")
            break
set_password()
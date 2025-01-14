"""Modify your program a final time so that it executes until the user successfully
 chooses a password. That is, if the password chosen fails any of the checks, the
 program should return to asking for the password the first time."""

def set_password():
    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
    while True:
        password=input("Enter a password which should be between 8 to 12 characters:")
        if len(password)<8 or len(password)>12:
            print("Password doesnot meet the requirement.Please try again.")
            continue
            
        if password in BAD_PASSWORDS:
            print("Password too common. Try another one.")
            continue
        
        password1=input("Re-enter your password again:")
        if password == password1:
            print("Password set")
        else:
            print("Error: Passwords do not match. Try again.")
            break
set_password()
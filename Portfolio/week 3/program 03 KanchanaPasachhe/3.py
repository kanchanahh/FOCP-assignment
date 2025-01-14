"""Modify your previous program so that the password must be between 8 and 12
 characters (inclusive) long."""

def set_password():
    password=input("Enter new password:")
    if len(password)<8 or len(password)>12:
        print("Password doesnot meet the requirement.Please try again.")
        return
                
    password1=input("Re-enter your password again:")
    if password == password1:
        print("Password set")
    else:
        print("Error: Passwords do not match. Try again.")

set_password()
"""Write a program that simulates the way in which a user might choose a password.
 The program should prompt for a new password, and then prompt again. If the two
 passwords entered are the same the program should say "Password Set" or
 similar, otherwise it should report an error."""

def set_password():
    password=input("Enter new password:")
    password1=input("Re-enter your password again:")
    if password == password1:
        print("Password set")
    else:
        print("Error: Passwords do not match. Try again.")

set_password()
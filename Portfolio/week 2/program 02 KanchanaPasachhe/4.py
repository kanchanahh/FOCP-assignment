"""A kind teacher wishes to distribute a tub of sweets between her pupils. She will
 first count the sweets and then divide them according to how many pupils attend
 that day. Write a program that will tell the teacher how many sweets to give to each
 pupil, and how many she will have left over."""

numberofsweets=input("Please enter number of sweets:")
numberofstudents=input("Please enter the number of students:")

 
sweets=int(numberofsweets)//int(numberofstudents)
remaining_students=int(numberofsweets)%int(numberofstudents)
print(f"{sweets} sweets each should be given to {numberofstudents} students with {remaining_students} sweets remaining")
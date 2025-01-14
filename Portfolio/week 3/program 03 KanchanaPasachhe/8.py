"""Modify the "Times Table" again so that the user still enters the number of the table,
 but if this number is negative the table is printed backwards. So entering "-7"
 would produce the Seven Times Table starting at "12 times" down to "0 times"."""


number=int(input("Enter the number of the table you require: "))
if number<0:
    for i in range(12, -1, -1):
        prod=i*number
        print(i, 'x', number, '=', prod)
else:
    for i in range(13):
        prod=1*number
        print(number, 'x 7 =',prod)
        number+=1
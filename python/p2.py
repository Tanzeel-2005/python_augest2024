#read a number from the user and check a number is a even or not
my_number=int(input("Enter a number to check a number is even or not"))
print(type(my_number))
if my_number %2==0:
    print(my_number,"is a even number")
else:
    print(f'{my_number} is not a even number')
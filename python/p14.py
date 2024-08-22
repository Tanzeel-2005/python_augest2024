#Program to find 2nd smallest digit in a number
int_num=int(input("Enter a number to find the 2nd smallest dihit in a number"))
smallest=9
second_smallest=0
while int_num>0:
    last_digit=int_num%10
    int_num=int_num//10
    if last_digit<smallest:
        smallest=last_digit
print(smallest)






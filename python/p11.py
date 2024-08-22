#Program to Find Sum of digits of a number
int_num=int(input("Enter a number to find sum of digits of a number"))
sum_of_digits=0
while int_num>0:
    digits=int_num%10
    sum_of_digits=sum_of_digits+digits
    int_num=int_num//10
print(sum_of_digits,"Is the sum of digits of a number")

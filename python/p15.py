#Program to find Sum of even(odd) digits in a number
int_num=int(input("Enter a number to find sum of even digits in a number"))
original_num=int_num
sum_of_even=0
while int_num>0:
    last_digit=int_num%10
    int_num=int_num//10
    if last_digit%2==0:
        sum_of_even=sum_of_even+last_digit
    else:
        continue
print(sum_of_even,"Is the Sum of even(odd) digits in a number",original_num)
    

       


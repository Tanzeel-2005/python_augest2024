#Program to reverse a number
int_num=int(input("Enter a number to revers a number"))
original_number=int_num
rev_num=0
while int_num>0:
    last_digit=int_num%10
    rev_num=last_digit+(rev_num*10)
    int_num=int_num//10
print(rev_num,"Is thr reversed number of the number",original_number)
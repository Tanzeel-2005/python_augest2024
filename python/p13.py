#Program to find biggest (smallest) digit in a number
int_num=int(input("Enter a number to find the biggest dihit in a number"))
original_num=int_num
biggest_num=0
while int_num>0:
    last_digit=int_num%10
    int_num=int_num//10
    if last_digit>biggest_num:
        biggest_num=last_digit
    else:
        continue
print(biggest_num,"Is the biggest digit in a number ",original_num)

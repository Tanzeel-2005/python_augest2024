#Program to Find Odd(Even) placed digits in a number
int_num=int(input("Enter a number to find odd placed digits in a number"))
original_number=int_num
rev_num=0
i=1
while int_num>0:
    last_digit=int_num%10
    rev_num=last_digit+(rev_num*10)
    int_num=int_num//10
while rev_num>0:
    last_digit=rev_num%10
    rev_num=rev_num//10
    if i%2!=0:
        odd_digit=last_digit
        print(odd_digit)
        i=i+1
        continue
    else:
        i=i+1
        continue




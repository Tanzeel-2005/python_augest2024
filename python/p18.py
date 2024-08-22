#Program to Find Odd placed Even digits in a number
int_num=int(input("Enter a number to find odd placed Even digits in a number"))
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
        odd_placed_digit=last_digit
        if odd_placed_digit%2==0:
            print(odd_placed_digit)
            i=i+1
        else:
            i=i+1
    else:
        i=i+1
        continue

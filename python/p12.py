#Program to Find count of digits of a number
int_num=int(input("Enter a number to find count of digits"))
count=0

while int_num>0:
    int_num=int_num//10
    count=count+1
print(count)

#Program to print a Hollow Square of N lines
int_num=int(input("Enter the size to print a HAlloe square of n lines"))
for i in range(int_num):
    for j in range (int_num):
        if(i==0 or j==0 or i==int_num-1 or j==int_num-1 ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
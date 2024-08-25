#Program to print the Right angled Triangle of N lines
int_num=int(input("Enter a number of lines of a Equi lateral Triangle"))
for i in range(int_num):
    for j in range(i,int_num):
        print(" ",end=" ")
   
    for k in range(i+1):
        print("*",end=" ")
  
    for p in range(i):
        print("*",end=" ")
    print()

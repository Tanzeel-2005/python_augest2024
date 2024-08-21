#Program to check if a number is Perfect Square
import math
int_num=int(input("Enter a number to check if its is a perfect square"))
root=math.floor(math.sqrt(int_num))
if root*root==int_num:
    print(int_num,"is a perfect square")
else:
    print(int_num,"is not a perfect square")


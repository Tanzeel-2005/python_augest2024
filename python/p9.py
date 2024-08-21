input_num=int(input("Enter a number to print its math table"))
for i in range(1,21):
    #print(f'{input_num}*{i}={input_num*i}')
    print('%02d*%02d=%03d'%(input_num,i,input_num*i))
num=int(input("Enter number of element you want to enter : "))
Total_sum=0
for m in range(num):
    no=float(input("Enter Marks : "))
    Total_sum+=no
avg=Total_sum/num
print('Average of',num ,'number :',avg)
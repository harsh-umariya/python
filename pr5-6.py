a=int(input("Enter Number : "))
sum=0
for i in range(1,a):
    if a%i==0:
        sum+=i
        
if a==sum:
    print("It is a perfect Number!!!")
else:
    print("It is not a perfect Number!")
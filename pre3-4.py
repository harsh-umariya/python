a=int(input("Enter a 1st number: "))
b=int(input("Enter a 2nd number: "))
c=int(input("Enter a 3rd number: "))
d=int(input("Enter a 4th number: "))

j=(a if(a>b and a>c) else b if (b>a and b>c) else c)
print("maximum number is: ",j)
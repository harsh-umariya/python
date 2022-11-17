l2=[]
a=int(input("enter the number of element number:"))

for i in range(0,a):
    y=int(input(l2))
    l2.append(y)
print(l2)
a,b=0,0
for num in l2:
    if num%2==0:
        a+=1
    else:
        b+=1
print("even number of list:",a)
print("odd number of list:",b)    

temp=sum(l2)
c=temp/len(l2)
print("average of list :",c)
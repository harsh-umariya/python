
l1=[]
n=int(input("enter the number of element number:"))

for i in range(0,n):
    x=int(input(l1))
    l1.append(x)
print(l1)
pos,neg,zero=0,0,0
for num in l1:
    if num>0:
        pos +=1
    elif num<0:
        neg +=1
    else:
        zero+=1

print("possitev number:",pos) 
print("negative number:",neg)     
print("zero number:",zero)   
#6.2
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
   

